"""
Technique: Higher-Order Functions (Functions that Take/Return Functions)
Use When:
- Lets you inject behavior without inheritance
- Enables reusable transformations and policies
- Keeps code declarative and composable
"""

from collections.abc import Callable


def make_multiplier(factor: float) -> Callable[[float], float]:
    def multiply(x: float) -> float:
        return x * factor

    return multiply


def apply_all(values: list[float], fn: Callable[[float], float]) -> list[float]:
    return [fn(v) for v in values]


if __name__ == "__main__":
    times_two = make_multiplier(2)
    print(apply_all([1.0, 2.5, 3.0], times_two))
