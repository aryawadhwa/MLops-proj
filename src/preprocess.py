
from pathlib import Path
import pandas as pd

RAW_FILE = Path("data/raw/SM Cleaned Data BR Aggregated.csv")
OUTPUT_FILE = Path("data/processed/bareilly_br28_daily.csv")

# Load the source dataset
df = pd.read_csv(RAW_FILE)

# Select the chosen household meter
df = df[df["meter"] == "BR28"].copy()

# Standardize and validate columns
df["Date"] = pd.to_datetime(df["Date"], errors="coerce")
df["t_kWh"] = pd.to_numeric(df["t_kWh"], errors="coerce")

df = df.dropna(subset=["Date", "t_kWh"])
df["Date"] = df["Date"].dt.normalize()
df = df.sort_values("Date")

# Ensure there is only one record per date
if df["Date"].duplicated().any():
    raise ValueError("Duplicate dates found for BR28.")

if (df["t_kWh"] < 0).any():
    raise ValueError("Negative electricity consumption found.")

# Keep only the columns required for the first forecasting task
processed = df[["Date", "t_kWh"]].rename(
    columns={
        "Date": "date",
        "t_kWh": "daily_kwh",
    }
)

# Save the processed dataset
OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)
processed.to_csv(OUTPUT_FILE, index=False)

print("Preprocessing complete.")
print("Output:", OUTPUT_FILE)
print("Rows:", len(processed))
print("Date range:", processed["date"].min(), "to",
      processed["date"].max())
print("Missing values:\n", processed.isna().sum())
print("Duplicate dates:", processed["date"].duplicated().sum())
print("\nSummary:")
print(processed["daily_kwh"].describe().round(3))
