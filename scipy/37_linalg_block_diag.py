"""
Technique: Block Diagonal Matrices
Use When:
- Build block structures for models
"""

import numpy as np
from scipy.linalg import block_diag


if __name__ == '__main__':
    A = np.eye(2)
    B = 2 * np.eye(3)
    C = block_diag(A, B)
    print(C.shape)
