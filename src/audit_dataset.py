
from pathlib import Path
import pandas as pd

DATA_DIR = Path("data/raw")

FILES = [
    "SM Cleaned Data MH Aggregated.csv",
    "SM Cleaned Data BR Aggregated.csv",
]

for filename in FILES:
    path = DATA_DIR / filename

    print("\n" + "=" * 70)
    print(f"FILE: {filename}")

    df = pd.read_csv(path)

    # Standardize column names for this audit only
    df.columns = df.columns.str.strip()
    df["Date"] = pd.to_datetime(df["Date"], errors="coerce")
    df["t_kWh"] = pd.to_numeric(df["t_kWh"], errors="coerce")

    print("Rows:", len(df))
    print("Meters:", df["meter"].nunique())
    print("Date range:", df["Date"].min(), "to", df["Date"].max())
    print("Missing values:\n", df.isna().sum())
    print("Duplicate meter/date pairs:",
          df.duplicated(["meter", "Date"]).sum())

    print("\nConsumption summary (kWh):")
    print(df["t_kWh"].describe())

    print("Zero-consumption rows:", (df["t_kWh"] == 0).sum())
    print("Negative-consumption rows:", (df["t_kWh"] < 0).sum())

    print("\nRecords per meter:")
    print(df.groupby("meter").size().describe())

    # Detect missing calendar dates within each meter's observed range
    gaps = []

    for meter, group in df.groupby("meter"):
        dates = group["Date"].dropna().dt.normalize()
        if dates.empty:
            continue

        expected = pd.date_range(
            dates.min(), dates.max(), freq="D"
        )
        missing = expected.difference(dates.unique())

        if len(missing):
            gaps.append({
                "meter": meter,
                "missing_days": len(missing),
                "first_missing": missing.min().date(),
                "last_missing": missing.max().date(),
            })

    print("\nMeters with missing calendar dates:", len(gaps))
    for gap in gaps[:10]:
        print(gap)
