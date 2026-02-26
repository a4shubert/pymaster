"""Lecture 07: Numerical Integration (quad)

Focus:
- Integrate functions with error estimates.
- Used in pricing and probability calculations.
"""

import numpy as np
from scipy import integrate


def f(x: float) -> float:
    return float(np.exp(-x * x))


if __name__ == '__main__':
    val, err = integrate.quad(f, 0.0, 1.0)
    print(val, err)
