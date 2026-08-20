---
name: gotenberg-operations
description: Gotenberg operations: Docker and Kubernetes installation, all CLI flags and env vars, webhooks, URL filtering, metrics, troubleshooting, clients. Use when deploying or configuring Gotenberg.
---

# Gotenberg operations

Running and calling Gotenberg. It is stateless, so configuration is entirely flags and environment.

## Reference map

- **[CLIENTS.md](CLIENTS.md)**: Gotenberg is a standard HTTP API. [CLIENTS-DETAIL](CLIENTS-DETAIL.md).
- **[CONFIGURATION.md](CONFIGURATION.md)**: Configuration via CLI flags or environment variables. [CONFIGURATION-DETAIL](CONFIGURATION-DETAIL.md).
- **[INSTALLATION.md](INSTALLATION.md)**: Gotenberg runs exclusively as a Docker container. [INSTALLATION-DETAIL](INSTALLATION-DETAIL.md).
- **[INTRODUCTION.md](INTRODUCTION.md)**: Gotenberg is a **Docker-based, stateless HTTP API** for document conversion. [INTRODUCTION-DETAIL](INTRODUCTION-DETAIL.md).
- **[OUTBOUND-FILTERING.md](OUTBOUND-FILTERING.md)**: Configuring the outbound URL filter against SSRF and unwanted network access. [OUTBOUND-FILTERING-DETAIL](OUTBOUND-FILTERING-DETAIL.md).
- **[SYSTEM.md](SYSTEM.md)**: Health check, version info, Prometheus metrics and debug configuration. [SYSTEM-DETAIL](SYSTEM-DETAIL.md).
- **[TELEMETRY.md](TELEMETRY.md)**: OTEL integration for traces, metrics and logs. [TELEMETRY-DETAIL](TELEMETRY-DETAIL.md).
- **[TROUBLESHOOTING.md](TROUBLESHOOTING.md)**: Solutions for common problems: empty PDFs, font issues, LibreOffice crashes, webhook TLS errors, …. [TROUBLESHOOTING-DETAIL](TROUBLESHOOTING-DETAIL.md).
- **[WEBHOOK.md](WEBHOOK.md)**: Asynchronous processing: Gotenberg returns 204 immediately and sends the result via a callback request. [WEBHOOK-DETAIL](WEBHOOK-DETAIL.md).

## Source

Distilled from [gotenberg.dev](https://gotenberg.dev) — routes, configuration and every module — retrieved 2026-08-20.
