import pandas as pd

# 1. Load & preprocess
df = pd.read_csv('data/DQN1_Dataset.csv')
df = df.dropna(subset=['healthRiskScore'])
df['datetime'] = pd.to_datetime(df['datetimeEpoch'], unit='s')

# 2. Pattern 1: Diurnal cycle of healthRiskScore
df['hour'] = df['datetime'].dt.hour
hourly = df.groupby('hour')['healthRiskScore'] \
           .agg(['mean','count']).reset_index() \
           .rename(columns={'mean':'avg_risk','count':'n_obs'})
print("\nPattern 1: Average healthRiskScore by hour of day")
print(hourly.to_string(index=False))

# 3. Pattern 2: Correlation between key features
corr = df[['healthRiskScore','tempmax','humidity']].corr().round(2)
print("\nPattern 2: Correlation matrix of healthRiskScore, tempmax, humidity")
print(corr.to_string())

# 4. Save for narrative
hourly.to_csv('patterns_hourly_risk.csv', index=False)
corr.to_csv('patterns_correlation.csv')
print("\nSaved patterns to patterns_hourly_risk.csv and patterns_correlation.csv")
