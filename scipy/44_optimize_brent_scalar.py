"""
Technique: Scalar Minimization (Brent)
Use When:
- Fast 1D optimization (e.g., implied vol root/min)
"""

import numpy as np
from scipy.optimize import minimize_scalar


def f(x: float) -> float:
    return float((x - 1.234) ** 2 + 0.1 * np.sin(10 * x))


if __name__ == '__main__':
    res = minimize_scalar(f, method='brent')
    print(res.x, res.fun)
