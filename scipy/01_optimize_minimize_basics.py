"""Lecture 01: scipy.optimize.minimize (basics)

Focus:
- Unconstrained optimization with explicit objective.
- Common in calibration and parameter estimation.

Run:
- Requires scipy installed.
"""

import numpy as np
from scipy import optimize


def f(x: np.ndarray) -> float:
    # Simple convex bowl.
    return float((x[0] - 2) ** 2 + (x[1] + 1) ** 2)


if __name__ == '__main__':
    res = optimize.minimize(f, x0=np.array([0.0, 0.0]))
    print(res.x, res.fun, res.success)
