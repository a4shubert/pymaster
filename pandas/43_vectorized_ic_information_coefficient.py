"""Lecture 43: Information Coefficient (IC) per Date (Toy)

Hedge fund relevance:
- IC measures signal predictive power (corr(signal_t, return_{t+1})).
- Common for factor evaluation and monitoring.

Key techniques:
- align next-day returns with shift
- compute per-date correlation

Note:
- Toy example using Pearson corr.
"""

import pandas as pd


def ic_by_date(df: pd.DataFrame) -> pd.Series:
    # df columns: date, ticker, signal, ret
    df = df.copy()
    df["ret_fwd"] = df.groupby("ticker")["ret"].shift(-1)

    def corr(g: pd.DataFrame) -> float:
        return float(g["signal"].corr(g["ret_fwd"]))

    return df.groupby("date").apply(corr)


if __name__ == "__main__":
    df = pd.DataFrame(
        {
            "date": pd.to_datetime(["2026-02-24"] * 3 + ["2026-02-25"] * 3 + ["2026-02-26"] * 3),
            "ticker": ["A", "B", "C"] * 3,
            "signal": [1.0, 0.5, -0.5, 0.2, 0.1, -0.1, -0.3, 0.0, 0.4],
            "ret": [0.01, -0.02, 0.00, 0.03, 0.01, -0.01, -0.01, 0.02, 0.01],
        }
    )
    print(ic_by_date(df))
