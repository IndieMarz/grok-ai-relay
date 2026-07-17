# grok-ai-relay

[![CI](https://github.com/IndieMarz/grok-ai-relay/actions/workflows/ci.yml/badge.svg)](https://github.com/IndieMarz/grok-ai-relay/actions/workflows/ci.yml)
[![CodeQL](https://github.com/IndieMarz/grok-ai-relay/actions/workflows/codeql.yml/badge.svg)](https://github.com/IndieMarz/grok-ai-relay/actions/workflows/codeql.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Python 3.9+](https://img.shields.io/badge/python-3.9%2B-blue.svg)](https://www.python.org/downloads/)

**Hardened synchronous Python relay for the [Grok / xAI](https://docs.x.ai) chat completions API.**

A clean foundation for tools that need to call Grok without pulling in a full OpenAI SDK: retries, streaming, multi-turn history, system prompts, and typed errors — one small dependency (`requests`).

```bash
pip install -e ".[dev]"   # from a clone
export XAI_API_KEY=...    # https://console.x.ai
```

```python
from grok_ai_relay import send_to_grok

result = send_to_grok("Explain PEP 8 in one sentence")
print(result.content)
```

## Features

| Capability | API |
|---|---|
| One-shot chat | `send_to_grok()` / `GrokRelay.chat()` |
| System prompts | `system="You are…"` |
| Multi-turn | `relay.conversation()` |
| Streaming (SSE) | `stream_to_grok()` / `relay.stream()` |
| Retries | Exponential backoff on 429 / 5xx / timeouts |
| Typed errors | `GrokAuthError`, `GrokRateLimitError`, … |
| Env key loading | `XAI_API_KEY` |

Default model: **`grok-4.5`**. Endpoint: `https://api.x.ai/v1/chat/completions`.

## Install

```bash
# Development install from source
git clone https://github.com/IndieMarz/grok-ai-relay.git
cd grok-ai-relay
python -m venv .venv && source .venv/bin/activate
pip install -e ".[dev]"
```

Requires **Python 3.9+**.

## Quick start

### One-shot

```python
from grok_ai_relay import send_to_grok

result = send_to_grok(
    "List three benefits of type hints",
    system="You are a concise Python mentor.",
)
print(result.content)
print(result.usage)
```

### Client class

```python
from grok_ai_relay import GrokRelay

with GrokRelay(model="grok-4.5", max_retries=3) as relay:
    result = relay.chat("Hello!", system="Reply in one short sentence.")
    print(result.content)
```

### Multi-turn conversation

```python
from grok_ai_relay import GrokRelay

with GrokRelay() as relay:
    convo = relay.conversation(system="You are a helpful coding assistant.")
    print(convo.send("What is a context manager?").content)
    print(convo.send("Show a tiny example.").content)
    # convo.history holds the full message list
```

### Streaming

```python
from grok_ai_relay import stream_to_grok

for chunk in stream_to_grok("Write a haiku about open source"):
    print(chunk.content, end="", flush=True)
print()
```

## Configuration

| Env / arg | Default | Description |
|---|---|---|
| `XAI_API_KEY` / `api_key=` | — | Required API key from [console.x.ai](https://console.x.ai) |
| `model=` | `grok-4.5` | Model id (see [docs.x.ai/models](https://docs.x.ai/developers/models)) |
| `timeout=` | `60.0` | Request timeout (seconds) |
| `max_retries=` | `3` | Retries after the first attempt |
| `max_completion_tokens=` | `800` | Generation cap |
| `base_url=` | `https://api.x.ai/v1` | Override for proxies / self-hosted relays |

Never hard-code keys. Use `.env` (git-ignored) or your secret manager. See `.env.example`.

## Error handling

```python
from grok_ai_relay import (
    send_to_grok,
    GrokAuthError,
    GrokRateLimitError,
    GrokTimeoutError,
    GrokRequestError,
)

try:
    print(send_to_grok("ping").content)
except GrokAuthError:
    print("Check XAI_API_KEY")
except GrokRateLimitError as e:
    print("Back off", e.retry_after)
except GrokTimeoutError:
    print("Network / timeout")
except GrokRequestError as e:
    print(e.status_code, e.body)
```

## Project layout

```
grok-ai-relay/
├── src/grok_ai_relay/     # Library package
├── examples/              # Runnable demos
├── tests/                 # Pytest suite (mocked HTTP)
├── docs/                  # Extended documentation
├── .github/workflows/     # CI
├── pyproject.toml
└── README.md
```

## Development

```bash
pip install -e ".[dev]"
pytest
ruff check src tests examples
mypy
```

Live smoke test (uses real credits):

```bash
export XAI_API_KEY=...
python examples/basic.py
```

## Documentation

- [Usage guide](docs/usage.md)
- [Architecture notes](docs/architecture.md)
- [Contributing](docs/CONTRIBUTING.md)
- [Security policy](SECURITY.md)
- [Code of conduct](CODE_OF_CONDUCT.md)
- [xAI official docs](https://docs.x.ai)

## Community & GitHub

| Feature | Location |
|---|---|
| Bug / feature / question forms | `.github/ISSUE_TEMPLATE/` |
| PR checklist | `.github/PULL_REQUEST_TEMPLATE.md` |
| CI (pytest, ruff, mypy, build) | `.github/workflows/ci.yml` |
| CodeQL | `.github/workflows/codeql.yml` |
| Dependabot | `.github/dependabot.yml` |
| Auto-label PRs | `.github/workflows/labeler.yml` |
| Stale bot | `.github/workflows/stale.yml` |
| Release → PyPI | `.github/workflows/release.yml` |
| Labels bootstrap | `scripts/bootstrap_github_labels.py` |

## License

[MIT](LICENSE) — use freely in open tools and commercial products.

## Disclaimer

This project is **not** affiliated with xAI. Grok and xAI are trademarks of their respective owners. API behavior and model names may change; check [docs.x.ai](https://docs.x.ai) for the current contract.
