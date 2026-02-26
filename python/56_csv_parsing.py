"""
Technique: CSV Parsing with csv.DictReader
Use When:
- Web exports and integrations often deliver CSV
- DictReader handles headers and quoting correctly
"""

import csv
import io


def parse_rows(csv_text: str) -> list[dict[str, str]]:
    f = io.StringIO(csv_text)
    reader = csv.DictReader(f)
    rows: list[dict[str, str]] = []
    for row in reader:
        if row.get("email") is None:
            raise ValueError("missing email column")
        rows.append({k: (v or "").strip() for k, v in row.items() if k is not None})
    return rows


if __name__ == "__main__":
    csv_text = "id,email\n1, dev@example.com \n2,admin@example.com\n"
    print(parse_rows(csv_text))
