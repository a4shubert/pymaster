"""
Technique: Professional Project Structure

Why this is professional:
- Separates concerns (domain, infra, interfaces).
- Improves onboarding and discoverability.
- Scales better as codebase size grows.

Pattern:
1) Keep application entrypoints thin.
2) Keep business logic independent from frameworks.
3) Define clear package boundaries.
"""

PROJECT_LAYOUT = {
    "src/pymaster/domain/": ["models.py", "services.py"],
    "src/pymaster/infra/": ["db.py", "http_client.py"],
    "src/pymaster/interfaces/": ["cli.py", "api.py"],
    "tests/": ["test_services.py", "test_api.py"],
}


def print_layout() -> None:
    for folder, files in PROJECT_LAYOUT.items():
        print(folder)
        for file in files:
            print(f"  - {file}")


if __name__ == "__main__":
    print_layout()
