# Technique: Normalize Within Groups (Sector-Neutral Signals)
# Use When:
# - Sector-neutral ranking reduces unintended factor exposure
# - You frequently normalize within sector, industry, or region

import pandas as pd


def zscore(s: pd.Series) -> pd.Series:
    return (s - s.mean()) / s.std(ddof=0)


def demo() -> None:
    df = pd.DataFrame(
        {
            "date": ["2026-02-24"] * 6,
            "ticker": ["A", "B", "C", "D", "E", "F"],
            "sector": ["Tech", "Tech", "Tech", "Energy", "Energy", "Energy"],
            "signal": [1.0, 2.0, -1.0, 0.2, 0.1, 0.5],
        }
    )
    df["date"] = pd.to_datetime(df["date"])

    df["z_sector"] = df.groupby(["date", "sector"])["signal"].transform(zscore)
    df["rank_sector"] = df.groupby(["date", "sector"])["signal"].rank(pct=True)

    print(df.sort_values(["sector", "ticker"]))


if __name__ == "__main__":
    demo()
