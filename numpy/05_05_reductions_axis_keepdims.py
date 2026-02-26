# Technique: Reductions with axis/keepdims
# Use When:
# - Intermediate/advanced NumPy techniques with a quant/finance bias
# - Each file is runnable and uses only NumPy + stdlib

import numpy as np


def demo() -> None:
    x = np.arange(12).reshape(3, 4)
    print('sum all:', x.sum())
    print('sum axis=0:', x.sum(axis=0))
    print('sum axis=1:', x.sum(axis=1))
    print('mean axis=1 keepdims:', x.mean(axis=1, keepdims=True))


if __name__ == '__main__':
    demo()
