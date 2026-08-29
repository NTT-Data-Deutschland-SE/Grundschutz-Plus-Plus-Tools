"""
Manages the import of environment variables for the application.

This module retrieves configuration settings from the environment, providing
a single source of truth for all configurable parameters. It includes type
casting and default values to ensure robustness.
"""

import os
from typing import Optional


def _load_dotenv() -> None:
    """Loads .env files (KEY=VALUE lines) into os.environ without overriding.

    Looks in Gpp-ai-tool/.env first, then the repository root .env (both gitignored).
    Deliberately minimal (stdlib only, no python-dotenv dependency): the files carry
    local credentials such as GEMINI_API_KEY. Existing environment variables always
    win, so CI/Cloud-Run configuration stays authoritative.
    """
    src_dir = os.path.dirname(os.path.abspath(__file__))
    for dotenv_path in (
        os.path.join(src_dir, "..", ".env"),
        os.path.join(src_dir, "..", "..", ".env"),
    ):
        if not os.path.exists(dotenv_path):
            continue
        # Tolerate Windows editor/redirect encodings: PowerShell's `>` writes UTF-16 LE
        # with BOM, Notepad may write UTF-8 with BOM. Keys/values are ASCII either way.
        with open(dotenv_path, "rb") as f:
            raw = f.read()
        if raw.startswith(b"\xff\xfe") or raw.startswith(b"\xfe\xff"):
            text = raw.decode("utf-16")
        else:
            text = raw.decode("utf-8-sig")
        for line in text.splitlines():
            line = line.strip()
            if not line or line.startswith("#") or "=" not in line:
                continue
            key, value = line.split("=", 1)
            os.environ.setdefault(key.strip(), value.strip().strip('"').strip("'"))


_load_dotenv()


class AppConfig:
    """A dataclass-like container for application configuration."""

    def __init__(self):
        # Vertex AI / Gemini access (the only external service the pipeline still uses).
        self.gcp_project_id: Optional[str] = os.environ.get("GCP_PROJECT_ID")
        # Gemini Developer API key (AI Studio). When set, AiClient talks to the
        # Developer API instead of Vertex AI — no GCP project/ADC needed.
        self.gemini_api_key: Optional[str] = os.environ.get("GEMINI_API_KEY")
        self.region: Optional[str] = os.environ.get("REGION", "global")
        # Optional Vertex AI endpoint/model override. The model id otherwise comes from
        # constants.GROUND_TRUTH_MODEL, so this is not required to start the tool.
        self.ai_endpoint_id: Optional[str] = os.environ.get("AI_ENDPOINT_ID")
        self.is_test_mode: bool = os.environ.get("TEST", "false").lower() == "true"
        self.overwrite_temp_files: bool = (
            os.environ.get("OVERWRITE_TEMP_FILES", "false").lower() == "true"
        )
        self.max_concurrent_ai_requests: int = int(
            os.environ.get("MAX_CONCURRENT_AI_REQUESTS", "5")
        )
        # TTL for explicit Vertex context caches. The default (60 min) can elapse before a
        # full G++ run finishes, expiring the cache mid-stage; 4h comfortably outlives a run.
        self.context_cache_ttl_seconds: int = int(
            os.environ.get("CONTEXT_CACHE_TTL_SECONDS", "14400")
        )

        if not self.is_test_mode:
            self._validate_production_config()

    def _validate_production_config(self):
        """Ensures the required variables are set in a non-test environment.

        AI access needs either `GCP_PROJECT_ID` (Vertex AI via ADC) or `GEMINI_API_KEY`
        (Gemini Developer API, e.g. from Gpp-ai-tool/.env). The pipeline fetches inputs
        from GitHub and writes outputs to local directories, so the former GCS variables
        (BUCKET_NAME / SOURCE_PREFIX / OUTPUT_PREFIX) are no longer read and are not
        validated. AI_ENDPOINT_ID is optional (see __init__).
        """
        if self.gcp_project_id is None and self.gemini_api_key is None:
            raise ValueError(
                "Missing AI credentials: set GCP_PROJECT_ID (Vertex AI) or "
                "GEMINI_API_KEY (Developer API, e.g. in Gpp-ai-tool/.env)."
            )


# Create a single, importable instance of the AppConfig.
app_config = AppConfig()
