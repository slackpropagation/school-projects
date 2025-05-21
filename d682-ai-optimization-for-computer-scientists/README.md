# AI Optimization for Computer Scientists (WGU D682)

This repository contains my completed performance assessment for the **WGU D682 – Artificial Intelligence Optimization for Computer Scientists** course.

Over four tasks, I researched, implemented, optimized, and adapted an AI solution for predicting urban air‐quality health risks. Along the way I:

- Explored real‑world air quality data and identified key patterns  
- Built and tuned a Gradient Boosting Machine (GBM) model with scikit‑learn  
- Evaluated model performance with RMSE and MAE metrics  
- Applied ensemble methods (stacking & voting) for further accuracy gains  
- Adapted the solution to a new domain (indoor air‑quality monitoring)  

## Project Summary

- **Task 1:**  
  - Researched three candidate AI algorithms (Linear Regression, Random Forest, GBM)  
  - Selected GBM, implemented it in Python, and validated with RMSE & R²  
- **Task 2:**  
  - Optimized GBM with RandomizedSearchCV & BayesianSearchCV  
  - Applied regularization (shrinkage & subsampling)  
  - Built stacking and voting ensembles, reducing RMSE by up to 39%  
- **Task 3:**  
  - Performed data exploration (distributions, diurnal cycles, correlations)  
  - Interpreted model outputs (feature importances, SHAP insights)  
  - Generated actionable insights for future predictions  
- **Task 4:**  
  - Adapted the outdoor‐focused model to indoor air‐quality use cases  
  - Integrated new sensors (CO₂, VOC, PM₂.₅), ventilation and occupancy features  
  - Proposed edge‑deployment, transfer learning, and compliance with ASHRAE & GDPR  

## Key Components

- **`gbm_model.py`**  
  Loads data, builds a preprocessing + GBM pipeline, trains and saves the baseline model.  
- **`optimize_gbm.py`**  
  Hyperparameter tuning using RandomizedSearchCV and (optional) BayesianSearchCV.  
- **`ensemble_stack.py`** & **`ensemble_vote.py`**  
  Build and evaluate StackingRegressor and VotingRegressor ensembles.  
- **`evaluate_models.py`**  
  Computes RMSE & MAE for baseline, optimized, stacking, and voting models; outputs comparison.  
- **`explore_data.py`** & **`analyze_patterns.py`**  
  Data exploration: histograms, hourly risk cycles, and correlation matrices.  
- **`interpret_metrics.py`** & **`analyze_model_behavior.py`**  
  Interpret performance metrics and extract feature‑importance insights from the GBM.  
- **`Narrative_Report_Task1.docx`**, **`_Task2.docx`**, **`_Task3.docx`**, **`_Task4.docx`**  
  Detailed narrative reports covering research, implementation, evaluation, and adaptation.  
- **`requirements.txt`**  
  Lists project dependencies.  

## Algorithms & Techniques

- **Gradient Boosting Machine (GBM)**  
  Powerful tree‑based learner for regression tasks.  
- **Randomized & Bayesian Search**  
  Efficient hyperparameter optimization strategies.  
- **Shrinkage & Subsampling**  
  Regularization methods to reduce overfitting.  
- **Stacking & Voting Ensembles**  
  Combine multiple models to improve generalization and reduce error.  
- **Transfer Learning**  
  Fine‑tune a pre‑trained model on a new (indoor) domain to reduce data needs.  

## Task Requirements Covered

- Automated hyperparameter tuning and model evaluation with scikit‑learn  
- Comprehensive narrative reports with in‑text citations and APA reference lists  
- Data exploration and pattern identification with pandas and matplotlib  
- Model interpretation using feature importances and actionable insights  
- Adaptation strategies for a new domain, addressing scalability, integration, performance, and compliance  

## What I Learned

- How to implement and optimize GBM models for real‑world regression problems  
- The impact of regularization and ensembling on model performance  
- Techniques for exploratory data analysis and pattern discovery  
- Methods for interpreting model outputs and deriving business‑relevant insights  
- Best practices for adapting AI solutions to new domains with transfer learning  
- End‑to‑end project workflow: research, coding, evaluation, reporting, and version control  
