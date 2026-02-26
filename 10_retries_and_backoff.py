"""
Technique: Retries with Exponential Backoff (Resilient External Calls)

Why this is professional:
- External services fail transiently (timeouts, rate limits, network blips).
- Controlled retries improve reliability without spamming dependencies.
- Backoff + jitter reduces synchronized retry storms.

Pattern:
1) Retry only transient errors.
2) Cap attempts and delay growth.
3) Add jitter and log each attempt.
"""

import random
import time
from typing import Callable


class TransientError(Exception):
    pass


class PermanentError(Exception):
    pass


def compute_backoff_delay(attempt: int, base_delay: float, max_delay: float) -> float:
    delay = min(base_delay * (2 ** (attempt - 1)), max_delay)
    jitter = random.uniform(0, delay * 0.25)
    return delay + jitter


def with_retries(
    func: Callable[[], str],
    *,
    attempts: int = 4,
    base_delay: float = 0.2,
    max_delay: float = 2.0,
) -> str:
    if attempts < 1:
        raise ValueError("attempts must be >= 1")

    for attempt in range(1, attempts + 1):
        try:
            return func()
        except PermanentError:
            # Do not retry non-transient failures.
            raise
        except TransientError as exc:
            if attempt == attempts:
                raise RuntimeError(f"failed after {attempts} attempts") from exc

            sleep_for = compute_backoff_delay(attempt, base_delay, max_delay)
            print(f"attempt={attempt} transient_error='{exc}' retry_in={sleep_for:.2f}s")
            time.sleep(sleep_for)

    raise RuntimeError("unexpected retry flow")


def flaky_call_factory() -> Callable[[], str]:
    state = {"count": 0}

    def flaky_call() -> str:
        state["count"] += 1
        if state["count"] < 3:
            raise TransientError("temporary timeout")
        return "success"

    return flaky_call


if __name__ == "__main__":
    call = flaky_call_factory()
    result = with_retries(call, attempts=5, base_delay=0.1, max_delay=0.5)
    print("result:", result)
