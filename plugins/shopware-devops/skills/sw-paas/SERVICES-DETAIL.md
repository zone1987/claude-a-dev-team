# Shopware PaaS — Services (Deep Reference)

Sources: `products/paas/shopware/resources/databases.md`,
`products/paas/shopware/resources/object-storage.md`,
`products/paas/shopware/guides/opensearch.md`,
`products/paas/shopware-paas/elasticsearch.md`,
`products/paas/shopware-paas/rabbitmq.md`

---

## Contents

- [PaaS Native: Managed MySQL](#paas-native-managed-mysql)
- [PaaS Native: OpenSearch](#paas-native-opensearch)
- [PaaS Native: S3 Object Storage](#paas-native-s3-object-storage)
- [PaaS (Platform.sh): Elasticsearch / OpenSearch](#paas-platformsh-elasticsearch-opensearch)
- [PaaS (Platform.sh): RabbitMQ](#paas-platformsh-rabbitmq)
- [PaaS (Platform.sh): Redis](#paas-platformsh-redis)
- [PaaS (Platform.sh): Network Storage (Shared Filesystem)](#paas-platformsh-network-storage-shared-filesystem)

## PaaS Native: Managed MySQL

### Features (managed by the platform)

- Automatic backups and recovery
- High availability
- Performance monitoring and metrics
- Resource scaling (CPU, RAM, storage)
- Automatic encryption (at rest and in transit)

### Connecting via the CLI tunnel

```bash
sw-paas open service --service database --port 3306
```

**Known limitation:** the mTLS tunnel is incompatible with NAT.
In a VM or WSL: set the network mode to `Host` or `Mirrored`.

No direct public database access is possible.

---

## PaaS Native: OpenSearch

### Activation

In `application.yaml`:

```yaml
services:
  opensearch:
    enabled: true
```

```bash
git add application.yaml
git commit -m "Enable OpenSearch"
git push

sw-paas application update
```

### Indexing after activation

```bash
sw-paas exec --new
# Inside the container:
bin/console dal:refresh:index --use-queue
```

### OpenSearch and cloning

After cloning an application with OpenSearch, a reindex is required:

```bash
sw-paas exec --new
bin/console dal:refresh:index --use-queue
```

### OpenSearch in Grafana

SSO is not available. Access via:
```bash
sw-paas open grafana
```

---

## PaaS Native: S3 Object Storage

### Configuration

Every application automatically receives **2 S3-compatible buckets**:
- **Public bucket**: publicly accessible media
- **Private bucket**: non-public files

Configuration via `config/packages/operator.yaml` (installed by k8s-meta):
- Filesystem: public, private, theme, sitemap → all S3-backed

### Access

Object storage is **not reachable directly from outside**.
Access is only possible through:

- Shopware Admin (Media Manager)
- Shopware API
- PHP script in a container with filesystem access

### Contexts with filesystem access

| Context | Filesystem available |
|---------|---------------------|
| `storefront` | Yes |
| `admin` | Yes |
| `worker` | Yes |
| `exec` sessions | Yes |
| `migration` step | Yes |
| `setup` step | Yes |
| `build` step | **No** |

### Plugin compatibility

Third-party plugins must support S3-compatible storage.
In case of incompatibility: contact the plugin vendor.

---

## PaaS (Platform.sh): Elasticsearch / OpenSearch

### Activation in services.yaml

```yaml
# .platform/services.yaml
elasticsearch:
  type: opensearch:2
  disk: 256
```

### Add the relationship in applications.yaml

```yaml
# .platform/applications.yaml
relationships:
  elasticsearch: "elasticsearch:opensearch"
```

### Environment variables (set automatically)

After activation the following are available:
- `SHOPWARE_ES_HOSTS` (via the paas-meta package)
- `ELASTICSEARCH_URL`
- `ELASTICSEARCH_HOST`
- `ELASTICSEARCH_PORT`
- `OPENSEARCH_URL`
- `ADMIN_OPENSEARCH_URL`

### Enabling Elasticsearch

```bash
# Uncomment in platformsh-env.php OR set in the variables section:
SHOPWARE_ES_ENABLED=1
```

### Preparing Shopware for Elasticsearch

See: [Elasticsearch Setup](https://developer.shopware.com/docs/guides/hosting/infrastructure/elasticsearch/elasticsearch-setup#prepare-shopware-for-elasticsearch)

---

## PaaS (Platform.sh): RabbitMQ

**Enabled** by default in the template.

### Disabling (fallback to the SQL queue)

```yaml
# .platform/services.yaml
#rabbitmq:
#  type: rabbitmq:3.8
#  disk: 1024
```

```yaml
# .platform/applications.yaml
#relationships:
#  rabbitmqqueue: "rabbitmq:rabbitmq"
```

```bash
git add .
git commit -m "Disable RabbitMQ, use SQL queue"
git push shopware main
```

### Environment variables (when enabled)

| Variable | Value |
|----------|------|
| `MESSENGER_TRANSPORT_DSN` | `amqp://guest:guest@rabbitmq.internal:5672/%2f/messages` |
| `MESSENGER_TRANSPORT_DSN_PREFIX` | `amqp://guest:guest@rabbitmq.internal:5672/%2f/` |

---

## PaaS (Platform.sh): Redis

Typically two Redis instances:

### Cache Redis

```yaml
# services.yaml
cacheredis:
  type: redis:7.0
```

Environment variables: `CACHE_DSN`, `CACHE_URL` = `redis://rediscache.internal:6379`

### Session Redis

```yaml
redissession:
  type: redis:7.0
```

Environment variables: `SESSION_REDIS_HOST`, `SESSION_REDIS_PORT`, `SESSION_REDIS_URL`

---

## PaaS (Platform.sh): Network Storage (Shared Filesystem)

```yaml
# services.yaml
fileshare:
  type: network-storage:2.0
  disk: 5000
```

Shared between all app instances. Used for:
- `/public/media`
- `/public/thumbnail`
- `/public/bundles`
- `/public/sitemap`

Local mounts (not shared):
- `/var/cache` (Symfony cache)
- `/var/log`
