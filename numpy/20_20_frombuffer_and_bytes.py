"""Lecture 20: frombuffer (zero-copy decode of binary)

Focus:
- Intermediate/advanced NumPy techniques with a quant/finance bias.
- Each file is runnable and uses only NumPy + stdlib.

"""

import numpy as np


def demo() -> None:
    x = np.array([1, 2, 3, 4], dtype=np.int32)
    b = x.tobytes()
    y = np.frombuffer(b, dtype=np.int32)
    print('y shares bytes:', y)


if __name__ == '__main__':
    demo()
