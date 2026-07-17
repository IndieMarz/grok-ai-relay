# Grok AI Relay

A Python-based AI relay and toolkit for Grok/xAI API interactions. Features request proxying, structured logging, response caching, multi-model support, prompt templating, and more.

## Features
- Clean, PEP 8 compliant core client
- Synchronous relay with easy extension to async (httpx)
- Extensible for logging, caching, retries, and security best practices
- Ready for CI/CD and testing

## Installation
```bash
git clone https://github.com/IndieMarz/grok-ai-relay.git
cd grok-ai-relay
pip install -e .
```

## Quick Start
```python
from grok_relay.client import send_to_grok

response = send_to_grok(
    prompt="Hello Grok!",
    api_key="your-xai-api-key",
)
print(response)
```

See `examples/simple_relay.py` for more.

## Development
- Lint & format: `ruff check .` and `black .`
- Run tests: `pytest`
- CI runs automatically on push/PR

## Project Structure
- `src/grok_relay/` — Core package
- `examples/` — Usage demos
- `tests/` — Test suite
- `.github/workflows/` — CI configuration

Built with love for the Grok/xAI ecosystem.

Contributions welcome!