"""
Technique: Simple Dependency Injection Container
Use When:
- Centralizes wiring of services
- Makes components testable (swap implementations)
- Helps scale applications as dependencies grow
"""

from collections.abc import Callable


class Container:
    def __init__(self) -> None:
        self._providers: dict[str, Callable[[], object]] = {}

    def register(self, name: str, provider: Callable[[], object]) -> None:
        self._providers[name] = provider

    def resolve(self, name: str) -> object:
        if name not in self._providers:
            raise KeyError(f"unknown service: {name}")
        return self._providers[name]()


class Clock:
    def now(self) -> str:
        return "2026-02-26T00:00:00Z"


class Greeter:
    def __init__(self, clock: Clock) -> None:
        self._clock = clock

    def greet(self, who: str) -> str:
        return f"hello {who} at {self._clock.now()}"


if __name__ == "__main__":
    c = Container()
    c.register("clock", lambda: Clock())
    c.register("greeter", lambda: Greeter(c.resolve("clock")))

    greeter = c.resolve("greeter")
    print(greeter.greet("dev"))  # type: ignore[attr-defined]
