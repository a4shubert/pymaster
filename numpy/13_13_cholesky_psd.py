"""Lecture 13: Cholesky (SPD matrices) and checks

Focus:
- Intermediate/advanced NumPy techniques with a quant/finance bias.
- Each file is runnable and uses only NumPy + stdlib.

"""

import numpy as np


def demo() -> None:
    A = np.array([[4.0, 2.0], [2.0, 3.0]])  # SPD
    L = np.linalg.cholesky(A)
    recon = L @ L.T
    print('L:
', L)
    print('recon close:', np.allclose(A, recon))


if __name__ == '__main__':
    demo()
