#!/usr/bin/env python3
"""Multi-turn conversation example. Requires XAI_API_KEY."""

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
            convo = relay.conversation(
                system="You are a friendly Python tutor. Keep answers short.",
            )
            turns = [
                "What is a list comprehension?",
                "Convert this loop to one: squares = []; for i in range(5): squares.append(i*i)",
                "Any common pitfalls?",
            ]
            for user_text in turns:
                print(f"\nUSER: {user_text}")
                result = convo.send(user_text, max_completion_tokens=250)
                print(f"ASSISTANT: {result.content}")
    except GrokRelayError as exc:
        print(f"API error: {exc}", file=sys.stderr)
        return 3

    print("\n--- transcript roles ---")
    for msg in convo.history:
        print(f"  {msg.role}: {msg.content[:60]!r}...")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
