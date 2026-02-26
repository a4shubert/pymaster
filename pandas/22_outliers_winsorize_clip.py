"""
Technique: Outliers (clip / winsor-like handling)
Use When:
- Bad prints or corporate action errors can create huge outliers
- Outliers can dominate z-scores, correlations, and risk estimates
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
