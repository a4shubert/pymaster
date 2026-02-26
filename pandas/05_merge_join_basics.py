# Technique: merge vs join (Reference Data Enrichment)
# Use When:
# - Enrich trades with security master fields (sector, currency, lot size)
# - Bad joins create silent row explosions or dropped observations

import pandas as pd


def demo() -> None:
    trades = pd.DataFrame(
        {
            "trade_id": [1, 2, 3],
            "ticker": ["AAPL", "MSFT", "AAPL"],
            "qty": [100, 50, 200],
        }
    )

    secmaster = pd.DataFrame(
        {
            "ticker": ["AAPL", "MSFT"],
            "sector": ["Tech", "Tech"],
            "currency": ["USD", "USD"],
        }
    )

    enriched = trades.merge(
        secmaster,
        on="ticker",
        how="left",
        validate="many_to_one",
        indicator=True,
    )

    print(enriched)


if __name__ == "__main__":
    demo()
