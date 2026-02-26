# Technique: polyfit (toy regression)
# Use When:
# - Intermediate/advanced NumPy techniques with a quant/finance bias
# - Each file is runnable and uses only NumPy + stdlib

import numpy as np


def demo() -> None:
    x = np.array([0.0, 1.0, 2.0, 3.0])
    y = np.array([1.0, 2.1, 3.9, 6.2])
    coef = np.polyfit(x, y, deg=1)
    print('coef:', coef)
    pred = np.polyval(coef, x)
    print('pred:', pred)


if __name__ == '__main__':
    demo()
