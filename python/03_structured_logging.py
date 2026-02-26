"""
Technique: Structured Logging (Context-Rich, Queryable Logs)
Use When:
- Logs are machine-parseable and easier to search in production
- Every log line carries context (request_id, user_id, item_count, etc.)
- Failures become diagnosable without reproducing locally
"""

import logging
from dataclasses import dataclass


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(name)s %(message)s",
)
logger = logging.getLogger("pricing")


@dataclass(frozen=True)
class LineItem:
    name: str
    price: float
    qty: int


def calculate_totals(items: list[LineItem], tax: float, request_id: str) -> dict[str, float]:
    logger.info(
        "event=pricing_start request_id=%s item_count=%d tax=%.4f",
        request_id,
        len(items),
        tax,
    )

    if tax < 0:
        logger.warning("event=pricing_invalid_tax request_id=%s tax=%.4f", request_id, tax)
        raise ValueError("tax must be >= 0")

    totals: dict[str, float] = {}
    for item in items:
        if item.price < 0 or item.qty <= 0:
            logger.warning(
                "event=pricing_invalid_item request_id=%s item_name=%s price=%.2f qty=%d",
                request_id,
                item.name,
                item.price,
                item.qty,
            )
            raise ValueError(f"invalid item: {item.name}")

        totals[item.name] = round(item.price * item.qty * (1 + tax), 2)

    logger.info(
        "event=pricing_success request_id=%s unique_items=%d",
        request_id,
        len(totals),
    )
    return totals


if __name__ == "__main__":
    request_id = "req-2026-02-26-001"
    items = [LineItem("Book", 12.5, 2), LineItem("Pen", 1.2, 3)]

    try:
        totals = calculate_totals(items=items, tax=0.1, request_id=request_id)
        print("Totals:", totals)
    except ValueError as exc:
        logger.exception("event=pricing_failed request_id=%s error=%s", request_id, exc)
