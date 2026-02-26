# Technique: Pairwise Distances (cdist)
# Use When:
# - Distance matrices for clustering/NN

import numpy as np
from scipy.spatial.distance import cdist


if __name__ == '__main__':
    A = np.array([[0.0, 0.0], [1.0, 1.0]])
    B = np.array([[1.0, 0.0]])
    print(cdist(A, B))
