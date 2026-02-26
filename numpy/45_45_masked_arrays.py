"""Lecture 45: Masked arrays (explicit missingness)

Focus:
- Intermediate/advanced NumPy techniques with a quant/finance bias.
- Each file is runnable and uses only NumPy + stdlib.

"""

import numpy as np


def demo() -> None:
    x = np.array([1.0, 2.0, -999.0, 3.0])
    mx = np.ma.masked_equal(x, -999.0)
    print('mean:', float(mx.mean()))


if __name__ == '__main__':
    demo()
