# Technique: Health Checks (Liveness vs Readiness)
# Use When:
# - Orchestrators (Kubernetes, ECS) rely on health endpoints
# - Liveness: process is running
# - Readiness: process can serve traffic (deps available)

import sqlite3
from dataclasses import dataclass


@dataclass(frozen=True)
class Health:
    ok: bool
    detail: str


def liveness() -> Health:
    return Health(ok=True, detail="alive")


def readiness(conn: sqlite3.Connection) -> Health:
    try:
        conn.execute("SELECT 1").fetchone()
    except Exception as exc:
        return Health(ok=False, detail=f"db_error={exc}")
    return Health(ok=True, detail="ready")


if __name__ == "__main__":
    conn = sqlite3.connect(":memory:")
    print("liveness:", liveness())
    print("readiness:", readiness(conn))
