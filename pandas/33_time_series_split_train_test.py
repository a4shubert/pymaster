"""
Technique: Time Series Train/Test Split (No Leakage)
Use When:
- Random splits leak future information
- Always split by time (and often embargo around events)
"""

import pandas as pd


def time_split(df: pd.DataFrame, split_date: str) -> tuple[pd.DataFrame, pd.DataFrame]:
    split_ts = pd.Timestamp(split_date)
    train = df.loc[df.index < split_ts].copy()
    test = df.loc[df.index >= split_ts].copy()
    return train, test


if __name__ == "__main__":
    df = pd.DataFrame({"ret": [0.01, -0.02, 0.03, 0.01]}, index=pd.date_range("2026-02-01", periods=4, freq="D"))
    train, test = time_split(df, "2026-02-03")
    print("train:\n", train)
    print("\ntest:\n", test)
