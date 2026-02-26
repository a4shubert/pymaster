# Technique: Resampling Signals (resample_poly)
# Use When:
# - Rational resampling with anti-alias filtering

import numpy as np
from scipy.signal import resample_poly


if __name__ == '__main__':
    x = np.arange(10, dtype=float)
    y = resample_poly(x, up=2, down=1)
    print(y.shape)
