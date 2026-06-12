---
name: sw-b2b-suite-migration
description: >
  Migration von B2B Suite zu B2B Components (Shopware Commercial). Migrationsablauf via
  Message Queue, Mapping-Tabellen, Fehlerverfolgung, XML-Konfiguration der Feldmappings,
  Handler (AbstractFieldTransformer), eigene Komponenten hinzufuegen, Erweiterungs-XML.
  B2B Suite wird ab Shopware 6.8 nicht mehr unterstuetzt.
triggers:
  - "b2b suite migration"
  - "B2BSuiteMigration"
  - "b2b_components_migration_state"
  - "b2b_components_migration_map"
  - "b2b_components_migration_errors"
  - "AbstractFieldTransformer"
  - "b2b.migration.transformer"
  - "FieldTransformerRegistry"
  - "b2b suite zu b2b components"
  - "migration b2b legacy"
---

# Skill: sw-b2b-suite-migration

Entwickler-Referenz fuer die Migration von B2B Suite zu B2B Components.

## Referenzen

- [B2B Suite Migration Vollreferenz](references/deep/b2b-suite-migration.md)

## Querverweise

B2B Suite (Quelle): `sw-b2b-suite`. B2B Components (Ziel): `sw-b2b-components`.
