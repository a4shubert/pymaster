"""Lecture 08: ODE Solving (solve_ivp)

Focus:
- Solve initial value problems.
- Shows up in term structure models and dynamics.
"""

import numpy as np
from scipy.integrate import solve_ivp


def rhs(t: float, y: np.ndarray) -> np.ndarray:
    # dy/dt = -y
    return -y


if __name__ == '__main__':
    sol = solve_ivp(rhs, t_span=(0.0, 5.0), y0=np.array([1.0]), t_eval=np.linspace(0, 5, 6))
    print(sol.y[0])
