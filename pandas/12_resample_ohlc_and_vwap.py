# Technique: Resampling to Bars (OHLC) and VWAP
# Use When:
# - You often convert irregular trades to fixed interval bars
# - OHLC bars and VWAP are standard downstream inputs

import pandas as pd


def demo() -> None:
    ts = pd.to_datetime(
        [
            "2026-02-26T14:30:10Z",
            "2026-02-26T14:30:20Z",
            "2026-02-26T14:30:50Z",
            "2026-02-26T14:31:10Z",
            "2026-02-26T14:31:40Z",
        ],
        utc=True,
    )
    trades = pd.DataFrame({"ts": ts, "price": [100.0, 100.1, 99.9, 100.2, 100.3], "qty": [10, 20, 5, 10, 15]})
    trades = trades.set_index("ts").sort_index()

    ohlc = trades["price"].resample("1min").ohlc()
    vol = trades["qty"].resample("1min").sum().rename("volume")

    vwap_num = (trades["price"] * trades["qty"]).resample("1min").sum()
    vwap_den = trades["qty"].resample("1min").sum()
    vwap = (vwap_num / vwap_den).rename("vwap")

    bars = pd.concat([ohlc, vol, vwap], axis=1)
    print(bars)


if __name__ == "__main__":
    demo()
