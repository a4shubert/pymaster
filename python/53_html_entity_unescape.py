"""
Technique: HTML Entity Handling with html.unescape

Why this matters:
- Web pages often contain entities (&amp;, &lt;, &quot;).
- You typically want to decode entities before processing text.

Pattern:
1) Extract text.
2) Apply html.unescape.
3) Normalize whitespace if needed.
"""

import html


def normalize_text(raw: str) -> str:
    return " ".join(html.unescape(raw).split())


if __name__ == "__main__":
    s = "Tom &amp; Jerry &lt;3  \n  "
    print(normalize_text(s))
