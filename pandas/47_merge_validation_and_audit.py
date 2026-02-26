"""Lecture 47: Merge Validation + Audit (Avoid Row Explosions)

Hedge fund relevance:
- Joining positions to ref data can silently explode if keys aren't unique.
- Use `validate` and `_merge` indicators to catch errors early.

Key techniques:
- `merge(..., validate='many_to_one', indicator=True)`
- analyze `_merge` counts
"""

import pandas as pd


def demo() -> None:
    pos = pd.DataFrame({"ticker": ["AAPL", "MSFT"], "qty": [100, 50]})
    ref = pd.DataFrame({"ticker": ["AAPL", "MSFT"], "sector": ["Tech", "Tech"]})

    merged = pos.merge(ref, on="ticker", how="left", validate="one_to_one", indicator=True)
    print(merged)
    print("merge counts:\n", merged["_merge"].value_counts())


if __name__ == "__main__":
    demo()
