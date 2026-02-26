# Technique: Caching with functools.lru_cache
# Use When:
# - Avoids repeating expensive pure computations
# - Improves latency with minimal code
# - Makes performance tuning explicit and bounded

import time
from functools import lru_cache


@lru_cache(maxsize=128)
def currency_rate(base: str, quote: str) -> float:
    # Simulate expensive call.
    time.sleep(0.2)
    rates = {("USD", "EUR"): 0.92, ("USD", "JPY"): 148.0}
    if (base, quote) not in rates:
        raise ValueError(f"unsupported pair: {base}/{quote}")
    return rates[(base, quote)]


if __name__ == "__main__":
    print(currency_rate("USD", "EUR"))
    print(currency_rate("USD", "EUR"))
    print(currency_rate.cache_info())
