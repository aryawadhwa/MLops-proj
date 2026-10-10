# Phase 1 Evaluation Results

The models were evaluated using a chronological train/test split (80% train, 20% test) on the daily aggregated electricity consumption data for Bareilly Meter BR28 (`bareilly_br28_daily.csv`).

## Model Metrics

| Model | Mean Absolute Error (MAE) | Root Mean Squared Error (RMSE) |
| :--- | :--- | :--- |
| **Random Forest** | 0.818 kWh | 1.338 kWh |
| **Gradient Boosting** | 0.761 kWh | 1.337 kWh |

## Conclusion
The **Gradient Boosting** model slightly outperforms the Random Forest model across both metrics, forecasting daily electricity consumption with an average absolute error of just 0.761 kWh.
