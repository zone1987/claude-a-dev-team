# Shopware 6 — Architecture Orientation

Shopware is API-first (three APIs) with its own **Data Abstraction Layer (DAL)** instead of the Doctrine ORM and
an **event-driven** extension system. Keep these fixed points in mind before starting any task:

## NOT standard Symfony/Doctrine
- **No Doctrine ORM** → `EntityDefinition` classes + `EntityRepository`. See `sw-entity-definition`.
- **No QueryBuilder** → the `Criteria` API (filter/sorting/aggregation). See `sw-criteria`.
- **No Doctrine annotations/repositories** → the DAL. Plain SQL only in justified cases (`sw-plain-sql-vs-dal`).

## Extension priority
1. **Prefer events** — `EventSubscriberInterface` covers most cases (`sw-events-subscriber`).
2. **Decorators only** when the event timing does not fit (`sw-service-decoration`).
3. **Extension points** for defined extension slots (`sw-extension-points`).

## Three APIs
| API | Path | Purpose |
|---|---|---|
| Admin | `/api/` | full CRUD/admin operations |
| Store | `/store-api/` | customer-facing / storefront |
| Sync | `/api/_action/sync` | bulk operations |

## Bundle structure (source)
`src/Core` (business + framework), `src/Administration` (Vue 3 admin), `src/Storefront` (Twig/JS),
`src/Elasticsearch`. Plugins live under `custom/plugins/<PluginName>` with `src/` as the PSR-4 root.

## Stack fixed points (6.7)
PHP 8.2+, Symfony 7, DBAL 4, Vue 3 + Pinia/Vite (admin, `mt-*`), Twig + Bootstrap 5 + Webpack (storefront),
MySQL 8/MariaDB 10.11+, OpenSearch 2/ES 8, Redis optional, PHPUnit/PHPStan/Jest/Playwright.

For concrete building blocks: `shopware-core` (fundamentals), `shopware-data` (DAL), `shopware-framework`,
`shopware-storefront`, `shopware-admin`, `shopware-cms`, `shopware-checkout`.
