# Technique: Views vs copies (slicing can alias memory)
# Use When:
# - Intermediate/advanced NumPy techniques with a quant/finance bias
# - Each file is runnable and uses only NumPy + stdlib

import numpy as np


def demo() -> None:
    x = np.arange(10)
    view = x[2:6]      # view
    copy = x[2:6].copy()

    view[:] = 99
    print('x after view write:', x)

    x[:] = np.arange(10)
    copy[:] = 77
    print('x after copy write:', x)


if __name__ == '__main__':
    demo()
