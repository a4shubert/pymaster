"""
Technique: Fast String Ops (Cleaning Symbol IDs)
Use When:
- Identifiers arrive messy (spaces, case, vendor suffixes)
- Vectorized string methods keep it fast and consistent
"""

import pandas as pd


def demo() -> None:
    s = pd.Series([" AAPL ", "msft", "BRK.B ", None], dtype="string")
    cleaned = s.str.strip().str.upper().str.replace(".", "-", regex=False)
    print(pd.DataFrame({"raw": s, "cleaned": cleaned}))


if __name__ == "__main__":
    demo()
