"""
Technique: Dependency Injection (Design for Testability)
Use When:
- Business logic does not hardcode external systems (DB, API, clock, email)
- You can swap real implementations with fakes in tests
- Code becomes modular and easier to evolve
"""

from dataclasses import dataclass
from typing import Protocol


@dataclass(frozen=True)
class LineItem:
    name: str
    price: float
    qty: int


class TaxProvider(Protocol):
    def get_tax_rate(self, region: str) -> float:
        ...


class StaticTaxProvider:
    def __init__(self, rates: dict[str, float]) -> None:
        self._rates = rates

    def get_tax_rate(self, region: str) -> float:
        if region not in self._rates:
            raise ValueError(f"unknown region: {region}")
        return self._rates[region]


class PricingService:
    def __init__(self, tax_provider: TaxProvider) -> None:
        self._tax_provider = tax_provider

    def calculate_totals(self, items: list[LineItem], region: str) -> dict[str, float]:
        tax = self._tax_provider.get_tax_rate(region)
        if tax < 0:
            raise ValueError("tax must be >= 0")

        totals: dict[str, float] = {}
        for item in items:
            if item.qty <= 0 or item.price < 0:
                raise ValueError(f"invalid item: {item.name}")
            totals[item.name] = round(item.price * item.qty * (1 + tax), 2)

        return totals


if __name__ == "__main__":
    provider = StaticTaxProvider({"US-CA": 0.0825, "US-NY": 0.088})
    service = PricingService(provider)

    items = [LineItem("Book", 12.5, 2), LineItem("Pen", 1.2, 3)]
    print(service.calculate_totals(items, region="US-CA"))
