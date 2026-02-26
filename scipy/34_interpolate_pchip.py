"""
Technique: Shape-Preserving Interpolation (PCHIP)
Use When:
- Monotone interpolation useful for curves (rates) to avoid overshoot
"""

import numpy as np
from scipy.interpolate import PchipInterpolator


if __name__ == '__main__':
    x = np.array([0, 1, 2, 3], dtype=float)
    y = np.array([0, 1, 1.5, 1.6], dtype=float)
    f = PchipInterpolator(x, y)
    print(f(np.array([0.5, 1.5, 2.5])))
