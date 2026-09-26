# EcoSentinel: Satellite Monitoring for Environmental Protection

[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![MLflow](https://img.shields.io/badge/MLflow-Tracking-0194E2.svg)](https://mlflow.org/)
[![DVC](https://img.shields.io/badge/DVC-Data_Versioning-945DD6.svg)](https://dvc.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

**EcoSentinel** is a robust, end-to-end MLOps pipeline designed to continuously scan multi-spectral satellite imagery. Our mission is to automate the detection of illegal waste dumping and water contamination before the environmental damage spreads.

This repository serves as our Phase 1 prototype and focuses on the **Vrishabhavathi-Arkavathi river basin** in Karnataka, India—an ecosystem currently suffering from severe industrial effluent dumping.

---

## Table of Contents
- [The Problem & Our Solution](#the-problem--our-solution)
- [MLOps Architecture](#mlops-architecture)
- [Repository Structure](#repository-structure)
- [Getting Started (Installation)](#getting-started)
- [Data Versioning (DVC)](#data-versioning-dvc)
- [Experiment Tracking (MLflow)](#experiment-tracking-mlflow)
- [Team & Phase 1 Goals](#team--phase-1-goals)

---

## The Problem & Our Solution
### The Crisis
The Vrishabhavathi River acts as a primary carrier for unauthorized industrial effluents and untreated waste. Traditional monitoring relies on manual inspections and localized water sampling, meaning contamination often goes undetected for weeks until immense ecological damage is done.

### The EcoSentinel Solution
By processing high-resolution Sentinel-2 satellite imagery, we use machine learning to extract key ecological indicators:
- **NDWI (Normalized Difference Water Index):** Isolates water bodies to track effluent discoloration.
- **NDVI (Normalized Difference Vegetation Index):** Detects unnatural, profuse weed/algae growth caused by chemical dumping.

The model flags anomalous coordinates, acting as an early-warning system for authorities.

---

## MLOps Architecture
This project strictly adheres to MLOps best practices to ensure reproducibility and scalability:
1. **Data Versioning:** Massive `.tiff` satellite files are versioned outside of Git using **DVC (Data Version Control)**.
2. **Experiment Tracking:** All model hyperparameter tuning, feature engineering variations, and performance metrics (F1, Recall) are logged via **MLflow**.
3. **Automated Pipelines:** Data ingestion, feature extraction, and model inference are connected in a continuous, reproducible pipeline.

---

## Repository Structure

```text
├── data/
│   ├── raw/           # Raw, immutable satellite imagery (tracked via DVC)
│   └── processed/     # Cleaned, engineered datasets (NDWI, NDVI)
├── docs/              # Project documentation and phase plans
├── notebooks/         # Jupyter notebooks for EDA and prototyping
├── src/               # Source code for the ML pipeline
│   ├── data/          # Scripts to fetch and clean data
│   ├── features/      # Scripts to extract spectral features
│   └── models/        # Scripts to train and predict (tracked via MLflow)
├── tests/             # Unit and integration tests
├── requirements.txt   # Python dependencies
└── README.md          # Project overview (You are here)
```

---

## Getting Started

### Prerequisites
- Python 3.9 or higher
- Git

### Installation
1. **Clone the repository:**
   ```bash
   git clone https://github.com/aryawadhwa/MLops-proj.git
   cd MLops-proj
   ```
2. **Create and activate a virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```
3. **Install the required dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

---

## Data Versioning (DVC)
Due to the sheer size of geospatial data, we do not push `.tiff` files or large datasets to GitHub. Instead, we use DVC.

1. Ensure your Google Drive or AWS S3 credentials are set up (ask your team lead for the remote bucket link).
2. Pull the latest dataset versions:
   ```bash
   dvc pull
   ```

---

## Experiment Tracking (MLflow)
To view our model iterations and baseline experiments:
1. Run the MLflow UI server locally:
   ```bash
   mlflow ui
   ```
2. Open your browser and navigate to `http://localhost:5000` to view the dashboards.

---

## Team & Phase 1 Goals
Please refer to the [Phase 1 Team Plan](docs/Phase_1_Team_Plan.md) in the `/docs` folder for specific tasks and assignments leading up to the Phase 1 Review (Oct 13 - Oct 17). 
