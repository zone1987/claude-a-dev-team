---
name: sw-hosting-observability
description: >
  Shopware 6 Observability — Logging, Monolog, OpenTelemetry, Grafana, Profiling.
  Triggers: "logging", "monolog", "opentelemetry", "grafana", "tracing", "metrics",
  "observability", "profiling", "Logging konfigurieren", "OpenTelemetry einrichten",
  "Tideways", "Blackfire", "Datadog", "Tempo", "Loki", "Prometheus", "otel"
---

# Shopware Hosting — Observability

Refer to `references/deep/observability.md` for full configuration examples and Grafana stack setup.

## Logging (Monolog)

```yaml
# config/packages/prod/monolog.yaml
monolog:
    handlers:
        main:
            level: error
            buffer_size: 30
        business_event_handler_buffer:
            level: error   # set to 'info' to log all flow events
```

Log files: `var/log/` (or stdout when `shopware/docker` package is installed).

## OpenTelemetry

```bash
composer require shopware/opentelemetry
# also install: open-telemetry/transport-grpc open-telemetry/exporter-otlp
```

PHP extension required: `ext-opentelemetry` (optionally `ext-grpc`).

```dotenv
OTEL_PHP_AUTOLOAD_ENABLED=true
OTEL_SERVICE_NAME=shopware
OTEL_TRACES_EXPORTER=otlp
OTEL_LOGS_EXPORTER=otlp
OTEL_METRICS_EXPORTER=otlp
OTEL_EXPORTER_OTLP_PROTOCOL=grpc
OTEL_EXPORTER_OTLP_ENDPOINT=http://localhost:4317
```

Available traces: Controller, Symfony HTTP Client, MySQL Queries.

## Grafana Stack (self-hosted)
- Grafana (Dashboard)
- Loki (Logs)
- Prometheus (Metrics)
- Tempo (Traces)
- OpenTelemetry Collector

Example stack: https://github.com/shopware/opentelemetry/tree/main/docker

## Profiling tools
- [Blackfire](https://www.blackfire.io/)
- [Tideways](https://tideways.com/)
- [Datadog](https://www.datadoghq.com/)

Install custom PHP extension in Docker:
```dockerfile
USER root
RUN install-php-extensions tideways
USER www-data
```

See also: `sw-hosting-performance` (log level tuning), `sw-hosting-env-config`.

Full reference: `references/deep/observability.md`
