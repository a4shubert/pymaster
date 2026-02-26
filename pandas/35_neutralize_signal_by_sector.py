"""Lecture 35: Sector Neutralization (Demean within Group)

Hedge fund relevance:
- Removes sector tilts from signals.
- Often used as a cheap, robust neutralization step.

Key techniques:
- groupby transform with mean
- create neutralized signal = signal - group_mean
"""

import pandas as pd


def demo() -> None:
    df = pd.DataFrame(
        {
            "date": ["2026-02-24"] * 6,
            "ticker": list("ABCDEF"),
            "sector": ["Tech", "Tech", "Tech", "Energy", "Energy", "Energy"],
            "signal": [1.0, 2.0, -1.0, 0.2, 0.1, 0.5],
        }
    )
    df["date"] = pd.to_datetime(df["date"])

    grp_mean = df.groupby(["date", "sector"])["signal"].transform("mean")
    df["signal_neutral"] = df["signal"] - grp_mean
    print(df)


if __name__ == "__main__":
    demo()
