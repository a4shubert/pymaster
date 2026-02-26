"""Lecture 15: Missing Data (dropna, fillna, ffill) for Time Series

Hedge fund relevance:
- Corporate actions, trading halts, and vendor gaps create missing values.
- You need explicit rules per dataset (prices vs fundamentals vs signals).

Key techniques:
- `isna`, `dropna`
- `ffill` for last-known price (with limits)
- careful with `fillna(0)` (can be wrong for prices/returns)
"""

import pandas as pd


def demo() -> None:
    idx = pd.date_range("2026-02-24", periods=5, freq="D")
    px = pd.Series([100.0, None, None, 103.0, None], index=idx, name="px")

    df = px.to_frame()
    df["px_ffill"] = df["px"].ffill(limit=2)
    df["ret"] = df["px"].pct_change()
    df["ret_safe"] = df["px_ffill"].pct_change()

    print(df)


if __name__ == "__main__":
    demo()
