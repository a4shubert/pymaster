"""
Technique: URL Parsing with urllib.parse

Why this matters:
- Correct URL parsing avoids subtle bugs (encoding, query params, fragments).
- Safer than manual string splitting.

Pattern:
1) Use urlsplit/urlunsplit.
2) Use parse_qs/urlencode for query strings.
3) Normalize/validate before use.
"""

from urllib.parse import parse_qs, urlencode, urlsplit, urlunsplit


def add_query_param(url: str, key: str, value: str) -> str:
    parts = urlsplit(url)
    query = parse_qs(parts.query, keep_blank_values=True)
    query.setdefault(key, []).append(value)
    new_query = urlencode(query, doseq=True)
    return urlunsplit((parts.scheme, parts.netloc, parts.path, new_query, parts.fragment))


if __name__ == "__main__":
    u = "https://example.com/search?q=python#top"
    print(add_query_param(u, "page", "2"))
