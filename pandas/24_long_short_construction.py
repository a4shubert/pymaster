"""Lecture 24: Long/Short Portfolio Construction (Toy)

Hedge fund relevance:
- Most equity L/S flows: rank -> pick top/bottom -> equal weight or score weight.
- Important: shift positions to avoid lookahead bias.

Key techniques:
- rank -> bucket selection
- groupby to normalize weights

Warning:
- Toy example: ignores costs, constraints, borrow, liquidity.
"""

import pandas as pd


def make_weights(df: pd.DataFrame, long_n: int, short_n: int) -> pd.Series:
    df = df.copy()
    df["rank"] = df.groupby("date")["signal"].rank(method="first", ascending=False)

    def bucket(g: pd.DataFrame) -> pd.Series:
        longs = g["rank"] <= long_n
        shorts = g["rank"] > (len(g) - short_n)

        w = pd.Series(0.0, index=g.index)
        if longs.any():
            w.loc[longs] = 1.0 / longs.sum()
        if shorts.any():
            w.loc[shorts] = -1.0 / shorts.sum()
        return w

    return df.groupby("date", group_keys=False).apply(bucket)


if __name__ == "__main__":
    df = pd.DataFrame(
        {
            "date": ["2026-02-24"] * 4,
            "ticker": ["A", "B", "C", "D"],
            "signal": [1.0, 2.0, 0.0, -1.0],
        }
    )
    df["date"] = pd.to_datetime(df["date"])

    df["w"] = make_weights(df, long_n=1, short_n=1)
    print(df)
