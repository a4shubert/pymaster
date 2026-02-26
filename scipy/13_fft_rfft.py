# Technique: FFT (scipy.fft)
# Use When:
# - Real FFT and frequency bins

import numpy as np
from scipy.fft import rfft, rfftfreq


if __name__ == '__main__':
    fs = 64.0
    t = np.arange(0, 1, 1/fs)
    x = np.sin(2*np.pi*8*t)
    X = np.abs(rfft(x))
    f = rfftfreq(t.size, d=1/fs)
    print(f[int(np.argmax(X))])
