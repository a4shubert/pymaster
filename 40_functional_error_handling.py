"""
Technique: Functional Error Handling (Result Pattern)

Why this is professional:
- Makes success/failure explicit in return types.
- Avoids using exceptions for expected control flow.
- Works well in pipelines and batch processing.

Pattern:
1) Return (ok, value/error).
2) Callers handle both branches explicitly.
3) Keep errors informative.
"""

from dataclasses import dataclass


@dataclass(frozen=True)
class Ok:
    value: float


@dataclass(frozen=True)
class Err:
    error: str


Result = Ok | Err


def parse_float(raw: str) -> Result:
    try:
        return Ok(float(raw))
    except ValueError:
        return Err(f"not a float: {raw!r}")


if __name__ == "__main__":
    for raw in ["1.2", "x"]:
        res = parse_float(raw)
        match res:
            case Ok(value=v):
                print("ok", v)
            case Err(error=e):
                print("err", e)
