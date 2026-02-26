"""Lecture 26: Simpson Integration (samples)

Focus:
- Integrate sampled data.
"""

import numpy as np
from scipy.integrate import simpson


if __name__ == '__main__':
    x = np.linspace(0, 1, 101)
    y = np.exp(-x * x)
    print(float(simpson(y, x=x)))
