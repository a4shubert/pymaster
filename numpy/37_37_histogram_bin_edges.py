"""
Technique: histogram and bin edges
Use When:
- Intermediate/advanced NumPy techniques with a quant/finance bias
- Each file is runnable and uses only NumPy + stdlib
"""

import numpy as np


def demo() -> None:
    rng = np.random.default_rng(0)
    x = rng.normal(size=1000)
    counts, edges = np.histogram(x, bins=10)
    print(counts)
    print(edges)


if __name__ == '__main__':
    demo()
