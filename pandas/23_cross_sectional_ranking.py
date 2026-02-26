"""
Technique: Cross-Sectional Ranking (Signals)
Use When:
- Many strategies rank assets daily (momentum, value, quality)
- Ranks are robust to outliers compared to raw values
"""

import pandas as pd


def demo() -> None:
    df = pd.DataFrame(
        {
            "date": ["2026-02-24"] * 4 + ["2026-02-25"] * 4,
            "ticker": ["A", "B", "C", "D"] * 2,
            "signal": [1.0, 2.0, 2.0, -1.0, 0.5, 0.2, 1.5, 1.5],
        }
    )
    df["date"] = pd.to_datetime(df["date"])

    df["rank_pct"] = df.groupby("date")["signal"].rank(pct=True, method="average")
    print(df.sort_values(["date", "rank_pct"]))


if __name__ == "__main__":
    demo()
