import pandas as pd
import joblib
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix, \
    classification_report
import matplotlib.pyplot as plt
import seaborn as sns

# Load preprocessed data
df = pd.read_csv('data/preprocessed_telco.csv')
X = df.drop('Churn', axis=1)
y = df['Churn']

# Load trained models
logreg = joblib.load('models/logreg_model.pkl')
rf = joblib.load('models/rf_model.pkl')
svm = joblib.load('models/svm_model.pkl')

# Make predictions
models = {'Logistic Regression': logreg, 'Random Forest': rf, 'SVM': svm}
results = {}

for name, model in models.items():
    y_pred = model.predict(X)
    acc = accuracy_score(y, y_pred)
    prec = precision_score(y, y_pred)
    rec = recall_score(y, y_pred)
    f1 = f1_score(y, y_pred)
    print(f"\n✅ {name} Results:")
    print(f"Accuracy: {acc:.4f}")
    print(f"Precision: {prec:.4f}")
    print(f"Recall: {rec:.4f}")
    print(f"F1 Score: {f1:.4f}")
    print(classification_report(y, y_pred))

    # Save confusion matrix plot
    cm = confusion_matrix(y, y_pred)
    plt.figure(figsize=(6, 4))
    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues')
    plt.title(f'{name} Confusion Matrix')
    plt.xlabel('Predicted')
    plt.ylabel('Actual')
    plt.tight_layout()
    plt.savefig(f'outputs/{name.lower().replace(" ", "_")}_confusion_matrix.png')
    plt.close()

    results[name] = {'accuracy': acc, 'precision': prec, 'recall': rec, 'f1': f1}

print("\n✅ Confusion matrix plots saved to /outputs folder.")