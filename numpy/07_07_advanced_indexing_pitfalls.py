# Technique: Advanced indexing (creates copies)
# Use When:
# - Intermediate/advanced NumPy techniques with a quant/finance bias
# - Each file is runnable and uses only NumPy + stdlib

import numpy as np


def demo() -> None:
    x = np.arange(10)
    idx = np.array([2, 5, 7])
    sub = x[idx]
    sub[:] = 99
    print('x unchanged:', x)

    # Use direct assignment with idx to mutate.
    x[idx] = 88
    print('x mutated:', x)


if __name__ == '__main__':
    demo()
