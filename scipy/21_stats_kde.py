"""
Technique: Kernel Density Estimation (gaussian_kde)
Use When:
- Nonparametric density estimation (risk tails exploration)
"""

import numpy as np
from scipy.stats import gaussian_kde


if __name__ == '__main__':
    rng = np.random.default_rng(0)
    x = rng.normal(size=200)
    kde = gaussian_kde(x)
    xs = np.linspace(-3, 3, 5)
    print(kde(xs))
