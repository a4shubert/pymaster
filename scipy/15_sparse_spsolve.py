"""
Technique: Sparse Linear Solve (spsolve)
Use When:
- Solve Ax=b when A is sparse
"""

import numpy as np
from scipy import sparse
from scipy.sparse.linalg import spsolve


if __name__ == '__main__':
    A = sparse.csr_matrix([[4.0, 1.0], [1.0, 3.0]])
    b = np.array([1.0, 2.0])
    x = spsolve(A, b)
    print(x)
