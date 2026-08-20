# Gotenberg — Telemetry / OpenTelemetry (Full Reference)

## Contents

- [Concept](#concept)
- [Traces configuration](#traces-configuration)
- [Trace spans and attributes](#trace-spans-and-attributes)
- [Metrics configuration](#metrics-configuration)
- [Logs configuration](#logs-configuration)
- [Telemetry control for high-frequency routes](#telemetry-control-for-high-frequency-routes)
- [Complete Docker Compose example](#complete-docker-compose-example)
- [Notes](#notes)

## Concept

Gotenberg integrates OpenTelemetry for:
- **Distributed Tracing** — spans for every request and all sub-operations
- **Metrics** — HTTP server metrics, module metrics, queue sizes
- **Logs** — structured log shipping via OTLP

Configuration entirely via environment variables (standard OTEL convention).

---

## Traces configuration

### Environment variables

| Variable | Type | Default | Allowed values | Description |
|----------|-----|---------|----------------|--------------|
| `OTEL_TRACES_EXPORTER` | enum | `none` | `none`, `otlp`, `jaeger`, `zipkin` | Trace exporter type |
| `OTEL_EXPORTER_OTLP_ENDPOINT` | string | — | URL | OTLP endpoint for all signals (traces + metrics + logs) |
| `OTEL_EXPORTER_OTLP_TRACES_ENDPOINT` | string | — | URL | OTLP endpoint for traces only (overrides the general endpoint) |
| `OTEL_EXPORTER_OTLP_PROTOCOL` | enum | `grpc` | `grpc`, `http/protobuf` | OTLP transport protocol |
| `OTEL_EXPORTER_OTLP_HEADERS` | string | — | `Key=Value` | Custom request headers for the OTLP exporter |
| `OTEL_SERVICE_NAME` | string | `gotenberg` | any | Service name identifier in traces |
| `OTEL_TRACES_SAMPLER` | string | `parentbased_always_on` | OTEL sampler | Sampling strategy |
| `OTEL_TRACES_SAMPLER_ARG` | string | — | Sampler argument | For `traceidratio`: sampling rate (e.g. `0.1` = 10%) |

---

## Trace spans and attributes

### HTTP server spans

A server span is created per request. Child spans for all sub-operations.

### Module spans

| Span name | Description | Attributes/events |
|-----------|-------------|-----------------|
| `chromium.Pdf` | Chromium PDF conversion | Engine version, queue depth, conversions since start, error type |
| `chromium.Screenshot` | Chromium screenshot | Network attributes, `chromium.heaviest_resource` event, file/byte counters |
| `chromium.print_to_pdf` | Print-to-PDF operation | — |
| `chromium.queue.wait` | Waiting for a Chromium slot | Slot wait time |
| `chromium.process.start` | Chromium process start | Start reason: `first_start`, `unhealthy`, `max_requests` |
| `libreoffice.Pdf` | LibreOffice PDF conversion | Engine version, input/output byte counters |
| `libreoffice.queue.wait` | Waiting for a LibreOffice slot | Slot wait time |
| `libreoffice.process.start` | LibreOffice process start | Start reason |
| `process.exec` | External binary invocation | Binary name, version tags |
| `qpdf.InjectFacturXXMP` | Factur-X XMP injection | — |
| `qpdf.ReadPdfAConformance` | PDF/A conformance check | — |

(Available as of v8.34.0)

---

## Metrics configuration

### Environment variables

| Variable | Type | Default | Allowed values | Description |
|----------|-----|---------|----------------|--------------|
| `OTEL_METRICS_EXPORTER` | enum | `none` | `none`, `otlp`, `prometheus` | Metrics exporter type |
| `OTEL_EXPORTER_OTLP_METRICS_ENDPOINT` | string | — | URL | OTLP endpoint for metrics |
| `OTEL_METRICS_EXEMPLAR_FILTER` | enum | `trace_based` | `trace_based`, `always_on`, `always_off` | Exemplar filtering |
| `OTEL_EXPORTER_PROMETHEUS_HOST` | string | `localhost` | IP/hostname | Bind address for the built-in Prometheus exporter |
| `OTEL_EXPORTER_PROMETHEUS_PORT` | integer | `9464` | Port | Port for the built-in Prometheus exporter |

### Available metrics

| Metric | Type | Description |
|--------|-----|-------------|
| HTTP server metrics | Counter/Histogram | Request count, duration, size |
| `chromium.network.requests.total` | Counter | Chromium network requests with outcome labels |
| `chromium.network.bytes` | Histogram | Chromium network bytes |
| `libreoffice.conversion.retries.total` | Counter | LibreOffice conversion retries |
| Observable gauges (module-specific) | Gauge | Conversion duration, output size, queue size, restarts |

### Prometheus migration (from /prometheus/metrics)

**Option 1: OTLP → Prometheus-compatible backend (via collector)**

```yaml
# otel-collector-config.yaml
receivers:
  otlp:
    protocols:
      grpc:
        endpoint: 0.0.0.0:4317

exporters:
  prometheus:
    endpoint: 0.0.0.0:8889

service:
  pipelines:
    metrics:
      receivers: [otlp]
      exporters: [prometheus]
```

**Option 2: built-in Prometheus exporter**

```bash
OTEL_METRICS_EXPORTER=prometheus
OTEL_EXPORTER_PROMETHEUS_HOST=0.0.0.0
OTEL_EXPORTER_PROMETHEUS_PORT=9464
```

Endpoint: `http://0.0.0.0:9464/metrics`

---

## Logs configuration

### Environment variables

| Variable | Type | Default | Allowed values | Description |
|----------|-----|---------|----------------|--------------|
| `OTEL_LOGS_EXPORTER` | enum | `none` | `none`, `otlp` | Logs exporter type |
| `OTEL_EXPORTER_OTLP_LOGS_ENDPOINT` | string | — | URL | OTLP endpoint for logs |
| `LOG_STD_FORMAT` | enum | `auto` | `auto`, `json`, `text` | Stdout log format |
| `LOG_STD_ENABLE_GCP_FIELDS` | boolean | `false` | `true`/`false` | GCP-compatible field names for Cloud Logging |

---

## Telemetry control for high-frequency routes

| Flag / env variable | Description | Default |
|--------------------|-------------|---------|
| `API_DISABLE_ROOT_ROUTE_TELEMETRY` | Root route `/` | `true` |
| `API_DISABLE_DEBUG_ROUTE_TELEMETRY` | Debug route `/debug` | `true` |
| `API_DISABLE_VERSION_ROUTE_TELEMETRY` | Version route `/version` | `true` |
| `API_DISABLE_HEALTH_CHECK_ROUTE_TELEMETRY` | Health check `/health` | `true` |
| `PROMETHEUS_DISABLE_ROUTE_TELEMETRY` | Prometheus `/prometheus/metrics` | `true` |

---

## Complete Docker Compose example

```yaml
services:
  gotenberg:
    image: gotenberg/gotenberg:8
    ports:
      - "3000:3000"
    environment:
      OTEL_SERVICE_NAME: "gotenberg"
      OTEL_TRACES_EXPORTER: "otlp"
      OTEL_METRICS_EXPORTER: "otlp"
      OTEL_LOGS_EXPORTER: "otlp"
      OTEL_EXPORTER_OTLP_ENDPOINT: "http://otel-collector:4317"
      OTEL_EXPORTER_OTLP_PROTOCOL: "grpc"
      LOG_STD_FORMAT: "json"

  otel-collector:
    image: otel/opentelemetry-collector-contrib
    ports:
      - "4317:4317"    # OTLP gRPC
      - "8889:8889"    # Prometheus metrics export
    volumes:
      - ./otel-collector-config.yaml:/etc/otelcol-contrib/config.yaml
```

### Jaeger integration

```yaml
environment:
  OTEL_TRACES_EXPORTER: "otlp"
  OTEL_EXPORTER_OTLP_TRACES_ENDPOINT: "http://jaeger:4317"
  OTEL_EXPORTER_OTLP_PROTOCOL: "grpc"
```

### Zipkin integration

```yaml
environment:
  OTEL_TRACES_EXPORTER: "zipkin"
  OTEL_EXPORTER_OTLP_TRACES_ENDPOINT: "http://zipkin:9411/api/v2/spans"
```

### Sampling (only 10% of traces)

```yaml
environment:
  OTEL_TRACES_SAMPLER: "traceidratio"
  OTEL_TRACES_SAMPLER_ARG: "0.1"
```

---

## Notes

- The `/prometheus/metrics` endpoint is deprecated as of v8.29.0 — migrate to OTEL
- The W3C `traceparent` header is also sent along in webhook callbacks as of v8.34.0
- Rich trace attributes (v8.34.0+) require an up-to-date Gotenberg image

---

Source: https://gotenberg.dev/docs/telemetry
