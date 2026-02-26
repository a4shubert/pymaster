# Technique: Stable softmax (numerical stability)
# Use When:
# - Intermediate/advanced NumPy techniques with a quant/finance bias
# - Each file is runnable and uses only NumPy + stdlib

import numpy as np


def softmax(x: np.ndarray) -> np.ndarray:
    x = x - np.max(x)
    e = np.exp(x)
    return e / e.sum()


def demo() -> None:
    x = np.array([1000.0, 1001.0, 999.0])
    print(softmax(x))


if __name__ == '__main__':
    demo()
