# Technique: putmask / place (in-place conditional updates)
# Use When:
# - Intermediate/advanced NumPy techniques with a quant/finance bias
# - Each file is runnable and uses only NumPy + stdlib

import numpy as np


def demo() -> None:
    x = np.arange(6, dtype=np.float64)
    np.putmask(x, x % 2 == 0, -1)
    print(x)


if __name__ == '__main__':
    demo()
