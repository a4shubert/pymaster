"""
Technique: Parsing XML Sitemaps (sitemap.xml)

Why this matters:
- Sitemaps are a common, crawl-friendly way to discover URLs.
- Namespaces are the main gotcha when parsing.

Pattern:
1) Parse XML.
2) Handle namespaces.
3) Extract <loc> values.
"""

import xml.etree.ElementTree as ET


def extract_sitemap_urls(xml_text: str) -> list[str]:
    root = ET.fromstring(xml_text)
    ns = {"sm": "http://www.sitemaps.org/schemas/sitemap/0.9"}
    return [el.text or "" for el in root.findall("./sm:url/sm:loc", ns)]


if __name__ == "__main__":
    xml_text = """
    <urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
      <url><loc>https://example.com/</loc></url>
      <url><loc>https://example.com/about</loc></url>
    </urlset>
    """.strip()
    print(extract_sitemap_urls(xml_text))
