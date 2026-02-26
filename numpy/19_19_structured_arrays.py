"""Lecture 19: Structured arrays (typed records)

Focus:
- Intermediate/advanced NumPy techniques with a quant/finance bias.
- Each file is runnable and uses only NumPy + stdlib.

"""

import numpy as np


def demo() -> None:
    dt = np.dtype([('ticker', 'U8'), ('qty', 'i4'), ('price', 'f8')])
    rec = np.array([('AAPL', 100, 190.2), ('MSFT', 50, 412.0)], dtype=dt)
    notionals = rec['qty'] * rec['price']
    print(notionals)


if __name__ == '__main__':
    demo()
