"""
Technique: Context Managers (Reliable Resource Cleanup)
Use When:
- Resources (files, DB sessions, locks, timers) are always cleaned up
- Cleanup runs even when exceptions happen
- Code is safer and easier to reason about
"""

from contextlib import contextmanager
from time import perf_counter


@contextmanager
def timed_block(label: str):
    start = perf_counter()
    try:
        yield
    finally:
        duration_ms = (perf_counter() - start) * 1000
        print(f"{label} took {duration_ms:.2f} ms")


def load_numbers(path: str) -> list[int]:
    numbers: list[int] = []
    # Built-in context manager closes file automatically.
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            numbers.append(int(line))
    return numbers


def compute_sum(path: str) -> int:
    with timed_block("compute_sum"):
        values = load_numbers(path)
        return sum(values)


if __name__ == "__main__":
    sample_path = "/tmp/pymaster_numbers.txt"

    with open(sample_path, "w", encoding="utf-8") as f:
        f.write("10\n20\n30\n")

    total = compute_sum(sample_path)
    print("Total:", total)
