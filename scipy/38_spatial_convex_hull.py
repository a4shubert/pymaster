"""
Technique: Convex Hull (geometry)
Use When:
- Geometry utilities via scipy.spatial
"""

import numpy as np
from scipy.spatial import ConvexHull


if __name__ == '__main__':
    pts = np.array([[0, 0], [1, 0], [1, 1], [0, 1], [0.2, 0.2]])
    hull = ConvexHull(pts)
    print(hull.vertices)
