# Technique: itertools Pipelines (Lazy, Composable Data Processing)
# Use When:
# - Efficient for large sequences (lazy evaluation)
# - Powerful building blocks for data pipelines
# - Keeps memory usage low

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
