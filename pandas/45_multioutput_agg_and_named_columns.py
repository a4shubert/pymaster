# Technique: Multi-Output Aggregations with Named Columns
# Use When:
# - Reporting often needs multiple metrics per group (PnL, vol, hit rate)
# - Named aggs keep outputs tidy and avoid MultiIndex columns

import pandas as pd


def hit_rate(s: pd.Series) -> float:
    s = s.dropna()
    if len(s) == 0:
        return 0.0
    return float((s > 0).mean())


if __name__ == "__main__":
    pnl = pd.DataFrame(
        {
            "pm": ["A", "A", "A", "B", "B"],
            "day": pd.to_datetime(["2026-02-24", "2026-02-25", "2026-02-26", "2026-02-24", "2026-02-25"]),
            "pnl": [10.0, -3.0, 5.0, 2.0, -1.0],
        }
    )

    rpt = pnl.groupby("pm", as_index=False).agg(
        pnl_sum=("pnl", "sum"),
        pnl_mean=("pnl", "mean"),
        hit=("pnl", hit_rate),
        n=("pnl", "size"),
    )

    print(rpt)
