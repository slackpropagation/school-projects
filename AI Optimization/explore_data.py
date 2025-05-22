import pandas as pd
import matplotlib.pyplot as plt

# 1. Load the CSV
df = pd.read_csv('data/DQN1_Dataset.csv')

# 2. Summary stats for our three key variables
print("\n=== Summary statistics ===")
print(df[['healthRiskScore', 'tempmax', 'humidity']].describe())

# 3. Plot each distribution in its own figure
for col, xlabel in [
    ('healthRiskScore', 'Health Risk Score'),
    ('tempmax',         'Maximum Temperature (°F)'),
    ('humidity',        'Relative Humidity (%)'),
]:
    plt.figure()
    df[col].hist()
    plt.title(f'Distribution of {xlabel}')
    plt.xlabel(xlabel)
    plt.ylabel('Frequency')
    plt.tight_layout()
    plt.show()
