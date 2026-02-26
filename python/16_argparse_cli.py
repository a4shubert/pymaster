# Technique: CLI Design with argparse
# Use When:
# - Provides discoverable commands and help text
# - Validates user input at the command boundary
# - Makes scripts reusable in automation and CI

import argparse


def calculate_total(price: float, qty: int, tax: float) -> float:
    if price < 0 or qty <= 0 or tax < 0:
        raise ValueError("invalid input values")
    return round(price * qty * (1 + tax), 2)


def main() -> int:
    parser = argparse.ArgumentParser(description="Compute line total with tax")
    parser.add_argument("--price", type=float, required=True)
    parser.add_argument("--qty", type=int, required=True)
    parser.add_argument("--tax", type=float, default=0.0)
    args = parser.parse_args()

    try:
        total = calculate_total(args.price, args.qty, args.tax)
    except ValueError as exc:
        print(f"error: {exc}")
        return 2

    print(total)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
