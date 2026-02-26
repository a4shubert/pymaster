# Technique: Special Functions (erf)
# Use When:
# - Common in normal CDF relationships

import numpy as np
from scipy import special


if __name__ == '__main__':
    x = np.array([-1.0, 0.0, 1.0])
    print(special.erf(x))
