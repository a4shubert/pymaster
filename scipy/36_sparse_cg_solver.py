"""
Technique: Iterative Solve (Conjugate Gradient)
Use When:
- Large SPD systems solved iteratively
"""

import numpy as np
from scipy import sparse
from scipy.sparse.linalg import cg


if __name__ == '__main__':
    A = sparse.csr_matrix([[4.0, 1.0], [1.0, 3.0]])
    b = np.array([1.0, 2.0])
    x, info = cg(A, b, maxiter=50)
    print(x, info)
