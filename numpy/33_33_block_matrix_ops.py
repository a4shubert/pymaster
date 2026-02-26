"""Lecture 33: Block operations with reshape

Focus:
- Intermediate/advanced NumPy techniques with a quant/finance bias.
- Each file is runnable and uses only NumPy + stdlib.

"""

import numpy as np


def demo() -> None:
    x = np.arange(24).reshape(2, 3, 4)
    # Treat last two dims as a matrix per batch.
    s = x.sum(axis=(1, 2))
    print(s)


if __name__ == '__main__':
    demo()
