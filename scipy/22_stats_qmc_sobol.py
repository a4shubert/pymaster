"""
Technique: Quasi-Monte Carlo (Sobol)
Use When:
- Low-discrepancy sequences for faster convergence (when applicable)
"""

from scipy.stats import qmc


if __name__ == '__main__':
    sampler = qmc.Sobol(d=2, scramble=True, seed=0)
    x = sampler.random_base2(m=3)
    print(x.shape)
