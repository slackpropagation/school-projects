import pandas as pd
import joblib
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
import numpy as np

# Load preprocessed dataset
df = pd.read_csv('data/preprocessed_telco.csv')
X = df.drop('Churn', axis=1)
y = df['Churn']

# Define models
models = {
    'Logistic Regression': LogisticRegression(max_iter=1000),
    'Random Forest': RandomForestClassifier(),
    'SVM': SVC()
}

# Apply 5-fold cross-validation
for name, model in models.items():
    scores = cross_val_score(model, X, y, cv=5, scoring='accuracy')
    print(f"\n✅ {name} Cross-Validation Results:")
    print(f"Scores per fold: {np.round(scores, 4)}")
    print(f"Mean Accuracy: {scores.mean():.4f}")
    print(f"Standard Deviation: {scores.std():.4f}")