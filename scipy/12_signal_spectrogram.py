# Technique: Spectrogram (time-frequency)
# Use When:
# - Inspect frequency content over time

import numpy as np
from scipy import signal


if __name__ == '__main__':
    fs = 100.0
    t = np.arange(0, 2, 1/fs)
    x = np.sin(2*np.pi*(5 + 10*t)*t)
    f, tt, Sxx = signal.spectrogram(x, fs=fs)
    print(Sxx.shape)
