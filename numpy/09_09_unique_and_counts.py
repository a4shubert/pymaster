"""Lecture 09: unique + counts (frequency tables)

Focus:
- Intermediate/advanced NumPy techniques with a quant/finance bias.
- Each file is runnable and uses only NumPy + stdlib.

"""

import numpy as np


def demo() -> None:
    x = np.array(['AAPL', 'MSFT', 'AAPL', 'TSLA', 'MSFT', 'AAPL'])
    vals, counts = np.unique(x, return_counts=True)
    order = np.argsort(-counts)
    for v, c in zip(vals[order], counts[order]):
        print(v, int(c))


if __name__ == '__main__':
    demo()
