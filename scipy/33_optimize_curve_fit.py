# Technique: curve_fit (quick param fit)
# Use When:
# - Fit parametric curves; careful with extrapolation

import numpy as np
from scipy.optimize import curve_fit


def model(x: np.ndarray, a: float, b: float) -> np.ndarray:
    return a * x + b


if __name__ == '__main__':
    x = np.array([0.0, 1.0, 2.0, 3.0])
    y = np.array([1.0, 2.1, 3.9, 6.2])
    p, _ = curve_fit(model, x, y)
    print(p)
