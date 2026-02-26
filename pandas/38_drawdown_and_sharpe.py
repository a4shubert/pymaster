"""
Technique: Performance Metrics (Sharpe, Max Drawdown)
Use When:
- Sharpe and drawdown are baseline reporting metrics
- Always define your conventions (annualization factor, risk-free rate)
"""

import numpy as np
import pandas as pd


def sharpe(returns: pd.Series, ann_factor: float = 252.0) -> float:
    r = returns.dropna()
    if r.std(ddof=0) == 0:
        return 0.0
    return float(np.sqrt(ann_factor) * r.mean() / r.std(ddof=0))


def max_drawdown(equity: pd.Series) -> float:
    peak = equity.cummax()
    dd = equity / peak - 1.0
    return float(dd.min())


if __name__ == "__main__":
    ret = pd.Series([0.01, -0.02, 0.015, 0.0, -0.005, 0.02])
    equity = (1 + ret).cumprod()
    print("sharpe:", sharpe(ret))
    print("max_dd:", max_drawdown(equity))
