# sw-core-entity-reference

Statically generated reference of all **312** Shopware 6 core DAL entity definitions from `src/` (trunk).

- 218 EntityDefinition [E]
- 40 MappingEntityDefinition [M]
- 54 EntityTranslationDefinition [T]
- 3 excluded (not a DAL entity: DataValidationDefinition, LineItemGroupDefinition, ConsentDefinition)

## Files

| File | Content |
|-------|--------|
| [references/deep/core-entities.json](references/deep/core-entities.json) | Machine-readable full tree — all entities with fields[], associations[], translations[], meta |
| [CORE-ENTITY-REFERENCE-CORE-ENTITIES-INDEX.md](CORE-ENTITY-REFERENCE-CORE-ENTITIES-INDEX.md) | Index of all 312 entities (alphabetical) + domain overview |
| [CORE-ENTITY-REFERENCE-CORE-ENTITIES-CONTENT.md](CORE-ENTITY-REFERENCE-CORE-ENTITIES-CONTENT.md) | Content domain (Product, Category, CMS, Media, ...) |
| [CORE-ENTITY-REFERENCE-CORE-ENTITIES-CHECKOUT.md](CORE-ENTITY-REFERENCE-CORE-ENTITIES-CHECKOUT.md) | Checkout domain (Order, Customer, Cart, Payment, Shipping, Promotion) |
| [CORE-ENTITY-REFERENCE-CORE-ENTITIES-SYSTEM.md](CORE-ENTITY-REFERENCE-CORE-ENTITIES-SYSTEM.md) | System domain (SalesChannel, Tax, Currency, Country, Language, ...) |
| [CORE-ENTITY-REFERENCE-CORE-ENTITIES-FRAMEWORK.md](CORE-ENTITY-REFERENCE-CORE-ENTITIES-FRAMEWORK.md) | Framework domain (App, Plugin, Webhook, DAL, ...) |
| [CORE-ENTITY-REFERENCE-CORE-ENTITIES-CORE.md](CORE-ENTITY-REFERENCE-CORE-ENTITIES-CORE.md) | Core-internal entities (Core/Framework, Core/System, Core/Checkout subpaths) |
| [CORE-ENTITY-REFERENCE-CORE-ENTITIES-STOREFRONT.md](CORE-ENTITY-REFERENCE-CORE-ENTITIES-STOREFRONT.md) | Storefront domain (Theme, ...) |
| [CORE-ENTITY-REFERENCE-CORE-ENTITIES-ADMINISTRATION.md](CORE-ENTITY-REFERENCE-CORE-ENTITIES-ADMINISTRATION.md) | Administration domain (Notification, Snippet) |
| [CORE-ENTITY-REFERENCE-CORE-ENTITIES-ELASTICSEARCH.md](CORE-ENTITY-REFERENCE-CORE-ENTITIES-ELASTICSEARCH.md) | Elasticsearch definitions |

## Usage

```
# Quick field lookup via JSON (jq):
cat references/deep/core-entities.json | jq '.entities[] | select(.entity == "product") | .fields[]'

# All entities of a domain:
cat references/deep/core-entities.json | jq '.entities[] | select(.domain | startswith("Content")) | .entity'

# Associations for order:
cat references/deep/core-entities.json | jq '.entities[] | select(.entity == "order") | .associations[]'
```

## JSON structure (core-entities.json)

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

## Distinction from sw-entity-catalog

| | sw-core-entity-reference | sw-entity-catalog |
|---|---|---|
| **Scope** | Shopware core (trunk) | Project-owned + custom entities |
| **Source** | Statically generated from `src/` | Running DB / DefinitionRegistry |
| **Custom Entities** | No | Yes |
| **App Entities** | No | Yes |
| **Up to date** | Regenerate on core updates | Always current (DB) |
