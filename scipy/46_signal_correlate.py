# Technique: Correlation (signal.correlate)
# Use When:
# - Cross-correlation for lag relationships

import numpy as np
from scipy.signal import correlate


if __name__ == '__main__':
    x = np.array([1, 2, 3])
    y = np.array([0, 1, 0.5])
    c = correlate(x, y, mode='full')
    print(c)
