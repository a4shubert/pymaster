"""Lecture 40: Stability + Reproducibility (Determinism)

Hedge fund relevance:
- Research must be reproducible to be trusted.
- Deterministic outputs reduce debugging time and deployment risk.

Key techniques:
- stable sorting before group operations
- explicit random seeds
- avoid depending on implicit index order
"""

import numpy as np
import pandas as pd


def demo() -> None:
    rng = np.random.default_rng(42)

    df = pd.DataFrame(
        {
            "date": ["2026-02-24"] * 5,
            "ticker": ["B", "A", "E", "C", "D"],
            "signal": rng.normal(size=5),
        }
    )
    df["date"] = pd.to_datetime(df["date"])

    # Stable order to avoid surprises when breaking ties.
    df = df.sort_values(["date", "ticker"], kind="mergesort").reset_index(drop=True)

    df["rank"] = df.groupby("date")["signal"].rank(method="first", ascending=False)
    print(df)


if __name__ == "__main__":
    demo()
