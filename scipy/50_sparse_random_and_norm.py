"""Lecture 50: Sparse Random Matrices + Norms

Focus:
- Generate sparse random and compute norms.
"""

import numpy as np
from scipy import sparse
from scipy.sparse.linalg import norm


if __name__ == '__main__':
    A = sparse.random(100, 100, density=0.01, format='csr', random_state=0)
    print(float(norm(A)))
