from grok_relay.client import send_to_grok

if __name__ == "__main__":
    # Example usage (load key securely in production)
    result = send_to_grok(
        prompt="Explain PEP 8 best practices for open-source tools",
        api_key="sk-your-key-here",
    )
    print(result)