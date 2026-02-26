"""Lecture 44: datetime64/timedelta64 basics

Focus:
- Intermediate/advanced NumPy techniques with a quant/finance bias.
- Each file is runnable and uses only NumPy + stdlib.

"""

import numpy as np


def demo() -> None:
    t = np.array(['2026-02-26', '2026-02-27'], dtype='datetime64[D]')
    dt = np.diff(t).astype('timedelta64[D]')
    print(t)
    print(dt)


if __name__ == '__main__':
    demo()
