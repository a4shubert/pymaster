"""
Technique: Quantile Binning (Deciles/Quintiles)
Use When:
- Standard in factor research: bucket assets into deciles by signal
- Used for long/short portfolio formation and performance attribution
"""

import pandas as pd


def demo() -> None:
    df = pd.DataFrame({"ticker": list("ABCDEFGH"), "signal": [1, 2, 3, 4, 5, 6, 7, 8]})
    df["bucket"] = pd.qcut(df["signal"], q=4, labels=False, duplicates="drop")
    print(df.sort_values("signal"))


if __name__ == "__main__":
    demo()
