# Technique: Dataclasses with slots (Memory + Attribute Safety)
# Use When:
# - `slots=True` reduces per-instance overhead for many objects
# - Prevents accidental attribute creation (typos become errors)
# - Works well for large collections of objects

from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class Point:
    x: float
    y: float


if __name__ == "__main__":
    p = Point(1.0, 2.0)
    print(p)
    # This would fail (good): p.z = 3.0
