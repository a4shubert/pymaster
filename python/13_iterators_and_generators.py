"""
Technique: Generators for Streaming Data
Use When:
- Processes large inputs lazily instead of loading everything in memory
- Keeps pipelines composable and efficient
- Simplifies line-by-line or record-by-record processing
"""

from collections.abc import Iterable, Iterator


def parse_ints(rows: Iterable[str]) -> Iterator[int]:
    for row in rows:
        row = row.strip()
        if not row:
            continue
        yield int(row)


def non_negative(values: Iterable[int]) -> Iterator[int]:
    for value in values:
        if value >= 0:
            yield value


def squared(values: Iterable[int]) -> Iterator[int]:
    for value in values:
        yield value * value


if __name__ == "__main__":
    rows = ["10", "-3", "5", "", "2"]
    pipeline = squared(non_negative(parse_ints(rows)))
    print(list(pipeline))
