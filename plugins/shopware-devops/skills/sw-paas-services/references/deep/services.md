# Shopware PaaS — Services (Deep Reference)

Quellen: `products/paas/shopware/resources/databases.md`,
`products/paas/shopware/resources/object-storage.md`,
`products/paas/shopware/guides/opensearch.md`,
`products/paas/shopware-paas/elasticsearch.md`,
`products/paas/shopware-paas/rabbitmq.md`

---

## PaaS Native: Managed MySQL

### Features (Plattformseitig verwaltet)

- Automatische Backups und Recovery
- High Availability
- Performance Monitoring und Metriken
- Ressourcen-Skalierung (CPU, RAM, Storage)
- Automatische Encryption (at rest und in transit)

### Verbindung via CLI-Tunnel

```bash
sw-paas open service --service database --port 3306
```

**Bekannte Einschränkung:** mTLS-Tunnel ist inkompatibel mit NAT.
In VM oder WSL: Netzwerk-Modus auf `Host` oder `Mirrored` stellen.

Kein direkter öffentlicher Datenbankzugriff möglich.

---

## PaaS Native: OpenSearch

### Aktivierung

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

### Indexierung nach Aktivierung

```bash
sw-paas exec --new
# Im Container:
bin/console dal:refresh:index --use-queue
```

### OpenSearch und Cloning

Nach Cloning einer Application mit OpenSearch muss reindexiert werden:

```bash
sw-paas exec --new
bin/console dal:refresh:index --use-queue
```

### OpenSearch im Grafana

SSO ist nicht verfügbar. Zugang über:
```bash
sw-paas open grafana
```

---

## PaaS Native: S3 Object Storage

### Konfiguration

Jede Application erhält automatisch **2 S3-kompatible Buckets**:
- **Public Bucket**: Öffentlich zugängliche Medien
- **Private Bucket**: Nicht-öffentliche Dateien

Konfiguration via `config/packages/operator.yaml` (durch k8s-meta installiert):
- Filesystem: public, private, theme, sitemap → alle S3-backed

### Zugriff

Object Storage ist **nicht direkt von außen** erreichbar.
Zugriff nur möglich über:

- Shopware Admin (Media Manager)
- Shopware API
- PHP-Script in einem Container mit Filesystem-Zugriff

### Kontexte mit Filesystem-Zugriff

| Kontext | Filesystem verfügbar |
|---------|---------------------|
| `storefront` | Ja |
| `admin` | Ja |
| `worker` | Ja |
| `exec`-Sessions | Ja |
| `migration`-Schritt | Ja |
| `setup`-Schritt | Ja |
| `build`-Schritt | **Nein** |

### Plugin-Kompatibilität

Third-Party-Plugins müssen S3-kompatiblen Storage unterstützen.
Bei Inkompatibilität: Plugin-Anbieter kontaktieren.

---

## PaaS (Platform.sh): Elasticsearch / OpenSearch

### Aktivierung in services.yaml

```yaml
# .platform/services.yaml
elasticsearch:
  type: opensearch:2
  disk: 256
```

### Relationship in applications.yaml hinzufügen

```yaml
# .platform/applications.yaml
relationships:
  elasticsearch: "elasticsearch:opensearch"
```

### Umgebungsvariablen (automatisch gesetzt)

Nach Aktivierung stehen bereit:
- `SHOPWARE_ES_HOSTS` (via paas-meta Package)
- `ELASTICSEARCH_URL`
- `ELASTICSEARCH_HOST`
- `ELASTICSEARCH_PORT`
- `OPENSEARCH_URL`
- `ADMIN_OPENSEARCH_URL`

### Elasticsearch aktivieren

```bash
# In platformsh-env.php auskommentieren ODER in variables-Sektion setzen:
SHOPWARE_ES_ENABLED=1
```

### Shopware für Elasticsearch vorbereiten

Siehe: [Elasticsearch Setup](https://developer.shopware.com/docs/guides/hosting/infrastructure/elasticsearch/elasticsearch-setup#prepare-shopware-for-elasticsearch)

---

## PaaS (Platform.sh): RabbitMQ

Standard in Template **aktiviert**.

### Deaktivieren (Fallback auf SQL-Queue)

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

### Umgebungsvariablen (wenn aktiviert)

| Variable | Wert |
|----------|------|
| `MESSENGER_TRANSPORT_DSN` | `amqp://guest:guest@rabbitmq.internal:5672/%2f/messages` |
| `MESSENGER_TRANSPORT_DSN_PREFIX` | `amqp://guest:guest@rabbitmq.internal:5672/%2f/` |

---

## PaaS (Platform.sh): Redis

Typisch zwei Redis-Instanzen:

### Cache Redis

```yaml
# services.yaml
cacheredis:
  type: redis:7.0
```

Umgebungsvariablen: `CACHE_DSN`, `CACHE_URL` = `redis://rediscache.internal:6379`

### Session Redis

```yaml
redissession:
  type: redis:7.0
```

Umgebungsvariablen: `SESSION_REDIS_HOST`, `SESSION_REDIS_PORT`, `SESSION_REDIS_URL`

---

## PaaS (Platform.sh): Network Storage (Shared Filesystem)

```yaml
# services.yaml
fileshare:
  type: network-storage:2.0
  disk: 5000
```

Geteilt zwischen allen App-Instanzen. Verwendet für:
- `/public/media`
- `/public/thumbnail`
- `/public/bundles`
- `/public/sitemap`

Local Mounts (nicht geteilt):
- `/var/cache` (Symfony-Cache)
- `/var/log`
