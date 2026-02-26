"""
Technique: Cross-Sectional Neutralization (Demean Matrix)
Use When:
- A cheap neutralization step is to remove the per-date mean
- Helps reduce unwanted net exposure when signals are biased
"""

import pandas as pd


def demean_by_date(wide: pd.DataFrame) -> pd.DataFrame:
    row_mean = wide.mean(axis=1)
    return wide.sub(row_mean, axis=0)


if __name__ == "__main__":
    wide = pd.DataFrame(
        {
            "A": [0.1, 0.2, -0.1],
            "B": [0.0, 0.1, 0.0],
            "C": [-0.1, -0.3, 0.2],
        },
        index=pd.date_range("2026-02-24", periods=3, freq="D"),
    )
    print("raw:\n", wide)
    print("\ndemeaned:\n", demean_by_date(wide))
