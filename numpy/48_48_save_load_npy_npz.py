"""Lecture 48: Save/load .npy/.npz

Focus:
- Intermediate/advanced NumPy techniques with a quant/finance bias.
- Each file is runnable and uses only NumPy + stdlib.

"""

import numpy as np

import os
import numpy as np


def demo() -> None:
    x = np.arange(5)
    y = np.linspace(0, 1, 5)
    path = '/tmp/pymaster_arrays.npz'
    if os.path.exists(path):
        os.remove(path)
    np.savez(path, x=x, y=y)

    data = np.load(path)
    print(data['x'])
    print(data['y'])


if __name__ == '__main__':
    demo()
