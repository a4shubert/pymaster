# Technique: Turnover and Simple Transaction Cost Model (Toy)
# Use When:
# - Gross returns without costs are misleading
# - Turnover is a first-order proxy for costs and capacity

import pandas as pd


def demo() -> None:
    df = pd.DataFrame(
        {
            "date": pd.date_range("2026-02-01", periods=5, freq="D"),
            "w": [0.0, 1.0, 1.0, -1.0, 0.0],
            "ret": [0.0, 0.01, -0.02, 0.015, 0.0],
        }
    ).set_index("date")

    df["turnover"] = df["w"].diff().abs().fillna(0)
    k = 0.001  # 10 bps per 1.0 turnover (toy)
    df["cost"] = k * df["turnover"]

    df["gross"] = df["w"].shift(1).fillna(0) * df["ret"]
    df["net"] = df["gross"] - df["cost"]
    df["equity_net"] = (1 + df["net"]).cumprod()

    print(df)


if __name__ == "__main__":
    demo()
