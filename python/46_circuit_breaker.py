"""
Technique: Circuit Breaker (Protect Dependencies)

Why this is enterprise:
- Prevents cascading failures when a downstream service is unhealthy.
- Gives the dependency time to recover.
- Improves overall system stability.

Pattern:
1) Track consecutive failures.
2) Open the circuit after a threshold.
3) Half-open after cooldown to probe recovery.
"""

import time
from dataclasses import dataclass
from typing import Callable


class CircuitOpenError(RuntimeError):
    pass


@dataclass
class CircuitBreaker:
    failure_threshold: int
    cooldown_s: float

    _failures: int = 0
    _opened_at: float | None = None

    def call(self, func: Callable[[], str]) -> str:
        now = time.time()
        if self._opened_at is not None:
            if now - self._opened_at < self.cooldown_s:
                raise CircuitOpenError("circuit is open")
            # half-open: allow a probe call
            self._opened_at = None
            self._failures = 0

        try:
            out = func()
        except Exception:
            self._failures += 1
            if self._failures >= self.failure_threshold:
                self._opened_at = time.time()
            raise

        self._failures = 0
        return out


def flaky_factory() -> Callable[[], str]:
    state = {"n": 0}

    def f() -> str:
        state["n"] += 1
        if state["n"] <= 3:
            raise RuntimeError("downstream timeout")
        return "ok"

    return f


if __name__ == "__main__":
    cb = CircuitBreaker(failure_threshold=2, cooldown_s=1.0)
    f = flaky_factory()

    for i in range(1, 7):
        try:
            print(i, cb.call(f))
        except Exception as exc:
            print(i, type(exc).__name__, exc)
        time.sleep(0.3)
