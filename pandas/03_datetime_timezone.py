"""Lecture 03: Datetime + Timezones (Market Data Correctness)

Hedge fund relevance:
- Mixing naive/aware timestamps silently breaks joins and resampling.
- Normalize to UTC for storage; convert to local exchange tz for session logic.

Key techniques:
- `pd.to_datetime(..., utc=True)`
- `dt.tz_convert(...)`
- `dt.floor('min')` for bucketing
"""

import pandas as pd


def demo() -> None:
    df = pd.DataFrame(
        {
            "ts": [
                "2026-02-26 09:30:10-05:00",
                "2026-02-26 09:30:40-05:00",
                "2026-02-26 09:31:05-05:00",
            ],
            "price": [100.0, 100.2, 100.1],
        }
    )

    df["ts"] = pd.to_datetime(df["ts"], utc=True)
    df["minute"] = df["ts"].dt.floor("min")
    df["ts_ny"] = df["ts"].dt.tz_convert("America/New_York")

    print(df)


if __name__ == "__main__":
    demo()
