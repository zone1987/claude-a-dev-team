# sw-core-entity-reference

Statisch generierte Referenz aller **312** Shopware-6-Core-DAL-Entity-Definitionen aus `src/` (trunk).

- 218 EntityDefinition [E]
- 40 MappingEntityDefinition [M]
- 54 EntityTranslationDefinition [T]
- 3 ausgeschlossen (kein DAL-Entity: DataValidationDefinition, LineItemGroupDefinition, ConsentDefinition)

## Dateien

| Datei | Inhalt |
|-------|--------|
| [references/deep/core-entities.json](references/deep/core-entities.json) | Maschinenlesbarer Vollbaum — alle Entities mit fields[], associations[], translations[], meta |
| [CORE-ENTITY-REFERENCE-CORE-ENTITIES-INDEX.md](CORE-ENTITY-REFERENCE-CORE-ENTITIES-INDEX.md) | Index aller 312 Entities (alphabetisch) + Domain-Übersicht |
| [CORE-ENTITY-REFERENCE-CORE-ENTITIES-CONTENT.md](CORE-ENTITY-REFERENCE-CORE-ENTITIES-CONTENT.md) | Domäne Content (Product, Category, CMS, Media, ...) |
| [CORE-ENTITY-REFERENCE-CORE-ENTITIES-CHECKOUT.md](CORE-ENTITY-REFERENCE-CORE-ENTITIES-CHECKOUT.md) | Domäne Checkout (Order, Customer, Cart, Payment, Shipping, Promotion) |
| [CORE-ENTITY-REFERENCE-CORE-ENTITIES-SYSTEM.md](CORE-ENTITY-REFERENCE-CORE-ENTITIES-SYSTEM.md) | Domäne System (SalesChannel, Tax, Currency, Country, Language, ...) |
| [CORE-ENTITY-REFERENCE-CORE-ENTITIES-FRAMEWORK.md](CORE-ENTITY-REFERENCE-CORE-ENTITIES-FRAMEWORK.md) | Domäne Framework (App, Plugin, Webhook, DAL, ...) |
| [CORE-ENTITY-REFERENCE-CORE-ENTITIES-CORE.md](CORE-ENTITY-REFERENCE-CORE-ENTITIES-CORE.md) | Core-interne Entities (Core/Framework, Core/System, Core/Checkout Subpfade) |
| [CORE-ENTITY-REFERENCE-CORE-ENTITIES-STOREFRONT.md](CORE-ENTITY-REFERENCE-CORE-ENTITIES-STOREFRONT.md) | Domäne Storefront (Theme, ...) |
| [CORE-ENTITY-REFERENCE-CORE-ENTITIES-ADMINISTRATION.md](CORE-ENTITY-REFERENCE-CORE-ENTITIES-ADMINISTRATION.md) | Domäne Administration (Notification, Snippet) |
| [CORE-ENTITY-REFERENCE-CORE-ENTITIES-ELASTICSEARCH.md](CORE-ENTITY-REFERENCE-CORE-ENTITIES-ELASTICSEARCH.md) | Elasticsearch-Definitions |

## Nutzung

```
# Schnelle Feldabfrage via JSON (jq):
cat references/deep/core-entities.json | jq '.entities[] | select(.entity == "product") | .fields[]'

# Alle Entities einer Domäne:
cat references/deep/core-entities.json | jq '.entities[] | select(.domain | startswith("Content")) | .entity'

# Associations für order:
cat references/deep/core-entities.json | jq '.entities[] | select(.entity == "order") | .associations[]'
```

## JSON-Struktur (core-entities.json)

```json
{
  "meta": {
    "total": 312,
    "by_kind": {"Entity": 218, "Mapping": 40, "Translation": 54},
    "generated": "2026-06-12"
  },
  "entities": [
    {
      "entity": "product",
      "class": "ProductDefinition",
      "file": "Core/Content/Product/ProductDefinition.php",
      "kind": "Entity",
      "domain": "Content/Product",
      "entity_class": "ProductEntity",
      "collection_class": "ProductCollection",
      "parent_definition": "",
      "defaults": {"isCloseout": false, "minPurchase": 1, "type": "physical"},
      "fields": [
        {"type": "IdField", "storage": "id", "property": "id", "flags": ["ApiAware", "PrimaryKey", "Required"]},
        {"type": "FkField", "storage": "product_manufacturer_id", "property": "manufacturerId", "flags": ["ApiAware", "Inherited"], "references": "ProductManufacturerDefinition"},
        {"type": "TranslatedField", "storage": "", "property": "name", "flags": ["ApiAware", "SearchRanking"]}
      ],
      "associations": [
        {"property": "manufacturer", "type": "ManyToOne", "field_class": "ManyToOneAssociationField", "target": "ProductManufacturerDefinition", "local_field": "product_manufacturer_id", "reference_field": "id"},
        {"property": "translations", "type": "OneToMany", "field_class": "TranslationsAssociationField", "target": "ProductTranslationDefinition"}
      ],
      "translated_fields": ["metaDescription", "name", "keywords", "description", "customSearchKeywords", "packUnit", "packUnitPlural", "customFields"]
    }
  ]
}
```

## Abgrenzung zu sw-entity-catalog

| | sw-core-entity-reference | sw-entity-catalog |
|---|---|---|
| **Scope** | Shopware Core (trunk) | Projekt-eigene + Custom Entities |
| **Quelle** | Statisch generiert aus `src/` | Laufende DB / DefinitionRegistry |
| **Custom Entities** | Nein | Ja |
| **App Entities** | Nein | Ja |
| **Aktuell** | Bei Core-Updates neu generieren | Immer aktuell (DB) |
