"""
Technique: concatenate vs stack
Use When:
- Intermediate/advanced NumPy techniques with a quant/finance bias
- Each file is runnable and uses only NumPy + stdlib
"""

import numpy as np


def demo() -> None:
    a = np.array([1, 2, 3])
    b = np.array([4, 5, 6])
    print('concat:', np.concatenate([a, b]))
    print('stack:', np.stack([a, b], axis=0))


if __name__ == '__main__':
    demo()
