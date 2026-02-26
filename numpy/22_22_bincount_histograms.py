"""Lecture 22: bincount / histograms (fast counting)

Focus:
- Intermediate/advanced NumPy techniques with a quant/finance bias.
- Each file is runnable and uses only NumPy + stdlib.

"""

import numpy as np


def demo() -> None:
    x = np.array([0, 1, 1, 2, 2, 2, 4])
    counts = np.bincount(x, minlength=6)
    print(counts)


if __name__ == '__main__':
    demo()
