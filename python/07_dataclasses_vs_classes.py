"""
Technique: Dataclasses vs Regular Classes (Choose the Right Model)
Use When:
- `@dataclass` removes boilerplate for data containers
- Regular classes are better when behavior/lifecycle dominates
- Clear model choice improves readability and maintainability
"""

from dataclasses import dataclass


@dataclass(frozen=True)
class Money:
    amount: float
    currency: str

    def add(self, other: "Money") -> "Money":
        if self.currency != other.currency:
            raise ValueError("cannot add different currencies")
        return Money(amount=round(self.amount + other.amount, 2), currency=self.currency)


class InvoiceService:
    def __init__(self, tax_rate: float) -> None:
        if tax_rate < 0:
            raise ValueError("tax_rate must be >= 0")
        self._tax_rate = tax_rate

    def total_with_tax(self, subtotal: Money) -> Money:
        taxed = subtotal.amount * (1 + self._tax_rate)
        return Money(amount=round(taxed, 2), currency=subtotal.currency)


if __name__ == "__main__":
    line1 = Money(10.0, "USD")
    line2 = Money(15.5, "USD")
    subtotal = line1.add(line2)

    service = InvoiceService(tax_rate=0.1)
    total = service.total_with_tax(subtotal)

    print("Subtotal:", subtotal)
    print("Total:", total)
