import joblib
import pandas as pd
from pathlib import Path
from math import sqrt
from sklearn.metrics import mean_squared_error, mean_absolute_error

# 1. Load test set
df = pd.read_csv("data/DQN1_Dataset.csv")
df = df.dropna(subset=["healthRiskScore"])
df["datetime"] = pd.to_datetime(df["datetimeEpoch"], unit="s")
df = df.sort_values("datetime")

target = "healthRiskScore"
features = df.columns.difference([target, "datetime", "datetimeEpoch"])
split_idx = int(len(df) * 0.8)
X_test = df[features].iloc[split_idx:]
y_test = df[target].iloc[split_idx:]

# 2. Load models
models = {
    "Baseline_GBM": joblib.load("models/gbm.pkl"),
    "Optimized_GBM": joblib.load("models/gbm_opt.pkl"),
    "Stacking": joblib.load("models/stack.pkl"),
    "Voting": joblib.load("models/vote.pkl"),
}

# 3. Evaluate and collect results
results = []
for name, model in models.items():
    y_pred = model.predict(X_test)
    rmse = sqrt(mean_squared_error(y_test, y_pred))
    mae  = mean_absolute_error(y_test, y_pred)
    results.append(f"{name}; RMSE={rmse:.3f}; MAE={mae:.3f}")
    print(results[-1])

# 4. Write to file
with open("comparison_results.txt", "w") as f:
    f.write("\n".join(results))
print("Saved comparison to comparison_results.txt")
