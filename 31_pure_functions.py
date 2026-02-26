"""
Technique: Pure Functions (Predictable, Testable Code)

Why this is professional:
- Pure functions are deterministic: same inputs, same output.
- No hidden side effects makes testing and reasoning easy.
- Encourages clean boundaries between logic and I/O.

Pattern:
1) Keep inputs explicit.
2) Return new values (do not mutate inputs).
3) Separate pure logic from I/O wrappers.
"""

from dataclasses import dataclass


@dataclass(frozen=True)
class LineItem:
    name: str
    price: float
    qty: int


def line_total(item: LineItem, tax: float) -> float:
    if tax < 0 or item.price < 0 or item.qty <= 0:
        raise ValueError("invalid inputs")
    return round(item.price * item.qty * (1 + tax), 2)


if __name__ == "__main__":
    print(line_total(LineItem("Book", 10.0, 2), tax=0.1))
