"""
Technique: 1D Interpolation (interp1d)
Use When:
- Interpolate curves (yield curves, vol surfaces slices)
- Choose kind and bounds behavior
"""

import numpy as np
from scipy.interpolate import interp1d


if __name__ == '__main__':
    x = np.array([0.0, 1.0, 2.0, 3.0])
    y = np.array([0.0, 1.0, 0.0, 1.0])
    f = interp1d(x, y, kind='linear', fill_value='extrapolate')
    xs = np.linspace(0, 3, 7)
    print(f(xs))
