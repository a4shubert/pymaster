# Technique: groupby transform vs apply (Performance + Correctness)
# Use When:
# - Cross-sectional normalization (z-scores) should keep original shape
# - `transform` returns same length as input; `apply` can change shape

import pandas as pd


def cross_section_zscore(df: pd.DataFrame) -> pd.Series:
    # z-score of returns per date across tickers
    def z(x: pd.Series) -> pd.Series:
        return (x - x.mean()) / x.std(ddof=0)

    return df.groupby("date")["ret"].transform(z)


if __name__ == "__main__":
    data = pd.DataFrame(
        {
            "date": ["2026-02-24", "2026-02-24", "2026-02-25", "2026-02-25"],
            "ticker": ["AAPL", "MSFT", "AAPL", "MSFT"],
            "ret": [0.01, -0.02, 0.03, 0.01],
        }
    )
    data["date"] = pd.to_datetime(data["date"])
    data["z"] = cross_section_zscore(data)
    print(data)
