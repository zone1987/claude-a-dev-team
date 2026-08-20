---
name: gotenberg-deploy
description: Scaffold a Gotenberg deployment — docker run / docker-compose / Kubernetes / Cloud Run with health check, ports, resources and the matching CLI flags/env vars (api-*, chromium-*, libreoffice-*, webhook-*, log-*, outbound filtering).
argument-hint: <target> docker|compose|k8s|cloudrun [--auth basic] [--webhook] [--prometheus]
allowed-tools: Read, Glob, Grep, Write, Edit
model: sonnet
---

# /gotenberg-deploy

Produce a ready-to-run Gotenberg operating configuration. Skills: `gotenberg-operations`, `gotenberg-operations`,
`gotenberg-operations` (health/metrics), `gotenberg-operations`, and if needed `gotenberg-operations`, `gotenberg-operations`.

## Procedure
1. **Target platform** from `$ARGUMENTS` (docker run, docker-compose, K8s manifest, Cloud Run).
2. **Create the base**: official image `gotenberg/gotenberg:<tag>`, port `3000`, health check against `/health`
   (`gotenberg-operations`), sensible resource limits (Chromium/LibreOffice are memory-hungry).
3. **Flags/env vars** — add ONLY documented ones (source: `gotenberg-operations`), e.g. `--api-timeout`,
   `--api-port`, `--chromium-disable-javascript`, `--libreoffice-restart-after`, `--log-level`, `--api-enable-basic-auth`
   (with `GOTENBERG_API_BASIC_AUTH_USERNAME/PASSWORD` as **placeholders**, never real values).
4. **Options**: `--auth basic` → basic auth; `--webhook` → notes/allowlist (`gotenberg-operations`); `--prometheus` →
   keep the metrics endpoint enabled (`gotenberg-operations`). Recommend SSRF protection via outbound filtering.
5. Brief operating note: stateless → horizontally scalable; no persistence needed.

Never guess flags/defaults — check them against `gotenberg-operations`/`-installation`. No real credentials in the manifest.
