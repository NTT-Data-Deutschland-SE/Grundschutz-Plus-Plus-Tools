"""
Typed application settings (pydantic-settings).

One `Settings` singleton (`app_config`) reads the environment and the two gitignored `.env`
files (repository root, then `Gpp-ai-tool/`; later files override earlier ones, real
environment variables always win). Every field appears in `.env.example` and in the README
configuration table — keep the three in sync.

Importing this module needs no credentials: whether `GCP_PROJECT_ID` or `GEMINI_API_KEY` is
set is only checked when an `AiClient` is constructed (`require_ai_credentials`).
"""

import os
from pathlib import Path

from pydantic import Field, field_validator
from pydantic_settings import BaseSettings, SettingsConfigDict

_TOOL_ROOT = Path(__file__).resolve().parent.parent
_REPO_ROOT = _TOOL_ROOT.parent

# App-level names → Argon thinking levels. Argon has no "minimal" and no "off" (both HTTP 400);
# legacy values are mapped to "low" so an old .env never 400s.
_THINKING_LEVELS = {"low": "low", "medium": "medium", "high": "high",
                    "minimal": "low", "off": "low", "max": "high"}


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=(str(_REPO_ROOT / ".env"), str(_TOOL_ROOT / ".env")),
        env_file_encoding="utf-8-sig",
        extra="ignore",
    )

    # --- Gemini access (one of the two) ---
    gcp_project_id: str | None = Field(default=None, alias="GCP_PROJECT_ID")
    gemini_api_key: str | None = Field(default=None, alias="GEMINI_API_KEY")
    region: str = Field(default="global", alias="REGION")

    # --- Model: one id, quality and cost via thinking level ---
    gemini_model: str = Field(default="gemini-4-argon", alias="GEMINI_MODEL")
    maker_thinking_level: str = Field(default="medium", alias="MAKER_THINKING_LEVEL")
    checker_thinking_level: str = Field(default="high", alias="CHECKER_THINKING_LEVEL")
    max_output_tokens: int = Field(default=65_536, alias="MAX_OUTPUT_TOKENS")
    max_concurrent_ai_requests: int = Field(default=5, alias="MAX_CONCURRENT_AI_REQUESTS")
    api_max_retries: int = Field(default=5, alias="API_MAX_RETRIES")

    # --- Run ---
    is_test_mode: bool = Field(default=False, alias="TEST")
    overwrite_temp_files: bool = Field(default=False, alias="OVERWRITE_TEMP_FILES")
    log_level: str = Field(default="INFO", alias="LOG_LEVEL")

    @field_validator("maker_thinking_level", "checker_thinking_level", mode="before")
    @classmethod
    def _thinking(cls, value: str) -> str:
        key = str(value or "").strip().lower()
        if key not in _THINKING_LEVELS:
            raise ValueError(f"thinking level {value!r} unknown — use low, medium or high")
        return _THINKING_LEVELS[key]

    @field_validator("max_output_tokens")
    @classmethod
    def _max_output(cls, value: int) -> int:
        # The cap includes thinking tokens: below 32,768 the model thinks the budget away and
        # returns truncated JSON without an error.
        if not 32_768 <= value <= 1_048_576:
            raise ValueError("MAX_OUTPUT_TOKENS must be between 32768 and 1048576")
        return value

    @field_validator("api_max_retries")
    @classmethod
    def _retries(cls, value: int) -> int:
        # Core rule: at most 5 retries per call, the first attempt not counted.
        if not 0 <= value <= 5:
            raise ValueError("API_MAX_RETRIES must be between 0 and 5")
        return value

    def require_ai_credentials(self) -> None:
        """Fails closed when neither Vertex (ADC + project) nor a Developer-API key is configured."""
        if self.is_test_mode or self.gcp_project_id or self.gemini_api_key:
            return
        raise ValueError(
            "Missing AI credentials: set GCP_PROJECT_ID (Agent Platform via ADC) or "
            "GEMINI_API_KEY (Developer API), e.g. in Gpp-ai-tool/.env."
        )


# `--fresh` on the CLI is the explicit way to start over; OVERWRITE_TEMP_FILES stays as the
# env alias so existing scripts keep working.
if os.environ.get("GPP_FRESH", "").lower() == "true":
    os.environ["OVERWRITE_TEMP_FILES"] = "true"

app_config = Settings()
