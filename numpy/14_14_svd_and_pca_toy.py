"""
Technique: SVD / PCA toy (demean then SVD)
Use When:
- Intermediate/advanced NumPy techniques with a quant/finance bias
- Each file is runnable and uses only NumPy + stdlib
"""

import numpy as np


def demo() -> None:
    X = np.array([[1.0, 2.0], [2.0, 1.0], [3.0, 0.0], [4.0, -1.0]])
    Xc = X - X.mean(axis=0, keepdims=True)
    U, S, Vt = np.linalg.svd(Xc, full_matrices=False)
    print('singular values:', S)
    pc1 = Vt[0]
    print('pc1:', pc1)


if __name__ == '__main__':
    demo()
