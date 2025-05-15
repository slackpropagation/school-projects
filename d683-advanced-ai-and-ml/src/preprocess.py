import pandas as pd
from sklearn.preprocessing import LabelEncoder, StandardScaler

# Load dataset
df = pd.read_csv('data/Telco-Customer-Churn.csv')

# Drop customerID (not useful for prediction)
df.drop('customerID', axis=1, inplace=True)

# Handle missing values
df['TotalCharges'] = pd.to_numeric(df['TotalCharges'], errors='coerce')
df['TotalCharges'].fillna(df['TotalCharges'].median(), inplace=True)

# Encode categorical variables
le = LabelEncoder()
for col in df.select_dtypes(include=['object']).columns:
    df[col] = le.fit_transform(df[col])

# Scale numeric features
scaler = StandardScaler()
num_cols = ['tenure', 'MonthlyCharges', 'TotalCharges']
df[num_cols] = scaler.fit_transform(df[num_cols])

# Save preprocessed dataset
df.to_csv('data/preprocessed_telco.csv', index=False)

print("✅ Preprocessing complete. Preprocessed dataset saved to data/preprocessed_telco.csv")