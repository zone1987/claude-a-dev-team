# Shopware framework concepts (further) — complete documentation

Sources: `concepts/framework/flow-concept.md`, `http_cache.md`, `elasticsearch.md`, `migrations.md`,
`storefront-components.md`, `system-check.md`

---

## Contents

- [Flow builder (flow-concept.md)](#flow-builder-flow-conceptmd)
- [HTTP cache (http_cache.md)](#http-cache-http_cachemd)
- [Elasticsearch (elasticsearch.md)](#elasticsearch-elasticsearchmd)
- [Migrations (migrations.md)](#migrations-migrationsmd)
- [Storefront components (from 6.7.11.0) (storefront-components.md)](#storefront-components-from-67110-storefront-componentsmd)
- [System checks (system-check.md)](#system-checks-system-checkmd)

## Flow builder (flow-concept.md)

### Concept

Shopware's automation solution for shop operators — without programming knowledge.

**Components:**

| Term | Description |
|---|---|
| **Flow** | Automation process; defines trigger → conditions → actions |
| **Trigger** | Event from the storefront or the application (e.g. `checkout.order.place`) |
| **Condition** | Business rule; determines whether the action is executed |
| **Action** | Task executed on the trigger/when the condition is met |
| **Flow template** | Ready-made flow (library); via app or plugin; not modifiable |

Priority: with several flows on the same trigger, priority decides the order of execution.
The special action "Stop flow" ends further actions in the flow sequence.

### Evaluation sequence

```
FlowDispatcher::dispatch()
→ FlowExecutor::execute()
→ FlowExecutor::sequenceRuleMatches()? → execute action
→ StopFlowAction::handleFlow()
```

**Example: placing an order**
```
User → CartOrderRoute::Order() → dispatch [checkout.order.place]
→ FlowDispatcher → FlowExecutor → executeAction → StopFlowAction
```

### Storer concept

Every flow can store data and provide it to actions.

- Storer classes: `ProductStorer`, `OrderStorer`, `MailStorer` etc. → extend `FlowStorer`
- Methods: `store()` and `restore()`
- Called on flow creation (`StorableFlow`) in the `FlowFactory`
- `restore()` can load directly or lazily

**Persistence**: by default flow data is **not** persisted in the DB (same request cycle).
Exception: for delayed flows the data is persisted for later retrieval.

---

## HTTP cache (http_cache.md)

### Concept

A reverse proxy cache between the user and the web application.
Caching saves application load by reusing cached responses.

### Activation

```php
#[Route(path: '/detail/{productId}', defaults: ['_httpCache' => true])]
public function index(SalesChannelContext $context, Request $request): Response
```

Only `GET` requests are considered cacheable.

### Cache key (sw-cache-hash cookie)

- Contains a hash of all cache-relevant information (logged-in status, tax status, currency, matched rules)
- Set as soon as the application state deviates from the default (not logged in, default currency, empty cart)
- **Important**: reverse proxies (Fastly, Varnish) or the Symfony cache use the `cache-hash` as part of the cache key
- Enables differentiated cache entries for the same request with a different application state

### Deprecated cookies (removed in 6.8.0.0)

- `sw-currency` — currency info is already in `sw-cache-hash`
- `sw-states` — states are already in `sw-cache-hash`

### Cache invalidation

- Responses are tagged (all cache tags generated during the request)
- HTTP cache invalidation of a storefront route = invalidation of the associated Store API routes
- **Listing routes** (product listing, search, category listings) are **not** tagged entity-specifically
  → they rely on TTL; no direct invalidation when a single entity changes
  (tracking across all possible listings would be too costly)

**Rationale**: an entity can appear in many different listings (different filters, sorting,
pagination). Strict consistency cannot be guaranteed; a small amount of staleness is accepted for stability.

**Invalidation logging** (from 6.7.7.0, disabled by default):
```yaml
shopware:
  cache:
    invalidation:
      tag_invalidation_log_enabled: false
```

### HTTP cache workflow (from 6.8.0.0 / 6.7.6.0 with the CACHE_REWORK flag)

`CacheResponseSubscriber` on response generation:
1. Apply the `sw-language-id` + `sw-currency-id` headers; extend the Vary header
2. Check early exits (is the HTTP cache enabled?)
3. Compute the `sw-context-hash` (cart, customer, rules, etc.)
4. Check cacheability (GET + the `_httpCache` attribute)
5. Validate the context hash (client vs. server); mismatch → no-cache
6. Apply the caching policy → set the `Cache-Control` headers

---

## Elasticsearch (elasticsearch.md)

### Concept

A NoSQL database focused on search capabilities. Shopware uses ES for improved product and
category search.

### Activation

ES is only used in explicitly defined searches.
By default: `ProductSearchRoute`, `ProductListingRoute`, `ProductSuggestRoute`.

```php
$context->addState(Context::STATE_ELASTICSEARCH_AWARE);
$repository->search($criteria, $context);
```

**Fallback**: on an ES error → MySQL data load. Can be disabled: `SHOPWARE_ES_THROW_EXCEPTION=1`

### Core components

| Class | Task |
|---|---|
| `ElasticsearchDefinition` | Defines fields + aggregations per entity for ES |
| `ElasticsearchEntitySearcher` | Decorates EntitySearcher → maps onto the ES structure; returns an IdSearchResult |
| `ElasticsearchEntityAggregator` | Like the searcher, but for aggregations |
| `CriteriaParser` | Translates Criteria into ES notation |
| `ProductSearchBuilder` | Specific search builder for product search |
| `ProductUpdater` | Subscribes to `ProductIndexerEvent`; triggers re-indexing |

### CLI commands

```bash
es:index          # Re-index all configured entities
es:reset          # Reset all active indices and empty the queue (only on corruption)
es:status         # Status of all current indices
es:create:alias   # Update the index alias (makes the new index active)
es:index:cleanup  # Delete outdated ES indices
es:test:analyzer  # Test ES analyzers on indices
```

---

## Migrations (migrations.md)

### Concept

PHP classes with database schema changes. Can be executed forwards/backwards.

### Plugin migrations

- Placement: the `Migration/` directory in the plugin source root
- Filename convention: a specific pattern (generate it via the Shopware console command)
- Shopware detects plugin migrations automatically

### Methods

| Method | Type | Description |
|---|---|---|
| `update()` | Non-destructive | Only reversible changes (add new tables, columns) |
| `updateDestructive()` | Destructive | Irreversible changes (drop tables/columns) |

---

## Storefront components (from 6.7.11.0) (storefront-components.md)

### Concept

A new component system based on **Symfony UX Twig components**.
Brings a modern, framework-like development experience to the storefront.

### Anonymous components (the simplest form)

A single Twig template file defines the component.

```
MyExtension/src/Resources/views/components/Button/Primary.html.twig
→ component name: MyExtension:Button:Primary
```

`index.html.twig` → the directory name becomes the component name.

**Defining properties:**
```twig
{% props label = 'Click here!', size = 'md' %}
<button class="my-button size-{{ size }}">{{ label }}</button>
```

**Usage:**
```twig
<twig:MyExtension:Button:Primary label="Buy now!" size="lg" />
```

### PHP-backed components (plugins only)

A PHP class alongside the template, for advanced logic.
Must be registered as a service with `autoconfigure: true`.

```php
#[AsTwigComponent()]
class Primary
{
    public string $label = 'Click me!';
    public string $size = 'md';
}
```

### Component SCSS

An SCSS file with the same name → automatically included in the component build.
No PHP theme compiler — a separate Vite build process.

**Theme variables**: available as CSS custom properties (not as SCSS variables):
```css
.btn-primary { background: var(--sw-color-brand-primary); }
```

### JavaScript component system

The successor to the JS plugin system. Important differences:

1. **Automatic initialisation** — via the `data-component` attribute; MutationObserver for DOM changes
2. **No manual registration** — ES module loading via a generated import map
3. **Event system instead of overrides** — `window.Shopware.emit/on/intercept`
4. **TypeScript support**

**Basic structure:**
```javascript
export default class ButtonPrimary extends ShopwareComponent {
    static options = { label: 'Click me!', size: 'md' };
    init() { /* initialisation */ }
    destroy() { /* cleanup */ }
}
```

**Event interception** (for manipulating data before it is sent):
```javascript
window.Shopware.intercept('BuyButton:PreSubmit', (data) => {
    data.formData.append('foo', 'bar');
    return data;
});
```

### Build process

```bash
# Complete storefront build
composer build:js:storefront

# Components only
composer npm:storefront run build:components
```

Build artefacts must be shipped with the extension (no compiling at runtime).

### Dev server

```bash
composer storefront:dev-server
```
Vite-based; live reload, no proxy needed; use the normal storefront URL.

---

## System checks (system-check.md)

### Concept

Checks to ensure a Shopware installation works normally.
Every check verifies a specific aspect of the functionality.

### Check types

| Type | Description |
|---|---|
| **Readiness checks** | Executed before the system is ready for traffic |
| **Health checks** | Periodically for system health; manually or by monitoring |
| **Long-running checks** | Subset of the health checks; can take long; always in the background |

### Categories

| Category | Description |
|---|---|
| `SYSTEM` | Backbone functionality (e.g. database connection) |
| `FEATURE` | Specific feature functionality (e.g. payment system) |
| `EXTERNAL` | External services (e.g. SMTP server reachable) |
| `AUXILIARY` | Auxiliary services (e.g. background tasks running) |

### Status values

`OK` → `SKIPPED` → `UNKNOWN` → `WARNING` → `ERROR` → `FAILURE`

- `SKIPPED`: the criteria for the check are not met (e.g. not applicable in the current environment)
- `ERROR`: runtime error; parts might still work
- `FAILURE`: unrecoverable error

### Execution context

| Context | Description |
|---|---|
| `WEB` | In the web environment |
| `CLI` | In a command line environment |
| `PRE_ROLLOUT` | Before a system rollout |
| `RECURRENT` | As a scheduled task |

Immutable environments: checking the runtime configuration after deployment is not needed,
but it is essential before rollout.
