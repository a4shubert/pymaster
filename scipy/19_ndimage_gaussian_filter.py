"""
Technique: ndimage Gaussian Filter
Use When:
- Smooth 2D arrays/images
"""

import numpy as np
from scipy.ndimage import gaussian_filter


if __name__ == '__main__':
    x = np.zeros((5, 5), dtype=float)
    x[2, 2] = 1.0
    y = gaussian_filter(x, sigma=1.0)
    print(float(y.sum()))
