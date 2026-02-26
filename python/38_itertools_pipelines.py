"""
Technique: itertools Pipelines (Lazy, Composable Data Processing)

Why this is professional:
- Efficient for large sequences (lazy evaluation).
- Powerful building blocks for data pipelines.
- Keeps memory usage low.

Pattern:
1) Use generator/iterators.
2) Combine with itertools tools.
3) Materialize at the boundary.
"""

import itertools


def chunked(values: list[int], size: int) -> list[list[int]]:
    if size <= 0:
        raise ValueError("size must be > 0")
    it = iter(values)
    out: list[list[int]] = []
    while True:
        chunk = list(itertools.islice(it, size))
        if not chunk:
            break
        out.append(chunk)
    return out


if __name__ == "__main__":
    print(chunked([1, 2, 3, 4, 5], 2))
