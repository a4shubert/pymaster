"""
Technique: HTTP Client Wrapper Pattern

Why this is professional:
- Centralizes timeout, headers, retries, and error mapping.
- Keeps endpoint callers thin and consistent.
- Makes integration points easy to mock in tests.

Pattern:
1) Wrap HTTP details in a dedicated client class.
2) Raise domain-specific errors.
3) Return typed/normalized data to callers.
"""

from dataclasses import dataclass


class ApiClientError(Exception):
    pass


@dataclass(frozen=True)
class UserDTO:
    id: int
    email: str


class ApiClient:
    def __init__(self, base_url: str, timeout_s: float = 2.0) -> None:
        self._base_url = base_url.rstrip("/")
        self._timeout_s = timeout_s

    def get_user(self, user_id: int) -> UserDTO:
        # Placeholder for real HTTP request (requests/httpx).
        # In production, this method would call an API endpoint.
        if user_id <= 0:
            raise ApiClientError("user_id must be positive")
        return UserDTO(id=user_id, email=f"user{user_id}@example.com")


if __name__ == "__main__":
    client = ApiClient("https://api.example.com", timeout_s=2.0)
    print(client.get_user(1))
