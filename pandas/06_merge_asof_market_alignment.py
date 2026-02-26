"""Lecture 06: merge_asof (Align Trades to Quotes/Bars)

Hedge fund relevance:
- You often need the last known quote before a trade (or a bar close).
- Regular merge fails because timestamps rarely match exactly.

Key techniques:
- `pd.merge_asof(..., direction='backward', tolerance=...)`
- sort by the key first
"""

import pandas as pd


def demo() -> None:
    quotes = pd.DataFrame(
        {
            "ts": pd.to_datetime(
                [
                    "2026-02-26T14:30:00Z",
                    "2026-02-26T14:30:30Z",
                    "2026-02-26T14:31:00Z",
                ],
                utc=True,
            ),
            "bid": [99.9, 100.0, 100.1],
            "ask": [100.1, 100.2, 100.3],
        }
    ).sort_values("ts")

    trades = pd.DataFrame(
        {
            "trade_id": [1, 2],
            "ts": pd.to_datetime(["2026-02-26T14:30:35Z", "2026-02-26T14:31:10Z"], utc=True),
            "price": [100.15, 100.25],
        }
    ).sort_values("ts")

    aligned = pd.merge_asof(
        trades,
        quotes,
        on="ts",
        direction="backward",
        tolerance=pd.Timedelta("45s"),
    )

    aligned["mid"] = (aligned["bid"] + aligned["ask"]) / 2
    print(aligned)


if __name__ == "__main__":
    demo()
