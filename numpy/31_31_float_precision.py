# Technique: Float precision: float32 vs float64
# Use When:
# - Intermediate/advanced NumPy techniques with a quant/finance bias
# - Each file is runnable and uses only NumPy + stdlib

import numpy as np


def demo() -> None:
    x64 = np.array([1e8, 1, -1e8], dtype=np.float64)
    x32 = np.array([1e8, 1, -1e8], dtype=np.float32)
    print('sum float64:', float(x64.sum()))
    print('sum float32:', float(x32.sum()))


if __name__ == '__main__':
    demo()
