"""Lecture 49: errstate (control warnings for invalid ops)

Focus:
- Intermediate/advanced NumPy techniques with a quant/finance bias.
- Each file is runnable and uses only NumPy + stdlib.

"""

import numpy as np


def demo() -> None:
    x = np.array([1.0, 0.0, -1.0])
    with np.errstate(divide='ignore', invalid='ignore'):
        y = 1.0 / x
    print(y)


if __name__ == '__main__':
    demo()
