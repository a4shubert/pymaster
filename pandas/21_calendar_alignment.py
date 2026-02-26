"""
Technique: Calendar Alignment (Trading Days vs Calendar Days)
Use When:
- Equity markets have holidays; crypto trades 24/7; rates have different calendars
- Misaligned calendars break backtests and risk
"""

import pandas as pd


def demo() -> None:
    # Missing a "holiday" on 2026-02-25 (simulated).
    px = pd.Series(
        [100.0, 101.0, 103.0],
        index=pd.to_datetime(["2026-02-24", "2026-02-26", "2026-02-27"]),
        name="px",
    )

    cal = pd.date_range("2026-02-24", "2026-02-27", freq="B")  # business days
    aligned = px.reindex(cal)
    aligned_ffill = aligned.ffill()

    out = pd.DataFrame({"px": aligned, "px_ffill": aligned_ffill})
    out["ret"] = out["px"].pct_change()
    out["ret_safe"] = out["px_ffill"].pct_change()

    print(out)


if __name__ == "__main__":
    demo()
