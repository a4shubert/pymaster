"""
Technique: Rolling Windows and EWM (Volatility, Trends, Risk)
Use When:
- Rolling stats drive signals (moving averages) and risk (rolling vol)
- EWM (exponentially weighted) reacts faster, common in risk models
"""

import pandas as pd


def demo() -> None:
    idx = pd.date_range("2026-02-01", periods=10, freq="D")
    prices = pd.Series([100, 101, 102, 101, 103, 104, 103, 105, 106, 107], index=idx, name="px")

    rets = prices.pct_change()
    out = pd.DataFrame({"px": prices, "ret": rets})

    out["ma_3"] = out["px"].rolling(3, min_periods=3).mean()
    out["vol_5"] = out["ret"].rolling(5, min_periods=5).std(ddof=0)

    out["ewm_ma"] = out["px"].ewm(span=3, adjust=False).mean()
    out["ewm_vol"] = out["ret"].ewm(span=5, adjust=False).std(bias=True)

    print(out)


if __name__ == "__main__":
    demo()
