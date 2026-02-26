"""
Technique: Strategy Pattern (Swap Algorithms Cleanly)

Why this is professional:
- Avoids large if/else trees for behavior selection.
- Makes algorithms testable in isolation.
- Enables runtime selection (config, feature flags).

Pattern:
1) Define a strategy interface.
2) Implement multiple strategies.
3) Inject strategy into the service.
"""

from dataclasses import dataclass
from typing import Protocol


@dataclass(frozen=True)
class Order:
    subtotal: float


class ShippingStrategy(Protocol):
    def shipping_cost(self, order: Order) -> float:
        ...


class FlatRateShipping:
    def __init__(self, fee: float) -> None:
        self._fee = fee

    def shipping_cost(self, order: Order) -> float:
        return self._fee


class FreeOverThreshold:
    def __init__(self, threshold: float, fee: float) -> None:
        self._threshold = threshold
        self._fee = fee

    def shipping_cost(self, order: Order) -> float:
        return 0.0 if order.subtotal >= self._threshold else self._fee


class CheckoutService:
    def __init__(self, shipping: ShippingStrategy) -> None:
        self._shipping = shipping

    def total(self, order: Order) -> float:
        if order.subtotal < 0:
            raise ValueError("subtotal must be >= 0")
        return round(order.subtotal + self._shipping.shipping_cost(order), 2)


if __name__ == "__main__":
    order = Order(subtotal=49.99)
    print(CheckoutService(FlatRateShipping(5.0)).total(order))
    print(CheckoutService(FreeOverThreshold(50.0, 5.0)).total(order))
