"""Lecture 17: Stride tricks: rolling window view (advanced)

Focus:
- Intermediate/advanced NumPy techniques with a quant/finance bias.
- Each file is runnable and uses only NumPy + stdlib.

"""

import numpy as np


def rolling_view(x: np.ndarray, window: int) -> np.ndarray:
    if window <= 0 or window > x.size:
        raise ValueError('bad window')
    shape = (x.size - window + 1, window)
    strides = (x.strides[0], x.strides[0])
    return np.lib.stride_tricks.as_strided(x, shape=shape, strides=strides)


def demo() -> None:
    x = np.arange(10, dtype=np.float64)
    w = rolling_view(x, 4)
    ma = w.mean(axis=1)
    print('rolling mean:', ma)


if __name__ == '__main__':
    demo()
