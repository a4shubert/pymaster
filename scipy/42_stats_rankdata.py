"""
Technique: Rank Data (rankdata)
Use When:
- Robust ranking for signals
"""

import numpy as np
from scipy.stats import rankdata


if __name__ == '__main__':
    x = np.array([10.0, 20.0, 20.0, 5.0])
    print(rankdata(x, method='average'))
