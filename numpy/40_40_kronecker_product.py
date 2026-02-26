"""
Technique: Kronecker product (block structure)
Use When:
- Intermediate/advanced NumPy techniques with a quant/finance bias
- Each file is runnable and uses only NumPy + stdlib
"""

import numpy as np


def demo() -> None:
    A = np.array([[1, 2], [3, 4]])
    B = np.array([[0, 5], [6, 7]])
    print(np.kron(A, B))


if __name__ == '__main__':
    demo()
