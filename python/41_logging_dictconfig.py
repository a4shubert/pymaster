# Technique: Centralized Logging with dictConfig
# Use When:
# - One place to configure log level, format, and handlers
# - Consistent, structured-ish logs across modules
# - Easy to tune behavior per environment (dev/stage/prod)

import logging
import logging.config


def configure_logging(level: str = "INFO") -> None:
    logging.config.dictConfig(
        {
            "version": 1,
            "disable_existing_loggers": False,
            "formatters": {
                "default": {
                    "format": "%(asctime)s %(levelname)s %(name)s %(message)s",
                }
            },
            "handlers": {
                "console": {
                    "class": "logging.StreamHandler",
                    "formatter": "default",
                }
            },
            "root": {
                "level": level,
                "handlers": ["console"],
            },
        }
    )


logger = logging.getLogger("app")


def run_job(job_id: str) -> None:
    logger.info("event=job_start job_id=%s", job_id)
    try:
        # business logic
        result = 2 + 2
        logger.info("event=job_success job_id=%s result=%d", job_id, result)
    except Exception:
        logger.exception("event=job_failed job_id=%s", job_id)
        raise


if __name__ == "__main__":
    configure_logging("INFO")
    run_job("job-001")
