"""
Technique: Random numbers: Generator API (reproducible)
Use When:
- Intermediate/advanced NumPy techniques with a quant/finance bias
- Each file is runnable and uses only NumPy + stdlib
"""

import numpy as np


def demo() -> None:
    rng = np.random.default_rng(42)
    x = rng.normal(size=5)
    y = rng.integers(0, 10, size=5)
    print(x)
    print(y)


if __name__ == '__main__':
    demo()
