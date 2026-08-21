# sw-elasticsearch-extension

Getting custom entities/fields into the Shopware Elasticsearch index.

## Indexing a custom entity (storefront)
Implement `AbstractElasticsearchDefinition` (`getMapping()`, `fetch()`), register it via the `shopware.es.definition`
tag — it defines the mapping plus the data per document.

## Adding fields to an existing index (e.g. product)
- Extend the mapping via the matching mapping event or a definition extension.
- **Custom fields**: listen to `ElasticsearchCustomFieldsMappingEvent` and add the field mapping.
- Translated fields via `ElasticsearchFieldBuilder::translated(...)`.

## Extending the admin search
Implement `AbstractAdminIndexer` (custom entity in the admin ES search). All 18 core admin entities already have
ready-made indexers.

Rebuild the index after mapping changes (`bin/console es:index`). Basics/activation: `sw-elasticsearch`.

→ Complete patterns (definition, field mapping, custom fields, admin indexer, examples): [ELASTICSEARCH-EXTENSION-EXTENSION-PATTERNS.md](ELASTICSEARCH-EXTENSION-EXTENSION-PATTERNS.md)
