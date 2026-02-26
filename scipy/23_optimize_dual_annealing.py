"""Lecture 23: Global Optimization (dual_annealing)

Focus:
- Non-convex problems; global search heuristic.
"""

import numpy as np
from scipy.optimize import dual_annealing


def f(x: np.ndarray) -> float:
    return float(np.sin(x[0]) + (x[0] - 2) ** 2)


if __name__ == '__main__':
    res = dual_annealing(f, bounds=[(-5, 5)])
    print(res.x, res.fun)
