# Technique: Signal Filtering (Butterworth)
# Use When:
# - Low/high-pass filtering with scipy.signal

import numpy as np
from scipy import signal


if __name__ == '__main__':
    fs = 100.0
    t = np.arange(0, 1, 1/fs)
    x = np.sin(2*np.pi*5*t) + 0.5*np.sin(2*np.pi*30*t)
    b, a = signal.butter(4, 10, btype='low', fs=fs)
    y = signal.filtfilt(b, a, x)
    print(float(y[:5].mean()))
