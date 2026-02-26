# Technique: ThreadPoolExecutor for Blocking I/O
# Use When:
# - Speeds up independent blocking operations
# - Keeps code simple when APIs are synchronous
# - Controls concurrency level explicitly

import time
from concurrent.futures import ThreadPoolExecutor, as_completed


def fetch_profile(user_id: int) -> str:
    # Simulated blocking I/O call.
    time.sleep(0.2)
    return f"user-{user_id}"


def fetch_many(user_ids: list[int]) -> list[str]:
    results: list[str] = []
    with ThreadPoolExecutor(max_workers=4) as pool:
        futures = [pool.submit(fetch_profile, user_id) for user_id in user_ids]
        for future in as_completed(futures):
            results.append(future.result())
    return results


if __name__ == "__main__":
    print(fetch_many([1, 2, 3, 4, 5]))
