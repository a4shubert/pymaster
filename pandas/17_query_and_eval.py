"""Lecture 17: query/eval for Fast, Readable Filtering

Hedge fund relevance:
- Analysts write lots of filters (liquidity, borrow cost, universe rules).
- `query` reads closer to a DSL and can be faster than chained masks.

Key techniques:
- `df.query('price > 100 and qty >= 50')`
- `df.eval('notional = price * qty')`

Note:
- Avoid using untrusted strings.
"""

import pandas as pd


def demo() -> None:
    df = pd.DataFrame({"ticker": ["AAPL", "MSFT", "TSLA"], "price": [190.2, 412.0, 210.0], "qty": [100, 10, 60]})
    df = df.eval("notional = price * qty")
    filt = df.query("price > 200 and qty >= 50")
    print(df)
    print("\nfiltered:\n", filt)


if __name__ == "__main__":
    demo()
