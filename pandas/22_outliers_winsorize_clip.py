"""Lecture 22: Outliers (clip / winsor-like handling)

Hedge fund relevance:
- Bad prints or corporate action errors can create huge outliers.
- Outliers can dominate z-scores, correlations, and risk estimates.

Key techniques:
- `Series.clip(lower, upper)`
- Quantile-based clipping

Note:
- True winsorization replaces extreme values with boundary quantiles.
"""

import pandas as pd


def clip_by_quantile(s: pd.Series, q: float = 0.01) -> pd.Series:
    lo = s.quantile(q)
    hi = s.quantile(1 - q)
    return s.clip(lower=lo, upper=hi)


if __name__ == "__main__":
    s = pd.Series([0.01, 0.02, -0.03, 0.5, -0.4, 0.015], name="ret")
    print("raw:\n", s)
    print("clipped:\n", clip_by_quantile(s, q=0.1))
