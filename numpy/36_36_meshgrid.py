"""
Technique: meshgrid (parameter grids)
Use When:
- Intermediate/advanced NumPy techniques with a quant/finance bias
- Each file is runnable and uses only NumPy + stdlib
"""

import numpy as np


def demo() -> None:
    a = np.array([0.1, 0.2, 0.3])
    b = np.array([1, 2])
    A, B = np.meshgrid(a, b, indexing='xy')
    print(A)
    print(B)


if __name__ == '__main__':
    demo()
