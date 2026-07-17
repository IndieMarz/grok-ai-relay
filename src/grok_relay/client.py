"""Core client for Grok/xAI API relay."""

import requests
from typing import Any


def send_to_grok(
    prompt: str, api_key: str, model: str = "grok-3", max_tokens: int = 800
) -> dict[str, Any] | None:
    """Relay a user prompt to the Grok/xAI chat completions API.

    Args:
        prompt: The user message content to send.
        api_key: Valid xAI API key. Prefer environment variables in production.
        model: Model identifier (default: grok-3).
        max_tokens: Maximum tokens to generate.

    Returns:
        Parsed JSON response on success, or None on failure.
    """
    url = "https://api.x.ai/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
    }
    payload = {
        "model": model,
        "messages": [{"role": "user", "content": prompt}],
        "max_tokens": max_tokens,
    }

    response = requests.post(url, headers=headers, json=payload)

    if response.status_code == 200:
        return response.json()

    # TODO: Replace with proper logging and custom exceptions
    print(f"Error {response.status_code}: {response.text}")
    return None