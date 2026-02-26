"""Lecture 27: Lagging + Feature Engineering (Avoid Lookahead)

Hedge fund relevance:
- Feature engineering often uses rolling stats.
- You must lag features to ensure they are known at decision time.

Key techniques:
- `shift(1)` on features
- build features from past data only
"""

import pandas as pd


def demo() -> None:
    idx = pd.date_range("2026-02-01", periods=6, freq="D")
    px = pd.Series([100, 101, 102, 101, 103, 104], index=idx, name="px")

    df = px.to_frame()
    df["ret"] = df["px"].pct_change()
    df["ma3"] = df["px"].rolling(3, min_periods=3).mean()
    df["ma3_lag1"] = df["ma3"].shift(1)

    # signal: price above lagged MA
    df["signal"] = (df["px"] > df["ma3_lag1"]).astype("Int64")

    print(df)


if __name__ == "__main__":
    demo()
