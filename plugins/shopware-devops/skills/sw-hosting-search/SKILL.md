---
name: sw-hosting-search
description: >
  Shopware 6 Elasticsearch / OpenSearch Setup, Indexing, Cluster, N-Gram, Admin Search.
  Triggers: "elasticsearch setup", "opensearch setup", "es:index", "search indexing",
  "elasticsearch cluster", "opensearch cluster", "SHOPWARE_ES_ENABLED", "ES index prefix",
  "Elasticsearch einrichten", "OpenSearch konfigurieren", "Suche indexieren",
  "admin elasticsearch", "n-gram search", "es:admin:index"
---

# Shopware Hosting — Elasticsearch / OpenSearch

Refer to `references/deep/search.md` for cluster architecture details, shard config, and debugging.

## Environment variables

```dotenv
OPENSEARCH_URL=localhost:9200
SHOPWARE_ES_ENABLED=1
SHOPWARE_ES_INDEXING_ENABLED=1
SHOPWARE_ES_INDEX_PREFIX=sw
SHOPWARE_ES_THROW_EXCEPTION=0     # 0 = fallback to MySQL on error (recommended prod)
```

## Install bundle

```bash
composer require shopware/elasticsearch
```

## Indexing

```bash
bin/console cache:clear
bin/console es:index                               # index storefront
bin/console dal:refresh:index --use-queue          # full reindex (use with queue workers!)
bin/console es:create:alias                        # manual alias creation if needed
```

## Custom shard/replica config

```yaml
# config/packages/elasticsearch.yaml
elasticsearch:
    index_settings:
        number_of_shards: 3
        number_of_replicas: 1
```

## Admin search (since 6.4.19)

```dotenv
ADMIN_OPENSEARCH_URL=localhost:9200
SHOPWARE_ADMIN_ES_ENABLED=1
SHOPWARE_ADMIN_ES_INDEX_PREFIX=sw-admin
SHOPWARE_ADMIN_ES_INDEXING_BATCH_SIZE=1000
```

```bash
bin/console es:admin:index
```

## N-gram tuning

```dotenv
SHOPWARE_ES_NGRAM_MIN_GRAM=4
SHOPWARE_ES_NGRAM_MAX_GRAM=5
```

Reindex required after change: `bin/console es:index`

## Staging isolation
Set `SHOPWARE_ES_INDEX_PREFIX` to a unique value per environment to avoid conflicts.

See also: `sw-hosting-worker-cron` (message queue for indexing), `sw-hosting-performance`.

Full reference: `references/deep/search.md`
