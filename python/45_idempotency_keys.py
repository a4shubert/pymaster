"""
Technique: Idempotency Keys for Safe Retries

Why this is enterprise:
- Prevents double-processing when clients retry requests.
- Makes APIs safe under timeouts and network failures.
- Improves correctness in payment/order flows.

Pattern:
1) Accept an idempotency key from caller.
2) Store key -> result mapping.
3) If key already processed, return stored result.
"""

import sqlite3
from dataclasses import dataclass


@dataclass(frozen=True)
class Result:
    ok: bool
    message: str


def init_schema(conn: sqlite3.Connection) -> None:
    conn.execute(
        "CREATE TABLE IF NOT EXISTS idempotency (key TEXT PRIMARY KEY, ok INTEGER NOT NULL, message TEXT NOT NULL)"
    )
    conn.commit()


def get_cached(conn: sqlite3.Connection, key: str) -> Result | None:
    row = conn.execute("SELECT ok, message FROM idempotency WHERE key=?", (key,)).fetchone()
    if row is None:
        return None
    return Result(ok=bool(row[0]), message=row[1])


def put_cached(conn: sqlite3.Connection, key: str, result: Result) -> None:
    conn.execute(
        "INSERT INTO idempotency(key, ok, message) VALUES (?, ?, ?)",
        (key, int(result.ok), result.message),
    )
    conn.commit()


def process_order(conn: sqlite3.Connection, idem_key: str, order_id: int) -> Result:
    cached = get_cached(conn, idem_key)
    if cached is not None:
        return cached

    # Simulated side effect.
    result = Result(ok=True, message=f"processed order {order_id}")
    put_cached(conn, idem_key, result)
    return result


if __name__ == "__main__":
    conn = sqlite3.connect(":memory:")
    init_schema(conn)

    print(process_order(conn, "k1", 100))
    print(process_order(conn, "k1", 100))
