# Technique: Descriptors (Reusable Attribute Validation)
# Use When:
# - Centralizes repeated validation logic
# - Enforces invariants across multiple classes
# - Useful for lightweight domain models

from __future__ import annotations


class PositiveFloat:
    def __set_name__(self, owner: type, name: str) -> None:
        self._private_name = f"_{name}"

    def __get__(self, obj: object, objtype: type | None = None) -> float:
        if obj is None:
            return self  # type: ignore[return-value]
        return float(getattr(obj, self._private_name))

    def __set__(self, obj: object, value: float) -> None:
        if not isinstance(value, (int, float)):
            raise TypeError("value must be numeric")
        if value <= 0:
            raise ValueError("value must be > 0")
        setattr(obj, self._private_name, float(value))


class Product:
    price = PositiveFloat()

    def __init__(self, name: str, price: float) -> None:
        self.name = name
        self.price = price


if __name__ == "__main__":
    p = Product("Book", 10.0)
    print(p.name, p.price)
