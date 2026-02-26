"""
Technique: map/filter + Comprehensions (Declarative Data Transforms)

Why this is professional:
- Expresses transformation intent clearly.
- Reduces mutable state and loop noise.
- Easy to test by comparing input/output.

Rule of thumb:
- Prefer comprehensions for readability.
- Use map/filter when it makes the pipeline clearer.
"""


def normalize_emails(raw: list[str]) -> list[str]:
    return [e.strip().lower() for e in raw if e.strip()]


if __name__ == "__main__":
    data = [" Dev@Example.com ", "", "ADMIN@EXAMPLE.COM"]
    print(normalize_emails(data))
