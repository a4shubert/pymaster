"""
Technique: Mitigating cancellation with sorted sum
Use When:
- Intermediate/advanced NumPy techniques with a quant/finance bias
- Each file is runnable and uses only NumPy + stdlib
"""

import numpy as np


def demo() -> None:
    x = np.array([1e8] + [1.0] * 10000 + [-1e8], dtype=np.float64)
    naive = x.sum()
    better = np.sort(x).sum()
    print('naive:', float(naive))
    print('sorted:', float(better))


if __name__ == '__main__':
    demo()
