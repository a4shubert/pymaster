# Technique: Distributions (scipy.stats)
# Use When:
# - PDF/CDF/PPF, random variates
# - Core for risk metrics and simulations

from scipy import stats


if __name__ == '__main__':
    dist = stats.norm(loc=0.0, scale=1.0)
    print('cdf(0):', dist.cdf(0.0))
    print('ppf(0.95):', dist.ppf(0.95))
