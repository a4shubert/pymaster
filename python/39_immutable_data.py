"""
Technique: Immutable Data (Safer by Default)
Use When:
- Reduces bugs from shared mutable state
- Makes functions easier to reason about
- Fits naturally with concurrency
"""

from dataclasses import dataclass


@dataclass(frozen=True)
class Cart:
    items: tuple[str, ...]


def add_item(cart: Cart, item: str) -> Cart:
    if not item:
        raise ValueError("item must be non-empty")
    return Cart(items=cart.items + (item,))


if __name__ == "__main__":
    cart = Cart(items=())
    cart2 = add_item(cart, "Book")
    print(cart, cart2)
