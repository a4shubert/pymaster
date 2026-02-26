"""
Technique: Vectorized PnL (Signals -> Positions -> Returns)
Use When:
- Fast research iteration requires vectorized backtests
- A common pattern: signal -> position (shift to avoid lookahead) -> PnL
"""

import pandas as pd


def demo() -> None:
    df = pd.DataFrame(
        {
            "date": pd.date_range("2026-02-20", periods=6, freq="D"),
            "ret": [0.01, -0.02, 0.015, 0.00, -0.005, 0.02],
            "signal": [1, 1, -1, -1, 1, 1],
        }
    ).set_index("date")

    df["pos"] = df["signal"].shift(1).fillna(0)  # trade tomorrow based on today's signal
    df["strat_ret"] = df["pos"] * df["ret"]
    df["equity"] = (1 + df["strat_ret"]).cumprod()

    print(df)


if __name__ == "__main__":
    demo()
