# Technique: searchsorted (align events to grid)
# Use When:
# - Intermediate/advanced NumPy techniques with a quant/finance bias
# - Each file is runnable and uses only NumPy + stdlib

import numpy as np


def demo() -> None:
    grid = np.array([10, 20, 30, 40, 50])
    events = np.array([9, 10, 11, 35, 60])
    idx = np.searchsorted(grid, events, side='right') - 1  # last grid <= event
    idx = np.clip(idx, 0, len(grid) - 1)
    print('aligned:', grid[idx])


if __name__ == '__main__':
    demo()
