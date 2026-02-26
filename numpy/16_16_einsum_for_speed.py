"""Lecture 16: einsum (explicit tensor contractions)

Focus:
- Intermediate/advanced NumPy techniques with a quant/finance bias.
- Each file is runnable and uses only NumPy + stdlib.

"""

import numpy as np


def demo() -> None:
    A = np.arange(6).reshape(2, 3)
    B = np.arange(12).reshape(3, 4)

    m1 = A @ B
    m2 = np.einsum('ij,jk->ik', A, B)
    print(np.allclose(m1, m2))


if __name__ == '__main__':
    demo()
