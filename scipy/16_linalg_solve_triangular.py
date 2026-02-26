"""
Technique: Triangular Solve (solve_triangular)
Use When:
- Efficient solves after Cholesky/QR
"""

import numpy as np
from scipy.linalg import solve_triangular


if __name__ == '__main__':
    L = np.array([[2.0, 0.0], [1.0, 1.0]])
    b = np.array([2.0, 2.0])
    y = solve_triangular(L, b, lower=True)
    print(y)
