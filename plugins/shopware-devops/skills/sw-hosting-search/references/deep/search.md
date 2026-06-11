# Shopware 6 — Elasticsearch / OpenSearch (Deep Reference)

Sources: `guides/hosting/infrastructure/elasticsearch/elasticsearch-setup.md`, `guides/hosting/infrastructure/elasticsearch/elasticsearch.md`, `guides/hosting/infrastructure/elasticsearch/elasticsearch-debugging.md`

## Requirements

- Supported: OpenSearch 1.0+ or Elasticsearch 7.8+
- Recommended: OpenSearch 2.17.1
- Admin search preview: requires OpenSearch 2.12+ or ES 8.8+
- OpenSearch 3.1 supported since Shopware 6.7.3.1
- Running message queue workers required for indexing

## Install bundle

```bash
composer require shopware/elasticsearch
```

## Environment variables

| Variable | Default | Description |
|---|---|---|
| `OPENSEARCH_URL` | (empty) | Comma-separated ES/OS hosts (e.g., `localhost:9200`) |
| `SHOPWARE_ES_ENABLED` | `0` | Enable ES for storefront search |
| `SHOPWARE_ES_INDEXING_ENABLED` | `0` | Enable indexing to ES |
| `SHOPWARE_ES_INDEX_PREFIX` | (empty) | Index prefix (e.g., `sw`) |
| `SHOPWARE_ES_THROW_EXCEPTION` | `1` | `0` = fallback to MySQL on error (recommended prod); `1` = throw exception |
| `SHOPWARE_ES_NGRAM_MIN_GRAM` | `4` | Min n-gram size |
| `SHOPWARE_ES_NGRAM_MAX_GRAM` | `5` | Max n-gram size |
| `SHOPWARE_ES_EXCLUDE_SOURCE` | `0` | Exclude _source from index |
| `SHOPWARE_ES_INDEXING_BATCH_SIZE` | `100` | Indexing batch size |
| `SHOPWARE_ES_USE_LANGUAGE_ANALYZER` | `1` | Use language-specific analyzers |

### Use cases for separate ENABLED/INDEXING flags

- **Full:** `SHOPWARE_ES_ENABLED=1` + `SHOPWARE_ES_INDEXING_ENABLED=1` — search + indexing
- **Read-only:** `SHOPWARE_ES_ENABLED=1` + `SHOPWARE_ES_INDEXING_ENABLED=0` — search only (e.g., some app servers only read)

## Production .env example

```bash
APP_ENV=prod
OPENSEARCH_URL="elasticsearchhost:9200"
SHOPWARE_ES_ENABLED="1"
SHOPWARE_ES_INDEXING_ENABLED="1"
SHOPWARE_ES_INDEX_PREFIX="sw"
SHOPWARE_ES_THROW_EXCEPTION=0
```

## Indexing commands

```bash
bin/console cache:clear              # clear cache first
bin/console es:index                 # index storefront
bin/console es:create:alias          # create aliases manually (if needed)
bin/console dal:refresh:index --use-queue  # full reindex (all entities, needs workers)
```

## Custom index settings (since 6.4.12.0)

```yaml
# config/packages/elasticsearch.yaml
elasticsearch:
    index_settings:
        number_of_shards: 3
        number_of_replicas: 1
```

Default: 3 shards, 3 replicas.

## N-gram search tuning

Default tokenization of "shopware":
```
["shop", "hopw", "opwa", "pwar", "ware", "shopw", "hopwa", "opwar", "pware"]
```

```dotenv
SHOPWARE_ES_NGRAM_MIN_GRAM=4
SHOPWARE_ES_NGRAM_MAX_GRAM=5
```

After change: full reindex required (`bin/console es:index`).

## Admin search (since 6.4.19.0)

```dotenv
ADMIN_OPENSEARCH_URL=localhost:9200
SHOPWARE_ADMIN_ES_ENABLED=1
SHOPWARE_ADMIN_ES_INDEX_PREFIX=sw-admin
SHOPWARE_ADMIN_ES_INDEXING_BATCH_SIZE=1000
SHOPWARE_ADMIN_ES_REFRESH_INDICES=1
SHOPWARE_ADMIN_ES_THROW_EXCEPTION=1
```

```bash
bin/console es:admin:index
bin/console es:admin:reset
bin/console es:admin:test
```

### Apply OpenSearch globally to Admin API (experimental, since 6.7.9.0)

```dotenv
ENABLE_OPENSEARCH_FOR_ADMIN_API=1
```

Requirements: `ADMIN_OPENSEARCH_URL` set and `SHOPWARE_ADMIN_ES_ENABLED=1`. Then reindex.

## ES/OS error handling

| Setting | Behavior |
|---|---|
| `SHOPWARE_ES_THROW_EXCEPTION=0` | Fallback to MySQL — recommended for production |
| `SHOPWARE_ES_THROW_EXCEPTION=1` | Throw exception — recommended for development |

In large projects: if ES fails and throw_exception=0, MySQL gets overloaded. Set to `1` in production when ES is critical.

## Cluster architecture

### Node types

| Type | Role |
|---|---|
| Master | Manages cluster-wide settings, index CRUD, shard allocation |
| Ingest | Pre-processes documents before indexing |
| Data | Holds shards, executes CRUD/search/aggregations |

### Master nodes

- Minimum 3 master-eligible nodes for quorum (N/2+1)
- Best practice: 5 nodes (3 master-eligible + 2 data-only)
- Prevents split-brain scenario
- Set `cluster.initial_master_nodes` on all master-eligible nodes

### Shards

- **Primary**: holds original data
- **Replica**: copy of primary (increases reliability and read throughput)
- Replicas never co-locate with their primary on the same node

### JVM configuration

Only modify if you know what you're doing. Most hosting providers provide suitable defaults.

## Configuration file (elasticsearch.yml)

Key settings:
- `cluster.name` — cluster identifier
- `node.name` — node identifier
- `discovery.seed_hosts` — nodes that know each other
- `node.master`, `node.data`, `node.ingest` — node roles
- `network.host` — listen address

## Search configuration note

Shopware's search configuration in Admin has no effect when using Elasticsearch.
To configure searchable fields with ES, install the [Advanced Search](https://docs.shopware.com/en/shopware-6-en/extensions/advanced-search) extension.

## Staging isolation

Always set a unique `SHOPWARE_ES_INDEX_PREFIX` per environment to avoid production/staging index conflicts.
The staging mode (`system:setup:staging`) checks that no ES indices exist and warns if they do.
