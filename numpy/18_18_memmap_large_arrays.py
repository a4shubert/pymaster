# Technique: memmap (out-of-core arrays)
# Use When:
# - Intermediate/advanced NumPy techniques with a quant/finance bias
# - Each file is runnable and uses only NumPy + stdlib

import numpy as np

import os
import numpy as np


def demo() -> None:
    path = '/tmp/pymaster_memmap.dat'
    if os.path.exists(path):
        os.remove(path)

    m = np.memmap(path, dtype='float64', mode='w+', shape=(1000,))
    m[:] = np.linspace(0.0, 1.0, num=1000)
    m.flush()

    m2 = np.memmap(path, dtype='float64', mode='r', shape=(1000,))
    print(float(m2[:5].sum()))


if __name__ == '__main__':
    demo()
