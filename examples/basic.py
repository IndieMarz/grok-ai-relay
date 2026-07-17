#!/usr/bin/env python3
"""One-shot completion example. Requires XAI_API_KEY."""

from __future__ import annotations

import os
import sys

from grok_ai_relay import GrokAuthError, GrokRelay, GrokRelayError


def main() -> int:
    if not os.environ.get("XAI_API_KEY"):
        print("Set XAI_API_KEY first (see .env.example)", file=sys.stderr)
        return 1

    try:
        with GrokRelay() as relay:
            result = relay.chat(
                "Explain the benefits of PEP 8 for open-source tools in 3 bullets.",
                system="You are a concise technical writer.",
                max_completion_tokens=300,
            )
    except GrokAuthError as exc:
        print(f"Auth error: {exc}", file=sys.stderr)
        return 2
    except GrokRelayError as exc:
        print(f"API error: {exc}", file=sys.stderr)
        return 3

    print(result.content)
    if result.usage:
        print("\n--- usage ---", result.usage, sep="\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
