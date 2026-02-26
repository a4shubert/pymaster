"""Lecture 04: Ufuncs + where (branchless selection)

Focus:
- Intermediate/advanced NumPy techniques with a quant/finance bias.
- Each file is runnable and uses only NumPy + stdlib.

"""

import numpy as np


def demo() -> None:
    x = np.array([-2.0, -0.5, 0.0, 0.5, 2.0])
    y = np.where(x >= 0, x * x, -x)  # example piecewise
    print(y)


if __name__ == '__main__':
    demo()
