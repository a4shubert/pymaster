# Technique: pathlib + Explicit File I/O
# Use When:
# - `Path` objects are clearer and less error-prone than string paths
# - File operations become cross-platform and composable
# - Encoding/newline behavior is explicit

from pathlib import Path


def write_report(path: Path, lines: list[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    payload = "\n".join(lines) + "\n"
    path.write_text(payload, encoding="utf-8")


def read_report(path: Path) -> list[str]:
    text = path.read_text(encoding="utf-8")
    return [line for line in text.splitlines() if line.strip()]


if __name__ == "__main__":
    report_path = Path("/tmp/pymaster") / "daily_report.txt"
    write_report(report_path, ["status=ok", "items=3"])
    print(read_report(report_path))
