"""Lecture 07: concat + Alignment Pitfalls

Hedge fund relevance:
- Combining signals/returns from different sources can misalign dates.
- Pandas aligns on index by default, which is powerful but can surprise.

Key techniques:
- `pd.concat(..., axis=1)` aligns on index
- `join='inner'` to keep intersection
- explicit `reindex` to a target calendar
"""

import pandas as pd


def demo() -> None:
    idx1 = pd.date_range("2026-02-24", periods=3, freq="D")
    idx2 = pd.date_range("2026-02-25", periods=3, freq="D")

    s1 = pd.Series([0.01, -0.02, 0.03], index=idx1, name="strat_a")
    s2 = pd.Series([0.00, 0.01, -0.01], index=idx2, name="strat_b")

    wide_outer = pd.concat([s1, s2], axis=1)  # union of dates
    wide_inner = pd.concat([s1, s2], axis=1, join="inner")  # intersection of dates

    print("outer:\n", wide_outer)
    print("\ninner:\n", wide_inner)


if __name__ == "__main__":
    demo()
