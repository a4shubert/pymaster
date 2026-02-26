"""Lecture 12: Linear algebra: solve vs inverse

Focus:
- Intermediate/advanced NumPy techniques with a quant/finance bias.
- Each file is runnable and uses only NumPy + stdlib.

"""

import numpy as np


def demo() -> None:
    A = np.array([[3.0, 1.0], [1.0, 2.0]])
    b = np.array([9.0, 8.0])

    x = np.linalg.solve(A, b)
    print('solve:', x)

    inv = np.linalg.inv(A)
    x2 = inv @ b
    print('inv@b:', x2)


if __name__ == '__main__':
    demo()
