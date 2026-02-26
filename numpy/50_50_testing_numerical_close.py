# Technique: Testing numerics with allclose
# Use When:
# - Intermediate/advanced NumPy techniques with a quant/finance bias
# - Each file is runnable and uses only NumPy + stdlib

import numpy as np


def demo() -> None:
    x = np.array([0.1, 0.2, 0.3])
    y = np.array([0.1, 0.2000000001, 0.3])
    print('equal:', np.array_equal(x, y))
    print('allclose:', np.allclose(x, y, rtol=1e-8, atol=1e-12))


if __name__ == '__main__':
    demo()
