#!/usr/bin/env python3
"""Streaming completion example. Requires XAI_API_KEY."""

from __future__ import annotations

import os
import sys

from grok_ai_relay import GrokRelay, GrokRelayError


def main() -> int:
    if not os.environ.get("XAI_API_KEY"):
        print("Set XAI_API_KEY first (see .env.example)", file=sys.stderr)
        return 1

    try:
        with GrokRelay() as relay:
            print("ASSISTANT: ", end="", flush=True)
            for chunk in relay.stream(
                "Write a 4-line poem about open-source collaboration.",
                system="You write crisp, image-rich poems.",
                max_completion_tokens=200,
            ):
                print(chunk.content, end="", flush=True)
            print()
    except GrokRelayError as exc:
        print(f"\nAPI error: {exc}", file=sys.stderr)
        return 3

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
