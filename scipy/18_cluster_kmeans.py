"""Lecture 18: KMeans Clustering

Focus:
- Basic clustering via scipy.cluster.vq.
"""

import numpy as np
from scipy.cluster.vq import kmeans2


if __name__ == '__main__':
    rng = np.random.default_rng(0)
    x = np.r_[rng.normal(0, 0.2, size=(50, 2)), rng.normal(2, 0.2, size=(50, 2))]
    centroids, labels = kmeans2(x, 2, minit='points')
    print(centroids.shape, labels[:5])
