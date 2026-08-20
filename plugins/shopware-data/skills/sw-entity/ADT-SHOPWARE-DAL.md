# Shopware 6 Data Abstraction Layer (DAL)

The DAL is Shopware 6's ORM layer built on top of Doctrine DBAL. It provides entity definitions, typed field collections, a criteria-based search system, event-driven write operations, inheritance, versioning, and translation support.

## Contents

- [Architecture Overview](#architecture-overview)
- [Core Classes](#core-classes)
- [Field Types](#field-types)
- [Flags](#flags)
- [Association Fields](#association-fields)
- [Search / Criteria System](#search-criteria-system)
- [Write System and Events](#write-system-and-events)
- [Indexing System](#indexing-system)
- [Versioning System](#versioning-system)
- [Entity Protection](#entity-protection)
- [Pricing](#pricing)
- [PHP Attribute-Based Definitions](#php-attribute-based-definitions)
- [Examples](#examples)

## Architecture Overview

```
EntityRepository (CRUD facade)
  -> EntityDefinition (schema: fields, associations, flags)
       -> Field types (50+ field classes)
       -> Flag types (25 flag classes)
       -> Association fields (7 types)
  -> Search/Criteria (query builder)
       -> Filters, Sorting, Aggregations, Queries, Grouping
  -> Write system (EntityWriter, WriteCommands, Events)
  -> Indexing system (EntityIndexer, incremental + full)
  -> Version system (create, merge, clone)
```

## Core Classes

The foundational classes that every entity uses. Covers Entity, EntityCollection, EntityDefinition, EntityRepository, EntityTranslationDefinition, MappingEntityDefinition, EntityExtension, and supporting traits/registries.

-> [ADT-SHOPWARE-DAL-CORE-CLASSES.md](ADT-SHOPWARE-DAL-CORE-CLASSES.md)

## Field Types

All 50+ field classes organized by category: ID/FK fields, scalar fields, date/time fields, string fields, JSON fields, price/commerce fields, enum/serialized fields, tree/hierarchy fields, timestamp fields, audit fields, versioning fields, state machine fields, and non-storage fields.

-> [ADT-SHOPWARE-DAL-FIELD-TYPES.md](ADT-SHOPWARE-DAL-FIELD-TYPES.md)

### Field Inheritance Hierarchy

```
Field (abstract)
  ├── IdField [StorageAware]
  ├── FkField [StorageAware]
  │     ├── ParentFkField
  │     ├── CreatedByField / UpdatedByField
  │     ├── VersionField / ReferenceVersionField
  │     └── StateMachineStateField
  ├── StringField -> EmailField, TimeZoneField
  ├── LongTextField -> TreePathField
  ├── IntField -> AutoIncrementField, TreeLevelField, ChildCountField
  ├── FloatField, BoolField -> LockedField
  ├── DateField, DateTimeField -> CreatedAtField, UpdatedAtField
  ├── JsonField -> ListField (-> ManyToManyIdField), ObjectField, CustomFields,
  │                PriceField, CalculatedPriceField, CartPriceField, ...
  ├── BlobField, EnumField, SerializedField, PasswordField, RemoteAddressField
  ├── TranslatedField [NOT StorageAware]
  └── AssociationField -> ManyToOne, OneToMany, ManyToMany, OneToOne,
                          ParentAssociation, ChildrenAssociation, TranslationsAssociation
```

## Flags

25 flag classes that control field behavior: API visibility, validation, deletion cascading, write protection, inheritance, search ranking, and more.

-> [ADT-SHOPWARE-DAL-FLAGS.md](ADT-SHOPWARE-DAL-FLAGS.md)

## Association Fields

7 association field types for defining entity relationships: ManyToOne, OneToMany, ManyToMany, OneToOne, Parent, Children, and Translations.

-> [ADT-SHOPWARE-DAL-ASSOCIATIONS.md](ADT-SHOPWARE-DAL-ASSOCIATIONS.md)

## Search / Criteria System

The complete query system: Criteria builder with fluent API, 12 filter types, 2 sorting types, 11 aggregation types with result classes, score queries, field grouping, and full-text search infrastructure.

-> [ADT-SHOPWARE-DAL-SEARCH-CRITERIA.md](ADT-SHOPWARE-DAL-SEARCH-CRITERIA.md)

## Write System and Events

EntityWriter pipeline, write commands (Insert/Update/Delete/Cascade/SetNull/JsonUpdate), validation events, field exceptions, and 16 DAL event types.

-> [ADT-SHOPWARE-DAL-WRITE-SYSTEM.md](ADT-SHOPWARE-DAL-WRITE-SYSTEM.md)

## Indexing System

EntityIndexer abstract class, EntityIndexerRegistry orchestrator, incremental and full indexing, built-in updaters (ChildCount, Inheritance, ManyToManyId, Tree), message queue integration.

-> [ADT-SHOPWARE-DAL-INDEXING.md](ADT-SHOPWARE-DAL-INDEXING.md)

## Versioning System

VersionManager for creating/merging/cloning versioned entities, VersionDefinition, VersionCommit, VersionCommitData, audit logging, and cleanup tasks.

-> [ADT-SHOPWARE-DAL-VERSIONING.md](ADT-SHOPWARE-DAL-VERSIONING.md)

## Entity Protection

Scope-based read/write protection at the entity level, complementing field-level WriteProtected flags.

-> [ADT-SHOPWARE-DAL-PROTECTION.md](ADT-SHOPWARE-DAL-PROTECTION.md)

## Pricing

Multi-currency Price struct, PriceCollection with currency fallback, CashRoundingConfig, PriceRuleEntity for rule-based pricing.

-> [ADT-SHOPWARE-DAL-PRICING.md](ADT-SHOPWARE-DAL-PRICING.md)

## PHP Attribute-Based Definitions

Modern alternative to `defineFields()` using PHP 8 attributes: `#[Entity]`, `#[Field]`, `#[ManyToOne]`, `#[OneToMany]`, `#[ManyToMany]`, `#[Translations]`, etc.

-> [ADT-SHOPWARE-DAL-ATTRIBUTE-DEFINITIONS.md](ADT-SHOPWARE-DAL-ATTRIBUTE-DEFINITIONS.md)

## Examples

Real-world examples extracted from Shopware Core Content entities:

| Example | Description |
|---------|-------------|
| [examples/entity-definition.md](examples/entity-definition.md) | ProductDefinition - complex entity with inheritance, versioning, all association types |
| [examples/entity-class.md](examples/entity-class.md) | ProductEntity and CategoryEntity - typed entity classes with traits |
| [examples/entity-collection.md](examples/entity-collection.md) | ProductCollection, CategoryCollection, MediaCollection patterns |
| [examples/translation-definition.md](examples/translation-definition.md) | ProductTranslationDefinition and CategoryTranslationDefinition |
| [examples/mapping-definition.md](examples/mapping-definition.md) | ProductCategoryDefinition - ManyToMany pivot table |
| [examples/tree-entity.md](examples/tree-entity.md) | CategoryDefinition - tree structure with path, level, breadcrumb |
| [examples/media-definition.md](examples/media-definition.md) | MediaDefinition - Computed, RestrictDelete, SetNullOnDelete, Runtime fields |
| [examples/property-group.md](examples/property-group.md) | PropertyGroupDefinition + PropertyGroupOptionDefinition - parent/child with ReverseInherited |