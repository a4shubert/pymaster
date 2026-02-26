# Technique: Hypothesis Tests (t-test, Mann-Whitney)
# Use When:
# - Basic statistical tests for research sanity checks
# - Beware multiple testing and dependence

import numpy as np
from scipy import stats


if __name__ == '__main__':
    x = np.array([1.0, 2.0, 1.5, 2.1])
    y = np.array([0.9, 1.8, 1.2, 2.0])
    print('ttest:', stats.ttest_ind(x, y, equal_var=False))
    print('mw:', stats.mannwhitneyu(x, y, alternative='two-sided'))
