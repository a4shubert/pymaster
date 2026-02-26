"""
Technique: Categoricals for Reference Data (Speed + Memory)
Use When:
- Repeated strings (ticker, sector, venue, book) are common and expensive
- Categoricals compress memory and speed groupby operations
"""

import pandas as pd


def demo() -> None:
    df = pd.DataFrame(
        {
            "ticker": ["AAPL", "MSFT", "AAPL", "TSLA", "MSFT"],
            "sector": ["Tech", "Tech", "Tech", "Auto", "Tech"],
            "pnl": [10.0, -3.0, 5.0, 7.0, 2.0],
        }
    )

    print("before mem:", int(df.memory_usage(deep=True).sum()))
    df["ticker"] = df["ticker"].astype("category")
    df["sector"] = pd.Categorical(df["sector"], categories=["Tech", "Auto"], ordered=True)
    print("after mem:", int(df.memory_usage(deep=True).sum()))

    print(df.groupby("sector", observed=True).agg(pnl_sum=("pnl", "sum")))


if __name__ == "__main__":
    demo()
