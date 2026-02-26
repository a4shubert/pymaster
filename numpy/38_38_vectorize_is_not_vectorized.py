"""
Technique: np.vectorize is convenience, not speed
Use When:
- Intermediate/advanced NumPy techniques with a quant/finance bias
- Each file is runnable and uses only NumPy + stdlib
"""

import numpy as np


def f(x: float) -> float:
    return x * x + 1


def demo() -> None:
    x = np.arange(5, dtype=np.float64)
    vf = np.vectorize(f)
    print(vf(x))
    print('Prefer ufunc-style math when possible')


if __name__ == '__main__':
    demo()
