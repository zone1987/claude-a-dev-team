# Shopware framework concepts (further)

Complete concept documentation: `DATA-STORES-DETAIL.md`

## Brief overview

### Flow builder

- **Trigger** → **condition** → **action** (visual automation, no code)
- `FlowDispatcher` → `FlowExecutor` → sequence with rule checks
- **Storer concept**: `*Storer` classes persist flow data; lazy loading on immediate execution,
  DB persistence only for delayed flows
- Flow templates — ready-made flows (via apps or plugins)

### HTTP cache

- Reverse proxy approach; `_httpCache: true` in the route defaults enables caching
- **`sw-cache-hash` cookie** — encodes the current application state (logged in, currency, rules, etc.)
- Cache key = request + cache hash (maximum hit rate, minimal permutations)
- **Cache invalidation** via tags; listing routes rely on TTL instead of entity-specific invalidation
- Caching policies (experimental → standard from 6.8): configurable per route

### Elasticsearch

- Only explicitly enabled searches use ES (`STATE_ELASTICSEARCH_AWARE` in the context)
- `ElasticsearchDefinition` — defines fields and aggregations per entity
- Fallback to MySQL on an ES error (can be disabled via `SHOPWARE_ES_THROW_EXCEPTION`)
- Commands: `es:index`, `es:reset`, `es:status`, `es:create:alias`

### Migrations

- PHP classes with `update()` (non-destructive) and `updateDestructive()` (destructive)
- Detected automatically in the plugin's `Migration/` directory

### System checks

- Types: readiness, health, long-running
- Categories: SYSTEM, FEATURE, EXTERNAL, AUXILIARY
- Statuses: OK, SKIPPED, UNKNOWN, WARNING, ERROR, FAILURE
- Contexts: WEB, CLI, PRE_ROLLOUT, RECURRENT

### Storefront components (from 6.7.11)

- Symfony UX Twig components — atomic, reusable templates
- Anonymous (template only) or PHP-backed (plugin only)
- JS component system — auto-initialised via the `data-component` attribute, ES module loading (Vite)
- Event system via `window.Shopware.emit/on/intercept`
- Build: `composer npm:storefront run build:components`

Technical implementation: `shopware-framework`, `shopware-storefront` (dev plugins)
