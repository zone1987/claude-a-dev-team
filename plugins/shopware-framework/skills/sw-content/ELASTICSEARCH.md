# sw-elasticsearch

Das `Shopware\Elasticsearch`-Bundle integriert OpenSearch/Elasticsearch als Such-/Aggregationsbackend
(Client: `opensearch-project/opensearch-php`). **Storefront-** und **Admin-Suche** haben getrennte Index-Sätze
mit eigenen Env-Konfigs.

```bash
# Storefront-Suche
SHOPWARE_ES_ENABLED=1
SHOPWARE_ES_HOSTS=elasticsearch:9200
SHOPWARE_ES_INDEXING_ENABLED=1
# Admin-Suche
ADMIN_ES_ENABLED=1
ADMIN_ES_HOSTS=elasticsearch:9200
```

```bash
bin/console es:index            # Index (neu) aufbauen, blue-green via Alias
bin/console es:index:cleanup    # alte Indizes entfernen
bin/console dal:refresh:index   # DAL-Indexer (Voraussetzung für ES-Daten)
```

Indizierung läuft asynchron über Symfony Messenger. Eigene Entities/Felder in den Index bringen: `sw-elasticsearch-extension`.

→ Architektur, Registry, Mapping-System, Befehle, Troubleshooting: [ELASTICSEARCH-ARCHITECTURE.md](ELASTICSEARCH-ARCHITECTURE.md)
