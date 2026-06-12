# shopware-data

**Wofür:** Data Abstraction Layer (DAL) komplett: Entities/Definitions/Collections/Repositories, Field-Typen & Flags, alle Associations, Translations, Inheritance, Versioning, Criteria/Filter/Sorting/Aggregationen, Hydration/Aliases — plus vollständige Core-Entity-Referenz (312 Entities) und Projekt-Entity-Introspektion.

Teil des Marketplace **[claude-a-dev-team](../../README.md)**. Wissen ist aus der Shopware-/OCTO-Quelle destilliert; Skills laden Tiefe progressiv aus `references/`.

## Installation (Claude Code)

```
/plugin marketplace add zone1987/claude-a-dev-team
/plugin install shopware-data@claude-a-dev-team
```

## Skills (33)

`adt-shopware-dal`, `sw-aggregations`, `sw-associations-manytomany`, `sw-associations-manytoone`, `sw-associations-onetomany`, `sw-associations-onetoone`, `sw-attribute-entities`, `sw-core-entity-reference`, `sw-criteria`, `sw-custom-entity`, `sw-custom-fields`, `sw-database-migration`, `sw-entity-aliases`, `sw-entity-catalog`, `sw-entity-class`, `sw-entity-collection`, `sw-entity-definition`, `sw-entity-extension`, `sw-entity-hydration`, `sw-entity-indexer`, `sw-entity-protection`, `sw-entity-repository`, `sw-entity-versioning`, `sw-field-flags`, `sw-field-inheritance`, `sw-field-serializer`, `sw-field-types`, `sw-filters`, `sw-plain-sql-vs-dal`, `sw-pricing-field`, `sw-sorting`, `sw-translations`, `sw-write-events`

## Agents (2)

- **`shopware-dal-expert`** — Spezialist für die Shopware-6.7 Data Abstraction Layer (DAL): Entities/Definitions/Collections/Repositories, Field-Typen & Flags, Associations (1:1, 1:n, n:1, n:m), Translations, Inheritance, Versioni
- **`shopware-entity-mapper`** — Introspektions-Agent: scannt ein konkretes Shopware-6-Projekt (Core-Vendor + custom/plugins) und erzeugt einen gecachten Entity-Katalog (.shopware-catalog/entities.md) mit allen Entities, Feldern, Fla

## Commands (5)

- **`/sw-custom-field`** — Scaffold eines CustomFieldSet inkl. CustomFields für eine Shopware-6-Entity (Migration oder Lifecycle), mit Typen und Entity-Relation.
- **`/sw-entity-extension`** — Scaffold einer EntityExtension, um einer bestehenden Core-Entity (product, order, customer, ...) Felder/Associations hinzuzufügen — inkl.
- **`/sw-entity-map`** — Scannt das aktuelle Shopware-Projekt (Core + custom/plugins) und erzeugt/aktualisiert den Entity-Katalog .shopware-catalog/entities.md (Entities, Felder, Flags, Associations, Translations, CustomField
- **`/sw-entity`** — Scaffold einer kompletten Shopware-6 DAL-Entity — Definition + Entity-Klasse + Collection + Migration + services.xml-Registrierung (optional Translations).
- **`/sw-migration`** — Scaffold einer Shopware-6 Datenbank-Migration (MigrationStep) mit korrektem Timestamp, update()/updateDestructive() und Shopware-Konventionen (BINARY(16) id, DATETIME(3)).
