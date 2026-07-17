# Architecture

## Goals

1. **Small surface area** — one public client class + two convenience functions.
2. **No heavy SDK** — only `requests`, so the package is easy to vendor or embed.
3. **Production-ready defaults** — timeouts, retries, env keys, typed errors.
4. **OpenAI-compatible chat path** — targets `POST /v1/chat/completions` so relays and proxies stay interchangeable.

## Module map

```
grok_ai_relay/
├── __init__.py   # Public re-exports + version
├── client.py     # GrokRelay, Conversation, send_to_grok, stream_to_grok
├── errors.py     # Exception hierarchy
├── types.py      # ChatMessage, ChatResult, StreamChunk
└── py.typed      # PEP 561 marker
```

## Request path

```
caller
  → GrokRelay.chat / .stream / Conversation.send
    → _build_payload (messages + options)
      → _request_json / _request_stream
        → retry loop (status / network)
          → POST {base_url}/chat/completions
            → ChatResult / Iterator[StreamChunk]
```

## Design choices

### Synchronous first

The first release is intentionally sync so it drops into CLI tools, scripts, and simple services without an event loop. An async client can share the same types/errors later.

### Chat completions vs Responses API

xAI documents both `/v1/chat/completions` and `/v1/responses`. This package uses **chat completions** because:

- It matches the original relay example and most OpenAI-compatible proxies.
- Multi-turn is a simple local `messages` array (no server-side `previous_response_id` dependency).
- Streaming is standard SSE `data: …` / `[DONE]`.

A Responses adapter can be added without changing `ChatResult` consumers.

### Retries

Retries apply to idempotent-style completion requests. The client does **not** retry after a stream has already yielded chunks (only connection setup / status before body iteration). Callers that need resume semantics should track partial text themselves.

### Result objects

`ChatResult` and `StreamChunk` normalize the useful fields while keeping `raw` for forward compatibility when xAI adds response keys.

## Extension points

| Need | Approach |
|---|---|
| Proxy / mock server | `base_url=` on `GrokRelay` |
| Shared connection pool | pass a preconfigured `requests.Session` |
| Custom headers / fields | `extra=` dict merged into the JSON body |
| Tools / function calling | pass tools via `extra=` (raw API shape) |
| Async | future `AsyncGrokRelay` reusing types + errors |

## Out of scope (for now)

- Image / video / voice endpoints
- Server-side tool orchestration
- Automatic conversation compaction
- Official `openai` or `xai-sdk` wrappers (users can adopt those when they want a fuller stack)

See [docs.x.ai](https://docs.x.ai) for the live API contract.
