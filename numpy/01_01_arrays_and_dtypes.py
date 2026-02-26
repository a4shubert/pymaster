"""
Technique: Arrays + dtypes (why dtype discipline matters)
Use When:
- Intermediate/advanced NumPy techniques with a quant/finance bias
- Each file is runnable and uses only NumPy + stdlib
"""

import numpy as np


def demo() -> None:
    a = np.array([1, 2, 3])
    b = np.array([1, 2, 3], dtype=np.int32)
    c = np.array([1, 2, 3], dtype=np.float64)

    print('a', a.dtype, a.nbytes)
    print('b', b.dtype, b.nbytes)
    print('c', c.dtype, c.nbytes)


if __name__ == '__main__':
    demo()
