"""
Technique: repeat vs tile (be careful with memory)
Use When:
- Intermediate/advanced NumPy techniques with a quant/finance bias
- Each file is runnable and uses only NumPy + stdlib
"""

import numpy as np


def demo() -> None:
    x = np.array([1, 2, 3])
    print('repeat:', np.repeat(x, 2))
    print('tile:', np.tile(x, 2))


if __name__ == '__main__':
    demo()
