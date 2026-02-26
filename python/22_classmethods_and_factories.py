"""
Technique: @classmethod Factories (Multiple Constructors)

Why this is professional:
- Object creation rules stay centralized.
- Intent is explicit (from_env, from_json, from_dsn).
- Constructor changes can remain backwards-compatible.

Pattern:
1) Keep __init__ minimal.
2) Add @classmethod constructors per source.
3) Validate inside factories.
"""

import os
from dataclasses import dataclass


@dataclass(frozen=True)
class DbConfig:
    host: str
    port: int

    @classmethod
    def from_env(cls) -> "DbConfig":
        host = os.getenv("DB_HOST", "localhost")
        port_raw = os.getenv("DB_PORT", "5432")
        try:
            port = int(port_raw)
        except ValueError as exc:
            raise ValueError("DB_PORT must be an int") from exc
        if not (1 <= port <= 65535):
            raise ValueError("DB_PORT out of range")
        return cls(host=host, port=port)

    @classmethod
    def from_dsn(cls, dsn: str) -> "DbConfig":
        # Minimal parser: "host:port".
        if ":" not in dsn:
            raise ValueError("dsn must be 'host:port'")
        host, port_raw = dsn.split(":", 1)
        return cls(host=host, port=int(port_raw))


if __name__ == "__main__":
    os.environ.setdefault("DB_HOST", "db")
    os.environ.setdefault("DB_PORT", "5432")
    print(DbConfig.from_env())
    print(DbConfig.from_dsn("db:5432"))
