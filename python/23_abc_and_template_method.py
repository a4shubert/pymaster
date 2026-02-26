"""
Technique: ABC + Template Method
Use When:
- One stable workflow is implemented once
- Subclasses customize only specific steps
- Keeps rules consistent and reduces duplication
"""

from abc import ABC, abstractmethod


class ReportGenerator(ABC):
    def generate(self) -> str:
        header = self.header()
        body = self.body()
        footer = self.footer()
        return "\n".join([header, body, footer])

    @abstractmethod
    def header(self) -> str:
        raise NotImplementedError

    @abstractmethod
    def body(self) -> str:
        raise NotImplementedError

    def footer(self) -> str:
        return "-- end --"


class SalesReport(ReportGenerator):
    def header(self) -> str:
        return "Sales Report"

    def body(self) -> str:
        return "total=1234"


if __name__ == "__main__":
    print(SalesReport().generate())
