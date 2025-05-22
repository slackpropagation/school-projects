import joblib
import pandas as pd
from pathlib import Path
from sklearn.ensemble import VotingRegressor, HistGradientBoostingRegressor
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, mean_absolute_error
from math import sqrt  # added import

# 1. Load and prepare
df = pd.read_csv("data/DQN1_Dataset.csv")
df = df.dropna(subset=["healthRiskScore"])
df["datetime"] = pd.to_datetime(df["datetimeEpoch"], unit="s")
df = df.sort_values("datetime")

target = "healthRiskScore"
features = df.columns.difference([target, "datetime", "datetimeEpoch"])
X = df[features]
y = df[target]

split_idx = int(len(df) * 0.8)
X_train, X_test = X.iloc[:split_idx], X.iloc[split_idx:]
y_train, y_test = y.iloc[:split_idx], y.iloc[split_idx:]

# 2. Load optimized GBM
gbm = joblib.load("models/gbm_opt.pkl")

# 3. Define other estimators
hgb = HistGradientBoostingRegressor(max_iter=200, random_state=42)
lr  = LinearRegression()

estimators = [
    ("gbm", gbm),
    ("hgb", hgb),
    ("lr", lr),
]

# 4. Build voting ensemble
vote = VotingRegressor(estimators=estimators, n_jobs=-1)

# 5. Fit and save
vote.fit(X_train, y_train)
Path("models").mkdir(exist_ok=True)
joblib.dump(vote, "models/vote.pkl")
print("Voting model saved to models/vote.pkl")

# 6. Quick evaluation
y_pred = vote.predict(X_test)
rmse = sqrt(mean_squared_error(y_test, y_pred))  # use sqrt instead of squared=False
mae  = mean_absolute_error(y_test, y_pred)
print(f"Voting RMSE: {rmse:.3f}; MAE: {mae:.3f}")
