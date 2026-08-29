import logging
import json
import asyncio
import datetime
import httpx
from typing import List, Dict, Any, Optional

# New SDK Imports
from google import genai
from google.genai import types, errors

# Third-party Imports
from jsonschema import validate, ValidationError

# App Config
from config import app_config
from constants import *

logger = logging.getLogger(__name__)


class ContextCache:
    """A refreshable handle to a Vertex AI explicit context cache.

    Holds the source (corpus + system instruction + model) so the cache can be transparently
    recreated if it expires mid-run. The `name` attribute is mutable and shared by every
    concurrent request, so once one request refreshes an expired cache the others pick up the
    new name on their next attempt. Truthiness reflects whether a live cache name is held, so
    existing `if cached_content:` checks keep working.
    """

    def __init__(self, owner: "AiClient", model: str, content: str, system_instruction: str, name: str):
        self._owner = owner
        self._model = model
        self._content = content
        self._system_instruction = system_instruction
        self.name = name
        self._lock = asyncio.Lock()

    def __bool__(self) -> bool:
        return bool(self.name)

    async def refresh(self, expired_name: str) -> Optional[str]:
        """Recreates the cache after expiry and returns the new name (or None on failure).

        Idempotent under concurrency: if another request already refreshed the cache (so
        `self.name` no longer matches the `expired_name` the caller saw), the current name is
        returned without creating a duplicate.
        """
        async with self._lock:
            if self.name != expired_name:
                return self.name  # already refreshed by a concurrent request
            old_name = self.name
            try:
                new_name = await asyncio.to_thread(
                    self._owner._create_cache_resource,
                    self._content,
                    self._system_instruction,
                    self._model,
                )
            except Exception as e:
                logger.error(f"Failed to refresh expired context cache '{old_name}': {e}")
                self.name = None
                return None
            self.name = new_name
            logger.info(f"Refreshed expired context cache '{old_name}' -> '{new_name}'.")
            # Best-effort cleanup of the dead cache (it is expired, so this usually no-ops).
            await asyncio.to_thread(self._owner.delete_context_cache, old_name)
            return new_name


class AiClient:
    """A client for all Vertex AI model interactions, using the google-genai SDK (v1.52.0)."""

    def __init__(self, config):
        """
        Initializes the AiClient using the Unified Vertex AI Client.

        Args:
            config: The application configuration object.
        """
        self.config = config
        
        with open(PROMPT_CONFIG_PATH, 'r', encoding='utf-8') as f:
            prompt_config = json.load(f)
        
        base_system_message = prompt_config.get("system_message", "")
        if not base_system_message:
            logger.warning("System message is empty. AI calls will not have a predefined persona.")

        # Append the current date to the system prompt
        current_date = datetime.date.today().strftime("%Y-%m-%d")
        self.system_message = f"{base_system_message}\n\nImportant: Today's date is {current_date}."

        # Two auth modes for the same SDK surface: Vertex AI via ADC (the default), or the
        # Gemini Developer API via GEMINI_API_KEY (e.g. from the gitignored Gpp-ai-tool/.env)
        # for machines without gcloud/ADC. Same models, same caching API. The key itself is
        # never logged.
        if getattr(config, "gemini_api_key", None):
            logger.info("Initializing Google GenAI Client in Developer-API mode (GEMINI_API_KEY set).")
            self.client = genai.Client(api_key=config.gemini_api_key)
        else:
            logger.info(f"Initializing Google GenAI Client for project '{config.gcp_project_id}' in region '{config.region}'.")
            self.client = genai.Client(
                vertexai=True,
                project=config.gcp_project_id,
                location=config.region,
                http_options={'api_version': 'v1'}
            )
        
        logger.debug(f"System Message Context includes today's date: {current_date}")

        # Cumulative token bookkeeping across every successful call (docs/token-kostenplan.md,
        # Maßnahme 8): stages log the totals at the end so cost surprises show up in the log,
        # not on the invoice. Single event loop -> plain dict is safe.
        self.usage = {"calls": 0, "prompt": 0, "cached": 0, "output": 0}

    def log_usage_summary(self, label: str = "run") -> None:
        """Logs the cumulative token totals of this client instance."""
        u = self.usage
        logger.info(
            f"[{label}] Token-Bilanz: {u['calls']} Calls, prompt={u['prompt']:,} "
            f"(davon cached={u['cached']:,}), output={u['output']:,}."
        )

    def _create_cache_resource(self, content: str, system_instruction: str, model: str) -> str:
        """Creates one Vertex context cache and returns its resource name (raises on failure)."""
        ttl_seconds = self.config.context_cache_ttl_seconds
        cache = self.client.caches.create(
            model=model,
            config=types.CreateCachedContentConfig(
                contents=[content],
                system_instruction=system_instruction,
                ttl=f"{ttl_seconds}s",
            ),
        )
        logger.info(f"Created context cache '{cache.name}' for model '{model}' (ttl={ttl_seconds}s).")
        return cache.name

    def create_context_cache(self, content: str, system_instruction: str, model_override: Optional[str] = None) -> Optional["ContextCache"]:
        """Creates an explicit Vertex AI context cache for a large, reused grounding corpus.

        Implicit caching does not engage for this model/region, so a fixed corpus that every
        request shares (e.g. the stripped ED2023 Anforderungen list) is cached once here and
        reused via `cached_content=<handle>` on subsequent calls — paying for the prefix tokens
        a single time. Returns a `ContextCache` handle (which transparently recreates itself if
        the cache expires mid-run), or None if caching is unavailable (e.g. the corpus is below
        the model's minimum cacheable token count); callers should fall back to inline corpus.
        """
        model_to_use = model_override if model_override else GROUND_TRUTH_MODEL
        try:
            name = self._create_cache_resource(content, system_instruction, model_to_use)
            return ContextCache(self, model_to_use, content, system_instruction, name)
        except Exception as e:
            logger.warning(f"Could not create context cache (falling back to inline corpus): {e}")
            return None

    def delete_context_cache(self, cache) -> None:
        """Deletes a previously created context cache. Best-effort; logs and continues on error.

        Accepts either a raw resource-name string or a `ContextCache` handle.
        """
        name = cache.name if isinstance(cache, ContextCache) else cache
        if not name:
            return
        try:
            self.client.caches.delete(name=name)
            logger.info(f"Deleted context cache '{name}'.")
        except Exception as e:
            logger.warning(f"Failed to delete context cache '{name}': {e}")

    def _prepare_generation_config(self, json_schema: Dict[str, Any], use_thinking: bool = False, cached_content: Optional[str] = None) -> types.GenerateContentConfig:
        """Prepares and converts the JSON schema for the GenerateContentConfig.

        When `cached_content` (an explicit context-cache resource name) is provided, the
        system instruction lives inside that cache, so we attach the cache and must NOT also
        set `system_instruction` on the request (the API rejects setting both).
        """
        try:
            # Create a copy to avoid modifying the original
            schema_for_api = json.loads(json.dumps(json_schema))
            # The new SDK is robust, but removing $schema is still good practice
            schema_for_api.pop("$schema", None)
        except Exception as e:
            logger.error(f"Failed to process JSON schema before API call: {e}")
            raise ValueError("Invalid JSON schema provided.") from e

        try:
            # Map constants to the new types.GenerateContentConfig structure
            config_kwargs = {
                "response_mime_type": "application/json",
                "response_schema": schema_for_api,
                "max_output_tokens": API_MAX_OUTPUT_TOKEN,
                "temperature": API_TEMPERATURE,
            }
            if cached_content:
                # System instruction + grounding corpus are baked into the cache.
                config_kwargs["cached_content"] = cached_content
            else:
                config_kwargs["system_instruction"] = self.system_message
            if use_thinking:
                config_kwargs["thinking_config"] = types.ThinkingConfig(
                    thinking_level=types.ThinkingLevel.HIGH
                )
            return types.GenerateContentConfig(**config_kwargs)
        except Exception as e:
            logger.error(f"Failed to prepare generation config: {e}", exc_info=True)
            raise ValueError(f"Invalid or incompatible GenerateContentConfig: {e}") from e

    def _process_response(self, response) -> Dict[str, Any]:
        """Processes the model response, handling finish reasons, thought parts, and JSON parsing."""
        if not response.candidates:
            raise ValueError("The model response contained no candidates.")

        candidate = response.candidates[0]

        # --- Robust Finish Reason Check ---
        # In the new SDK, finish_reason is often an Enum string (e.g., "STOP"). 
        # We check strictly for success indicators.
        # "STOP" is standard success. "MAX_TOKENS" (often mapped to 2) might be acceptable depending on logic, 
        # but usually implies truncation.
        valid_reasons = ["STOP", 1] # 1 is the integer value for STOP in some contexts
        
        # Helper to get string representation safely
        f_reason = candidate.finish_reason
        
        is_valid = False
        if isinstance(f_reason, str) and f_reason in valid_reasons:
            is_valid = True
        elif isinstance(f_reason, int) and f_reason in valid_reasons:
            is_valid = True
            
        if not is_valid:
             raise ValueError(f"Model finished with non-OK reason: {f_reason}")
        # --- End Robust Finish Reason Check ---

        # --- START: Handle Thinking/Reasoning Parts ---
        # We iterate parts to safely extract only valid text, ignoring 'thought' blocks
        # which can break JSON parsing.
        full_text_parts = []
        
        if candidate.content and candidate.content.parts:
            for part in candidate.content.parts:
                try:
                    # In v1.52.0, part.text exists if it is a text part. 
                    # If it is a thought part, accessing text might be None or imply checking part.thought
                    if part.text:
                        full_text_parts.append(part.text)
                except Exception:
                    # If any attribute access fails, assume it's a non-text part
                    continue
        
        raw_response_text = "".join(full_text_parts)
        
        if not raw_response_text:
            raise ValueError("Model response contained candidates but no extractable text (only thoughts/empty).")
        # --- END: Handle Thinking/Reasoning Parts ---

        # Clean Markdown code blocks if present
        if raw_response_text.startswith("```json"):
            raw_response_text = raw_response_text.replace("```json", "").replace("```", "")
        elif raw_response_text.startswith("```"):
            raw_response_text = raw_response_text.replace("```", "")

        try:
            response_json = json.loads(raw_response_text)
        except json.JSONDecodeError as e:
            logger.error(f"Failed JSON Text: {raw_response_text}") 
            raise ValueError(f"Failed to parse model response as JSON: {str(e).split(':')[0]}")
        
        return response_json

    @staticmethod
    def _is_expired_cache_error(e) -> bool:
        """True for the Vertex 'Cache content ... is expired' (or missing-cache) ClientError."""
        msg = str(e).lower()
        return "cache" in msg and ("expired" in msg or "not found" in msg)

    def _log_token_usage(self, response, request_context_log: str, cache_active: bool) -> None:
        """Logs token counts, highlighting the cached prefix tokens we avoid re-paying for."""
        um = getattr(response, "usage_metadata", None)
        if not um:
            return
        cached = getattr(um, "cached_content_token_count", None) or 0
        prompt = getattr(um, "prompt_token_count", None) or 0
        output = getattr(um, "candidates_token_count", None) or 0
        self.usage["calls"] += 1
        self.usage["prompt"] += prompt
        self.usage["cached"] += cached
        self.usage["output"] += output
        if cache_active and cached:
            logger.info(
                f"[{request_context_log}] tokens: prompt={prompt} cached(saved)={cached} output={output}"
            )
        else:
            logger.debug(
                f"[{request_context_log}] tokens: prompt={prompt} cached={cached} output={output}"
            )

    async def generate_validated_json_response(
        self, 
        prompt: str, 
        json_schema: Dict[str, Any], 
        gcs_uris: List[str] = None,
        request_context_log: str = "Generic AI Request",
        model_override: Optional[str] = None,
        max_retries: int = None,
        cached_content: Optional[str] = None
    ) -> Dict[str, Any]:

        """
        Generates a JSON response from the AI model using google-genai SDK.

        If `cached_content` (a `ContextCache` handle from `create_context_cache`, or a raw
        resource-name string) is given, it is attached to the request so the model reuses the
        cached system instruction + grounding corpus instead of re-sending it. If the cache
        expires mid-run, the handle is refreshed in place and the request is retried.
        """

        retries = max_retries if max_retries is not None else API_MAX_RETRIES
        model_to_use = model_override if model_override else GROUND_TRUTH_MODEL

        # Resolve the cache handle (if any). cache_name is the current resource name and may be
        # swapped out by a refresh on expiry; gen_config is rebuilt whenever it changes.
        cache = cached_content if isinstance(cached_content, ContextCache) else None
        cache_name = cache.name if cache else cached_content

        try:
            # Prepare configuration (includes system_instruction unless a cache supplies it)
            use_thinking = True if model_to_use == GROUND_TRUTH_MODEL_PRO else False
            gen_config = self._prepare_generation_config(json_schema, use_thinking=use_thinking, cached_content=cache_name)
        except ValueError as e:
            logger.error(f"[{request_context_log}] Configuration failed. Cannot proceed with AI request: {e}")
            raise

        # Construct Content Parts
        # The new SDK allows mixing strings and types.Part objects
        contents = []
        
        # Add GCS Files if present
        if gcs_uris:
            for uri in gcs_uris:
                # Syntax: types.Part.from_uri(file_uri=..., mime_type=...)
                contents.append(types.Part.from_uri(file_uri=uri, mime_type="application/pdf"))
            if self.config.is_test_mode:
                logger.debug(f"Attaching {len(gcs_uris)} GCS files to the prompt.")

        # Add the text prompt
        contents.append(prompt)

        # Manual counter (not `for ... in range`) so a cache refresh can retry without
        # consuming one of the genuine error retries. Refreshes are themselves bounded so a
        # pathological "always expired" cache can never loop forever.
        attempt = 0
        cache_refreshes = 0
        max_cache_refreshes = 3
        while attempt < retries:
            try:
                logger.debug(f"[{request_context_log}] Attempt {attempt + 1}/{retries}: Calling Gemini model '{model_to_use}'...")
                
                # max logging
                # logger.debug(f"raw prompt: {contents}")

                # Asynchronous Generation call via .aio accessor
                response = await self.client.aio.models.generate_content(
                    model=model_to_use,
                    contents=contents,
                    config=gen_config,
                )
                # max logging
                # logger.debug(f"raw response JSON: {response}")
                response_json = self._process_response(response)

                validate(instance=response_json, schema=json_schema)

                self._log_token_usage(response, request_context_log, cache_active=bool(cache_name))
                logger.info(f"[{request_context_log}] Successfully generated and validated JSON on attempt {attempt + 1}.")
                return response_json

            except (errors.ClientError, ValueError, TypeError, ValidationError, httpx.ConnectError, httpx.TimeoutException) as e:
                # errors.ClientError covers most API-level issues in the new SDK
                # httpx.ConnectError and httpx.TimeoutException cover transient network/timeout issues

                # Expired/missing context cache: recreate it (once, shared across concurrent
                # requests) and retry immediately without counting it as a failed attempt.
                if cache and cache_refreshes < max_cache_refreshes and self._is_expired_cache_error(e):
                    cache_refreshes += 1
                    new_name = await cache.refresh(cache_name)
                    if new_name:
                        if new_name != cache_name:
                            cache_name = new_name
                            gen_config = self._prepare_generation_config(
                                json_schema, use_thinking=use_thinking, cached_content=cache_name
                            )
                        logger.warning(f"[{request_context_log}] Context cache expired; refreshed, retrying.")
                        continue  # does not increment `attempt`
                    # Refresh failed: drop the cache and fall through to normal retry/backoff.
                    logger.error(f"[{request_context_log}] Cache refresh failed; cannot ground this request.")

                wait_time = 2 ** attempt
                if attempt == retries - 1:
                    logger.critical(f"[{request_context_log}] AI generation failed after all {retries} retries.", exc_info=True)
                    raise

                error_msg = str(e)
                log_message = f"[{request_context_log}] Attempt {attempt + 1} failed. Retrying in {wait_time}s..."

                if isinstance(e, errors.ClientError):
                    logger.warning(f"[{request_context_log}] API Error: {e}. Retrying in {wait_time}s...")
                elif isinstance(e, ValidationError):
                    clean_msg = e.message.split('\n')[0] if '\n' in e.message else e.message
                    logger.warning(f"[{request_context_log}] Schema validation failed: '{clean_msg}'. Retrying in {wait_time}s...")
                else:
                    logger.warning(f"[{request_context_log}] Processing error: {error_msg}. Retrying in {wait_time}s...")

                await asyncio.sleep(wait_time)
                attempt += 1

            except Exception as e:
                logger.error(f"[{request_context_log}] Unexpected, non-retryable error: {type(e).__name__}: {e}", exc_info=True)
                raise