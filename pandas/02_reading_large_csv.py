# Technique: Reading Large CSVs (dtype, parse_dates, chunks)
# Use When:
# - You ingest vendor dumps (ticks, bars, ref data) that can be GBs
# - Correct `dtype` prevents object columns and speeds parsing
# - `chunksize` enables streaming and incremental processing

import io
import pandas as pd


def read_trades(csv_text: str) -> pd.DataFrame:
    return pd.read_csv(
        io.StringIO(csv_text),
        usecols=["ts", "ticker", "qty", "price"],
        dtype={"ticker": "string", "qty": "Int64", "price": "Float64"},
        parse_dates=["ts"],
    )


def read_trades_in_chunks(csv_text: str, chunk_rows: int = 2) -> pd.DataFrame:
    chunks = pd.read_csv(
        io.StringIO(csv_text),
        usecols=["ts", "ticker", "qty", "price"],
        dtype={"ticker": "string", "qty": "Int64", "price": "Float64"},
        parse_dates=["ts"],
        chunksize=chunk_rows,
    )
    out = pd.concat(chunks, ignore_index=True)
    return out


if __name__ == "__main__":
    csv_text = """ts,ticker,qty,price,ignored
2026-02-26T09:30:00Z,AAPL,100,189.1,x
2026-02-26T09:31:00Z,AAPL,200,190.2,x
2026-02-26T09:32:00Z,MSFT,,412.0,x
"""

    df1 = read_trades(csv_text)
    df2 = read_trades_in_chunks(csv_text, chunk_rows=2)

    print(df1)
    print(df1.dtypes)
    print("chunks equal:", df1.equals(df2))
