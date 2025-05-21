# Telco Churn Prediction (WGU D683 – Advanced AI/ML)

This repository contains my completed performance assessment for the **WGU D683 – Advanced Artificial Intelligence and Machine Learning** course.

Over two major tasks, I designed, developed, evaluated, and optimized an end-to-end AI/ML solution to predict telecom customer churn. The project simulates a real-world use case where early churn prediction enables proactive retention strategies.

## Project Summary

- **Task 1:**  
  - Defined a business problem: reducing customer churn in a telecom company  
  - Selected a SMART goal using the SBI framework  
  - Chose the Telco Customer Churn dataset and proposed an ML solution  
  - Outlined a project timeline, risks, mitigation strategies, and environment setup

- **Task 2:**  
  - Preprocessed the dataset: missing values, categorical encoding, feature scaling  
  - Trained multiple ML models (Logistic Regression, Random Forest, SVM)  
  - Evaluated model performance using accuracy, precision, recall, and F1 score  
  - Performed k-fold cross-validation to ensure generalizability  
  - Tuned hyperparameters for Random Forest using GridSearchCV  
  - Delivered a fully functional and reproducible AI/ML product

## Key Components

- **`src/preprocess.py`**  
  Cleans, encodes, scales the dataset; outputs `preprocessed_telco.csv`.  

- **`src/train_model.py`**  
  Trains Logistic Regression, Random Forest, and SVM classifiers; saves models.  

- **`src/evaluate.py`**  
  Evaluates models on classification metrics; saves confusion matrices.  

- **`src/cross_validation.py`**  
  Runs 5-fold cross-validation on all models and reports mean accuracy and variance.  

- **`src/hyperparameter_tuning.py`**  
  Performs GridSearchCV tuning for Random Forest and saves the best model.  

- **`requirements.txt`**  
  Python dependencies used across the project.  

## Algorithms & Techniques

- **Logistic Regression**  
  Baseline linear model for binary classification.  

- **Random Forest**  
  Tree-based ensemble model with strong generalization.  

- **Support Vector Machine (SVM)**  
  Non-linear classifier effective for high-dimensional data.  

- **Grid Search Cross-Validation**  
  Systematic hyperparameter tuning method.  

- **StandardScaler, LabelEncoder**  
  Feature scaling and encoding utilities for structured datasets.  

## Task Requirements Covered

- Complete AI/ML pipeline: preprocessing → training → evaluation → tuning  
- Accuracy, precision, recall, and F1 score metrics reported  
- Confusion matrices visualized and exported  
- k-fold cross-validation used to test model consistency  
- GridSearchCV applied for hyperparameter tuning  
- Professional documentation and GitLab version control demonstrated  

## What I Learned

- How to design a complete AI/ML product with business value  
- Data preprocessing best practices for classification tasks  
- Differences in model behavior and evaluation metrics  
- How to use GridSearchCV and cross-validation to improve model robustness  
- Tools for model interpretability (confusion matrix, classification report)  
- The importance of reproducibility and documentation in professional AI development  
