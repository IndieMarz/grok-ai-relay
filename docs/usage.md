# Usage guide

## Authentication

Set the key once in your shell or process environment:

```bash
export XAI_API_KEY="xai-..."
```

Or pass it explicitly (prefer env in production):

```python
from grok_ai_relay import GrokRelay

relay = GrokRelay(api_key="xai-...")
```

Keys are created at [console.x.ai](https://console.x.ai). Never commit keys or ship them in client-side bundles.

## One-shot completion

```python
from grok_ai_relay import send_to_grok

result = send_to_grok("Summarize asyncio in two bullets")
print(result.content)       # assistant text
print(result.model)         # model id used
print(result.finish_reason) # e.g. "stop"
print(result.usage)         # token usage dict (if returned)
print(result.raw)           # full JSON payload
```

### System prompt

```python
result = send_to_grok(
    "How do I open a file?",
    system="You are a senior Python instructor. Prefer pathlib.",
)
```

### Custom model and limits

```python
result = send_to_grok(
    "Write a regex for emails",
    model="grok-4.5",
    max_completion_tokens=200,
    temperature=0.2,
)
```

## Multi-turn with `Conversation`

```python
from grok_ai_relay import GrokRelay

with GrokRelay() as relay:
    chat = relay.conversation(
        system="You are a terse devops coach.",
        temperature=0.3,
    )
    r1 = chat.send("What is a liveness probe?")
    r2 = chat.send("Give a minimal Kubernetes example.")
    print(r1.content)
    print(r2.content)
    print(chat.messages_as_dicts())  # full transcript
    chat.clear(keep_system=True)
```

You can also pass an explicit `messages` list to `chat()` / `stream()` for full control (including `ChatMessage` objects or plain dicts).

## Streaming

```python
from grok_ai_relay import GrokRelay

with GrokRelay() as relay:
    for chunk in relay.stream("Tell a short joke about Python"):
        print(chunk.content, end="", flush=True)
    print()
```

Stream chunks expose:

- `content` — delta string (may be empty on the final chunk)
- `finish_reason` — set on the last meaningful chunk
- `done` — `True` when `finish_reason` is present
- `raw` — underlying SSE JSON object

## Retries and timeouts

```python
relay = GrokRelay(
    timeout=30.0,
    max_retries=5,
    backoff_base=0.5,
    backoff_max=20.0,
)
```

Retried conditions:

- HTTP **408, 409, 429, 500, 502, 503, 504**
- `requests` timeouts and connection errors

Non-retryable auth failures (**401/403**) fail immediately as `GrokAuthError`.

Backoff uses full jitter. When the API sends `Retry-After`, that value is honored (capped by `backoff_max`).

## Passing extra API fields

Anything not covered by first-class kwargs can go through `extra=`:

```python
result = relay.chat(
    "Hello",
    extra={"seed": 42, "user": "relay-demo"},
)
```

## Logging

The client uses the standard library `logging` module under the logger name `grok_ai_relay.client`.

```python
import logging

logging.basicConfig(level=logging.DEBUG)
```

## Examples

Runnable scripts under `examples/`:

| Script | What it shows |
|---|---|
| `basic.py` | One-shot completion |
| `multi_turn.py` | Conversation history |
| `stream.py` | Token streaming |
| `error_handling.py` | Typed exception handling |

All require `XAI_API_KEY`.
