# Technique: Data Validation Checks (Cheap Guardrails)
# Use When:
# - Silent data issues (duplicates, missing keys) destroy PnL credibility
# - Lightweight assertions catch issues early in notebooks/ETL

import pandas as pd


def validate_trades(df: pd.DataFrame) -> None:
    required = {"trade_id", "ts", "ticker", "qty", "price"}
    missing = required - set(df.columns)
    if missing:
        raise ValueError(f"missing columns: {sorted(missing)}")

    if df["trade_id"].duplicated().any():
        raise ValueError("trade_id must be unique")

    if df[["ts", "ticker", "qty", "price"]].isna().any().any():
        raise ValueError("ts/ticker/qty/price must be non-null")

    if (df["qty"] <= 0).any():
        raise ValueError("qty must be > 0")

    if (df["price"] <= 0).any():
        raise ValueError("price must be > 0")


if __name__ == "__main__":
    df = pd.DataFrame(
        {
            "trade_id": [1, 2],
            "ts": pd.to_datetime(["2026-02-26T14:30:00Z", "2026-02-26T14:30:01Z"], utc=True),
            "ticker": ["AAPL", "MSFT"],
            "qty": [100, 50],
            "price": [190.2, 412.0],
        }
    )
    validate_trades(df)
    print("ok")
