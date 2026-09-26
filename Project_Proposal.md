# Project Proposal: EcoSentinel 
**An MLOps Pipeline for Continuous Satellite Monitoring of Illegal Waste & Water Contamination**

---

## 1. Executive Summary
### The Problem
When illegal dumping occurs in remote land areas or open water bodies, it goes undetected for weeks due to the vastness of these environments and a reliance on manual inspections. This delay allows waste to accumulate, leach toxins into soil, and spread across waterways before authorities can respond—making early, automated detection critical.

### The Solution
**EcoSentinel** is a unified, ML-powered environmental monitoring platform. By continuously scanning multi-spectral satellite imagery, our pipeline detects both terrestrial dumping sites and aquatic debris accumulations, instantly flagging anomalies for authorities to intervene before the damage spreads.

---

## 2. Real-World Case Study: The Vrishabhavathi Crisis
To demonstrate the urgent need for this technology, this project focuses its initial modeling on the **Vrishabhavathi-Arkavathi river basin in Karnataka**. 

### The Context
The Vrishabhavathi River, once a 69-kilometer stretch of pure water originating from a natural spring, was historically used for drinking and sacred rituals. Today, locals refer to it as *Visha-bhavathi* (Poison River). Unchecked industrial effluents and illegal dumping have transformed this ecosystem into an open urban drainage channel. 

According to an **ENVIS Technical Report (Report 122) by the Indian Institute of Science (IISc)**:
*   The valley has lost nearly half its lakes since the 1970s (reduced from 71 to 35).
*   The primary causes of this ecosystem collapse are the indiscriminate disposal of untreated industrial effluents, solid waste, and construction debris.
*   This pollution has severely altered the biological integrity of the basin, leading to profuse, unnatural weed growth.

**Our Objective:** Automate the detection of these exact environmental degradation parameters identified by the IISc using satellite imagery and MLOps, replacing slow manual reporting with continuous, longitudinal ML monitoring.

---

## 3. Project Feasibility & Technical Architecture
This project is highly feasible and perfectly scoped for an MLOps curriculum. By utilizing geospatial data (which is inherently large and complex), the project naturally demands robust MLOps practices.

### A. Data Acquisition
*   **Primary Source:** Sentinel-2 Satellite Imagery (via Google Earth Engine or Copernicus Hub).
*   **Data Characteristics:** High-resolution, multi-spectral `.tiff` files.
*   **Feasibility:** Sentinel-2 data is open-source, freely available, and provides historical data to train longitudinal models.

### B. MLOps Pipeline (Phase 1 Deliverables)
1.  **Data Versioning (DVC):** Satellite images are too large for standard Git repositories. DVC will be implemented to version control the geospatial datasets locally or via cloud buckets, ensuring strict reproducibility.
2.  **Feature Engineering:** 
    *   **NDWI (Normalized Difference Water Index):** To isolate water bodies and detect effluent discoloration.
    *   **NDVI (Normalized Difference Vegetation Index):** To identify unnatural weed growth caused by chemical dumping.
3.  **Experiment Tracking (MLflow):** Multiple baseline models (e.g., Random Forest, XGBoost) will be trained on engineered spectral features. MLflow will track hyperparameters, feature importance, and validation metrics (F1-score, Precision).

---

## 4. What We Will Build and Showcase
By the final review, we will showcase a fully functional, reproducible MLOps pipeline with the following components:

### 1. The MLflow Dashboard
We will demonstrate a tracked history of our model experiments, proving that we iteratively improved our model based on different spectral bands and engineered features.

### 2. The Automated Pipeline
We will showcase a pipeline script where:
*   A new satellite image is ingested.
*   The script automatically extracts NDWI/NDVI features.
*   The deployed model runs inference and outputs a classification (e.g., "Anomalous Discoloration Detected").

### 3. The "Before & After" Visualization
To make the presentation beautiful and impactful, we will display historical satellite views of the Vrishabhavathi basin alongside our model's predictions. We will visually highlight the exact coordinates where the model successfully flagged illegal effluent dumping or waste accumulation, proving the real-world viability of **EcoSentinel**.
