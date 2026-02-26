"""
Technique: Handling gzip-compressed HTTP bodies
Use When:
- Many web servers compress responses
- You need to decode correctly based on Content-Encoding
"""

import gzip


def decode_gzip_body(body: bytes, charset: str = "utf-8") -> str:
    decompressed = gzip.decompress(body)
    return decompressed.decode(charset, errors="replace")


if __name__ == "__main__":
    original = "hello gzip"
    compressed = gzip.compress(original.encode("utf-8"))
    print(decode_gzip_body(compressed))
