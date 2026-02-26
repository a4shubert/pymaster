"""
Technique: Unit Testing with pytest (Fast, Focused, Deterministic)
Use When:
- Tests verify behavior and protect against regressions
- Unit tests run fast because they isolate one unit of logic
- Parametrization reduces repetitive test code
"""

from dataclasses import dataclass


@dataclass(frozen=True)
class LineItem:
    name: str
    price: float
    qty: int


def calculate_total(item: LineItem, tax: float) -> float:
    if tax < 0:
        raise ValueError("tax must be >= 0")
    if item.price < 0:
        raise ValueError("price must be >= 0")
    if item.qty <= 0:
        raise ValueError("qty must be > 0")

    return round(item.price * item.qty * (1 + tax), 2)


# Example pytest tests (put in a test file, e.g. tests/test_pricing.py)
# ---------------------------------------------------------------
# import pytest
# from 05_pytest_unit_tests import LineItem, calculate_total
#
# def test_calculate_total_happy_path():
#     item = LineItem(name="Book", price=10.0, qty=2)
#     assert calculate_total(item, tax=0.1) == 22.0
#
# @pytest.mark.parametrize(
#     "item,tax,expected_error",
#     [
#         (LineItem("Book", -1.0, 1), 0.1, "price must be >= 0"),
#         (LineItem("Book", 10.0, 0), 0.1, "qty must be > 0"),
#         (LineItem("Book", 10.0, 1), -0.01, "tax must be >= 0"),
#     ],
# )
# def test_calculate_total_validation_errors(item, tax, expected_error):
#     with pytest.raises(ValueError, match=expected_error):
#         calculate_total(item, tax)


if __name__ == "__main__":
    # Demo run only; real verification should be in pytest tests.
    sample = LineItem(name="Book", price=10.0, qty=2)
    print(calculate_total(sample, tax=0.1))
