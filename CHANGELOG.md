# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.2.0] - 2026-07-17

### Added

- `GrokRelay` class with context-manager support
- System prompts, multi-turn `Conversation`, and message history
- SSE streaming via `stream()` / `stream_to_grok()`
- Exponential backoff retries for 429 / 5xx / timeouts
- Typed exceptions (`GrokAuthError`, `GrokRateLimitError`, …)
- Structured `ChatResult` and `StreamChunk` dataclasses
- Examples, unit tests, CI, and documentation

### Changed

- Default model is now `grok-4.5`
- Prefer `max_completion_tokens` over deprecated `max_tokens`
- `send_to_grok` raises on failure instead of returning `None`

## [0.1.0] - 2026-07-17

### Added

- Initial `send_to_grok` synchronous helper (minimal relay example)
