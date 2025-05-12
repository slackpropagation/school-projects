# optimize_gbm.py
"""
Task 2 – B1; apply two optimization techniques to the baseline GBM model.

This script offers two tuners selectable via CLI:
1. **RandomizedSearchCV** – stochastic exploration of hyper‑parameters.
2. **BayesianSearchCV** (from scikit‑optimize) – sequential model‑based optimization.

Usage;
    python optimize_gbm.py random   ; run RandomizedSearchCV
    python optimize_gbm.py bayes    ; run BayesianSearchCV

Outputs;
    • best model saved to models/gbm_opt.pkl (overwrites if exists)
    • tuner log printed to console

Author; Eray Yaman
Date; 2025‑05‑05
"""

import argparse
import joblib
from pathlib import Path

import numpy as np
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.metrics import make_scorer, mean_squared_error
from math import sqrt
from sklearn.model_selection import RandomizedSearchCV, TimeSeriesSplit
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.ensemble import GradientBoostingRegressor

# Optional import; if scikit‑optimize isn’t installed (or installed version moved BayesSearchCV), fall back to RandomizedSearch only
try:
    from skopt.searchcv import BayesSearchCV
    HAS_SKOPT = True
except ImportError:
    HAS_SKOPT = False

# -----------------------------------------------------------------------------
# 1. Data loading helper (reuse logic from gbm_model)
# -----------------------------------------------------------------------------

def load_dataset(csv_path: Path):
    df = pd.read_csv(csv_path)
    if "datetimeEpoch" not in df.columns:
        raise KeyError("datetimeEpoch column missing; cannot make time‑aware split")
    df["datetime"] = pd.to_datetime(df["datetimeEpoch"], unit="s")
    df = df.sort_values("datetime")
    df = df.dropna(subset=["healthRiskScore"])
    return df


# -----------------------------------------------------------------------------
# 2. Build preprocessing + GBM pipeline
# -----------------------------------------------------------------------------

def build_pipeline(num_features, cat_features):
    numeric_tf = Pipeline([("scale", StandardScaler())])
    cat_tf = Pipeline([("oh", OneHotEncoder(handle_unknown="ignore"))])
    pre = ColumnTransformer([
        ("num", numeric_tf, num_features),
        ("cat", cat_tf,  cat_features),
    ])
    gbm = GradientBoostingRegressor(random_state=42)
    return Pipeline([("pre", pre), ("gbm", gbm)])


# -----------------------------------------------------------------------------
# 3. Hyper‑parameter spaces
# -----------------------------------------------------------------------------

 # Regularization methods include:
 #  - shrinkage via low learning_rate values
 #  - subsampling via gbm__subsample values < 1.0
SEARCH_SPACE = {
    "gbm__n_estimators": [int(x) for x in np.linspace(100, 600, 11)],
    "gbm__learning_rate": np.logspace(-3, -1, 5),
    "gbm__max_depth": [2, 3, 4, 5],
    "gbm__subsample": [0.6, 0.8, 1.0],
}

neg_rmse = make_scorer(lambda y, y_pred: -sqrt(mean_squared_error(y, y_pred)))

def random_search(pipeline, X_train, y_train):
    tscv = TimeSeriesSplit(n_splits=5)
    rs = RandomizedSearchCV(
        pipeline,
        param_distributions=SEARCH_SPACE,
        n_iter=200,
        cv=tscv,
        scoring=neg_rmse,
        n_jobs=-1,
        random_state=42,
        verbose=1,
    )
    rs.fit(X_train, y_train)
    return rs.best_estimator_


def bayes_search(pipeline, X_train, y_train):
    if not HAS_SKOPT:
        raise ImportError("scikit‑optimize not installed; run pip install scikit‑optimize or use random search")
    tscv = TimeSeriesSplit(n_splits=5)
    bs = BayesSearchCV(
        pipeline,
        search_spaces=SEARCH_SPACE,
        n_iter=50,
        cv=tscv,
        scoring=neg_rmse,
        n_jobs=-1,
        random_state=42,
        verbose=0,
    )
    bs.fit(X_train, y_train)
    return bs.best_estimator_


# -----------------------------------------------------------------------------
# 4. Main entry
# -----------------------------------------------------------------------------

def main(mode: str):
    data_path = Path("data/DQN1_Dataset.csv")
    df = load_dataset(data_path)
    target = "healthRiskScore"
    feature_cols = df.columns.difference([target, "datetime", "datetimeEpoch"])
    num_cols = [c for c in feature_cols if df[c].dtype != "object"]
    cat_cols = [c for c in feature_cols if df[c].dtype == "object"]

    split = int(len(df) * 0.8)
    train_df = df.iloc[:split]

    pipeline = build_pipeline(num_cols, cat_cols)

    X_train, y_train = train_df[feature_cols], train_df[target]

    if mode == "random":
        best_model = random_search(pipeline, X_train, y_train)
    elif mode == "bayes":
        best_model = bayes_search(pipeline, X_train, y_train)
    else:
        raise ValueError("mode must be 'random' or 'bayes'")

    Path("models").mkdir(exist_ok=True)
    joblib.dump(best_model, "models/gbm_opt.pkl")
    print("Optimized model saved to models/gbm_opt.pkl")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Optimize GBM with Random or Bayesian search")
    parser.add_argument("mode", choices=["random", "bayes"], help="Choose optimization mode")
    args = parser.parse_args()
    main(args.mode)
