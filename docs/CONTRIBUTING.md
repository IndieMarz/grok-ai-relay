# Contributing

Thanks for helping improve **grok-ai-relay**.

## Setup

```bash
git clone https://github.com/IndieMarz/grok-ai-relay.git
cd grok-ai-relay
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -e ".[dev]"
```

## Checks to run before a PR

```bash
pytest
ruff check src tests examples
ruff format --check src tests examples
mypy
```

Or rely on GitHub Actions — the same suite runs on every push/PR.

## Guidelines

1. **No secrets** — never commit API keys, real `.env` files, or recorded live traffic with credentials.
2. **Tests stay offline** — unit tests mock HTTP with `responses` (or similar). Live calls belong only in optional examples.
3. **Keep the surface small** — prefer extending `GrokRelay` / types over new top-level modules unless needed.
4. **Type everything** — the package ships `py.typed`; keep public APIs annotated.
5. **Document user-facing changes** — update `README.md`, `docs/usage.md`, and `CHANGELOG.md`.

## Pull request checklist

- [ ] Tests added/updated for behavior changes
- [ ] Lint and typecheck clean
- [ ] Changelog entry under `[Unreleased]` or the next version
- [ ] Docs reflect new parameters or errors

## Reporting issues

Include:

- Python version and OS
- Package version (`import grok_ai_relay; print(grok_ai_relay.__version__)`)
- Minimal repro (sanitized of keys)
- Whether the failure is local network, auth, or API response content

## Code of conduct

Be respectful. Assume good intent. Harassment or spam will be removed.
