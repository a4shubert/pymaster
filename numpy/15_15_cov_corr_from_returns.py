"""Lecture 15: Covariance/correlation from returns matrix

Focus:
- Intermediate/advanced NumPy techniques with a quant/finance bias.
- Each file is runnable and uses only NumPy + stdlib.

"""

import numpy as np


def demo() -> None:
    # rows = time, cols = assets
    R = np.array(
        [
            [0.01, 0.00, 0.02],
            [-0.02, 0.01, -0.03],
            [0.03, -0.01, 0.01],
        ]
    )

    cov = np.cov(R, rowvar=False, ddof=0)
    std = np.sqrt(np.diag(cov))
    corr = cov / np.outer(std, std)

    print('cov:
', cov)
    print('corr:
', corr)


if __name__ == '__main__':
    demo()
