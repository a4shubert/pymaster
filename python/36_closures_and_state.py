"""
Technique: Closures (State without Classes)

Why this is professional:
- Encapsulates state in a small, testable unit.
- Useful for lightweight counters, memoization, configuration.
- Avoids over-engineering with classes.

Pattern:
1) Keep state in an enclosing scope.
2) Expose minimal functions that operate on that state.
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
