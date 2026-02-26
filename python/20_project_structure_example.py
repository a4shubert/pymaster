# Technique: Professional Project Structure
# Use When:
# - Separates concerns (domain, infra, interfaces)
# - Improves onboarding and discoverability
# - Scales better as codebase size grows

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
