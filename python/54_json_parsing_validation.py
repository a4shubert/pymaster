"""
Technique: JSON Parsing + Lightweight Validation

Why this matters:
- Most web APIs are JSON.
- Parsing is easy; validating shape/types is where production bugs happen.

Pattern:
1) json.loads
2) Validate required keys and types.
3) Convert to a typed model.
"""

import json
from dataclasses import dataclass
from typing import Any


@dataclass(frozen=True)
class UserDTO:
    id: int
    email: str


def parse_user(payload: str) -> UserDTO:
    data: Any = json.loads(payload)
    if not isinstance(data, dict):
        raise ValueError("expected object")
    if not isinstance(data.get("id"), int):
        raise ValueError("id must be int")
    if not isinstance(data.get("email"), str):
        raise ValueError("email must be str")
    return UserDTO(id=data["id"], email=data["email"])


if __name__ == "__main__":
    print(parse_user('{"id": 1, "email": "dev@example.com"}'))
