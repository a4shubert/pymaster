"""
Technique: Dunder Methods (__repr__, __str__, ordering)
Use When:
- Good __repr__ helps debugging and logging
- Rich comparisons enable sorting and consistent behavior
- Value objects behave like values
"""

from dataclasses import dataclass


@dataclass(frozen=True, order=True)
class Version:
    major: int
    minor: int
    patch: int

    def __str__(self) -> str:
        return f"{self.major}.{self.minor}.{self.patch}"


if __name__ == "__main__":
    versions = [Version(1, 2, 0), Version(1, 1, 9), Version(2, 0, 0)]
    print("sorted:", [str(v) for v in sorted(versions)])
    print("repr:", versions[0])
