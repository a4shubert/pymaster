# Technique: Sparse Matrices (CSR)
# Use When:
# - Build and multiply sparse matrices

import numpy as np
from scipy import sparse


if __name__ == '__main__':
    A = sparse.csr_matrix([[1, 0, 0], [0, 2, 0], [0, 0, 3]])
    x = np.array([1.0, 1.0, 1.0])
    print(A @ x)
