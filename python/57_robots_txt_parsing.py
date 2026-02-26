# Technique: robots.txt Parsing with urllib.robotparser
# Use When:
# - Basic politeness and compliance for scraping
# - Quickly checks whether a URL is allowed for a user-agent

from urllib.robotparser import RobotFileParser


def can_fetch(robots_txt: str, user_agent: str, url: str) -> bool:
    rp = RobotFileParser()
    rp.parse(robots_txt.splitlines())
    return rp.can_fetch(user_agent, url)


if __name__ == "__main__":
    robots = """
    User-agent: *
    Disallow: /private
    """.strip()
    print(can_fetch(robots, "mybot", "https://example.com/"))
    print(can_fetch(robots, "mybot", "https://example.com/private"))
