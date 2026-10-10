import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error
import mlflow
import mlflow.sklearn
import warnings
warnings.filterwarnings('ignore')

def create_features(df):
    """Create time series features from datetime index."""
    df = df.copy()
    df['dayofweek'] = df.index.dayofweek
    df['quarter'] = df.index.quarter
    df['month'] = df.index.month
    df['year'] = df.index.year
    df['dayofyear'] = df.index.dayofyear
    df['dayofmonth'] = df.index.day
    # Lag feature
    df['lag_1'] = df['daily_kwh'].shift(1)
    # Rolling mean
    df['rolling_mean_7'] = df['daily_kwh'].rolling(window=7).mean()
    return df.dropna()

def main():
    # Load processed data
    print("Loading data...")
    df = pd.read_csv('data/processed/bareilly_br28_daily.csv')
    df['date'] = pd.to_datetime(df['date'])
    df = df.set_index('date')
    
    # Feature Engineering
    print("Engineering features...")
    df_features = create_features(df)
    
    # Chronological Train/Test Split
    train_size = int(len(df_features) * 0.8)
    train, test = df_features.iloc[:train_size], df_features.iloc[train_size:]
    
    FEATURES = ['dayofweek', 'quarter', 'month', 'year', 'dayofyear', 'dayofmonth', 'lag_1', 'rolling_mean_7']
    TARGET = 'daily_kwh'
    
    X_train = train[FEATURES]
    y_train = train[TARGET]
    X_test = test[FEATURES]
    y_test = test[TARGET]
    
    print(f"Training on {len(train)} samples, testing on {len(test)} samples.")
    
    # Setup MLflow
    mlflow.set_experiment('CarbonCalc_Electricity_Forecasting')
    
    models = {
        'RandomForest': RandomForestRegressor(n_estimators=100, random_state=42),
        'GradientBoosting': GradientBoostingRegressor(n_estimators=100, random_state=42)
    }
    
    for name, model in models.items():
        with mlflow.start_run(run_name=name):
            print(f"Training {name}...")
            model.fit(X_train, y_train)
            predictions = model.predict(X_test)
            
            mae = mean_absolute_error(y_test, predictions)
            rmse = np.sqrt(mean_squared_error(y_test, predictions))
            
            print(f"{name} Results - MAE: {mae:.3f}, RMSE: {rmse:.3f}")
            
            # Log to MLflow
            mlflow.log_param('model_type', name)
            mlflow.log_metric('mae', mae)
            mlflow.log_metric('rmse', rmse)
            mlflow.sklearn.log_model(model, "model")
            
    print("Training complete. Run 'mlflow ui' to view the results.")

if __name__ == "__main__":
    main()
