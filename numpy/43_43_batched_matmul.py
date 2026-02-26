"""
Technique: Batched matmul with @
Use When:
- Intermediate/advanced NumPy techniques with a quant/finance bias
- Each file is runnable and uses only NumPy + stdlib
"""

import numpy as np


def demo() -> None:
    A = np.arange(12).reshape(2, 2, 3)  # batch=2
    B = np.arange(18).reshape(2, 3, 3)
    C = A @ B
    print(C.shape)


if __name__ == '__main__':
    demo()
