"""Lecture 20: Vectorized PnL (Signals -> Positions -> Returns)

Hedge fund relevance:
- Fast research iteration requires vectorized backtests.
- A common pattern: signal -> position (shift to avoid lookahead) -> PnL.

Key techniques:
- `shift(1)` to prevent lookahead bias
- elementwise multiply for strategy returns
- cumprod for equity curve

Warning:
- This is a toy example (no costs, slippage, borrow, constraints).
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
