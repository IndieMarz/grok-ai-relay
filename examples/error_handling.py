#!/usr/bin/env python3
"""Demonstrate typed error handling (works with or without a real key)."""

from __future__ import annotations

import os

from grok_ai_relay import (
    GrokAuthError,
    GrokRateLimitError,
    GrokRelay,
    GrokRequestError,
    GrokTimeoutError,
)


def main() -> int:
    # Force a bad key if none is set so auth path is exercised offline-friendly.
    key = os.environ.get("XAI_API_KEY") or "sk-invalid-demo-key"

    try:
        with GrokRelay(api_key=key, timeout=15.0, max_retries=0) as relay:
            result = relay.chat("ping")
            print("OK:", result.content[:80])
            return 0
    except GrokAuthError as exc:
        print(f"[auth] {exc}")
        print("  → Create a key at https://console.x.ai and export XAI_API_KEY")
        return 2
    except GrokRateLimitError as exc:
        print(f"[rate limit] {exc} retry_after={exc.retry_after}")
        return 3
    except GrokTimeoutError as exc:
        print(f"[timeout] {exc}")
        return 4
    except GrokRequestError as exc:
        print(f"[request] status={exc.status_code} body={exc.body!r}")
        return 5


if __name__ == "__main__":
    raise SystemExit(main())
