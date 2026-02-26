# Technique: NaN-aware stats: isnan, nanmean, nanstd
# Use When:
# - Intermediate/advanced NumPy techniques with a quant/finance bias
# - Each file is runnable and uses only NumPy + stdlib

import numpy as np


def demo() -> None:
    x = np.array([1.0, np.nan, 2.0, 3.0, np.nan])
    print('mean:', np.mean(x))
    print('nanmean:', np.nanmean(x))
    print('nanstd:', np.nanstd(x))


if __name__ == '__main__':
    demo()
