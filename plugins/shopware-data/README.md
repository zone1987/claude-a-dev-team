# shopware-data

> The Data Abstraction Layer (DAL) in full depth + complete core entity reference.

`shopware-data` documents the **Data Abstraction Layer (DAL)** — Shopware's own data access layer in place of a
Doctrine ORM — on **three levels**, so that both "how do I build it" and "what exists" get answered:

1. **Mechanics / how-to**: `EntityDefinition`, entity class, collection and repository; all **field types** and
   **flags**; all four **association** kinds (1:1, 1:n, n:1, n:m including the mapping entity);
   **translations**, **field inheritance**, **versioning**, **EntityExtension**, **custom fields** and
   **custom entities**; **Criteria** with **filters/sorting/aggregations**; **write events**, **indexers**,
   **field serializers**, **pricing field**, **entity protection**, **attribute entities** as well as
   **hydration** and **aliases**. Plus **database migrations** and the trade-off **DAL vs. plain SQL**.
2. **Complete core entity reference**: **all 312 core entities** generated from the trunk source — per entity
   the table name, entity/collection class, **all fields** (type, storageName, propertyName, flags, default),
   **all associations**, translations and inheritance — as machine-readable **JSON** (742 KB) and as Markdown
   split by domain. This makes it possible to look up at any time which fields and relations, for example,
   `product` or `order` has.
3. **Project introspection** (`/sw-entity-map`, agent `shopware-entity-mapper`): scans the **concrete** project
   (core + `custom/plugins`) and produces a cached catalogue including custom entities/extensions.

The specialist **`shopware-dal-expert`** and the scaffolders **`/sw-entity`**, **`/sw-entity-extension`**,
**`/sw-custom-field`**, **`/sw-migration`** generate convention-compliant building blocks. **When to use:** as
soon as data models, entities, fields, relations or queries are involved.

Part of the **[claude-a-dev-team](../../README.md)** marketplace. The knowledge is distilled from the official
sources and embedded; depth sits in flat reference files beside each SKILL.md, loaded on demand.

## Installation

```
/plugin marketplace add https://github.com/zone1987/claude-a-dev-team
/plugin install shopware-data@claude-a-dev-team
```

## Skills (4)

| Skill | Description |
|---|---|
| `sw-entity` | Shopware DAL entities: EntityDefinition, entity class, collection, repository, extensions, versioning, indexers, custom entities. Use when the request names a Shopware entity or EntityDefinition |
| `sw-fields` | Shopware DAL fields: field types, flags, inheritance, serializers, custom fields, translations, all four association kinds. Use when the request names a Shopware field type or association |
| `sw-query` | Shopware DAL queries: the Criteria API, filters, sorting, aggregations, and when plain SQL beats the DAL. Use when the request names a Shopware Criteria, DAL filter or aggregation |
| `sw-write` | Shopware DAL writes: write events and their payloads, database migrations. Use when the request names a Shopware write event or database migration |

## Agents (2)

| Agent | Description |
|---|---|
| `shopware-dal-expert` | Specialist for the Shopware 6.7 Data Abstraction Layer (DAL): entities/definitions/collections/repositories, field types and flags, associations (1:1, 1:n, n:1, n:m), translations, inheritance, versioning, EntityExtension, custom fields/custom |
| `shopware-entity-mapper` | Introspection agent: scans a concrete Shopware 6 project (core vendor + custom/plugins) and produces a cached entity catalogue (.shopware-catalog/entities.md) with all entities, fields, flags, associations, translations, custom fi |

## Commands (5)

| Command | Description |
|---|---|
| `/sw-custom-field` | Scaffolds a CustomFieldSet including CustomFields for a Shopware 6 entity (migration or lifecycle), with types and entity relation |
| `/sw-entity-extension` | Scaffolds an EntityExtension to add fields/associations to an existing core entity (product, order, customer, ...) — incl |
| `/sw-entity-map` | Scans the current Shopware project (core + custom/plugins) and creates or updates the entity catalogue .shopware-catalog/entities.md (entities, fields, flags, associations, translations, custom fields, custom entities) |
| `/sw-entity` | Scaffolds a complete Shopware 6 DAL entity — definition + entity class + collection + migration + services.xml registration (optionally translations) |
| `/sw-migration` | Scaffolds a Shopware 6 database migration (MigrationStep) with the correct timestamp, update()/updateDestructive() and Shopware conventions (BINARY(16) id, DATETIME(3)) |
