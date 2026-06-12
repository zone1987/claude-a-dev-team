---
name: gotenberg-system
description: >
  Gotenberg system endpoints: health check, version, Prometheus metrics, debug.
  Triggers: "gotenberg health", "gotenberg version", "gotenberg metrics",
  "gotenberg debug", "GET /health", "GET /version", "GET /prometheus/metrics",
  "GET /debug", health check route, liveness probe, Prometheus scraping.
---

# Gotenberg — System-Endpunkte

Health-Check (GET/HEAD /health), Versioninfo (/version),
Prometheus-Metriken (/prometheus/metrics, deprecated → OTEL) und
Debug-Konfiguration (/debug, requires API_ENABLE_DEBUG_ROUTE=true).
Referenz: `references/deep/system.md`
