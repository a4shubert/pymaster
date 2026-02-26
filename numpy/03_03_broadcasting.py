# Technique: Broadcasting (vectorize across dimensions)
# Use When:
# - Intermediate/advanced NumPy techniques with a quant/finance bias
# - Each file is runnable and uses only NumPy + stdlib

import numpy as np


def demo() -> None:
    m = np.arange(6).reshape(2, 3)
    v = np.array([10, 20, 30])
    print(m)
    print(m + v)  # v broadcasts across rows


if __name__ == '__main__':
    demo()
