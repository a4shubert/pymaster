"""
Technique: Higher-Order Functions (Functions that Take/Return Functions)

Why this is professional:
- Lets you inject behavior without inheritance.
- Enables reusable transformations and policies.
- Keeps code declarative and composable.

Pattern:
1) Accept a callable as an argument.
2) Return a callable for specialization.
3) Keep the callable contracts small.
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
