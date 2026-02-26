"""
Technique: Mixins (Optional Shared Behavior)
Use When:
- Reuses small behavior without deep inheritance
- Keeps feature sets composable
- Avoids monolithic base classes
"""

from dataclasses import dataclass


class JsonSerializableMixin:
    def to_json(self) -> dict[str, object]:
        return self.__dict__.copy()


class AuditMixin:
    def audit_line(self) -> str:
        return f"audit type={type(self).__name__}"


@dataclass
class User(JsonSerializableMixin, AuditMixin):
    id: int
    email: str


if __name__ == "__main__":
    user = User(id=1, email="dev@example.com")
    print(user.to_json())
    print(user.audit_line())
