"""
Technique: Configuration Management (Single Source of Runtime Settings)

Why this is professional:
- Keeps environment-specific values out of business logic.
- Makes local/dev/prod behavior explicit and auditable.
- Fails fast when required config is missing.

Pattern:
1) Read config from environment.
2) Parse/validate once at startup.
3) Pass typed config object to application services.
"""

import os
from dataclasses import dataclass


@dataclass(frozen=True)
class AppConfig:
    app_env: str
    db_url: str
    request_timeout_s: float


def load_config() -> AppConfig:
    app_env = os.getenv("APP_ENV", "dev")
    db_url = os.getenv("DB_URL")
    timeout_raw = os.getenv("REQUEST_TIMEOUT_S", "2.0")

    if not db_url:
        raise RuntimeError("DB_URL is required")

    try:
        timeout = float(timeout_raw)
    except ValueError as exc:
        raise RuntimeError("REQUEST_TIMEOUT_S must be numeric") from exc

    if timeout <= 0:
        raise RuntimeError("REQUEST_TIMEOUT_S must be > 0")

    return AppConfig(app_env=app_env, db_url=db_url, request_timeout_s=timeout)


if __name__ == "__main__":
    os.environ.setdefault("DB_URL", "postgresql://localhost:5432/pymaster")
    config = load_config()
    print(config)
