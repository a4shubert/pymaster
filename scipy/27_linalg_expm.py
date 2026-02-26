"""
Technique: Matrix Exponential (expm)
Use When:
- Used in continuous-time models and Markov chains
"""

import numpy as np
from scipy.linalg import expm


if __name__ == '__main__':
    A = np.array([[0.0, 1.0], [-1.0, 0.0]])
    print(expm(A))
