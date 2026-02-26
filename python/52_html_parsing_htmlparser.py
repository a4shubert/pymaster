# Technique: HTML Parsing with html.parser (Standard Library)
# Use When:
# - Avoids brittle regex parsing for HTML
# - Good for simple scraping/extraction tasks

from html.parser import HTMLParser


class LinkExtractor(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.links: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        if tag != "a":
            return
        href = dict(attrs).get("href")
        if href:
            self.links.append(href)


if __name__ == "__main__":
    html = "<p>See <a href='https://example.com'>Example</a> and <a href='/local'>Local</a></p>"
    parser = LinkExtractor()
    parser.feed(html)
    print(parser.links)
