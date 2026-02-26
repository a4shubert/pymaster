"""
Technique: percentile/quantile (risk percentiles)
Use When:
- Intermediate/advanced NumPy techniques with a quant/finance bias
- Each file is runnable and uses only NumPy + stdlib
"""

import numpy as np


def demo() -> None:
    pnl = np.array([1.0, -2.0, 0.5, 3.0, -1.0, -4.0])
    print('p01:', np.percentile(pnl, 1))
    print('p50:', np.percentile(pnl, 50))
    print('p99:', np.percentile(pnl, 99))


if __name__ == '__main__':
    demo()
