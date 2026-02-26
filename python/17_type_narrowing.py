# Technique: Type Narrowing and Type Guards
# Use When:
# - Reduces runtime type errors
# - Lets static checkers prove safety after validation
# - Makes heterogeneous input handling explicit

from typing import Any, TypeGuard


def is_price_payload(value: Any) -> TypeGuard[dict[str, float]]:
    if not isinstance(value, dict):
        return False
    return isinstance(value.get("price"), (int, float)) and isinstance(value.get("tax"), (int, float))


def compute_from_unknown(payload: Any) -> float:
    if not is_price_payload(payload):
        raise ValueError("payload must contain numeric price and tax")

    price = float(payload["price"])
    tax = float(payload["tax"])
    if price < 0 or tax < 0:
        raise ValueError("price and tax must be >= 0")
    return round(price * (1 + tax), 2)


if __name__ == "__main__":
    print(compute_from_unknown({"price": 10.0, "tax": 0.1}))
