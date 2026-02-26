"""
Technique: asyncio Basics (Concurrent I/O without Threads)
Use When:
- Efficient for many I/O-bound tasks (HTTP calls, DB/network waits)
- Clear control over concurrency with `await` and task groups
- Better throughput when tasks spend time waiting
"""

import asyncio
from dataclasses import dataclass


@dataclass(frozen=True)
class Product:
    sku: str
    base_price: float


async def fetch_discount(sku: str) -> float:
    # Simulated I/O latency (e.g., external API call)
    await asyncio.sleep(0.2)
    return 0.1 if sku.startswith("A") else 0.05


async def price_with_discount(product: Product) -> tuple[str, float]:
    discount = await fetch_discount(product.sku)
    final_price = round(product.base_price * (1 - discount), 2)
    return product.sku, final_price


async def price_all(products: list[Product]) -> dict[str, float]:
    tasks = [price_with_discount(product) for product in products]
    pairs = await asyncio.gather(*tasks)
    return dict(pairs)


async def main() -> None:
    products = [
        Product("A-BOOK", 20.0),
        Product("B-PEN", 5.0),
        Product("A-NOTE", 10.0),
    ]
    priced = await price_all(products)
    print(priced)


if __name__ == "__main__":
    asyncio.run(main())
