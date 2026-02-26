# Technique: Custom Exceptions for Clear Error Contracts
# Use When:
# - Callers can handle failures by category instead of string matching
# - Domain errors are separated from low-level runtime errors
# - Error handling becomes predictable in services and APIs

from dataclasses import dataclass


class PricingError(Exception):
    """Base exception for pricing domain errors."""


class InvalidTaxError(PricingError):
    pass


class InvalidItemError(PricingError):
    pass


class DuplicateItemError(PricingError):
    pass


@dataclass(frozen=True)
class LineItem:
    name: str
    price: float
    qty: int


def validate_item(item: LineItem) -> None:
    if not item.name.strip():
        raise InvalidItemError("name must be non-empty")
    if item.price < 0:
        raise InvalidItemError(f"price must be >= 0 for '{item.name}'")
    if item.qty <= 0:
        raise InvalidItemError(f"qty must be > 0 for '{item.name}'")


def calculate_totals(items: list[LineItem], tax: float) -> dict[str, float]:
    if tax < 0:
        raise InvalidTaxError("tax must be >= 0")

    totals: dict[str, float] = {}
    for item in items:
        validate_item(item)
        if item.name in totals:
            raise DuplicateItemError(f"duplicate item name: '{item.name}'")
        totals[item.name] = round(item.price * item.qty * (1 + tax), 2)

    return totals


def run_pricing(items: list[LineItem], tax: float) -> None:
    """Boundary function (like CLI/API handler)."""
    try:
        totals = calculate_totals(items, tax)
        print("OK:", totals)
    except PricingError as exc:
        print("Pricing failed:", exc)


if __name__ == "__main__":
    good_items = [LineItem("Book", 10.0, 2), LineItem("Pen", 1.5, 3)]
    bad_items = [LineItem("", 10.0, 1)]

    run_pricing(good_items, tax=0.1)
    run_pricing(bad_items, tax=0.1)
