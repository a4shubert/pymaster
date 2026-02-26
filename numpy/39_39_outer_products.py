"""Lecture 39: outer products and factor models

Focus:
- Intermediate/advanced NumPy techniques with a quant/finance bias.
- Each file is runnable and uses only NumPy + stdlib.

"""

import numpy as np


def demo() -> None:
    a = np.array([1.0, 2.0, 3.0])
    b = np.array([10.0, 20.0])
    print(np.outer(a, b))


if __name__ == '__main__':
    demo()
