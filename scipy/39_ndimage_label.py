"""Lecture 39: Connected Components (ndimage.label)

Focus:
- Label connected regions in a binary matrix.
"""

import numpy as np
from scipy.ndimage import label


if __name__ == '__main__':
    x = np.array([[1, 0, 0], [1, 1, 0], [0, 0, 1]], dtype=int)
    lbl, n = label(x)
    print(n)
    print(lbl)
