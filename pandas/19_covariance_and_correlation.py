"""Lecture 19: Covariance/Correlation Matrices (Risk + Diversification)

Hedge fund relevance:
- Portfolio risk models start with cov/corr of returns.
- Proper alignment and missing handling are critical.

Key techniques:
- wide returns matrix (date x ticker)
- `corr()` and `cov()`
"""

import pandas as pd


def demo() -> None:
    rets = pd.DataFrame(
        {
            "date": pd.to_datetime(["2026-02-24", "2026-02-25", "2026-02-26"]),
            "AAPL": [0.01, -0.02, 0.03],
            "MSFT": [0.00, 0.01, -0.01],
            "TSLA": [0.02, -0.03, 0.01],
        }
    ).set_index("date")

    print("corr:\n", rets.corr())
    print("\ncov:\n", rets.cov())


if __name__ == "__main__":
    demo()
