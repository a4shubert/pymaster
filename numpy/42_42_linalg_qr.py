"""Lecture 42: QR decomposition (numerical methods)

Focus:
- Intermediate/advanced NumPy techniques with a quant/finance bias.
- Each file is runnable and uses only NumPy + stdlib.

"""

import numpy as np


def demo() -> None:
    A = np.array([[1.0, 1.0], [1.0, -1.0], [1.0, 0.0]])
    Q, R = np.linalg.qr(A)
    print('Q:
', Q)
    print('R:
', R)
    print('recon close:', np.allclose(A, Q @ R))


if __name__ == '__main__':
    demo()
