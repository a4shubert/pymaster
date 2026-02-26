"""
Technique: Normality Test (Anderson-Darling)
Use When:
- Quick check for distributional assumptions
"""

import numpy as np
from scipy import stats


if __name__ == '__main__':
    rng = np.random.default_rng(0)
    x = rng.normal(size=200)
    print(stats.anderson(x, dist='norm'))
