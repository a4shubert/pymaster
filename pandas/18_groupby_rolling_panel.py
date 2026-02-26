"""Lecture 18: groupby + rolling (Per-Asset Rolling Metrics)

Hedge fund relevance:
- Compute rolling vol per ticker across dates.
- Avoid Python loops by using groupby+rolling.

Key techniques:
- `groupby('ticker')['ret'].rolling(window).std()`
- `reset_index(level=0, drop=True)` to align back to original index
"""

import pandas as pd


def demo() -> None:
    df = pd.DataFrame(
        {
            "date": ["2026-02-24", "2026-02-25", "2026-02-26", "2026-02-24", "2026-02-25", "2026-02-26"],
            "ticker": ["AAPL", "AAPL", "AAPL", "MSFT", "MSFT", "MSFT"],
            "ret": [0.01, -0.02, 0.03, 0.00, 0.01, -0.01],
        }
    )
    df["date"] = pd.to_datetime(df["date"])
    df = df.sort_values(["ticker", "date"]).reset_index(drop=True)

    df["vol_2"] = (
        df.groupby("ticker")["ret"].rolling(2, min_periods=2).std(ddof=0).reset_index(level=0, drop=True)
    )

    print(df)


if __name__ == "__main__":
    demo()
