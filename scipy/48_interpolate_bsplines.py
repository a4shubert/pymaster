"""Lecture 48: B-splines (BSpline)

Focus:
- Low-level spline representation.
"""

import numpy as np
from scipy.interpolate import BSpline


if __name__ == '__main__':
    t = np.array([0, 0, 0, 1, 2, 3, 3, 3], dtype=float)
    c = np.array([0.0, 1.0, 0.0, 1.0, 0.0])
    k = 2
    sp = BSpline(t, c, k)
    print(sp(np.array([0.5, 1.5, 2.5])))
