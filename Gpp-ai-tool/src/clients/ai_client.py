"""
The one place the pipeline talks to Gemini (google-genai >= 2.30.1, Gemini 4 Argon).

One model for everything; cost and quality are dialed per call through `thinking` (low |
medium | high) and `max_output_tokens`, never through a second model. Maker and Checker are the
same model in two roles (Checker at `high`).

Argon facts the code relies on (verified 14 Oct 2026):
  - temperature/top_p/top_k are ignored, candidate_count and the penalties return 400 — no
    sampling parameters are sent; determinism lives in prompt + schema;
  - explicit caching (caches.create / cached_content) returns 400 — there is none here.
    Caching is implicit: a repeated prompt PREFIX (system instruction, corpus, rules) above
    6,144 tokens is discounted by 95 %, so stages put the stable part first and the varying
    item last;
  - max_output_tokens counts thinking tokens; above 65,536 the SDK continues in 64K hops
    (`automatic_continuation`), one hop may run 20 minutes — hence the client timeout.

Retries: transient failures (429, 5xx, timeouts, dropped connections) and responses that fail
the JSON schema are retried with exponential backoff, at most `API_MAX_RETRIES` (<= 5) times
per call. Permanent errors (400/401/403/404) raise at once. All google imports are lazy so
importing this module needs no credentials.
"""

import asyncio
import datetime
import json
import logging
import random
from typing import Any, Dict, Optional

from jsonschema import ValidationError, validate

from constants import PROMPT_CONFIG_PATH

logger = logging.getLogger(__name__)

# One long-decode hop may run 20 minutes before the server closes it (milliseconds).
HTTP_TIMEOUT_MS = 1_200_000
_BACKOFF_MIN_S = 2.0
_BACKOFF_MAX_S = 30.0


def is_recoverable(exc: BaseException) -> bool:
    """True for transient failures only: 429, 5xx, timeouts and connection drops.

    Permanent errors (400 invalid request, 401/403 auth, 404) are not retried — retrying
    wastes quota and hides the real error.
    """
    code = getattr(exc, "code", None) or getattr(exc, "status_code", None)
    if isinstance(code, int):
        return code == 429 or 500 <= code < 600
    msg = str(exc).lower()
    return any(s in msg for s in (
        "429", "resource_exhausted", "rate limit", "quota",
        "503", "unavailable", "500", "internal", "502", "504",
        "deadline", "timeout", "timed out", "connection", "reset",
    ))


def error_detail(exc: BaseException, action: str) -> str:
    """One line with action, code/status and the upstream message — what an operator needs."""
    code = getattr(exc, "code", None) or getattr(exc, "status_code", None)
    status = getattr(exc, "status", None)
    message = getattr(exc, "message", None) or str(exc)
    tag = " ".join(str(p) for p in (code, status) if p)
    prefix = f"{action} failed" + (f" ({tag})" if tag else "")
    return f"{prefix}: {message}" if message else prefix


class OutputTruncatedError(RuntimeError):
    """The model hit MAX_OUTPUT_TOKENS; the output is unusable and a retry cannot fix it."""


class AiClient:
    """Structured-output calls against one Gemini model with per-call thinking level."""

    def __init__(self, config):
        self.config = config
        config.require_ai_credentials()

        with open(PROMPT_CONFIG_PATH, "r", encoding="utf-8") as f:
            prompt_config = json.load(f)
        base_system_message = prompt_config.get("system_message", "")
        if not base_system_message:
            logger.warning("System message is empty. AI calls will not have a predefined persona.")
        current_date = datetime.date.today().strftime("%Y-%m-%d")
        self.system_message = f"{base_system_message}\n\nImportant: Today's date is {current_date}."

        self.model = config.gemini_model
        self._client = None
        # Cumulative token bookkeeping across every successful call: stages log the totals at
        # the end so cost surprises show up in the log, not on the invoice.
        self.usage = {"calls": 0, "prompt": 0, "cached": 0, "thoughts": 0, "output": 0}

    # ── client construction (lazy, credentialed) ───────────────────────────────────────────
    def _genai(self):
        if self._client is None:
            from google import genai
            from google.genai import types

            http = types.HttpOptions(timeout=HTTP_TIMEOUT_MS)
            if self.config.gemini_api_key:
                # Gemini Developer API (AI Studio): same SDK surface, no GCP project needed.
                # The key itself is never logged.
                logger.info("Initializing google-genai in Developer-API mode (GEMINI_API_KEY set).")
                self._client = genai.Client(api_key=self.config.gemini_api_key, http_options=http)
            else:
                logger.info(
                    f"Initializing google-genai for project '{self.config.gcp_project_id}' "
                    f"in location '{self.config.region}'."
                )
                kwargs = {"project": self.config.gcp_project_id, "location": self.config.region,
                          "http_options": http}
                # enterprise=True is the Agent Platform flag since google-genai 1.74.0; vertexai=True
                # its legacy alias. Passing both raises — pick one.
                try:
                    self._client = genai.Client(enterprise=True, **kwargs)
                except TypeError:
                    self._client = genai.Client(vertexai=True, **kwargs)
        return self._client

    def log_usage_summary(self, label: str = "run") -> None:
        """Logs the cumulative token totals of this client instance."""
        u = self.usage
        logger.info(
            f"[{label}] Token-Bilanz: {u['calls']} Calls, prompt={u['prompt']:,} "
            f"(davon cached={u['cached']:,}), thoughts={u['thoughts']:,}, output={u['output']:,}."
        )

    # ── config ──────────────────────────────────────────────────────────────────────────────
    def _config(self, json_schema: Dict[str, Any], *, thinking: str, max_output_tokens: int,
                system_instruction: str):
        """GenerateContentConfig without sampling or caching fields (both are void on Argon)."""
        from google.genai import types

        schema_for_api = json.loads(json.dumps(json_schema))
        schema_for_api.pop("$schema", None)
        return types.GenerateContentConfig(
            system_instruction=system_instruction,
            response_mime_type="application/json",
            response_json_schema=schema_for_api,
            thinking_config=types.ThinkingConfig(thinking_level=thinking),
            max_output_tokens=max_output_tokens,
            # Default True on >= 2.30.1; stated explicitly so an older pinned SDK fails loudly here.
            automatic_continuation=True,
        )

    # ── response handling ──────────────────────────────────────────────────────────────────
    def _log_usage(self, response, request_context_log: str) -> str:
        """One DEBUG line per call with the numbers that explain cost and truncation.

        Returns the finish reason name. MAX_TOKENS means the output budget was hit (raise
        MAX_OUTPUT_TOKENS); a surviving CONTINUATION means the SDK stopped continuing — both
        are truncation the parser would otherwise report as bad JSON.
        """
        um = getattr(response, "usage_metadata", None)
        cands = getattr(response, "candidates", None) or []
        fr = getattr(cands[0], "finish_reason", None) if cands else None
        fr_name = getattr(fr, "name", None) or (str(fr) if fr else "?")
        prompt = getattr(um, "prompt_token_count", None) or 0
        cached = getattr(um, "cached_content_token_count", None) or 0
        thoughts = getattr(um, "thoughts_token_count", None) or 0
        output = getattr(um, "candidates_token_count", None) or 0
        self.usage["calls"] += 1
        self.usage["prompt"] += prompt
        self.usage["cached"] += cached
        self.usage["thoughts"] += thoughts
        self.usage["output"] += output
        logger.debug(
            f"[{request_context_log}] {self.model}: finish={fr_name} prompt={prompt} "
            f"cached={cached} thoughts={thoughts} out={output}"
        )
        if fr_name not in ("STOP", "?"):
            logger.warning(
                f"[{request_context_log}] {self.model} ended with finish_reason={fr_name} — "
                "output may be truncated (MAX_TOKENS: raise MAX_OUTPUT_TOKENS)."
            )
        return fr_name

    @staticmethod
    def _response_text(response) -> str:
        """Concatenates the text parts of the first candidate, skipping thought parts."""
        if not getattr(response, "candidates", None):
            raise ValueError("The model response contained no candidates.")
        candidate = response.candidates[0]
        parts = []
        content = getattr(candidate, "content", None)
        for part in (getattr(content, "parts", None) or []):
            if getattr(part, "thought", False):
                continue
            text = getattr(part, "text", None)
            if text:
                parts.append(text)
        raw = "".join(parts).strip()
        if not raw:
            raise ValueError("Model response contained candidates but no extractable text.")
        if raw.startswith("```"):
            raw = raw.strip("`")
            if raw.startswith("json"):
                raw = raw[4:]
        return raw

    # ── the call ────────────────────────────────────────────────────────────────────────────
    async def generate_validated_json_response(
        self,
        prompt: str,
        json_schema: Dict[str, Any],
        request_context_log: str = "Generic AI Request",
        *,
        thinking: Optional[str] = None,
        system_instruction: Optional[str] = None,
        max_output_tokens: Optional[int] = None,
    ) -> Any:
        """Generates JSON that validates against `json_schema`.

        `thinking` defaults to MAKER_THINKING_LEVEL; checkers pass CHECKER_THINKING_LEVEL.
        `system_instruction` defaults to the shared persona from prompt_config; corpus stages
        pass their own and keep the corpus as the stable prefix of `prompt`.
        """
        thinking = thinking or self.config.maker_thinking_level
        max_output_tokens = max_output_tokens or self.config.max_output_tokens
        gen_config = self._config(
            json_schema, thinking=thinking, max_output_tokens=max_output_tokens,
            system_instruction=system_instruction or self.system_message,
        )
        retries = self.config.api_max_retries
        client = self._genai()

        attempt = 0
        while True:
            try:
                logger.debug(
                    f"[{request_context_log}] Attempt {attempt + 1}/{retries + 1}: "
                    f"{self.model} thinking={thinking}"
                )
                response = await client.aio.models.generate_content(
                    model=self.model, contents=[prompt], config=gen_config,
                )
                fr_name = self._log_usage(response, request_context_log)
                raw = self._response_text(response)
                if fr_name == "MAX_TOKENS":
                    # Deterministic: the same prompt overruns the same budget again. Retrying
                    # would re-bill the full prompt plus the whole output budget per attempt.
                    logger.error(f"[{request_context_log}] Output truncated at MAX_OUTPUT_TOKENS="
                                 f"{max_output_tokens}; not retried. Raise MAX_OUTPUT_TOKENS or shrink the batch.")
                    raise OutputTruncatedError(
                        f"finish_reason=MAX_TOKENS at max_output_tokens={max_output_tokens}"
                    )
                try:
                    response_json = json.loads(raw)
                except json.JSONDecodeError as e:
                    logger.error(f"[{request_context_log}] Failed JSON text (first 500 chars): {raw[:500]}")
                    raise ValueError(f"Failed to parse model response as JSON: {str(e).split(':')[0]}") from e
                validate(instance=response_json, schema=json_schema)
                logger.info(f"[{request_context_log}] JSON generated and validated on attempt {attempt + 1}.")
                return response_json
            except OutputTruncatedError:
                raise
            except (ValueError, ValidationError) as e:
                # Bad output (no text, broken JSON, schema violation): ask again, within the cap.
                reason = e.message.split("\n")[0] if isinstance(e, ValidationError) else str(e)
                if attempt >= retries:
                    logger.error(f"[{request_context_log}] Giving up after {attempt + 1} attempts: {reason}")
                    raise
                wait = min(_BACKOFF_MAX_S, _BACKOFF_MIN_S * (2 ** attempt)) * (1 + random.random() * 0.5)
                logger.warning(f"[{request_context_log}] Output unusable ({reason}). Retrying in {wait:.0f}s...")
            except Exception as e:  # noqa: BLE001 — classified below, never swallowed
                if not is_recoverable(e) or attempt >= retries:
                    logger.error(f"[{request_context_log}] {error_detail(e, 'AI call')}", exc_info=True)
                    raise
                wait = min(_BACKOFF_MAX_S, _BACKOFF_MIN_S * (2 ** attempt)) * (1 + random.random() * 0.5)
                logger.warning(f"[{request_context_log}] {error_detail(e, 'AI call')}. Retrying in {wait:.0f}s...")
            attempt += 1
            await asyncio.sleep(wait)
