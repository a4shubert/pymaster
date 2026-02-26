"""Lecture 26: Time Series Joins for Many Assets (Panel Merge)

Hedge fund relevance:
- Combine returns + signals + fundamentals keyed by (date, ticker).
- MultiIndex joins prevent accidental cartesian products.

Key techniques:
- set MultiIndex and join on index
- `join(..., how='inner'/'left')`
- verify row counts and missingness
"""

import pandas as pd


def demo() -> None:
    idx = pd.MultiIndex.from_product(
        [pd.to_datetime(["2026-02-24", "2026-02-25"]), ["AAPL", "MSFT"]],
        names=["date", "ticker"],
    )

    rets = pd.DataFrame({"ret": [0.01, -0.02, 0.03, 0.01]}, index=idx)
    sig = pd.DataFrame({"signal": [1, 0, -1, 1]}, index=idx)

    panel = rets.join(sig, how="inner")
    print(panel)


if __name__ == "__main__":
    demo()
