# Technique: NumPy Interop (Fast Math, Stable Outputs)
# Use When:
# - Many quant transforms are expressed naturally in NumPy
# - Use NumPy for heavy numeric kernels, pandas for alignment/indexing

import numpy as np
import pandas as pd


def demo() -> None:
    s = pd.Series([100.0, 101.0, 99.0, 103.0], name="px")

    arr = s.to_numpy()
    logret = np.log(arr[1:] / arr[:-1])

    out = pd.Series([np.nan] + logret.tolist(), index=s.index, name="logret")
    print(pd.concat([s, out], axis=1))


if __name__ == "__main__":
    demo()
