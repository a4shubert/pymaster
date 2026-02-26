"""
Technique: Structural Pattern Matching (match/case)

Why this is professional:
- Clear handling of variant-shaped inputs.
- Replaces long if/elif chains.
- Works well for parsing commands and events.

Pattern:
1) Define a small set of supported shapes.
2) Use match/case to route behavior.
3) Keep a default case for unknown inputs.
"""


def handle_event(event: dict[str, object]) -> str:
    match event:
        case {"type": "user_created", "id": int(user_id)}:
            return f"create user {user_id}"
        case {"type": "user_deleted", "id": int(user_id)}:
            return f"delete user {user_id}"
        case {"type": str(t)}:
            return f"unknown event type: {t}"
        case _:
            return "invalid event"


if __name__ == "__main__":
    print(handle_event({"type": "user_created", "id": 1}))
    print(handle_event({"type": "x", "id": 2}))
    print(handle_event({"no": "shape"}))
