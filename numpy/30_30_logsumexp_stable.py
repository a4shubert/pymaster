"""Lecture 30: Stable logsumexp

Focus:
- Intermediate/advanced NumPy techniques with a quant/finance bias.
- Each file is runnable and uses only NumPy + stdlib.

"""

import numpy as np


def logsumexp(x: np.ndarray) -> float:
    m = float(np.max(x))
    return m + float(np.log(np.exp(x - m).sum()))


def demo() -> None:
    x = np.array([1000.0, 1001.0, 999.0])
    print(logsumexp(x))


if __name__ == '__main__':
    demo()
