import joblib
import pandas as pd
from pathlib import Path
from sklearn.ensemble import StackingRegressor, RandomForestRegressor
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, mean_absolute_error
from math import sqrt
from sklearn.model_selection import train_test_split

# 1. Load data
# Chronological time‑aware split
# (load, clean, sort by datetimeEpoch)
df = pd.read_csv("data/DQN1_Dataset.csv")
df = df.dropna(subset=["healthRiskScore"])
df["datetime"] = pd.to_datetime(df["datetimeEpoch"], unit="s")
df = df.sort_values("datetime")

# 2. Features & target
target = "healthRiskScore"
features = df.columns.difference([target, "datetime", "datetimeEpoch"])
X = df[features]
y = df[target]

# 3. Train–test split (80/20 chronological)
split_idx = int(len(df) * 0.8)
X_train, X_test = X.iloc[:split_idx], X.iloc[split_idx:]
y_train, y_test = y.iloc[:split_idx], y.iloc[split_idx:]

# 4. Load optimized GBM model
gbm = joblib.load("models/gbm_opt.pkl")

# 5. Define other base learners
rf = RandomForestRegressor(n_estimators=200, random_state=42)
lr = LinearRegression()

estimators = [
    ("gbm", gbm),
    ("rf", rf),
    ("lr", lr),
]

# 6. Build stacking ensemble
stack = StackingRegressor(
    estimators=estimators,
    final_estimator=LinearRegression(),
    cv=5,
    n_jobs=-1,
)

# 7. Fit and save
stack.fit(X_train, y_train)
Path("models").mkdir(exist_ok=True)
joblib.dump(stack, "models/stack.pkl")
print("Stacking model saved to models/stack.pkl")

# 8. Quick evaluation
y_pred = stack.predict(X_test)
rmse = sqrt(mean_squared_error(y_test, y_pred))
mae = mean_absolute_error(y_test, y_pred)
print(f"Stacking RMSE: {rmse:.3f}; MAE: {mae:.3f}")
