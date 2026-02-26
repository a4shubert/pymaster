"""
Technique: HTTP Header Parsing with email.message

Why this matters:
- Headers are structured but messy (case-insensitive, folding, duplicates).
- Standard library provides robust parsing.

Pattern:
1) Parse raw headers.
2) Access values case-insensitively.
3) Handle missing/duplicate headers.
"""

from email.parser import Parser


def parse_headers(raw: str) -> dict[str, str]:
    msg = Parser().parsestr(raw)
    return {k: v for k, v in msg.items()}


if __name__ == "__main__":
    raw = """Host: example.com\nContent-Type: text/html; charset=utf-8\nX-Test: a\nX-Test: b\n"""
    print(parse_headers(raw))
