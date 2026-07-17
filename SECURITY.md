# Security policy

## Supported versions

| Version | Supported          |
| ------- | ------------------ |
| 0.2.x   | :white_check_mark: |
| < 0.2   | :x:                |

## Reporting a vulnerability

Please **do not** open a public GitHub issue for security problems.

Instead:

1. Use GitHub **Private vulnerability reporting** on this repository (Security → Report a vulnerability), **or**
2. Email the maintainers if private reporting is unavailable (see the repo owner profile for contact options).

Include:

- Description of the issue and impact
- Steps to reproduce (proof of concept without exploiting third parties)
- Affected versions / commit SHA if known

We aim to acknowledge reports within **7 days** and provide a remediation plan or fix timeline as soon as practical.

## What is in scope

- Credential leakage or unsafe defaults in this library
- Remote code execution / injection via response handling
- Path or SSRF issues if introduced by helpers that touch the network filesystem

## What is out of scope

- Compromised **xAI API keys** or account takeover (rotate keys in [console.x.ai](https://console.x.ai))
- Issues solely in the upstream xAI service
- Denial of service against public API endpoints

## Safe usage notes

- Load keys from `XAI_API_KEY` or a secret manager — never hard-code them
- Keep keys **server-side**; do not embed them in browser bundles
- Prefer short-lived keys and least privilege where the platform allows it
