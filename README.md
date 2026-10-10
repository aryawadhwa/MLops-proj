# CarbonCalc

CarbonCalc is a project focused on helping households and organizations understand their environmental impact and identify ways to reduce it.

The long-term idea is to collect information about activities such as electricity consumption, transportation, water usage, food consumption and physical waste. This information can be used to estimate environmental impact and, eventually, identify patterns and forecast future consumption.

For the initial MLOps phase, we are starting with one specific part of the project: **forecasting household electricity consumption using Indian smart-meter data**.

## Current Scope

Phase 1 focuses on building a basic, reproducible machine-learning pipeline. Rather than trying to implement every feature of CarbonCalc at once, we are first establishing the data and modelling workflow that the rest of the project can build on.

Our initial task is to use historical daily electricity consumption to predict next-day consumption and evaluate the predictions on a later, unseen period.

## Dataset

We are using the *What Smart Meters Can Tell Us: Insights on Electricity Supply and Use in Mathura and Bareilly Households* dataset, published by the Council on Energy, Environment and Water (CEEW).

- **Dataset source:** [Harvard Dataverse](https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi:10.7910/DVN/GOCHJH)
- **Geographic coverage:** Mathura and Bareilly, Uttar Pradesh, India.
- **Original observation frequency:** Three-minute intervals.
- **Available period:** Approximately 2019–2021, depending on the meter and location.
- **Initial selection:** Bareilly meter BR28.

We selected BR28 for the first experiment because its daily aggregated data has relatively high date coverage and no recorded zero-consumption days in the initial audit.

The source dataset contains daily aggregated readings as well as higher-frequency measurements. We compared daily totals calculated from the raw three-minute readings with the published aggregated data for overlapping dates in 2020 and 2021. The values matched exactly for the dates checked.

### Dataset limitations

The selected data represents one household meter in Bareilly. It is useful for developing and testing the initial forecasting pipeline, but it is not representative of every Indian household.

The observations are also historical, and some calendar dates are missing. These gaps must be handled carefully rather than automatically treating missing readings as zero.

## Work Completed

### 1. Dataset acquisition and inspection

- Obtained the CEEW smart-meter dataset and read its accompanying documentation.
- Inspected the available raw and aggregated CSV files.
- Examined column names, dataset sizes, missing values and duplicate records.
- Compared date coverage and zero-consumption readings across meters in Mathura and Bareilly.

### 2. Meter selection

Bareilly was selected for the initial experiment because its aggregated dataset showed better overall date coverage than Mathura in our initial audit.

Meter BR28 was selected for the first experiment based on its observed history and data-quality checks. Other meters will remain candidates for later experiments.

### 3. Aggregation validation

We compared the published daily readings for BR28 against the sums of its raw three-minute electricity-consumption readings for overlapping dates in 2020 and 2021.

The mean and maximum absolute differences were both 0.0 kWh for the dates compared. This supports the aggregation method for those dates, although it does not establish that every reading in the full dataset has been independently validated.

### 4. Initial preprocessing

A Python preprocessing script was created at `src/preprocess.py`.

It:
- Selects meter BR28 from the aggregated Bareilly dataset.
- Converts dates and electricity-consumption values to the appropriate data types.
- Removes rows with invalid dates or consumption values.
- Checks for duplicate dates and negative consumption.
- Retains the date and daily electricity-consumption columns.
- Saves the resulting dataset to `data/processed/bareilly_br28_daily.csv`.

The resulting dataset contains **827 daily observations**, covering 17 July 2019 to 31 October 2021.

The processed CSV has no missing cells or duplicate dates. There are still 11 missing calendar dates, which have not been filled with artificial zero values.

## Repository Structure

```text
CarbonCalc/
├── data/
│   ├── raw/
│   └── processed/
│       └── bareilly_br28_daily.csv
├── docs/
│   └── dataset_card.md
├── notebooks/
├── src/
│   ├── audit_dataset.py
│   ├── check_meter_coverage.py
│   ├── inspect_candidates.py
│   ├── validate_aggregation.py
│   └── preprocess.py
├── reports/
├── models/
├── README.md
├── LICENSE
└── .gitignore
```

This structure describes the intended project layout. Some directories may still be empty, and the dataset files are not listed individually because the raw data is stored separately from the code.

## Planned Work

The next stages of Phase 1 are:

1. Finalize the dataset documentation and selection criteria.
2. Configure DVC to track the raw and processed datasets.
3. Commit the code and DVC metadata to Git and push the repository to GitHub.
4. Perform exploratory data analysis (EDA).
5. Develop forecasting features, including historical consumption and calendar information.
6. Establish a simple baseline and train Random Forest and Gradient Boosting regressors.
7. Evaluate the models using a chronological train/test split and metrics such as MAE and RMSE.
8. Use MLflow to record experiment parameters and evaluation metrics.
9. Document how to reproduce the workflow and its results.

## Team Approach

CarbonCalc is being developed as a team project. The aim is to build the pipeline incrementally, understand the decisions behind each stage, and keep the code and experiments reproducible so that other team members can inspect and extend the work.

The current implementation is an initial forecasting experiment, not a completed production system. The wider CarbonCalc application, additional environmental categories, recommendations and longer-term forecasting remain future work.