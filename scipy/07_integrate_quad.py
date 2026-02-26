# Technique: Numerical Integration (quad)
# Use When:
# - Integrate functions with error estimates
# - Used in pricing and probability calculations

import numpy as np
from scipy import integrate


def f(x: float) -> float:
    return float(np.exp(-x * x))


if __name__ == '__main__':
    val, err = integrate.quad(f, 0.0, 1.0)
    print(val, err)
