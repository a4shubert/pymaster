"""
Technique: Token Bucket Rate Limiter
Use When:
- Protects services from overload
- Enforces fair usage across callers
- Smooths burst traffic
"""

import time
from dataclasses import dataclass


@dataclass
class TokenBucket:
    capacity: float
    refill_rate_per_s: float

    _tokens: float | None = None
    _last: float | None = None

    def allow(self, cost: float = 1.0) -> bool:
        now = time.time()
        if self._tokens is None:
            self._tokens = self.capacity
            self._last = now

        assert self._last is not None
        elapsed = now - self._last
        self._tokens = min(self.capacity, self._tokens + elapsed * self.refill_rate_per_s)
        self._last = now

        if cost <= self._tokens:
            self._tokens -= cost
            return True
        return False


if __name__ == "__main__":
    bucket = TokenBucket(capacity=3, refill_rate_per_s=1)
    for i in range(10):
        allowed = bucket.allow()
        print(i, "allowed" if allowed else "blocked")
        time.sleep(0.2)
