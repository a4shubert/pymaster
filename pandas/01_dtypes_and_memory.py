"""Lecture 01: Dtypes and Memory Discipline (Trading Data at Scale)

Hedge fund relevance:
- Market/position data gets large quickly; dtype choices drive latency and cost.
- Use nullable dtypes for clean missing handling without object columns.
- Use categoricals for repeated strings (tickers, venues, sectors).

Key techniques:
- `astype` to numeric/nullable types
- `category` dtype
- `memory_usage(deep=True)`

Run:
- Requires `pandas` installed.
"""

import pandas as pd


def demo() -> None:
    df = pd.DataFrame(
        {
            "ticker": ["AAPL", "AAPL", "MSFT", "MSFT"],
            "venue": ["NASDAQ", "NASDAQ", "NASDAQ", "NASDAQ"],
            "qty": [100, 200, None, 50],
            "price": [189.1, 190.2, 412.0, None],
        }
    )

    print("before dtypes:\n", df.dtypes)
    print("before mem:", int(df.memory_usage(deep=True).sum()), "bytes")

    df["ticker"] = df["ticker"].astype("category")
    df["venue"] = df["venue"].astype("category")
    df["qty"] = df["qty"].astype("Int64")
    df["price"] = df["price"].astype("Float64")

    print("\nafter dtypes:\n", df.dtypes)
    print("after mem:", int(df.memory_usage(deep=True).sum()), "bytes")
    print("\nnormalized:\n", df)


if __name__ == "__main__":
    demo()
