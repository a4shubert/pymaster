"""Lecture 48: Fast String Ops (Cleaning Symbol IDs)

Hedge fund relevance:
- Identifiers arrive messy (spaces, case, vendor suffixes).
- Vectorized string methods keep it fast and consistent.

Key techniques:
- `Series.str.strip/lower/replace`
- avoid Python loops
"""

import pandas as pd


def demo() -> None:
    s = pd.Series([" AAPL ", "msft", "BRK.B ", None], dtype="string")
    cleaned = s.str.strip().str.upper().str.replace(".", "-", regex=False)
    print(pd.DataFrame({"raw": s, "cleaned": cleaned}))


if __name__ == "__main__":
    demo()
