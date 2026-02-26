# Technique: URL Parsing with urllib.parse
# Use When:
# - Correct URL parsing avoids subtle bugs (encoding, query params, fragments)
# - Safer than manual string splitting

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
