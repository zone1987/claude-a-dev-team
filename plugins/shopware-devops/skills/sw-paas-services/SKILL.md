---
name: sw-paas-services
description: >
  Shopware PaaS Native und PaaS Services: MySQL/MariaDB, Redis, OpenSearch,
  Elasticsearch, RabbitMQ, S3 Object Storage. Konfiguration, Aktivierung,
  Verbindung, Indexierung. Trigger: "paas datenbank verbinden", "paas opensearch
  aktivieren", "paas redis", "paas rabbitmq deaktivieren", "paas elasticsearch",
  "paas mysql cluster", "paas object storage s3", "paas services.yaml",
  "opensearch paas konfigurieren", "paas db tunnel", "paas object storage".
---

# Shopware PaaS — Services

## PaaS Native: Managed MySQL

- Automatische Backups, High Availability, Encryption at rest/transit
- Kein direkter öffentlicher Zugang — nur via CLI-Tunnel

```bash
sw-paas open service --service database --port 3306
# Hinweis: NAT-inkompatibel (VM/WSL → Host/Mirrored Modus)
```

## PaaS Native: OpenSearch

In `application.yaml`:
```yaml
services:
  opensearch:
    enabled: true
```

```bash
sw-paas application update
sw-paas exec --new
bin/console dal:refresh:index --use-queue
```

## PaaS Native: Object Storage (S3)

- 2 Buckets per Application: public + private
- Konfiguriert in `config/packages/operator.yaml` (via k8s-meta)
- Kein direkter externer Zugriff — nur via Container, Admin, API, exec-Session
- Build-Phase hat keinen Zugriff auf Filesystem

## PaaS (Platform.sh): Elasticsearch/OpenSearch

In `.platform/services.yaml`:
```yaml
elasticsearch:
  type: opensearch:2
  disk: 256
```
In `applications.yaml` Relationship hinzufügen, dann `SHOPWARE_ES_ENABLED=1` setzen.

## PaaS (Platform.sh): RabbitMQ

Standard aktiviert — deaktivieren:
```yaml
# .platform/services.yaml
#rabbitmq:
#  type: rabbitmq:3.8
#  disk: 1024
```
Relationship in `applications.yaml` ebenfalls auskommentieren.

## Vertiefung

[references/deep/services.md](references/deep/services.md)
