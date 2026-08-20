# Shopware DAL — Konzept

Vollständige Konzept-Doku: `DAL-DETAIL.md`

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
