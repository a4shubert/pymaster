"""Lecture 14: MultiIndex, stack/unstack (Panel Data)

Hedge fund relevance:
- A common representation is (date, ticker) -> fields.
- stack/unstack reshapes between panel (MultiIndex) and matrix forms.

Key techniques:
- `set_index([...]).sort_index()`
- `unstack` to wide (columns by ticker)
- `stack` back to long/panel
"""

import pandas as pd


def demo() -> None:
    df = pd.DataFrame(
        {
            "date": ["2026-02-24", "2026-02-24", "2026-02-25", "2026-02-25"],
            "ticker": ["AAPL", "MSFT", "AAPL", "MSFT"],
            "close": [100.0, 200.0, 101.0, 201.0],
        }
    )
    df["date"] = pd.to_datetime(df["date"])

    panel = df.set_index(["date", "ticker"]).sort_index()
    wide = panel["close"].unstack("ticker")
    back = wide.stack("ticker").rename("close").to_frame()

    print("panel:\n", panel)
    print("\nwide:\n", wide)
    print("\nback:\n", back)


if __name__ == "__main__":
    demo()
