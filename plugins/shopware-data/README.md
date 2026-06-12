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

| Skill | Beschreibung |
|---|---|
| `adt-shopware-dal` | Comprehensive reference for Shopware 6 Data Abstraction Layer (DAL) |
| `sw-aggregations` | Aggregationen in der Shopware-6 Criteria-API: TermsAggregation, CountAggregation, SumAggregation, AvgAggregation, StatsAggregation, FilterAggregation, verschachtelte Aggregationen + Ergebnis auslesen |
| `sw-associations-manytomany` | ManyToMany-Associations in Shopware 6 DAL über eine Mapping-Entity (MappingEntityDefinition) inkl |
| `sw-associations-manytoone` | ManyToOne-Associations in Shopware 6 DAL (viele Kinder zeigen auf ein Eltern-Objekt) inkl |
| `sw-associations-onetomany` | OneToMany-Associations in Shopware 6 DAL (Eltern hat viele Kinder), inkl |
| `sw-associations-onetoone` | OneToOne-Associations in Shopware 6 DAL (genau ein zugeordnetes Objekt) inkl |
| `sw-attribute-entities` | Attribut-basierte DAL-Entities in Shopware 6 (6.6+): Entity-Definition via PHP-Attribute (#[Entity], Field-Attribute) statt klassischer EntityDefinition |
| `sw-core-entity-reference` | Statische Vollreferenz aller Shopware-6-Core-DAL-Entities (312 Definitionen, generiert aus trunk src/) |
| `sw-criteria` | Die Shopware-6 Criteria-API als zentrales Query-Werkzeug der DAL: IDs, Limit/Offset, Associations laden, getAssociation, Total-Count-Mode, Criteria kombinieren |
| `sw-custom-entity` | Custom Entities in Shopware 6 (codearm, via custom_entity.xml / Entities.xml definierte Entities ohne eigene PHP-Definition), inkl |
| `sw-custom-fields` | Custom Fields in Shopware 6: CustomFieldSet + CustomField per Migration/Repository anlegen, Typen, Entity-Zuordnung, Auslesen via getCustomFields(), Media-/Entity-Selection-Typ |
| `sw-database-migration` | Datenbank-Migrations in Shopware 6: MigrationStep (getCreationTimestamp, update, updateDestructive), Namens-/Verzeichniskonvention Migration/MigrationV{major}, destructive vs |
| `sw-entity-aliases` | Shopware DAL Storage-Aliasing — storageName vs propertyName, SQL-Aliase in Queries, Association-Aliase in Criteria, getByStorageName, buildTranslationChain |
| `sw-entity-catalog` | Den projektspezifischen Entity-Katalog von Shopware nutzen — welche Entities, Felder, Associations, Translations und CustomFields es im KONKRETEN Projekt (Core + custom/plugins) wirklich gibt |
| `sw-entity-class` | Die Entity-Klasse einer Shopware-6 DAL-Definition: Properties, Getter/Setter, EntityIdTrait, translated-Felder, Association-Properties |
| `sw-entity-collection` | Die EntityCollection einer Shopware-6 DAL-Entity: typisierte Collection, getExpectedClass(), eigene Filter-/Map-Helfer |
| `sw-entity-definition` | Eine Shopware-6 DAL-EntityDefinition bauen: defineFields(), getEntityName(), getEntityClass(), getCollectionClass(), Registrierung via shopware.entity.definition |
| `sw-entity-extension` | Bestehende Core-Entities in Shopware 6 erweitern: EntityExtension mit extendFields(), zusätzliche Felder/ Associations zu product/order/customer etc |
| `sw-entity-hydration` | Shopware DAL EntityHydrator — wie DB-Zeilen in Entity-Objekte verwandelt werden |
| `sw-entity-indexer` | Eigener EntityIndexer in Shopware 6 DAL: vorberechnete/abgeleitete Daten bei Schreibvorgängen aktualisieren, IndexerRegistry, partial/full index, EntityIndexingMessage |
| `sw-entity-protection` | Zugriffsschutz in Shopware 6 DAL: ApiAware-Scopes, ReadProtected/WriteProtected, EntityProtection, interne Felder von der API ausschließen |
| `sw-entity-repository` | CRUD mit dem Shopware-6 EntityRepository: search, searchIds, create, update, upsert, delete, aggregate; Context vs |
| `sw-entity-versioning` | Entity-Versioning in Shopware 6 DAL: createVersion, merge, Versionskontext, ReferenceVersionField, VersionField |
| `sw-field-flags` | Shopware-6 DAL-Field-Flags: PrimaryKey, Required, ApiAware, Inherited, Runtime, Computed, ReadProtected, WriteProtected, SearchRanking, AllowHtml, CascadeDelete, RestrictDelete, SetNullOnDelete |
| `sw-field-inheritance` | Field-Inheritance in Shopware 6 DAL (Parent→Child, z.B. Produkt-Varianten erben vom Hauptprodukt) mit dem Inherited-Flag und setParentDefinition/Inheritance-Aware-Definition |
| `sw-field-serializer` | Eigener FieldSerializer in Shopware 6 DAL: Schreib-/Leselogik eines (eigenen) Field-Typs, encode/decode, Validation-Constraints |
| `sw-field-types` | Alle Shopware-6 DAL-Field-Typen: IdField, FkField, StringField, IntField, FloatField, BoolField, JsonField, DateTimeField, ListField, PriceField, TranslatedField, EnumField, Association-Felder u.v.m |
| `sw-filters` | Filter in der Shopware-6 Criteria-API: EqualsFilter, EqualsAnyFilter, ContainsFilter, RangeFilter, MultiFilter (AND/OR), NotFilter, PrefixFilter, post-filter |
| `sw-plain-sql-vs-dal` | Entscheidung in Shopware 6: wann DAL (Criteria/Repository) und wann plain SQL via Doctrine\DBAL\Connection |
| `sw-pricing-field` | Preise in Shopware 6 DAL: PriceField/PriceCollection, Price (net/gross je Currency), CashRounding, Preise schreiben/lesen |
| `sw-sorting` | Sortierung in der Shopware-6 Criteria-API: FieldSorting (ASC/DESC), CountSorting, natural sorting, Sortierung über Associations |
| `sw-translations` | Übersetzbare Felder in Shopware 6 DAL: TranslatedField + TranslationDefinition + TranslationsAssociationField, das translated-Array, Schreiben pro Sprache |
| `sw-write-events` | Das Shopware-6 DAL-Write-System & seine Events: EntityWrittenEvent, EntityWrittenContainerEvent, BeforeWriteEvent, EntityDeletedEvent, auf Schreibvorgänge reagieren |

## Agents (2)

| Agent | Beschreibung |
|---|---|
| `shopware-dal-expert` | Spezialist für die Shopware-6.7 Data Abstraction Layer (DAL): Entities/Definitions/Collections/Repositories, Field-Typen & Flags, Associations (1:1, 1:n, n:1, n:m), Translations, Inheritance, Versioning, EntityExtension, CustomFields/Custom |
| `shopware-entity-mapper` | Introspektions-Agent: scannt ein konkretes Shopware-6-Projekt (Core-Vendor + custom/plugins) und erzeugt einen gecachten Entity-Katalog (.shopware-catalog/entities.md) mit allen Entities, Feldern, Flags, Associations, Translations, CustomFi |

## Commands (5)

| Command | Beschreibung |
|---|---|
| `/sw-custom-field` | Scaffold eines CustomFieldSet inkl. CustomFields für eine Shopware-6-Entity (Migration oder Lifecycle), mit Typen und Entity-Relation |
| `/sw-entity-extension` | Scaffold einer EntityExtension, um einer bestehenden Core-Entity (product, order, customer, ...) Felder/Associations hinzuzufügen — inkl |
| `/sw-entity-map` | Scannt das aktuelle Shopware-Projekt (Core + custom/plugins) und erzeugt/aktualisiert den Entity-Katalog .shopware-catalog/entities.md (Entities, Felder, Flags, Associations, Translations, CustomFields, CustomEntities) |
| `/sw-entity` | Scaffold einer kompletten Shopware-6 DAL-Entity — Definition + Entity-Klasse + Collection + Migration + services.xml-Registrierung (optional Translations) |
| `/sw-migration` | Scaffold einer Shopware-6 Datenbank-Migration (MigrationStep) mit korrektem Timestamp, update()/updateDestructive() und Shopware-Konventionen (BINARY(16) id, DATETIME(3)) |
