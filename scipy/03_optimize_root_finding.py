"""Lecture 03: Root Finding (scipy.optimize.root)

Focus:
- Solve systems f(x)=0.
- Appears in implied volatility and equilibrium conditions.
"""

import numpy as np
from scipy import optimize


def g(x: np.ndarray) -> np.ndarray:
    # Solve: x0^2 + x1 = 4, x0 + x1^2 = 4
    return np.array([x[0] ** 2 + x[1] - 4, x[0] + x[1] ** 2 - 4])


if __name__ == '__main__':
    res = optimize.root(g, x0=np.array([1.0, 1.0]))
    print(res.x, res.success)
