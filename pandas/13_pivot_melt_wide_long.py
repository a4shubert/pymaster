# Technique: Wide vs Long (pivot, pivot_table, melt)
# Use When:
# - Research often needs wide matrices (date x ticker returns)
# - Storage/ETL often prefers long format (tidy records)

import pandas as pd


def demo() -> None:
    df = pd.DataFrame(
        {
            "date": ["2026-02-24", "2026-02-24", "2026-02-25", "2026-02-25"],
            "ticker": ["AAPL", "MSFT", "AAPL", "MSFT"],
            "ret": [0.01, -0.02, 0.03, 0.01],
        }
    )
    df["date"] = pd.to_datetime(df["date"])

    wide = df.pivot(index="date", columns="ticker", values="ret")
    long = wide.reset_index().melt(id_vars=["date"], var_name="ticker", value_name="ret")

    print("wide:\n", wide)
    print("\nlong:\n", long.sort_values(["date", "ticker"]))


if __name__ == "__main__":
    demo()
