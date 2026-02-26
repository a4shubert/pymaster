"""
Technique: 1D Root Finding (bisect)
Use When:
- Reliable bracketing root method
"""

from scipy.optimize import bisect


def f(x: float) -> float:
    return x * x - 2.0


if __name__ == '__main__':
    r = bisect(f, 1.0, 2.0)
    print(r)
