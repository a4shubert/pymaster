"""
Technique: Typed Settings Loaded from Environment

Why this is enterprise:
- Clear, validated configuration contracts.
- Fails fast when required settings are missing/invalid.
- Keeps environment details out of business logic.

Pattern:
1) Parse env vars once at startup.
2) Validate aggressively.
3) Pass settings object through your app.
"""

import os
from dataclasses import dataclass


@dataclass(frozen=True)
class Settings:
    app_env: str
    service_name: str
    timeout_s: float


def load_settings() -> Settings:
    app_env = os.getenv("APP_ENV", "dev")
    service_name = os.getenv("SERVICE_NAME", "pymaster")
    timeout_raw = os.getenv("TIMEOUT_S", "2.0")

    try:
        timeout_s = float(timeout_raw)
    except ValueError as exc:
        raise RuntimeError("TIMEOUT_S must be numeric") from exc

    if timeout_s <= 0:
        raise RuntimeError("TIMEOUT_S must be > 0")

    return Settings(app_env=app_env, service_name=service_name, timeout_s=timeout_s)


if __name__ == "__main__":
    os.environ.setdefault("APP_ENV", "dev")
    os.environ.setdefault("SERVICE_NAME", "billing")
    os.environ.setdefault("TIMEOUT_S", "1.5")
    print(load_settings())
