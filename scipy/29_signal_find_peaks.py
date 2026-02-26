"""
Technique: Peak Finding (find_peaks)
Use When:
- Detect peaks in a signal
"""

import numpy as np
from scipy.signal import find_peaks


if __name__ == '__main__':
    x = np.array([0, 1, 0, 2, 0, 1, 0], dtype=float)
    peaks, props = find_peaks(x, height=0.5)
    print(peaks, props['peak_heights'])
