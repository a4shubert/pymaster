"""
Technique: Vectorized operations over encoded IDs (use integers)
Use When:
- Intermediate/advanced NumPy techniques with a quant/finance bias
- Each file is runnable and uses only NumPy + stdlib
"""

import numpy as np


def demo() -> None:
    # Replace slow string ops by mapping symbols -> integer codes.
    symbols = np.array(['AAPL', 'MSFT', 'AAPL', 'TSLA'])
    uniq, codes = np.unique(symbols, return_inverse=True)
    print('uniq:', uniq)
    print('codes:', codes)


if __name__ == '__main__':
    demo()
