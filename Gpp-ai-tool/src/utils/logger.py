"""
One-call logging setup (the LOG_LEVEL lever).

Nothing is hand-instrumented: lowering the root level makes every backend client emit its own
wire logs (google-genai via httpx/httpcore, google.auth, urllib3). Logs go to stderr so stdout
stays clean for machine output. `LOG_LEVEL` is read at process start — restart to apply.
"""

import logging
import os

LOG_FORMAT = "%(asctime)s %(levelname)s %(name)s: %(message)s"


def configure_logging(level: str | None = None) -> None:
    """Configures the root logger once. `level` wins; otherwise `LOG_LEVEL`; else INFO.

    `force=True` re-installs the handler even if something configured logging first, so the
    chosen level always takes effect.
    """
    resolved = (level or os.getenv("LOG_LEVEL") or "INFO").upper()
    logging.basicConfig(level=resolved, format=LOG_FORMAT, force=True)
    if resolved != "DEBUG":
        # Below DEBUG the transport libraries only add noise.
        for name in ("google.auth", "urllib3", "httpx", "httpcore"):
            logging.getLogger(name).setLevel(logging.WARNING)
