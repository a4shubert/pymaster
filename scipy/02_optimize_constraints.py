"""Lecture 02: Constrained Optimization (bounds + constraints)

Focus:
- Bounds and linear/nonlinear constraints.
- Typical for portfolio constraints and calibration.
"""

import numpy as np
from scipy import optimize


def f(x: np.ndarray) -> float:
    return float((x[0] - 1) ** 2 + (x[1] - 2) ** 2)


if __name__ == '__main__':
    bounds = optimize.Bounds([0, 0], [2, 3])
    cons = ({'type': 'eq', 'fun': lambda x: x[0] + x[1] - 3},)
    res = optimize.minimize(f, x0=np.array([0.5, 2.5]), bounds=bounds, constraints=cons)
    print(res.x, res.success)
