# Technique: FFT basics (toy signal)
# Use When:
# - Intermediate/advanced NumPy techniques with a quant/finance bias
# - Each file is runnable and uses only NumPy + stdlib

import numpy as np


def demo() -> None:
    n = 64
    t = np.arange(n)
    x = np.sin(2 * np.pi * t / 8) + 0.5 * np.sin(2 * np.pi * t / 16)
    X = np.fft.rfft(x)
    mag = np.abs(X)
    print('peak bins:', np.argsort(-mag)[:5])


if __name__ == '__main__':
    demo()
