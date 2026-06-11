---
name: sw-concept-dal
description: >
  Shopware Data Abstraction Layer (DAL): kein ORM, EntityRepository, Criteria, Translations, Versioning,
  Inheritance, Indexing. Trigger: "DAL", "Data Abstraction Layer", "wie funktioniert die Datenbank in Shopware",
  "EntityRepository", "Criteria", "DAL vs Doctrine", "Shopware Datenbank-Abstraktion",
  "Vererbung im DAL", "Versionierung", "Entity Indexer", "shopware database access",
  "wie lese ich Entities", "Context in Shopware".
---

# Shopware DAL — Konzept

Vollständige Konzept-Doku: `references/deep/dal.md`

## Kurzüberblick

Shopware verwendet **kein Doctrine-ORM**, sondern eine eigene DAL. Vorteile: optimiert für E-Commerce
(Mehrsprachigkeit, Variantenvererbung, Versionierung). Zentrales Konzept: EntityRepository + Criteria.

## Kernfeatures

- **EntityRepository** — einziger empfohlener Datenbankzugriff
- **Criteria** — Filter, Sorting, Aggregationen, Associations (kein QueryBuilder)
- **3-stufige Übersetzungsauflösung** — aktuell → Parent-Sprache → Systemsprache
- **Vererbung** — Varianten erben von Parent-Produkten (Felder, Associations)
- **Versioning** — Entities können Versionen haben (Compound-PK: id + version_id)
- **Context** — definiert Sprache, Währung, Regeln; einmal pro Request
- **Entity Indexer** — schreiboptimiertes De-Normalisieren für schnelle Leseoperationen

Technische Umsetzung: `shopware-data` (Dev-Plugin)
