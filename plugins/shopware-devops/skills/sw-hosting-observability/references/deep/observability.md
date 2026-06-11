# Shopware 6 — Observability (Deep Reference)

Sources: `guides/hosting/configurations/observability/logging.md`, `guides/hosting/configurations/observability/opentelemetry.md`, `guides/hosting/configurations/observability/profiling.md`

## Logging (Monolog)

Log files: `var/log/` — with `shopware/docker` package installed: stdout instead.

### Default config location

```
config/packages/prod/monolog.yaml
```

### Log levels

| Level | Description |
|---|---|
| `DEBUG` | Detailed debug information |
| `INFO` | Interesting events (user login, SQL logs) |
| `NOTICE` | Normal but significant events |
| `WARNING` | Unusual occurrences (deprecated API usage) |
| `ERROR` | Runtime errors, should be monitored |
| `CRITICAL` | Component unavailable, unexpected exception |
| `ALERT` | Website down, DB unavailable — trigger alerts |
| `EMERGENCY` | System unusable |

### Production config

```yaml
# config/packages/prod/monolog.yaml
monolog:
    handlers:
        main:
            level: error        # log only errors and above
            buffer_size: 30     # prevent memory overflow in long-lived jobs
        business_event_handler_buffer:
            level: error        # set to 'info' to log all successful flow events
```

**Note:** Setting `business_event_handler_buffer` to `error` disables logging of flow activities that succeed (only failures are logged). This improves performance.

### Log all sent emails and flow events

```yaml
monolog:
    handlers:
        business_event_handler_buffer:
            level: info
```

**Performance impact:** Setting to `info` costs performance.

## OpenTelemetry

### Requirements

- `ext-opentelemetry` (PHP extension)
- `ext-grpc` (optional, for gRPC transport)

### Installation

```bash
composer require shopware/opentelemetry
# Creates config/packages/prod/opentelemetry.yaml via Symfony Flex

# For gRPC transport:
composer require open-telemetry/transport-grpc open-telemetry/exporter-otlp
```

### Environment variables

```dotenv
# Basic
OTEL_PHP_AUTOLOAD_ENABLED=true
OTEL_SERVICE_NAME=shopware

# Exporter (gRPC to OTLP collector)
OTEL_TRACES_EXPORTER=otlp
OTEL_LOGS_EXPORTER=otlp
OTEL_METRICS_EXPORTER=otlp
OTEL_EXPORTER_OTLP_PROTOCOL=grpc
OTEL_EXPORTER_OTLP_ENDPOINT=http://localhost:4317
```

See all env vars: https://opentelemetry.io/docs/instrumentation/php/sdk/#configuration

### Available instrumentation

The Shopware OTel bundle collects:
- Controller spans
- Symfony HTTP Client spans
- MySQL query spans

### Grafana stack (self-hosted)

Components:
- **Grafana** — Dashboard and visualization
- **Loki** — Log storage
- **Prometheus** — Metrics storage
- **Tempo** — Trace storage
- **OpenTelemetry Collector** — Collects and batches all signals

Example stack: https://github.com/shopware/opentelemetry/tree/main/docker

Features in pre-configured Grafana:
- Navigate from logs to traces
- Navigate from traces to logs
- Unified observability view

### Docker: install custom PHP profiling extension

```dockerfile
USER root
RUN install-php-extensions tideways
USER www-data
```

## Profiling tools (APM)

| Tool | Type | Notes |
|---|---|---|
| [Blackfire](https://www.blackfire.io/) | Profiler + APM | Code-level profiling |
| [Tideways](https://tideways.com/) | APM | PHP-focused monitoring |
| [Datadog](https://www.datadoghq.com/) | APM + monitoring | Full-stack observability |
| [Elastic](https://www.elastic.co/) | APM + logging | Open-source-friendly |

All require a PHP extension and are recommended for production performance monitoring.

## Log rotation

When logs are written to `var/log/`, set up OS-level log rotation (logrotate on Linux):

```
/var/www/html/var/log/*.log {
    daily
    rotate 14
    compress
    missingok
    notifempty
    create 0640 www-data www-data
}
```
