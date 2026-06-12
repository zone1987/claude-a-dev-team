# Gotenberg — Telemetrie / OpenTelemetry (Vollreferenz)

## Konzept

Gotenberg integriert OpenTelemetry fuer:
- **Distributed Tracing** — Spans fuer jeden Request und alle Unter-Operationen
- **Metrics** — HTTP-Server-Metriken, Modul-Metriken, Queue-Groessen
- **Logs** — Strukturiertes Log-Shipping via OTLP

Konfiguration komplett ueber Umgebungsvariablen (Standard-OTEL-Konvention).

---

## Traces-Konfiguration

### Umgebungsvariablen

| Variable | Typ | Standard | Erlaubte Werte | Beschreibung |
|----------|-----|---------|----------------|--------------|
| `OTEL_TRACES_EXPORTER` | enum | `none` | `none`, `otlp`, `jaeger`, `zipkin` | Trace-Exporter-Typ |
| `OTEL_EXPORTER_OTLP_ENDPOINT` | string | — | URL | OTLP-Endpunkt fuer alle Signale (Traces + Metriken + Logs) |
| `OTEL_EXPORTER_OTLP_TRACES_ENDPOINT` | string | — | URL | OTLP-Endpunkt nur fuer Traces (ueberschreibt allgemeinen Endpunkt) |
| `OTEL_EXPORTER_OTLP_PROTOCOL` | enum | `grpc` | `grpc`, `http/protobuf` | OTLP-Transportprotokoll |
| `OTEL_EXPORTER_OTLP_HEADERS` | string | — | `Key=Value` | Custom-Request-Header fuer OTLP-Exporter |
| `OTEL_SERVICE_NAME` | string | `gotenberg` | beliebig | Service-Name-Bezeichner in Traces |
| `OTEL_TRACES_SAMPLER` | string | `parentbased_always_on` | OTEL-Sampler | Sampling-Strategie |
| `OTEL_TRACES_SAMPLER_ARG` | string | — | Sampler-Argument | Fuer `traceidratio`: Sampling-Rate (z.B. `0.1` = 10%) |

---

## Trace-Spans und Attribute

### HTTP-Server-Spans

Pro Request wird ein Server-Span erstellt. Child-Spans fuer alle Unter-Operationen.

### Modul-Spans

| Span-Name | Beschreibung | Attribute/Events |
|-----------|-------------|-----------------|
| `chromium.Pdf` | Chromium PDF-Konvertierung | Engine-Version, Queue-Tiefe, Konvertierungen seit Start, Fehlertyp |
| `chromium.Screenshot` | Chromium Screenshot | Netzwerk-Attribute, `chromium.heaviest_resource`-Event, Datei-/Byte-Zaehler |
| `chromium.print_to_pdf` | Print-to-PDF-Operation | — |
| `chromium.queue.wait` | Warten auf Chromium-Slot | Slot-Wartezeit |
| `chromium.process.start` | Chromium-Prozessstart | Startgrund: `first_start`, `unhealthy`, `max_requests` |
| `libreoffice.Pdf` | LibreOffice PDF-Konvertierung | Engine-Version, Input/Output-Byte-Zaehler |
| `libreoffice.queue.wait` | Warten auf LibreOffice-Slot | Slot-Wartezeit |
| `libreoffice.process.start` | LibreOffice-Prozessstart | Startgrund |
| `process.exec` | Externer Binary-Aufruf | Binary-Name, Versions-Tags |
| `qpdf.InjectFacturXXMP` | Factur-X XMP-Injektion | — |
| `qpdf.ReadPdfAConformance` | PDF/A-Konformitaets-Check | — |

(Ab v8.34.0 verfuegbar)

---

## Metriken-Konfiguration

### Umgebungsvariablen

| Variable | Typ | Standard | Erlaubte Werte | Beschreibung |
|----------|-----|---------|----------------|--------------|
| `OTEL_METRICS_EXPORTER` | enum | `none` | `none`, `otlp`, `prometheus` | Metriken-Exporter-Typ |
| `OTEL_EXPORTER_OTLP_METRICS_ENDPOINT` | string | — | URL | OTLP-Endpunkt fuer Metriken |
| `OTEL_METRICS_EXEMPLAR_FILTER` | enum | `trace_based` | `trace_based`, `always_on`, `always_off` | Exemplar-Filterung |
| `OTEL_EXPORTER_PROMETHEUS_HOST` | string | `localhost` | IP/Hostname | Bind-Adresse fuer Built-in-Prometheus-Exporter |
| `OTEL_EXPORTER_PROMETHEUS_PORT` | integer | `9464` | Port | Port fuer Built-in-Prometheus-Exporter |

### Verfuegbare Metriken

| Metrik | Typ | Beschreibung |
|--------|-----|-------------|
| HTTP-Server-Metriken | Counter/Histogram | Request-Anzahl, -Dauer, -Groesse |
| `chromium.network.requests.total` | Counter | Chromium-Netzwerkanfragen mit Outcome-Labels |
| `chromium.network.bytes` | Histogram | Chromium-Netzwerk-Bytes |
| `libreoffice.conversion.retries.total` | Counter | LibreOffice-Konvertierungs-Wiederholungen |
| Observable Gauges (Modul-spezifisch) | Gauge | Konvertierungsdauer, Output-Groesse, Queue-Groesse, Neustarts |

### Prometheus-Migration (von /prometheus/metrics)

**Option 1: OTLP → Prometheus-kompatibler Backend (via Collector)**

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

**Option 2: Built-in Prometheus-Exporter**

```bash
OTEL_METRICS_EXPORTER=prometheus
OTEL_EXPORTER_PROMETHEUS_HOST=0.0.0.0
OTEL_EXPORTER_PROMETHEUS_PORT=9464
```

Endpunkt: `http://0.0.0.0:9464/metrics`

---

## Logs-Konfiguration

### Umgebungsvariablen

| Variable | Typ | Standard | Erlaubte Werte | Beschreibung |
|----------|-----|---------|----------------|--------------|
| `OTEL_LOGS_EXPORTER` | enum | `none` | `none`, `otlp` | Logs-Exporter-Typ |
| `OTEL_EXPORTER_OTLP_LOGS_ENDPOINT` | string | — | URL | OTLP-Endpunkt fuer Logs |
| `LOG_STD_FORMAT` | enum | `auto` | `auto`, `json`, `text` | Stdout-Log-Format |
| `LOG_STD_ENABLE_GCP_FIELDS` | boolean | `false` | `true`/`false` | GCP-kompatible Feldnamen fuer Cloud Logging |

---

## Telemetrie-Steuerung fuer High-Frequency-Routen

| Flag / Env-Variable | Beschreibung | Standard |
|--------------------|-------------|---------|
| `API_DISABLE_ROOT_ROUTE_TELEMETRY` | Root-Route `/` | `true` |
| `API_DISABLE_DEBUG_ROUTE_TELEMETRY` | Debug-Route `/debug` | `true` |
| `API_DISABLE_VERSION_ROUTE_TELEMETRY` | Version-Route `/version` | `true` |
| `API_DISABLE_HEALTH_CHECK_ROUTE_TELEMETRY` | Health-Check `/health` | `true` |
| `PROMETHEUS_DISABLE_ROUTE_TELEMETRY` | Prometheus `/prometheus/metrics` | `true` |

---

## Vollstaendiges Docker-Compose-Beispiel

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

### Jaeger-Integration

```yaml
environment:
  OTEL_TRACES_EXPORTER: "otlp"
  OTEL_EXPORTER_OTLP_TRACES_ENDPOINT: "http://jaeger:4317"
  OTEL_EXPORTER_OTLP_PROTOCOL: "grpc"
```

### Zipkin-Integration

```yaml
environment:
  OTEL_TRACES_EXPORTER: "zipkin"
  OTEL_EXPORTER_OTLP_TRACES_ENDPOINT: "http://zipkin:9411/api/v2/spans"
```

### Sampling (nur 10% der Traces)

```yaml
environment:
  OTEL_TRACES_SAMPLER: "traceidratio"
  OTEL_TRACES_SAMPLER_ARG: "0.1"
```

---

## Hinweise

- `/prometheus/metrics`-Endpunkt ist ab v8.29.0 deprecated — zu OTEL migrieren
- W3C `traceparent`-Header wird ab v8.34.0 auch in Webhook-Callbacks mitgesendet
- Reiche Trace-Attribute (v8.34.0+) erfordern aktuelles Gotenberg-Image

---

Quelle: https://gotenberg.dev/docs/telemetry
