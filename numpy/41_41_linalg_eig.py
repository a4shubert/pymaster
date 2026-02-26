"""
Technique: Linalg eig
Use When:
- You are working in numerical computing with arrays
- You need linalg eig as a reliable building block
"""

"""Lecture 41: Eigenvalues (risk PCA intuition)

Focus:
- Intermediate/advanced NumPy techniques with a quant/finance bias.
- Each file is runnable and uses only NumPy + stdlib.

"""

import numpy as np


def demo() -> None:
    A = np.array([[2.0, 1.0], [1.0, 2.0]])
    w, v = np.linalg.eig(A)
    print('eigvals:', w)
    print('eigvecs:
', v)


if __name__ == '__main__':
    demo()
