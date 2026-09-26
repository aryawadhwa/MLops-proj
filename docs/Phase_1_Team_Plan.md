# Phase 1: Development & Reproducibility (Oct 13 - Oct 17)
**Team Action Plan for EcoSentinel**

*Hey team, here is the breakdown of what we need to get done for our Phase 1 review. Since anyone taking leave gets marked zero, we need all hands on deck!*

## 1. Dataset Acquisition / Approval (Priority: HIGH)
*   **Action Item:** We need to source satellite data for the Vrishabhavathi-Arkavathi river basin (or a pre-labeled water pollution/waste dataset to act as a placeholder). 
*   **Sources to check:** Sentinel-2 (Copernicus Hub) or Kaggle (Search: "Satellite Image Water Quality").
*   **Assigned to:** [Name]

## 2. Git Repository & DVC Setup
*   **Action Item:** The base repo is set up at `aryawadhwa/MLops-proj`. We must strictly NOT push large `.tiff` datasets to GitHub. 
*   **Action Item:** Initialize DVC (`dvc init`) and configure a remote bucket (e.g., Google Drive or AWS S3) to store the actual data files.
*   **Assigned to:** [Name]

## 3. Data Exploration & Feature Engineering
*   **Action Item:** Create a Jupyter notebook in `notebooks/` to load and visualize the multispectral data.
*   **Action Item:** Engineer specific features:
    *   **NDWI (Normalized Difference Water Index):** Helps us isolate the river and look for effluent discoloration.
    *   **NDVI (Normalized Difference Vegetation Index):** Helps us detect unnatural weed/algae growth caused by pollution.
*   **Assigned to:** [Name]

## 4. Baseline Models & Initial Evaluation
*   **Action Item:** Train a simple baseline classifier (e.g., Random Forest or Logistic Regression) using our engineered features to classify pixels/images as "Clean" vs "Polluted" or "Normal Land" vs "Dump Site".
*   **Action Item:** Calculate accuracy, precision, recall, and F1-score. (Don't worry if it's low, it's just a baseline).
*   **Assigned to:** [Name]

## 5. MLflow Experiment Tracking
*   **Action Item:** Set up MLflow tracking. Wrap the baseline model training code so that it logs hyperparameters (e.g., `n_estimators`) and metrics (e.g., `f1-score`) to the MLflow server.
*   **Action Item:** Run at least 3-4 experiments with different parameters so we have a populated MLflow dashboard to show the professor.
*   **Assigned to:** [Name]
