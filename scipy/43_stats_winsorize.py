"""Lecture 43: Winsorization (mstats.winsorize)

Focus:
- Cap extremes to reduce outlier impact.
"""

import numpy as np
from scipy.stats.mstats import winsorize


if __name__ == '__main__':
    x = np.array([-10.0, -1.0, 0.0, 1.0, 10.0])
    y = winsorize(x, limits=(0.2, 0.2))
    print(np.asarray(y))
