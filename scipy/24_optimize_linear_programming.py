# Technique: Linear Programming (linprog)
# Use When:
# - LP problems show up in allocation and constraints

import numpy as np
from scipy.optimize import linprog


if __name__ == '__main__':
    # minimize c^T x subject to A_ub x <= b_ub, x>=0
    c = np.array([1.0, 2.0])
    A = np.array([[1.0, 1.0], [-1.0, 2.0]])
    b = np.array([4.0, 2.0])
    res = linprog(c, A_ub=A, b_ub=b, bounds=[(0, None), (0, None)])
    print(res.x, res.fun, res.success)
