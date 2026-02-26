"""
Technique: Vectorization vs apply (Speed for Research -> Prod)
Use When:
- The difference between vectorized ops and row-wise apply can be minutes vs seconds
- Prefer NumPy/pandas vector ops; reserve apply for unavoidable Python logic
"""

import pandas as pd


def demo() -> None:
    df = pd.DataFrame({"price": [100.0, 50.0, 200.0], "qty": [10, 0, 5]})

    # Vectorized notional
    df["notional"] = df["price"] * df["qty"]

    # Vectorized safe notional (qty must be > 0)
    df["notional_safe"] = df["notional"].where(df["qty"] > 0)

    print(df)


if __name__ == "__main__":
    demo()
