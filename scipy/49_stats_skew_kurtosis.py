"""
Technique: Skew/Kurtosis
Use When:
- Tail shape metrics (be cautious; noisy estimates)
"""

import numpy as np
from scipy.stats import skew, kurtosis


if __name__ == '__main__':
    x = np.array([1.0, 2.0, 3.0, 10.0, -5.0])
    print('skew:', float(skew(x)))
    print('kurt:', float(kurtosis(x)))
