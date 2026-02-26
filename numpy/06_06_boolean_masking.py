"""Lecture 06: Boolean masking (filter + assign)

Focus:
- Intermediate/advanced NumPy techniques with a quant/finance bias.
- Each file is runnable and uses only NumPy + stdlib.

"""

import numpy as np


def demo() -> None:
    x = np.array([1, 2, 3, 4, 5, 6])
    mask = x % 2 == 0
    print('evens:', x[mask])

    y = x.copy()
    y[mask] *= 10
    print('assigned:', y)


if __name__ == '__main__':
    demo()
