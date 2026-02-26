# Technique: Performance Hygiene (copies, chained assignment)
# Use When:
# - Research code becomes slow or wrong due to chained assignment
# - In production, you want explicit `.copy()` boundaries

import pandas as pd


def demo() -> None:
    df = pd.DataFrame({"a": [1, 2, 3, 4], "b": [10, 20, 30, 40]})

    # Good: explicit loc assignment
    mask = df["a"] % 2 == 0
    df.loc[mask, "b"] = df.loc[mask, "b"] * 2

    # Good: explicit copy boundary for derived frame
    even = df.loc[mask, ["a", "b"]].copy()
    even["c"] = even["a"] + even["b"]

    print(df)
    print(even)


if __name__ == "__main__":
    demo()
