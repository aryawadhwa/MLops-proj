
from pathlib import Path
import pandas as pd

path = Path("data/raw/SM Cleaned Data BR Aggregated.csv")
df = pd.read_csv(path)

df["Date"] = pd.to_datetime(df["Date"]).dt.normalize()
df["t_kWh"] = pd.to_numeric(df["t_kWh"], errors="coerce")

# Top six candidates from the coverage report
candidates = ["BR28", "BR45", "BR49", "BR26", "BR51", "BR06"]

for meter in candidates:
    group = (
        df[df["meter"] == meter]
        .sort_values("Date")
        .copy()
    )

    if group.empty:
        continue

    dates = pd.date_range(
        group["Date"].min(),
        group["Date"].max(),
        freq="D"
    )

    daily = (
        group.set_index("Date")["t_kWh"]
        .reindex(dates)
    )

    zero_mask = daily.eq(0).fillna(False)

    # Maximum consecutive run of observed zero-consumption days
    run_lengths = (
        zero_mask.groupby((zero_mask != zero_mask.shift()).cumsum())
        .sum()
    )
    max_zero_run = int(run_lengths.max()) if len(run_lengths) else 0

    print("\n" + "=" * 60)
    print("Meter:", meter)
    print("Date range:", daily.index.min().date(), "to",
          daily.index.max().date())
    print("Observed days:", int(daily.notna().sum()))
    print("Missing days:", int(daily.isna().sum()))
    print("Zero days:", int(zero_mask.sum()))
    print("Longest consecutive zero run:", max_zero_run)
    print("Consumption summary:")
    print(daily.describe().round(3))
    print("Lowest 10 observed values:")
    print(daily.dropna().nsmallest(10).to_string())
