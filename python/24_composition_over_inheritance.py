# Technique: Composition Over Inheritance
# Use When:
# - Inheritance is strong coupling; composition stays flexible
# - Behaviors can be swapped at runtime (policies/strategies)
# - Avoids fragile base-class problems

from dataclasses import dataclass
from typing import Protocol


@dataclass(frozen=True)
class LineItem:
    name: str
    price: float
    qty: int


class DiscountPolicy(Protocol):
    def discount_rate(self, item: LineItem) -> float:
        ...


class NoDiscount:
    def discount_rate(self, item: LineItem) -> float:
        return 0.0


class NamePrefixDiscount:
    def __init__(self, prefix: str, rate: float) -> None:
        self._prefix = prefix
        self._rate = rate

    def discount_rate(self, item: LineItem) -> float:
        return self._rate if item.name.startswith(self._prefix) else 0.0


class Pricing:
    def __init__(self, discount_policy: DiscountPolicy) -> None:
        self._discount_policy = discount_policy

    def total(self, item: LineItem, tax: float) -> float:
        if tax < 0:
            raise ValueError("tax must be >= 0")
        if item.price < 0 or item.qty <= 0:
            raise ValueError(f"invalid item: {item.name}")

        rate = self._discount_policy.discount_rate(item)
        if not (0 <= rate < 1):
            raise ValueError("discount rate out of range")

        subtotal = item.price * item.qty
        discounted = subtotal * (1 - rate)
        return round(discounted * (1 + tax), 2)


if __name__ == "__main__":
    item = LineItem("A-BOOK", 20.0, 1)
    print(Pricing(NoDiscount()).total(item, tax=0.1))
    print(Pricing(NamePrefixDiscount("A-", 0.2)).total(item, tax=0.1))
