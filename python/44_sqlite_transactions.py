"""
Technique: Transaction Boundaries (sqlite3)
Use When:
- Guarantees data consistency (all-or-nothing changes)
- Makes failure handling predictable
- Centralizes commit/rollback logic
"""

import sqlite3
from contextlib import contextmanager


@contextmanager
def transaction(conn: sqlite3.Connection):
    try:
        yield
        conn.commit()
    except Exception:
        conn.rollback()
        raise


def init_schema(conn: sqlite3.Connection) -> None:
    conn.execute("CREATE TABLE IF NOT EXISTS accounts (id INTEGER PRIMARY KEY, balance INTEGER NOT NULL)")


def transfer(conn: sqlite3.Connection, from_id: int, to_id: int, amount: int) -> None:
    if amount <= 0:
        raise ValueError("amount must be > 0")

    with transaction(conn):
        from_bal = conn.execute("SELECT balance FROM accounts WHERE id=?", (from_id,)).fetchone()
        to_bal = conn.execute("SELECT balance FROM accounts WHERE id=?", (to_id,)).fetchone()
        if from_bal is None or to_bal is None:
            raise ValueError("account not found")
        if from_bal[0] < amount:
            raise ValueError("insufficient funds")

        conn.execute("UPDATE accounts SET balance = balance - ? WHERE id=?", (amount, from_id))
        conn.execute("UPDATE accounts SET balance = balance + ? WHERE id=?", (amount, to_id))


if __name__ == "__main__":
    conn = sqlite3.connect(":memory:")
    init_schema(conn)
    conn.execute("INSERT INTO accounts(id, balance) VALUES (1, 100)")
    conn.execute("INSERT INTO accounts(id, balance) VALUES (2, 0)")
    conn.commit()

    transfer(conn, 1, 2, 50)
    print(conn.execute("SELECT id, balance FROM accounts ORDER BY id").fetchall())
