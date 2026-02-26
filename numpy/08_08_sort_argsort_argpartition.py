"""Lecture 08: Sorting: sort/argsort/argpartition (top-k)

Focus:
- Intermediate/advanced NumPy techniques with a quant/finance bias.
- Each file is runnable and uses only NumPy + stdlib.

"""

import numpy as np


def demo() -> None:
    x = np.array([5, 1, 9, 2, 7, 3])
    print('sorted:', np.sort(x))
    print('argsort:', np.argsort(x))

    k = 3
    idx = np.argpartition(x, -k)[-k:]
    topk = x[idx]
    print('topk (unordered):', topk)
    print('topk sorted:', np.sort(topk))


if __name__ == '__main__':
    demo()
