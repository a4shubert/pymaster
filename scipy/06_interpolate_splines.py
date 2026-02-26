"""
Technique: Splines (UnivariateSpline)
Use When:
- Smooth noisy observations with a smoothing parameter
- Useful for curve smoothing in noisy data
"""

import numpy as np
from scipy.interpolate import UnivariateSpline


if __name__ == '__main__':
    x = np.linspace(0, 10, 20)
    rng = np.random.default_rng(0)
    y = np.sin(x) + 0.1 * rng.normal(size=x.size)
    sp = UnivariateSpline(x, y, s=0.5)
    xs = np.linspace(0, 10, 5)
    print(sp(xs))
