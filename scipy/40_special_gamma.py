"""
Technique: Special Functions (gamma)
Use When:
- Gamma appears in distributions and normalization constants
"""

import numpy as np
from scipy import special


if __name__ == '__main__':
    x = np.array([0.5, 1.0, 2.5])
    print(special.gamma(x))
