---
name: gotenberg-operations
description: Gotenberg operations: Docker and Kubernetes installation, all CLI flags and env vars, webhooks, URL filtering, metrics, troubleshooting, clients. Use when deploying or configuring Gotenberg.
---

# Gotenberg operations

Running and calling Gotenberg. It is stateless, so configuration is entirely flags and environment.

## Reference map

- **[CLIENTS.md](CLIENTS.md)**: Gotenberg ist eine Standard-HTTP-API. [CLIENTS-DETAIL](CLIENTS-DETAIL.md).
- **[CONFIGURATION.md](CONFIGURATION.md)**: Konfiguration via CLI-Flags oder Umgebungsvariablen. [CONFIGURATION-DETAIL](CONFIGURATION-DETAIL.md).
- **[INSTALLATION.md](INSTALLATION.md)**: Gotenberg laeuft ausschliesslich als Docker-Container. [INSTALLATION-DETAIL](INSTALLATION-DETAIL.md).
- **[INTRODUCTION.md](INTRODUCTION.md)**: Gotenberg ist eine **Docker-basierte, zustandslose HTTP-API** zur Dokumentenkonvertierung. [INTRODUCTION-DETAIL](INTRODUCTION-DETAIL.md).
- **[OUTBOUND-FILTERING.md](OUTBOUND-FILTERING.md)**: Konfiguration des ausgehenden URL-Filters gegen SSRF und ungewollte Netzwerkzugriffe. [OUTBOUND-FILTERING-DETAIL](OUTBOUND-FILTERING-DETAIL.md).
- **[SYSTEM.md](SYSTEM.md)**: Health-Check, Versioninfo, Prometheus-Metriken und Debug-Konfiguration. [SYSTEM-DETAIL](SYSTEM-DETAIL.md).
- **[TELEMETRY.md](TELEMETRY.md)**: OTEL-Integration fuer Traces, Metriken und Logs. [TELEMETRY-DETAIL](TELEMETRY-DETAIL.md).
- **[TROUBLESHOOTING.md](TROUBLESHOOTING.md)**: Loesungen fuer haeufige Probleme: leere PDFs, Schriftartprobleme, LibreOffice-Abstuerze, Webhook-TLS-Fehler, …. [TROUBLESHOOTING-DETAIL](TROUBLESHOOTING-DETAIL.md).
- **[WEBHOOK.md](WEBHOOK.md)**: Asynchrone Verarbeitung: Gotenberg gibt sofort 204 zurueck, sendet das Ergebnis per Callback-Request. [WEBHOOK-DETAIL](WEBHOOK-DETAIL.md).

## Source

Distilled from [gotenberg.dev](https://gotenberg.dev) — routes, configuration and every module — retrieved 2026-08-20.
