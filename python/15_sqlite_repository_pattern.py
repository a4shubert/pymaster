"""
Technique: Repository Pattern with sqlite3
Use When:
- Keeps SQL access isolated from business logic
- Enables easier testing and future DB migration
- Defines clear persistence boundaries
"""

import sqlite3
from dataclasses import dataclass


@dataclass(frozen=True)
class User:
    id: int
    email: str


class UserRepository:
    def __init__(self, conn: sqlite3.Connection) -> None:
        self._conn = conn

    def init_schema(self) -> None:
        self._conn.execute(
            "CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, email TEXT NOT NULL UNIQUE)"
        )
        self._conn.commit()

    def create(self, email: str) -> User:
        cur = self._conn.execute("INSERT INTO users (email) VALUES (?)", (email,))
        self._conn.commit()
        return User(id=int(cur.lastrowid), email=email)

    def get(self, user_id: int) -> User | None:
        row = self._conn.execute("SELECT id, email FROM users WHERE id = ?", (user_id,)).fetchone()
        if row is None:
            return None
        return User(id=row[0], email=row[1])


if __name__ == "__main__":
    conn = sqlite3.connect(":memory:")
    repo = UserRepository(conn)
    repo.init_schema()
    created = repo.create("dev@example.com")
    print(repo.get(created.id))
