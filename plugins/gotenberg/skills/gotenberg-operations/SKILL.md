---
name: gotenberg-operations
description: Gotenberg operations: Docker and Kubernetes installation, all CLI flags and env vars, webhooks, URL filtering, metrics, troubleshooting, clients. Use when deploying or configuring Gotenberg.
---

# Gotenberg operations

Running and calling Gotenberg. It is stateless, so configuration is entirely flags and environment.

## Reference map

- **[CLIENTS.md](references/CLIENTS.md)**: Gotenberg is a standard HTTP API.
- **[CONFIGURATION.md](references/CONFIGURATION.md)**: Configuration via CLI flags or environment variables.
- **[INSTALLATION.md](references/INSTALLATION.md)**: Gotenberg runs exclusively as a Docker container.
- **[INTRODUCTION.md](references/INTRODUCTION.md)**: Gotenberg is a **Docker-based, stateless HTTP API** for document conversion.
- **[OUTBOUND-FILTERING.md](references/OUTBOUND-FILTERING.md)**: Configuring the outbound URL filter against SSRF and unwanted network access.
- **[SYSTEM.md](references/SYSTEM.md)**: Health check, version info, Prometheus metrics and debug configuration.
- **[TELEMETRY.md](references/TELEMETRY.md)**: OTEL integration for traces, metrics and logs.
- **[TROUBLESHOOTING.md](references/TROUBLESHOOTING.md)**: Solutions for common problems: empty PDFs, font issues, LibreOffice crashes, webhook TLS errors, ….
- **[WEBHOOK.md](references/WEBHOOK.md)**: Asynchronous processing: Gotenberg returns 204 immediately and sends the result via a callback request.

## Source

Distilled from [gotenberg.dev](https://gotenberg.dev) — routes, configuration and every module — retrieved 2026-08-20.
