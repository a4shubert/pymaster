"""
Technique: functools.partial (Practical Currying)
Use When:
- Pre-binds arguments to create specialized functions
- Reduces repetitive parameter passing
- Creates clearer APIs for pipelines
"""

from functools import partial


def compute_total(price: float, qty: int, tax: float) -> float:
    if price < 0 or qty <= 0 or tax < 0:
        raise ValueError("invalid inputs")
    return round(price * qty * (1 + tax), 2)


if __name__ == "__main__":
    compute_with_tax = partial(compute_total, tax=0.1)
    print(compute_with_tax(price=10.0, qty=2))
