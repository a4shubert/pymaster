"""Lecture 25: take_along_axis (gather with indices)

Focus:
- Intermediate/advanced NumPy techniques with a quant/finance bias.
- Each file is runnable and uses only NumPy + stdlib.

"""

import numpy as np


def demo() -> None:
    x = np.array([[10, 11, 12], [20, 21, 22]])
    idx = np.array([[2, 0, 1], [1, 1, 0]])
    y = np.take_along_axis(x, idx, axis=1)
    print(y)


if __name__ == '__main__':
    demo()
