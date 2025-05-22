import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
import joblib

# Load preprocessed dataset
df = pd.read_csv('data/preprocessed_telco.csv')

# Separate features and target
X = df.drop('Churn', axis=1)
y = df['Churn']

# Train/test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize models
logreg = LogisticRegression(max_iter=1000)
rf = RandomForestClassifier()
svm = SVC(probability=True)

# Train models
logreg.fit(X_train, y_train)
rf.fit(X_train, y_train)
svm.fit(X_train, y_train)

# Predict + evaluate
for name, model in [('Logistic Regression', logreg), ('Random Forest', rf), ('SVM', svm)]:
    y_pred = model.predict(X_test)
    acc = accuracy_score(y_test, y_pred)
    print(f"✅ {name} Accuracy: {acc:.4f}")

# Save models
joblib.dump(logreg, 'models/logreg_model.pkl')
joblib.dump(rf, 'models/rf_model.pkl')
joblib.dump(svm, 'models/svm_model.pkl')

print("✅ Models saved in /models folder.")