# EcoSentinel: Satellite Monitoring for Environmental Protection

## Overview
EcoSentinel is an MLOps pipeline designed to continuously scan multi-spectral satellite imagery to detect illegal waste dumping and water contamination. Our initial pilot project focuses on tracking industrial effluents and waste in the Vrishabhavathi-Arkavathi river basin in Karnataka.

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
└── README.md          # Project overview
```

## Getting Started
1. Clone the repository: `git clone https://github.com/aryawadhwa/MLops-proj.git`
2. Create a virtual environment: `python -m venv venv`
3. Activate the environment: `source venv/bin/activate` (or `venv\Scripts\activate` on Windows)
4. Install dependencies: `pip install -r requirements.txt`
5. Initialize DVC: `dvc pull` (Ensure you have access to the remote storage bucket).
