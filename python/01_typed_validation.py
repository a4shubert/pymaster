"""
Technique: Typed Validation Boundary (Parse Early, Trust Internal Data)
Use When:
- External input (APIs, files, user JSON) is untrusted
- Validate once at the boundary
- Convert to a typed domain model, then keep internal code strict and simple
"""

from dataclasses import dataclass
from typing import Any


@dataclass(frozen=True)
class LineItem:
    name: str
    price: float
    qty: int


def parse_line_item(raw: dict[str, Any]) -> LineItem:
    required = {"name", "price", "qty"}
    missing = required - set(raw)
    if missing:
        raise ValueError(f"missing keys: {sorted(missing)}")

    name = raw["name"]
    price = raw["price"]
    qty = raw["qty"]

    if not isinstance(name, str) or not name.strip():
        raise ValueError("name must be a non-empty string")
    if not isinstance(price, (int, float)):
        raise ValueError(f"price must be numeric for '{name}'")
    if not isinstance(qty, int):
        raise ValueError(f"qty must be an integer for '{name}'")
    if price < 0:
        raise ValueError(f"price must be >= 0 for '{name}'")
    if qty <= 0:
        raise ValueError(f"qty must be > 0 for '{name}'")

    return LineItem(name=name, price=float(price), qty=qty)


def calculate_totals(items: list[LineItem], tax: float) -> dict[str, float]:
    if tax < 0:
        raise ValueError("tax must be >= 0")

    result: dict[str, float] = {}
    for item in items:
        if item.name in result:
            raise ValueError(f"duplicate item name: '{item.name}'")
        result[item.name] = round(item.price * item.qty * (1 + tax), 2)
    return result


if __name__ == "__main__":
    raw_items = [
        {"name": "Book", "price": 12.5, "qty": 2},
        {"name": "Pen", "price": 1.2, "qty": 3},
    ]

    typed_items = [parse_line_item(raw) for raw in raw_items]
    print(calculate_totals(typed_items, tax=0.1))
