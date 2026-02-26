# Technique: KDTree Nearest Neighbors
# Use When:
# - Fast nearest neighbor queries

import numpy as np
from scipy.spatial import KDTree


if __name__ == '__main__':
    pts = np.array([[0.0, 0.0], [1.0, 1.0], [2.0, 2.0]])
    tree = KDTree(pts)
    d, i = tree.query([1.2, 1.2])
    print(d, i)
