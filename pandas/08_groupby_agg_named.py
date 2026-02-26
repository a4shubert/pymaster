"""Lecture 08: groupby + Named Aggregations

Hedge fund relevance:
- Summarize exposures by sector, region, book, PM.
- Named aggregations produce clean column names (no MultiIndex columns).

Key techniques:
- `groupby(...).agg(col=('src','func'))`
- `as_index=False` vs index output
"""

import pandas as pd


def demo() -> None:
    positions = pd.DataFrame(
        {
            "pm": ["A", "A", "B", "B"],
            "sector": ["Tech", "Energy", "Tech", "Tech"],
            "mv": [10_000, -2_000, 5_000, 7_000],
            "dv01": [120, -10, 40, 55],
        }
    )

    summary = (
        positions.groupby(["pm", "sector"], as_index=False)
        .agg(mv_sum=("mv", "sum"), dv01_sum=("dv01", "sum"), n=("mv", "size"))
        .sort_values(["pm", "sector"])
    )

    print(summary)


if __name__ == "__main__":
    demo()
