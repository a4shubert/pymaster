"""Lecture 39: Vectorized Position Limits (Clipping Weights)

Hedge fund relevance:
- Constraints (per-name, gross/net exposure) are central in real portfolios.
- First pass can clip per-name weights before more advanced optimization.

Key techniques:
- `clip` for per-asset limit
- compute gross/net exposure
"""

import pandas as pd


def demo() -> None:
    w = pd.Series({"AAPL": 0.12, "MSFT": -0.08, "TSLA": 0.20, "XOM": -0.15}, name="w")
    w_limited = w.clip(lower=-0.10, upper=0.10)

    gross = w_limited.abs().sum()
    net = w_limited.sum()

    print("raw:\n", w)
    print("\nlimited:\n", w_limited)
    print("\ngross:", float(gross), "net:", float(net))


if __name__ == "__main__":
    demo()
