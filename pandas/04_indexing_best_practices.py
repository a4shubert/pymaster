"""
Technique: Indexing Best Practices (DatetimeIndex, MultiIndex)
Use When:
- Time series operations (resample/rolling) are easiest with DatetimeIndex
- Panel data (date x asset) is natural with MultiIndex
"""

import pandas as pd


def demo() -> None:
    dates = pd.date_range("2026-02-24", periods=3, freq="D", tz="UTC")
    tickers = ["AAPL", "MSFT"]

    idx = pd.MultiIndex.from_product([dates, tickers], names=["ts", "ticker"])
    df = pd.DataFrame({"close": [100, 200, 101, 201, 102, 202]}, index=idx).sort_index()

    print("panel:\n", df)
    print("\nAAPL slice:\n", df.loc[(slice(None), "AAPL"), :])


if __name__ == "__main__":
    demo()
