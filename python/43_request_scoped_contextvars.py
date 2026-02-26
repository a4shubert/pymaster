"""
Technique: Request-Scoped Context with contextvars
Use When:
- Attaches correlation IDs to logs without passing params everywhere
- Works correctly across async tasks
- Supports tracing and debugging in distributed systems
"""

import logging
from contextlib import contextmanager
from contextvars import ContextVar


request_id_var: ContextVar[str] = ContextVar("request_id", default="-")
logger = logging.getLogger("svc")


@contextmanager
def request_context(request_id: str):
    token = request_id_var.set(request_id)
    try:
        yield
    finally:
        request_id_var.reset(token)


def do_work() -> None:
    rid = request_id_var.get()
    logger.info("event=work request_id=%s", rid)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="%(levelname)s %(message)s")

    do_work()
    with request_context("req-123"):
        do_work()
