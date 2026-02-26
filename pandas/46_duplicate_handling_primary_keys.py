"""Lecture 46: Duplicate Handling (Primary Keys) in Market Data

Hedge fund relevance:
- Vendor files sometimes duplicate records.
- You must decide a deterministic rule (last, first, max volume).

Key techniques:
- `duplicated` to detect
- `drop_duplicates(keep='last')`
- sort before dropping for determinism
"""

import pandas as pd


def demo() -> None:
    df = pd.DataFrame(
        {
            "ts": pd.to_datetime(["2026-02-26T14:30:00Z", "2026-02-26T14:30:00Z", "2026-02-26T14:31:00Z"], utc=True),
            "ticker": ["AAPL", "AAPL", "AAPL"],
            "price": [100.0, 100.1, 100.2],
            "seq": [1, 2, 3],
        }
    )

    # Deterministic: keep the record with the highest seq.
    df = df.sort_values(["ts", "ticker", "seq"]).drop_duplicates(["ts", "ticker"], keep="last")
    print(df)


if __name__ == "__main__":
    demo()
