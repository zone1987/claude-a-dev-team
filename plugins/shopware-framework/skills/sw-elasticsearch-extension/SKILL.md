---
name: sw-elasticsearch-extension
description: >
  Shopware Elasticsearch eigene Entities/Felder erweitern. Aktiviere wenn: eigene Entity in Elasticsearch indizieren,
  AbstractElasticsearchDefinition implementieren, eigene Felder in ES-Index, Custom Fields Mapping ES,
  ElasticsearchCustomFieldsMappingEvent, ElasticsearchFieldBuilder::translated, Produkt-Index erweitern,
  AbstractAdminIndexer eigene Admin-Suche, getMapping Shopware Elasticsearch.
---

# sw-elasticsearch-extension

Eigene Entities/Felder in den Shopware-Elasticsearch-Index bringen.

## Eigene Entity (Storefront) indizieren
`AbstractElasticsearchDefinition` implementieren (`getMapping()`, `fetch()`), via `shopware.es.definition`-Tag
registrieren — definiert Mapping + Daten je Dokument.

## Felder zu bestehendem Index (z.B. product) hinzufügen
- Mapping erweitern über den passenden Mapping-Event bzw. eine Definition-Extension.
- **Custom Fields**: auf `ElasticsearchCustomFieldsMappingEvent` hören und Feld-Mapping ergänzen.
- Übersetzte Felder über `ElasticsearchFieldBuilder::translated(...)`.

## Admin-Suche erweitern
`AbstractAdminIndexer` implementieren (eigene Entity in der Admin-ES-Suche). Alle 18 Core-Admin-Entities haben
bereits fertige Indexer.

Nach Mapping-Änderungen Index neu aufbauen (`bin/console es:index`). Grundlagen/Aktivierung: `sw-elasticsearch`.

→ Vollständige Muster (Definition, FieldMapping, CustomFields, AdminIndexer, Beispiele): [references/deep/extension-patterns.md](references/deep/extension-patterns.md)
