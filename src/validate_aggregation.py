
from pathlib import Path
import pandas as pd

DATA_DIR = Path("data/raw")

# Read the aggregated data
aggregated = pd.read_csv(
    DATA_DIR / "SM Cleaned Data BR Aggregated.csv"
)

aggregated["Date"] = pd.to_datetime(aggregated["Date"])
aggregated = aggregated[aggregated["meter"] == "BR28"].copy()

# Inspect raw files to locate BR28
raw_files = sorted(DATA_DIR.glob("CEEW - Smart meter data Bareilly *.csv"))

for path in raw_files:
    print(f"\nChecking {path.name}")

    raw = pd.read_csv(path)

    if "meter" not in raw.columns:
        continue

    raw = raw[raw["meter"] == "BR28"].copy()

    if raw.empty:
        print("No BR28 records in this file.")
        continue

    raw["x_Timestamp"] = pd.to_datetime(raw["x_Timestamp"])
    raw["Date"] = raw["x_Timestamp"].dt.normalize()

    print("Raw rows:", len(raw))
    print("Raw date range:", raw["Date"].min(), "to", raw["Date"].max())

    # Compare daily sums on dates present in both datasets
    raw_daily = raw.groupby("Date")["t_kWh"].sum()
    agg_daily = aggregated.groupby("Date")["t_kWh"].first()

    comparison = pd.concat(
        [
            raw_daily.rename("raw_sum_kWh"),
            agg_daily.rename("aggregated_kWh"),
        ],
        axis=1,
        join="inner",
    ).dropna()

    if comparison.empty:
        print("No overlapping dates to compare.")
        continue

    comparison["absolute_difference"] = (
        comparison["raw_sum_kWh"] - comparison["aggregated_kWh"]
    ).abs()

    print("\nSample comparison:")
    print(comparison.head(10).round(4).to_string())

    print(
        "\nMean absolute difference:",
        round(comparison["absolute_difference"].mean(), 6),
        "kWh",
    )
    print(
        "Maximum absolute difference:",
        round(comparison["absolute_difference"].max(), 6),
        "kWh",
    )
