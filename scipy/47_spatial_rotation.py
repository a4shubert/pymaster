# Technique: Rotations (spatial.transform.Rotation)
# Use When:
# - Demonstrates clean rotation APIs

import numpy as np
from scipy.spatial.transform import Rotation


if __name__ == '__main__':
    r = Rotation.from_euler('z', 90, degrees=True)
    v = np.array([1.0, 0.0, 0.0])
    print(r.apply(v))
