"""Lecture 49: Benchmark-Relative Returns (Alpha)

Hedge fund relevance:
- Many reports are relative to a benchmark (SPX, sector index).
- Requires careful date alignment.

Key techniques:
- align series by index
- compute excess returns
"""

import pandas as pd


def demo() -> None:
    idx = pd.date_range("2026-02-01", periods=5, freq="D")
    strat = pd.Series([0.01, -0.02, 0.015, 0.0, 0.005], index=idx, name="strat")
    bench = pd.Series([0.008, -0.01, 0.010, 0.001, 0.002], index=idx, name="bench")

    aligned = pd.concat([strat, bench], axis=1, join="inner")
    aligned["excess"] = aligned["strat"] - aligned["bench"]
    print(aligned)


if __name__ == "__main__":
    demo()
