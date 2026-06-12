# shopware-data

> Die Data Abstraction Layer (DAL) in voller Tiefe + komplette Core-Entity-Referenz.

`shopware-data` dokumentiert die **Data Abstraction Layer (DAL)** — Shopwares eigene Datenzugriffsschicht anstelle
eines Doctrine-ORM — auf **drei Ebenen**, damit sowohl „wie baue ich" als auch „was existiert" beantwortet wird:

1. **Mechanik / How-to** (Mikro-Skills): EntityDefinition, Entity-Klasse, Collection und Repository; alle
   **Field-Typen** und **Flags**; alle vier **Association**-Arten (1:1, 1:n, n:1, n:m inkl. Mapping-Entity);
   **Translations**, **Field-Inheritance**, **Versioning**, **EntityExtension**, **CustomFields** und
   **CustomEntities**; **Criteria** mit **Filtern/Sorting/Aggregationen**; **Write-Events**, **Indexer**,
   **FieldSerializer**, **Pricing-Field**, **EntityProtection**, **Attribut-Entities** sowie **Hydration** und
   **Aliases**. Dazu **Datenbank-Migrationen** und die Abwägung **DAL vs. plain SQL**.
2. **Vollständige Core-Entity-Referenz** (`sw-core-entity-reference`): **alle 312 Core-Entities** aus der
   Trunk-Quelle generiert — je Entity Tabellenname, Entity-/Collection-Klasse, **alle Felder** (Typ, storageName,
   propertyName, Flags, Default), **alle Associations**, Translations und Inheritance — als maschinenlesbares
   **JSON** (742 KB) und nach Domänen aufgeteiltes Markdown. Damit lässt sich jederzeit nachschlagen, welche Felder/
   Beziehungen z. B. `product` oder `order` hat.
3. **Projekt-Introspektion** (`sw-entity-catalog` + `/sw-entity-map`, Agent `shopware-entity-mapper`): scannt das
   **konkrete** Projekt (Core + `custom/plugins`) und erzeugt einen gecachten Katalog inkl. eigener Entities/Extensions.

Der Spezialist **`shopware-dal-expert`** und die Scaffolder **`/sw-entity`**, **`/sw-entity-extension`**,
**`/sw-custom-field`**, **`/sw-migration`** erzeugen konventionskonforme Bausteine. **Wann nutzen:** sobald
Datenmodelle, Entities, Felder, Beziehungen oder Abfragen im Spiel sind.

Teil des Marketplace **[claude-a-dev-team](../../README.md)**. Das Wissen ist aus den offiziellen Quellen destilliert und eingebettet; Skills laden ihre Tiefe progressiv aus `references/`.

## Installation

```
/plugin marketplace add https://github.com/zone1987/claude-a-dev-team
/plugin install shopware-data@claude-a-dev-team
```

## Skills (33)

`adt-shopware-dal`, `sw-aggregations`, `sw-associations-manytomany`, `sw-associations-manytoone`, `sw-associations-onetomany`, `sw-associations-onetoone`, `sw-attribute-entities`, `sw-core-entity-reference`, `sw-criteria`, `sw-custom-entity`, `sw-custom-fields`, `sw-database-migration`, `sw-entity-aliases`, `sw-entity-catalog`, `sw-entity-class`, `sw-entity-collection`, `sw-entity-definition`, `sw-entity-extension`, `sw-entity-hydration`, `sw-entity-indexer`, `sw-entity-protection`, `sw-entity-repository`, `sw-entity-versioning`, `sw-field-flags`, `sw-field-inheritance`, `sw-field-serializer`, `sw-field-types`, `sw-filters`, `sw-plain-sql-vs-dal`, `sw-pricing-field`, `sw-sorting`, `sw-translations`, `sw-write-events`

## Agents (2)

- **`shopware-dal-expert`** — Spezialist für die Shopware-6.7 Data Abstraction Layer (DAL): Entities/Definitions/Collections/Repositories, Field-Typen & Flags, Associations (1:1, 1:n, n:1, n:m), Translations, Inheritance, Versioning, EntityExtension,
- **`shopware-entity-mapper`** — Introspektions-Agent: scannt ein konkretes Shopware-6-Projekt (Core-Vendor + custom/plugins) und erzeugt einen gecachten Entity-Katalog (.shopware-catalog/entities.md) mit allen Entities, Feldern, Flags, Associations, Tr

## Commands (5)

- **`/sw-custom-field`** — Scaffold eines CustomFieldSet inkl. CustomFields für eine Shopware-6-Entity (Migration oder Lifecycle), mit Typen und Entity-Relation.
- **`/sw-entity-extension`** — Scaffold einer EntityExtension, um einer bestehenden Core-Entity (product, order, customer, ...) Felder/Associations hinzuzufügen — inkl.
- **`/sw-entity-map`** — Scannt das aktuelle Shopware-Projekt (Core + custom/plugins) und erzeugt/aktualisiert den Entity-Katalog .shopware-catalog/entities.md (Entities, Felder, Flags, Associations, Translations, CustomFields, CustomEntities).
- **`/sw-entity`** — Scaffold einer kompletten Shopware-6 DAL-Entity — Definition + Entity-Klasse + Collection + Migration + services.xml-Registrierung (optional Translations).
- **`/sw-migration`** — Scaffold einer Shopware-6 Datenbank-Migration (MigrationStep) mit korrektem Timestamp, update()/updateDestructive() und Shopware-Konventionen (BINARY(16) id, DATETIME(3)).
