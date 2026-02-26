"""
Technique: reduce (Folds) for Aggregation

Why this is professional:
- Captures aggregation logic as a single expression.
- Useful when building up a value with a clear accumulator.
- Works well with immutable accumulator patterns.

Note:
- In Python, explicit loops can be clearer than reduce.
- Use reduce when it improves readability.
"""

from functools import reduce


def total_length(words: list[str]) -> int:
    return reduce(lambda acc, w: acc + len(w), words, 0)


if __name__ == "__main__":
    print(total_length(["a", "bb", "ccc"]))
