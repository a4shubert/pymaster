"""Lecture 04: Nonlinear Least Squares (least_squares)

Focus:
- Fit model parameters by minimizing residuals.
- Used for curve fitting and calibration.
"""

import numpy as np
from scipy import optimize


def residuals(p: np.ndarray, x: np.ndarray, y: np.ndarray) -> np.ndarray:
    a, b = p
    return a * x + b - y


if __name__ == '__main__':
    x = np.array([0.0, 1.0, 2.0, 3.0])
    y = np.array([1.0, 2.1, 3.9, 6.2])
    res = optimize.least_squares(residuals, x0=np.array([1.0, 0.0]), args=(x, y))
    print(res.x)
