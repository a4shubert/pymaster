"""Lecture 41: Wide Returns Matrix + Alignment Discipline

Hedge fund relevance:
- Many risk/signal ops assume a (date x ticker) matrix.
- Alignment errors are the #1 silent bug in matrix-based work.

Key techniques:
- Build wide matrix with pivot/unstack
- `sort_index` and `sort_index(axis=1)`
- Explicitly align by index/columns before math
"""

import pandas as pd


def demo() -> None:
    long = pd.DataFrame(
        {
            "date": ["2026-02-24", "2026-02-24", "2026-02-25", "2026-02-25"],
            "ticker": ["AAPL", "MSFT", "AAPL", "MSFT"],
            "ret": [0.01, -0.02, 0.03, 0.01],
        }
    )
    long["date"] = pd.to_datetime(long["date"])

    wide = long.pivot(index="date", columns="ticker", values="ret").sort_index().sort_index(axis=1)
    print(wide)

    # Example alignment-safe operation: cross-sectional mean per date
    cs_mean = wide.mean(axis=1)
    print("\ncs_mean:\n", cs_mean)


if __name__ == "__main__":
    demo()
