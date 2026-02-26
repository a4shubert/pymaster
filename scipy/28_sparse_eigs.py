# Technique: Sparse Eigenvalues (eigs)
# Use When:
# - Large systems: compute a few eigenvalues

import numpy as np
from scipy import sparse
from scipy.sparse.linalg import eigs


if __name__ == '__main__':
    A = sparse.diags([1.0, 2.0, 3.0, 4.0], 0, format='csr')
    w, v = eigs(A, k=2)
    print(w)
