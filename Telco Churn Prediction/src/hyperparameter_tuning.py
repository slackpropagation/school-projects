import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import GridSearchCV, train_test_split
from sklearn.metrics import accuracy_score, classification_report
import joblib

# Load preprocessed dataset
df = pd.read_csv('data/preprocessed_telco.csv')
X = df.drop('Churn', axis=1)
y = df['Churn']

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Define model + parameter grid
rf = RandomForestClassifier(random_state=42)
param_grid = {
    'n_estimators': [50, 100, 150],
    'max_depth': [None, 10, 20],
    'min_samples_split': [2, 5, 10]
}

# GridSearchCV
grid_search = GridSearchCV(estimator=rf, param_grid=param_grid, cv=5, scoring='accuracy', n_jobs=-1, verbose=2)
grid_search.fit(X_train, y_train)

# Best model
best_rf = grid_search.best_estimator_
print(f"\n✅ Best Parameters: {grid_search.best_params_}")

# Evaluate on test set
y_pred = best_rf.predict(X_test)
acc = accuracy_score(y_test, y_pred)
print(f"✅ Tuned Random Forest Accuracy: {acc:.4f}")
print(classification_report(y_test, y_pred))

# Save tuned model
joblib.dump(best_rf, 'models/rf_tuned_model.pkl')
print("✅ Tuned model saved as models/rf_tuned_model.pkl")