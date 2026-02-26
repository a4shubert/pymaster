"""Lecture 25: Event-Driven-ish Backtest with Vectorization

Hedge fund relevance:
- Many real systems are event-driven, but research often approximates with
  daily bars and vector ops.

Key techniques:
- generate positions from signals
- apply returns with shift
- compute turnover (proxy for costs)
"""

import pandas as pd


def demo() -> None:
    df = pd.DataFrame(
        {
            "date": pd.date_range("2026-02-20", periods=6, freq="D"),
            "signal": [0, 1, 1, -1, -1, 0],
            "ret": [0.01, -0.02, 0.015, 0.00, -0.005, 0.02],
        }
    ).set_index("date")

    df["pos"] = df["signal"].shift(1).fillna(0)
    df["turnover"] = df["pos"].diff().abs().fillna(0)

    df["strat_ret"] = df["pos"] * df["ret"]
    df["equity"] = (1 + df["strat_ret"]).cumprod()

    print(df)


if __name__ == "__main__":
    demo()
