"""
Technique: 2D Interpolation (griddata)
Use When:
- Interpolate scattered points (toy vol surface points)
"""

import numpy as np
from scipy.interpolate import griddata


if __name__ == '__main__':
    pts = np.array([[0, 0], [0, 1], [1, 0], [1, 1]], dtype=float)
    vals = np.array([0.0, 1.0, 1.0, 0.0])
    xi = np.array([[0.5, 0.5]])
    print(griddata(pts, vals, xi, method='linear'))
