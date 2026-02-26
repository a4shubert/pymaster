"""Lecture 34: Factor Exposure Regression (Toy, No Statsmodels)

Hedge fund relevance:
- Exposure estimation (beta) and factor neutralization show up everywhere.
- Production uses robust stats tooling; here we show a minimal matrix approach.

Key techniques:
- build design matrix X
- solve least squares with numpy

Note:
- This is a toy illustration (no intercept handling issues, no robust errors).
"""

import numpy as np
import pandas as pd


def ols_beta(y: pd.Series, x: pd.Series) -> float:
    Y = y.to_numpy()
    X = np.column_stack([np.ones(len(x)), x.to_numpy()])  # intercept + factor
    coef, *_ = np.linalg.lstsq(X, Y, rcond=None)
    return float(coef[1])


if __name__ == "__main__":
    df = pd.DataFrame(
        {
            "mkt": [0.01, -0.02, 0.015, 0.0, 0.005],
            "asset": [0.012, -0.025, 0.020, -0.001, 0.006],
        },
        index=pd.date_range("2026-02-01", periods=5, freq="D"),
    )
    print("beta:", ols_beta(df["asset"], df["mkt"]))
