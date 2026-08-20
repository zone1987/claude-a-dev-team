# Shopware PaaS — Services

## PaaS Native: managed MySQL

- Automatic backups, high availability, encryption at rest/in transit
- No direct public access — only via the CLI tunnel

```bash
sw-paas open service --service database --port 3306
# Note: incompatible with NAT (VM/WSL → Host/Mirrored mode)
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

## PaaS Native: object storage (S3)

- 2 buckets per application: public + private
- Configured in `config/packages/operator.yaml` (via k8s-meta)
- No direct external access — only via container, admin, API, exec session
- The build phase has no filesystem access

## PaaS (Platform.sh): Elasticsearch/OpenSearch

In `.platform/services.yaml`:
```yaml
elasticsearch:
  type: opensearch:2
  disk: 256
```
Add the relationship in `applications.yaml`, then set `SHOPWARE_ES_ENABLED=1`.

## PaaS (Platform.sh): RabbitMQ

Enabled by default — to disable:
```yaml
# .platform/services.yaml
#rabbitmq:
#  type: rabbitmq:3.8
#  disk: 1024
```
Comment out the relationship in `applications.yaml` as well.

## Deep dive

[SERVICES-DETAIL.md](SERVICES-DETAIL.md)
