import argparse
import joblib
from pathlib import Path
from math import sqrt

import numpy as np
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import GridSearchCV, TimeSeriesSplit
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.ensemble import GradientBoostingRegressor

# -----------------------------------------------------------------------------
# 1. Utility Functions
# -----------------------------------------------------------------------------

def load_data(path: Path) -> pd.DataFrame:
    """Load the dataset from CSV into a pandas DataFrame.

    Args:
        path (Path): Path to the CSV file.

    Returns:
        pd.DataFrame: Loaded dataset.
    """
    df = pd.read_csv(path)

    # Basic sanity check – ensure datetime column exists
    if "datetimeEpoch" in df.columns:
        # Convert epoch to pandas datetime for time‑aware splitting
        df["datetime"] = pd.to_datetime(df["datetimeEpoch"], unit="s")
        df = df.sort_values("datetime")
    else:
        raise KeyError("Column 'datetimeEpoch' not found in dataset.")

    # Drop rows with missing target (healthRiskScore)
    df = df.dropna(subset=["healthRiskScore"])

    return df


def train_test_split_time(df: pd.DataFrame, test_size: float = 0.2):
    """Perform a chronological train‑test split to avoid data leakage."""
    split_index = int(len(df) * (1 - test_size))
    train_df = df.iloc[:split_index]
    test_df = df.iloc[split_index:]
    return train_df, test_df


# -----------------------------------------------------------------------------
# 2. Main Training Pipeline
# -----------------------------------------------------------------------------

def build_pipeline(num_features: list[str], cat_features: list[str]):
    """Create a preprocessing + GBM pipeline."""
    numeric_transformer = Pipeline(
        steps=[("scaler", StandardScaler())]
    )

    categorical_transformer = Pipeline(
        steps=[("onehot", OneHotEncoder(handle_unknown="ignore"))]
    )

    preprocessor = ColumnTransformer(
        transformers=[
            ("num", numeric_transformer, num_features),
            ("cat", categorical_transformer, cat_features),
        ]
    )

    gbm = GradientBoostingRegressor(random_state=42)

    pipeline = Pipeline(
        steps=[
            ("preprocessor", preprocessor),
            ("regressor", gbm),
        ]
    )
    return pipeline


def tune_hyperparameters(pipeline, X_train, y_train):
    """Grid‑search hyperparameters using time‑series cross‑validation."""
    param_grid = {
        "regressor__n_estimators": [200, 400],
        "regressor__learning_rate": [0.05, 0.1],
        "regressor__max_depth": [3, 4],
        "regressor__subsample": [0.8, 1.0],
    }

    tscv = TimeSeriesSplit(n_splits=5)

    grid = GridSearchCV(
        estimator=pipeline,
        param_grid=param_grid,
        cv=tscv,
        scoring="neg_root_mean_squared_error",
        n_jobs=-1,
        verbose=2,
    )

    grid.fit(X_train, y_train)
    return grid


# -----------------------------------------------------------------------------
# 3. Evaluation Helpers
# -----------------------------------------------------------------------------

def evaluate(model, X_test, y_test):
    """Compute RMSE and R² on the test set."""
    y_pred = model.predict(X_test)
    rmse = sqrt(mean_squared_error(y_test, y_pred))
    r2 = r2_score(y_test, y_pred)
    return rmse, r2


# -----------------------------------------------------------------------------
# 4. CLI Entry Point
# -----------------------------------------------------------------------------

def main(args):
    # Load data
    df = load_data(Path(args.data_path))

    # Select features and target
    target = "healthRiskScore"
    feature_cols = df.columns.difference([target, "datetime", "datetimeEpoch"])

    # Simple heuristic: numeric vs categorical columns
    num_features = [c for c in feature_cols if df[c].dtype != "object"]
    cat_features = [c for c in feature_cols if df[c].dtype == "object"]

    # Split dataset chronologically
    train_df, test_df = train_test_split_time(df)
    X_train, y_train = train_df[feature_cols], train_df[target]
    X_test, y_test = test_df[feature_cols], test_df[target]

    # Build preprocessing+model pipeline
    pipeline = build_pipeline(num_features, cat_features)

    # Hyperparameter tuning
    grid_model = tune_hyperparameters(pipeline, X_train, y_train)
    best_model = grid_model.best_estimator_

    # Evaluate on hold‑out set
    rmse, r2 = evaluate(best_model, X_test, y_test)
    print(f"Test RMSE: {rmse:.3f}")
    print(f"Test R²  : {r2:.3f}")

    # Persist model
    output_path = Path(args.model_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    joblib.dump(best_model, output_path)
    print(f"Best model saved to {output_path}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Train GBM for air‑quality health‑risk prediction")
    parser.add_argument("--data_path", type=str, required=True, help="Path to CSV dataset")
    parser.add_argument("--model_path", type=str, default="models/gbm.pkl", help="Where to save the trained model")
    main(parser.parse_args())
