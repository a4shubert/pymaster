"""
Technique: Context Manager as a Class (__enter__/__exit__)
Use When:
- Stateful context managers are sometimes clearer than generator-based
- Useful for resource objects (connections, locks, tracing spans)
- __exit__ controls whether exceptions are suppressed
"""

from __future__ import annotations

from time import perf_counter


class Timer:
    def __init__(self, label: str) -> None:
        self._label = label
        self._start: float | None = None

    def __enter__(self) -> "Timer":
        self._start = perf_counter()
        return self

    def __exit__(self, exc_type, exc, tb) -> bool:
        if self._start is None:
            return False
        duration_ms = (perf_counter() - self._start) * 1000
        print(f"{self._label} took {duration_ms:.2f} ms")
        return False


if __name__ == "__main__":
    with Timer("work"):
        total = sum(range(100_000))
    print("total:", total)
