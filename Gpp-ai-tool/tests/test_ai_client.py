"""Offline tests of the Gemini client wrapper: retry policy, JSON parsing, usage logging."""

import json
from types import SimpleNamespace

import pytest

from clients import ai_client as mod
from config import Settings


def _settings(**over):
    base = {"TEST": "true", "API_MAX_RETRIES": "2", "MAKER_THINKING_LEVEL": "medium"}
    base.update(over)
    return Settings(_env_file=None, **base)


def _response(text, finish="STOP", thought=False):
    part = SimpleNamespace(text=text, thought=thought)
    cand = SimpleNamespace(finish_reason=SimpleNamespace(name=finish), content=SimpleNamespace(parts=[part]))
    usage = SimpleNamespace(prompt_token_count=10, cached_content_token_count=4, thoughts_token_count=3,
                            candidates_token_count=2)
    return SimpleNamespace(candidates=[cand], usage_metadata=usage)


class FakeGenai:
    """Replays a scripted list of responses or exceptions; records the configs it was called with."""

    def __init__(self, script):
        self.script = list(script)
        self.calls = []
        outer = self

        async def generate_content(*, model, contents, config):
            outer.calls.append({"model": model, "contents": contents, "config": config})
            item = outer.script.pop(0)
            if isinstance(item, BaseException):
                raise item
            return item

        self.aio = SimpleNamespace(models=SimpleNamespace(generate_content=generate_content))


def _client(monkeypatch, script, **over):
    cfg = _settings(**over)
    client = mod.AiClient(cfg)
    fake = FakeGenai(script)
    monkeypatch.setattr(client, "_genai", lambda: fake)

    async def no_sleep(_s):
        return None

    monkeypatch.setattr(mod.asyncio, "sleep", no_sleep)
    return client, fake


SCHEMA = {"type": "object", "properties": {"a": {"type": "integer"}}, "required": ["a"]}


async def test_returns_validated_json_and_counts_usage(monkeypatch):
    client, fake = _client(monkeypatch, [_response('{"a": 1}')])
    out = await client.generate_validated_json_response("p", SCHEMA, "t", thinking="low")
    assert out == {"a": 1}
    assert client.usage == {"calls": 1, "prompt": 10, "cached": 4, "thoughts": 3, "output": 2}
    cfg = fake.calls[0]["config"]
    level = cfg.thinking_config.thinking_level
    assert str(getattr(level, "value", level)).lower() == "low"
    assert cfg.max_output_tokens == 65536
    assert getattr(cfg, "temperature", None) is None
    assert fake.calls[0]["model"] == "gemini-4-argon"


async def test_schema_violation_is_retried_within_cap(monkeypatch):
    client, fake = _client(monkeypatch, [_response('{"b": 1}'), _response('{"a": 2}')])
    assert await client.generate_validated_json_response("p", SCHEMA, "t") == {"a": 2}
    assert len(fake.calls) == 2


async def test_gives_up_after_cap(monkeypatch):
    client, fake = _client(monkeypatch, [_response("not json")] * 3, API_MAX_RETRIES="2")
    with pytest.raises(ValueError):
        await client.generate_validated_json_response("p", SCHEMA, "t")
    assert len(fake.calls) == 3  # 1 attempt + 2 retries


async def test_permanent_error_is_not_retried(monkeypatch):
    err = RuntimeError("403 PERMISSION_DENIED: Vertex AI is forbidden")
    err.code = 403
    client, fake = _client(monkeypatch, [err, _response('{"a": 1}')])
    with pytest.raises(RuntimeError):
        await client.generate_validated_json_response("p", SCHEMA, "t")
    assert len(fake.calls) == 1


async def test_transient_error_is_retried(monkeypatch):
    err = RuntimeError("429 RESOURCE_EXHAUSTED")
    err.code = 429
    client, fake = _client(monkeypatch, [err, _response('{"a": 1}')])
    assert await client.generate_validated_json_response("p", SCHEMA, "t") == {"a": 1}
    assert len(fake.calls) == 2


def test_thought_parts_are_skipped_and_fences_stripped():
    thought = SimpleNamespace(text="thinking...", thought=True)
    part = SimpleNamespace(text='```json\n{"a": 3}\n```', thought=False)
    cand = SimpleNamespace(finish_reason=SimpleNamespace(name="STOP"), content=SimpleNamespace(parts=[thought, part]))
    resp = SimpleNamespace(candidates=[cand], usage_metadata=None)
    assert json.loads(mod.AiClient._response_text(resp)) == {"a": 3}


def test_is_recoverable_classification():
    assert mod.is_recoverable(SimpleNamespace(code=503))
    assert mod.is_recoverable(RuntimeError("deadline exceeded"))
    assert not mod.is_recoverable(SimpleNamespace(code=400))
    assert not mod.is_recoverable(RuntimeError("invalid argument"))


def test_settings_map_legacy_thinking_names_and_fail_closed():
    assert _settings(MAKER_THINKING_LEVEL="minimal").maker_thinking_level == "low"
    with pytest.raises(Exception):
        _settings(MAKER_THINKING_LEVEL="ultra")
    with pytest.raises(ValueError):
        Settings(_env_file=None, TEST="false").require_ai_credentials()
