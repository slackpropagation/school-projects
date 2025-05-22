import joblib
import pandas as pd

# 1. Load the dataset just to get feature names
df = pd.read_csv("data/DQN1_Dataset.csv")
features = df.columns.difference(["healthRiskScore", "datetimeEpoch", "datetime"])

# 2. Load the optimized GBM pipeline
pipeline = joblib.load("models/gbm_opt.pkl")

# 3. Extract the GBM step from the pipeline and get feature importances
gbm = pipeline.named_steps["gbm"]
importances = gbm.feature_importances_

# 4. Build a DataFrame
imp_df = pd.DataFrame({
    "feature": features,
    "importance": importances
}).sort_values("importance", ascending=False)

# 5. Save full table and print top 5
imp_df.to_csv("feature_importances.csv", index=False)
print("\nTop 5 Feature Importances:")
print(imp_df.head(5).to_string(index=False))
