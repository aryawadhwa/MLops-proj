
from pathlib import Path
import pandas as pd

DATA_DIR = Path("data/raw")

FILES = {
    "Mathura": "SM Cleaned Data MH Aggregated.csv",
    "Bareilly": "SM Cleaned Data BR Aggregated.csv",
}

for city, filename in FILES.items():
    df = pd.read_csv(DATA_DIR / filename)

    df["Date"] = pd.to_datetime(df["Date"]).dt.normalize()
    df["t_kWh"] = pd.to_numeric(df["t_kWh"], errors="coerce")

    results = []

    for meter, group in df.groupby("meter"):
        group = group.sort_values("Date")

        first_date = group["Date"].min()
        last_date = group["Date"].max()

        # Expected calendar days between the first and last observation
        expected_days = (last_date - first_date).days + 1
        observed_days = group["Date"].nunique()

        results.append({
            "city": city,
            "meter": meter,
            "first_date": first_date.date(),
            "last_date": last_date.date(),
            "observed_days": observed_days,
            "expected_days": expected_days,
            "coverage_pct": round(
                100 * observed_days / expected_days, 2
            ),
            "zero_days": int((group["t_kWh"] == 0).sum()),
            "median_kWh": round(group["t_kWh"].median(), 3),
        })

    report = pd.DataFrame(results)
    report = report.sort_values(
        "coverage_pct", ascending=False
    )

    output = Path("reports") / f"{city.lower()}_meter_coverage.csv"
    output.parent.mkdir(parents=True, exist_ok=True)
    report.to_csv(output, index=False)

    print(f"\n{'=' * 70}")
    print(f"{city}: meter coverage")
    print(report.to_string(index=False))
    print("\nCoverage summary:")
    print(report["coverage_pct"].describe())
    print(f"\nSaved report to {output}")
