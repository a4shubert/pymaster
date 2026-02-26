"""Lecture 32: Bootstrap Confidence Interval

Focus:
- Resampling-based CI; useful with unknown distributions.
"""

import numpy as np
from scipy import stats


if __name__ == '__main__':
    rng = np.random.default_rng(0)
    x = rng.normal(loc=0.1, scale=1.0, size=200)
    res = stats.bootstrap((x,), np.mean, n_resamples=500, method='basic', random_state=0)
    print(res.confidence_interval)
