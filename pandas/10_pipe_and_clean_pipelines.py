"""Lecture 10: pipe for Clean Data Pipelines

Hedge fund relevance:
- Research code becomes production-like when pipelines are explicit.
- `pipe` reduces intermediate variables and encourages reusable steps.

Key techniques:
- `df.pipe(fn, ...)`
- small single-purpose functions
"""

import pandas as pd


def to_utc(df: pd.DataFrame) -> pd.DataFrame:
    out = df.copy()
    out["ts"] = pd.to_datetime(out["ts"], utc=True)
    return out


def add_mid(df: pd.DataFrame) -> pd.DataFrame:
    out = df.copy()
    out["mid"] = (out["bid"] + out["ask"]) / 2
    return out


def filter_spread(df: pd.DataFrame, max_spread: float) -> pd.DataFrame:
    out = df.copy()
    out["spread"] = out["ask"] - out["bid"]
    return out.loc[out["spread"] <= max_spread, ["ts", "mid", "spread"]]


if __name__ == "__main__":
    quotes = pd.DataFrame(
        {
            "ts": ["2026-02-26T14:30:00Z", "2026-02-26T14:31:00Z"],
            "bid": [99.9, 100.1],
            "ask": [100.2, 100.3],
        }
    )

    cleaned = quotes.pipe(to_utc).pipe(add_mid).pipe(filter_spread, max_spread=0.25)
    print(cleaned)
