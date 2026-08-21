# Shopware DAL — concept

Complete concept documentation: `DAL-DETAIL.md`

## Brief overview

Shopware uses **no Doctrine ORM**, but a DAL of its own. Advantages: optimised for e-commerce
(multi-language, variant inheritance, versioning). Central concept: EntityRepository + Criteria.

## Core features

- **EntityRepository** — the only recommended database access
- **Criteria** — filtering, sorting, aggregations, associations (no QueryBuilder)
- **3-stage translation resolution** — current → parent language → system language
- **Inheritance** — variants inherit from parent products (fields, associations)
- **Versioning** — entities can have versions (compound PK: id + version_id)
- **Context** — defines language, currency, rules; once per request
- **Entity indexer** — write-optimised denormalisation for fast read operations

Technical implementation: `shopware-data` (dev plugin)
