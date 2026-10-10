# Reproducibility Guide

This guide explains how to reproduce the smart-meter electricity forecasting workflow for Phase 1.

## 1. Setup Environment
Ensure you have the necessary dependencies installed:
```bash
pip install pandas numpy scikit-learn matplotlib seaborn jupyter mlflow
```

## 2. Data Preprocessing
The raw dataset is tracked via DVC. If you have the data, run the preprocessing script to generate the daily aggregated CSV for meter BR28:
```bash
python src/preprocess.py
```
This will output `data/processed/bareilly_br28_daily.csv`.

## 3. Exploratory Data Analysis (EDA)
To view the EDA:
```bash
jupyter notebook notebooks/01_EDA.ipynb
```

## 4. Model Training & Evaluation
To train the Random Forest and Gradient Boosting baseline models:
```bash
python src/train.py
```
This script performs feature engineering, splits the data chronologically, trains the models, and evaluates them using MAE and RMSE.

## 5. Experiment Tracking with MLflow
All experiments are logged using MLflow. To view the metrics, parameters, and saved models, launch the MLflow UI:
```bash
mlflow ui
```
Then open your browser to `http://localhost:5000` to compare the models.
