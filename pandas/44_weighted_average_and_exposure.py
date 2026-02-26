"""Lecture 44: Weighted Averages + Exposure Attribution

Hedge fund relevance:
- Portfolio-level metrics are weighted by positions.
- Exposure decomposition by sector/book is core reporting.

Key techniques:
- weighted average
- groupby weighted sums
"""

import pandas as pd


def weighted_avg(values: pd.Series, weights: pd.Series) -> float:
    w = weights.astype(float)
    v = values.astype(float)
    if w.abs().sum() == 0:
        return 0.0
    return float((v * w).sum() / w.sum())


if __name__ == "__main__":
    df = pd.DataFrame(
        {
            "ticker": ["AAPL", "MSFT", "XOM"],
            "sector": ["Tech", "Tech", "Energy"],
            "w": [0.05, -0.02, 0.03],
            "beta": [1.1, 1.0, 0.8],
        }
    )

    df["beta_contrib"] = df["w"] * df["beta"]
    by_sector = df.groupby("sector", as_index=False).agg(
        net_w=("w", "sum"),
        beta_exposure=("beta_contrib", "sum"),
    )

    print(by_sector)
