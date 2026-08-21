# sw-elasticsearch

The `Shopware\Elasticsearch` bundle integrates OpenSearch/Elasticsearch as the search/aggregation backend
(client: `opensearch-project/opensearch-php`). **Storefront** and **admin search** have separate index sets
with their own env configs.

```bash
# Storefront search
SHOPWARE_ES_ENABLED=1
SHOPWARE_ES_HOSTS=elasticsearch:9200
SHOPWARE_ES_INDEXING_ENABLED=1
# Admin search
ADMIN_ES_ENABLED=1
ADMIN_ES_HOSTS=elasticsearch:9200
```

```bash
bin/console es:index            # (re)build index, blue-green via alias
bin/console es:index:cleanup    # remove old indices
bin/console dal:refresh:index   # DAL indexer (prerequisite for ES data)
```

Indexing runs asynchronously via Symfony Messenger. To get custom entities/fields into the index: `sw-elasticsearch-extension`.

→ Architecture, registry, mapping system, commands, troubleshooting: [ELASTICSEARCH-ARCHITECTURE.md](ELASTICSEARCH-ARCHITECTURE.md)
