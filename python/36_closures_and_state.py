"""
Technique: Closures (State without Classes)
Use When:
- Encapsulates state in a small, testable unit
- Useful for lightweight counters, memoization, configuration
- Avoids over-engineering with classes
"""

from collections.abc import Callable


def make_counter() -> Callable[[], int]:
    state = {"count": 0}

    def inc() -> int:
        state["count"] += 1
        return state["count"]

    return inc


if __name__ == "__main__":
    c = make_counter()
    print(c(), c(), c())
