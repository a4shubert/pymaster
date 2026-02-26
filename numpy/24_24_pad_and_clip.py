"""Lecture 24: clip and pad patterns

Focus:
- Intermediate/advanced NumPy techniques with a quant/finance bias.
- Each file is runnable and uses only NumPy + stdlib.

"""

import numpy as np


def demo() -> None:
    x = np.array([-5, -1, 0, 1, 10])
    print(np.clip(x, -2, 3))
    y = np.array([1, 2, 3])
    print(np.pad(y, (2, 1), mode='constant', constant_values=0))


if __name__ == '__main__':
    demo()
