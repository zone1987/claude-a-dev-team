# Gotenberg — System Endpoints (Full Reference)

## Contents

- [Overview of all system routes](#overview-of-all-system-routes)
- [1. GET /health — Health check](#1-get-health-health-check)
- [2. HEAD /health — Lightweight health check](#2-head-health-lightweight-health-check)
- [3. GET /version — Version information](#3-get-version-version-information)
- [4. GET /prometheus/metrics — Prometheus metrics](#4-get-prometheusmetrics-prometheus-metrics)
- [5. GET /debug — Debug configuration](#5-get-debug-debug-configuration)
- [Telemetry control for system routes](#telemetry-control-for-system-routes)

## Overview of all system routes

| Method | Route | Description |
|---------|-------|-------------|
| `GET` | `/health` | Health status with detail JSON |
| `HEAD` | `/health` | Health status (status code only, no body) |
| `GET` | `/version` | Running Gotenberg version |
| `GET` | `/prometheus/metrics` | Prometheus metrics (deprecated as of v8.29.0) |
| `GET` | `/debug` | Runtime configuration + modules + dependencies (only when enabled) |

---

## 1. GET /health — Health check

### Route

```
GET /health
```

### Request headers

| Header | Type | Required | Description |
|--------|-----|---------|--------------|
| `Gotenberg-Trace` | string | No | Custom request ID for log identification |

### Response codes

| Code | Description |
|------|-------------|
| `200` | Service is healthy |
| `503` | Service is not healthy |

### Response body (200 — healthy)

```json
{
  "status": "up",
  "details": {
    "chromium": {
      "status": "up",
      "timestamp": "2021-07-01T08:05:14.603364Z"
    },
    "libreoffice": {
      "status": "up",
      "timestamp": "2021-07-01T08:05:14.603364Z"
    }
  }
}
```

### Response body (503 — not healthy)

```json
{
  "status": "down",
  "details": {
    "chromium": {
      "status": "up",
      "timestamp": "2021-07-01T08:05:14.603364Z"
    },
    "libreoffice": {
      "status": "down",
      "timestamp": "2021-07-01T08:05:14.603364Z",
      "error": "LibreOffice is not available"
    }
  }
}
```

### Response structure per module

| Field | Type | Description |
|------|-----|--------------|
| `status` | `"up"` / `"down"` | Module health |
| `timestamp` | ISO 8601 | Timestamp of the check |
| `error` | string (optional) | Error message when status=down |

### curl example

```bash
curl --request GET http://localhost:3000/health
```

---

## 2. HEAD /health — Lightweight health check

### Route

```
HEAD /health
```

### Description

Identical to `GET /health`, but without a response body. Ideal for frequent polling (e.g. Kubernetes liveness probe, load balancer checks), since less bandwidth is consumed.

### Response codes

| Code | Description |
|------|-------------|
| `200` | Service is healthy |
| `503` | Service is not healthy |

### curl example

```bash
curl --request HEAD http://localhost:3000/health
```

### Kubernetes liveness probe (example)

```yaml
livenessProbe:
  httpGet:
    path: /health
    port: 3000
  initialDelaySeconds: 10
  periodSeconds: 30
  failureThreshold: 3
```

**As of v8.33.0:** Tolerates a transient failing probe and briefly caches successful results — prevents probe spam from forcing healthy instances to restart.

---

## 3. GET /version — Version information

### Route

```
GET /version
```

### Request headers

| Header | Type | Required | Description |
|--------|-----|---------|--------------|
| `Gotenberg-Trace` | string | No | Custom request ID for log identification |

### Response

| Code | Content-Type | Body |
|------|-------------|------|
| `200` | `text/plain; charset=UTF-8` | Version string, e.g. `Gotenberg 8.0.0` |

### curl example

```bash
curl --request GET http://localhost:3000/version
```

### Response example

```
Gotenberg 8.0.0
```

Note: Custom builds may report non-standard versions (e.g. `8.0.0-live-demo-snapshot`).

---

## 4. GET /prometheus/metrics — Prometheus metrics

### Route

```
GET /prometheus/metrics
```

**Deprecated as of v8.29.0** — migration to OpenTelemetry is recommended (see `gotenberg-telemetry`).

### Request headers

| Header | Type | Required | Description |
|--------|-----|---------|--------------|
| `Gotenberg-Trace` | string | No | Custom request ID for log identification |

### Response

| Code | Content-Type | Description |
|------|-------------|--------------|
| `200` | Prometheus text format | Metrics in the Prometheus exposition format |

### curl example

```bash
curl --request GET http://localhost:3000/prometheus/metrics
```

### Configuration

The Prometheus endpoint is enabled by the Prometheus module. Configurable via Gotenberg start flags.

Telemetry route disable (default `true`):
- `PROMETHEUS_DISABLE_ROUTE_TELEMETRY=true` — the Prometheus metrics route itself generates no telemetry

---

## 5. GET /debug — Debug configuration

### Route

```
GET /debug
```

### Enabling

**Must be enabled explicitly:**

```bash
# As a start flag
--api-enable-debug-route

# As an environment variable
API_ENABLE_DEBUG_ROUTE=true
```

### Description

Returns:
- Runtime configuration (all active flags and their values)
- Active modules
- Dependency versions (Chromium, LibreOffice, ExifTool, etc.)

Useful for deployment verification and for debugging configuration problems.

### Request headers

| Header | Type | Required | Description |
|--------|-----|---------|--------------|
| `Gotenberg-Trace` | string | No | Custom request ID for log identification |

### Response

| Code | Description |
|------|-------------|
| `200` | Debug information (JSON-like format) |

### curl example

```bash
API_ENABLE_DEBUG_ROUTE=true
curl --request GET http://localhost:3000/debug
```

### Docker Compose activation

```yaml
services:
  gotenberg:
    image: gotenberg/gotenberg:8
    environment:
      API_ENABLE_DEBUG_ROUTE: "true"
```

**Security note:** Keep the debug route disabled in production! It can reveal internal configuration details, versions and password hints.

---

## Telemetry control for system routes

High-frequency routes generate no telemetry by default:

| Route | Env variable | Default |
|-------|-------------|---------|
| Root `/` | `API_DISABLE_ROOT_ROUTE_TELEMETRY` | `true` |
| `/debug` | `API_DISABLE_DEBUG_ROUTE_TELEMETRY` | `true` |
| `/version` | `API_DISABLE_VERSION_ROUTE_TELEMETRY` | `true` |
| `/health` | `API_DISABLE_HEALTH_CHECK_ROUTE_TELEMETRY` | `true` |
| `/prometheus/metrics` | `PROMETHEUS_DISABLE_ROUTE_TELEMETRY` | `true` |

---

Sources:
- https://gotenberg.dev/docs/system/get-health-check
- https://gotenberg.dev/docs/system/head-health-check
- https://gotenberg.dev/docs/system/version
- https://gotenberg.dev/docs/system/prometheus-metrics
- https://gotenberg.dev/docs/system/debug
