"""Lecture 27: diff/cumsum (PnL-style transforms)

Focus:
- Intermediate/advanced NumPy techniques with a quant/finance bias.
- Each file is runnable and uses only NumPy + stdlib.

"""

import numpy as np


def demo() -> None:
    px = np.array([100.0, 101.0, 99.0, 103.0])
    ret = np.diff(px) / px[:-1]
    eq = np.cumprod(np.concatenate([[1.0], 1.0 + ret]))
    print('ret:', ret)
    print('equity:', eq)


if __name__ == '__main__':
    demo()
