# Shopware 6.7 — complete release notes

Source: `RELEASE_INFO-6.7.md` (trunk/main). Version highlights cumulative from 6.7.0 to 6.7.12 (upcoming).

---

## Contents

- [Core](#core)
- [Storefront](#storefront)
- [Administration](#administration)
- [API](#api)
- [App System](#app-system)
- [Hosting & Configuration](#hosting-configuration)
- [Important deprecations (removal in 6.8)](#important-deprecations-removal-in-68)
- [Breaking changes (active since 6.7)](#breaking-changes-active-since-67)

## Core

### Symfony & PHP

- **Symfony 7.4** (since 6.7.7.0): all packages updated; php-redis ≥ 6.1 mandatory for cache.
- **PHP 8.5** support complete (since 6.7.6.0); `symfony/polyfill-php85` (`array_first`/`array_last`).

### Product type instead of `product.states`

New field `product.type` (`digital` / `physical` + extensible via `shopware.product.allowed_types`).
- `order_line_item.states` → `order_line_item.payload.product_type`
- `LineItemProductStatesRule` → `LineItemProductTypeRule`
- `StatesUpdater` and `ProductStatesBeforeChangeEvent`/`ProductStatesChangedEvent` deprecated

### DAL optimizations

- **EXISTS subqueries** instead of LEFT JOINs for nested filter groups → massive performance gains with complex Criteria (e.g. multiple `lineItems.type` filters).
- New `Immutable` DAL flag: `custom_field.name`, `custom_field.type`, `custom_field_set.name` are immutable after creation.
- `#[Field]` attribute: `maxLength` parameter for STRING and EMAIL fields.
- `#[ListField]`, `#[Password]`, `FieldType::EMAIL`, `FieldType::PRICE` as new attribute field types.
- **OpenAPI enum** support via `Choice` flag.
- Primary key validation in `dal:validate`.

### HTTP cache rework (`CACHE_REWORK` flag / 6.7.6+)

- HTTP caching policies: named policies per route and area (`storefront`/`store_api`).
- `sw-states` and `sw-currency` handling deprecated; cache in future also active for logged-in customers / filled cart.
- `sw-cache-hash` now only contains price-relevant rule IDs.
- `SHOPWARE_HTTP_DEFAULT_TTL`, `shopware.http_cache.stale_while_revalidate` etc. deprecated.

### Elasticsearch / OpenSearch

- **Dedicated `completion` field** for admin search autocomplete (ngram removed from `text`/`textBoosted`).
- **BM25 without field length normalization** (`b=0`) as index default; prose fields keep standard BM25.
- **`dis_max` `tie_breaker`** configurable via `elasticsearch.search.dismax_tie_breaker` (default 0.2).
- **Configurable `min_score`**: `core.search.minScore` (float, per sales channel).
- **`TokenQueryBuilder` refactored**: `AbstractFieldQueryBuilder` and `AbstractTokenQueryBuilder` as decoration extension points.
- **OpenSearch PHP Client 2.6** (6.7.8.0): multi-host configuration via CSV deprecated; → single LB endpoint.
- **`ENABLE_OPENSEARCH_FOR_ADMIN_API` flag** (experimental, 6.7.8.0): Admin API searches via OpenSearch.
- **Configurable shard/replica counts**: `SHOPWARE_ES_NUMBER_OF_SHARDS` / `SHOPWARE_ES_NUMBER_OF_REPLICAS` etc.
- **`SHOPWARE_ES_USE_LANGUAGE_ANALYZER`**: language analyzer for search queries controllable.

### Further core changes

- **`product.display_group`** now uses SHA-256 (64 characters instead of MD5 32 characters).
- **Product `descriptionTeaser`**: new read-only field, HTML-free 512-character teaser; `core.listing.partialDataLoading` reduces the listing payload.
- **Search variants by parent product name**: `parent.name` search field (disabled by default).
- **Thumbnail processor pluggable**: `ThumbnailProcessorInterface`; `GdImageThumbnailProcessor` (default) and `ImagickThumbnailProcessor` selectable via `shopware.media.thumbnail_processor`.
- **`product.main_category` inheritance** from parent product.
- **Salutation `position` field**: sortable salutations in forms.
- **Product Open Graph fields**: `og:title`, `og:description`, `og:image` per product (6.7.9.0).
- **Default CMS page ID** is now persisted in the DB (no longer runtime-only).
- **Internal comment** on state machine transitions.
- **State machine transitions** locked per entity (lock against race conditions).
- **Plugin snippet loader**: locale-specific instead of plugin-wide check.
- **`RegisterScheduleTaskMessage`** deprecated.
- **`IgnoreInUnusedMediaSearch` flag**: exclude technical media associations from `media:delete-unused`.
- **Double opt-in**: auto-resend after a configurable interval (`core.loginRegistration.doubleOptInResendInterval`).
- **CLI JSON output**: `--json`/`--output json` → `--format json` (deprecated, removed in 6.8).
- **Standardized `sha256` Twig filter**.
- **`translation:list`** command and `translation:install` interactive with locales.
- **Requirement-aware plugin installation order** for `plugin:install`.
- **`TestBootstrapper`**: Composer-managed plugins from `vendor/` supported.
- **JSONL product export** (`ProductExportEntity::FILE_FORMAT_JSONL`).
- **`product.search_keyword.indexing`** can be disabled; `relevant_keyword_count` configurable.
- **Configurable Elasticsearch shard/replica counts** via env vars.
- **Telemetry metrics** (behind the `TELEMETRY_METRICS` flag): `MetricTransportInterface::flush()`, per-label validation, `Telemetry` facade, `PeriodicMetricCollectorInterface`.
- **SVG upload allowlist** (6.7.10.1): strict passive allowlist, configurable via `shopware.media.svg.*`.

---

## Storefront

### New component system (6.7.11.0)

- Based on **Twig UX Components** + dedicated SCSS/JS handling.
- Documentation: https://developer.shopware.com/docs/concepts/framework/storefront-components.html

### Vite dev server (6.7.11.0)

```bash
composer storefront:dev-server
```
`composer watch:storefront` deprecated (next major).

### CSS custom properties for theme config (6.7.11.0)

Theme configuration values available as native CSS custom properties:
```css
.btn-primary { background: var(--sw-color-brand-primary); }
```

### Global JS event system (6.7.11.0)

New `window.Shopware` object with a Node EventEmitter-based system:
```js
window.Shopware.emit('Filter:Change', { foo: 'bar' });
window.Shopware.on('Filter:Change', ({ foo }) => { /* ... */ });
```

### JSON-LD structured data (6.7.9.0, `JSON_LD_DATA` flag)

Microdata replaced by JSON-LD in `<head>`:
- `WebSite` + `SearchAction`, `Organization`, `WebPage`/`ProductPage`, `BreadcrumbList`, `Product`, `ItemList`
- Custom templates under `storefront/layout/structured-data/`; 2 overridable blocks per template.

### Further storefront features

- **Single-file references in `theme.json`**: `@BundleName/path/to/file` for style and script.
- **PluginManager.callPluginMethod()**: call a method on all plugin instances.
- **GLTF animations** in 3D models (6.7.10.0).
- **Live purchase limits** for closeout products via the new Store API endpoint `GET /store-api/product/purchase-limit`.
- **Single-hit search redirect** also for EAN and manufacturer number (configurable via `shopware.storefront.redirect_on_single_hit_fields`).
- **Cookie consent language-dependent** (6.7.7.0).
- **Google Analytics 4**: extended e-commerce events (`add_to_wishlist`, `view_cart`, `add_shipping_info` etc.), new "Track Offcanvas Cart" configuration.
- **IDN email validation** in the storefront.
- **`list-price-affix.html.twig`**: central extension point for content before/after list prices (6.7.12.0).
- **`sizes` attribute for the XXL breakpoint** (6.7.12.0).
- **XHR login failures**: HTTP 403 instead of redirect (6.7.12.0).
- **Mail templates**: `theme_config()` in mails via a temporary `salesChannelContext` (6.7.12.0).
- **Google Ads Enhanced Conversions** (6.7.12.0).
- **Checkout gateway fallback method** for blocked payment/shipping methods (6.7.12.0).
- **Customer addresses** are trimmed on save (6.7.12.0).
- **Cookie bar focused earlier** (accessibility) and moved to the start of `<body>` (6.7.10.0).
- **Order cancellation** now only for orders in the `open` state (6.7.10.0).
- **Robots.txt** configurable with custom `User-agent` blocks (6.7.5.0).
- **Tax calculation B2B/B2C** separated (6.7.5.0).

---

## Administration

### SFC migration & Composition API

- **SFC codemod** (`npm run codemod:sfc-migration`): `.html.twig + index.js` → `.vue`; Options API → Composition API.
- **Composition API extension system** (`ADMIN_COMPOSITION_API_EXTENSION_SYSTEM` flag): `Options-API` overrides mapped automatically onto Composition API components (compat shim); `Shopware.Component.overrideComponentSetup()` as the new way.
- **Native `<sw-block>` runtime**: legacy Twig overrides still compatible, deprecation warning in the browser.

### MCP server (experimental, 6.7.11.0, `MCP_SERVER` flag)

- Endpoint `/api/_mcp` (streamable HTTP transport).
- Tools for entity management, state machine transitions, cache, storefront search.
- Resources: entity list, sales channels, state machines, business events, flow actions.
- Extensible by plugins via `mcp.tool`/`mcp.prompt`/`mcp.resource` tags.

### Agentic commerce (experimental, 6.7.10.0)

- New sales channel type "Agentic Commerce"; OpenAI Merchant Center as the first provider.
- Dedicated admin views for configuration, product mapping, usage insights.

### Further admin changes

- **`sw-date-filter`**: 15 period options (6.7.11.0), bug fix "Last Quarter" wrong year (6.7.11.0).
- **Mail template preview** sales-channel-aware, sandboxed iframe (6.7.11.0).
- **Internal order comments** in the order list (tooltip icon, 6.7.10.0).
- **`sw-entity-multi-id-select`**: variants distinguishable in labels (6.7.12.0).
- **Rule builder labels** for cart total conditions more precise (6.7.12.0).
- **Icon cache and speculation rules** configurable per sales channel (6.7.12.0).
- **Analytics settings** split into configuration and tracking cards (6.7.12.0).
- **Axios 1.x** alongside 0.30.2 (dual client, `useAxiosV1: true`; default in 6.8).
- **Search in the settings module** (6.7.6.0).
- **3D model viewer and editor** in media management (6.7.7.0).
- **Renaming media** triggers a URL update (6.7.12.0).

---

## API

### Store API

- **HTTP caching** for numerous Store API routes (behind the `CACHE_REWORK` flag, 6.7.6.0):
  `/store-api/product`, `/store-api/category`, `/store-api/navigation/*`, `/store-api/search`, `/store-api/cms/*`, and many more.
- **Gzip/base64url-encoded Criteria** as a query parameter (alternative for long URLs).
- **New shipping cost endpoints** (6.7.10.0):
  - `GET /store-api/shipping-cost/product/{productId}`
  - `GET /store-api/shipping-cost/cart`
- **Per-user and per-IP rate limiter** for login and OAuth (`shopware.api.rate_limiter`).
- **Newsletter routes** now return `200 OK` + body instead of `204 No Content`; `subscribe()`/`confirm()`/`unsubscribe()` deprecated → `*WithResponse()`.
- **Store API: cookie groups route** `/store-api/cookie-groups` (incl. `languageId`).
- **`/store-api/product/purchase-limit`**: live purchase limits for closeout products.

### Admin API

- **Sync API**: 7 new foreign key resolvers (e.g. `currency.iso_code`, `payment_method.technical_name`, `salutation.salutation_key`).
- **Mail template routes** (6.7.11.0): `/api/_action/mail-template/simulate`, `/preview`, `/get-data-and-send`, `/available-variables`.
- **Number range preview by ID**: `/api/_action/number-range/{numberRangeId}/preview-pattern` (new); type-based route deprecated (→ removed in 6.8).
- **Empty `sw-*` ID headers** are treated like missing headers (6.7.12.0).
- **Plain JSON API**: extension fields stay in the `extensions` object with `includes` (6.7.12.0).
- **Video cover management**: `POST /api/_action/media/{mediaId}/video-cover`.
- **External media thumbnails**: `POST/DELETE /api/_action/media/{id}/external-thumbnails`.
- **`/api/_info/queue.json` deprecated** → `/api/_info/message-stats.json`.
- **`/api/_action/mail-template/validate` deprecated** (removed in 6.8).

---

## App System

### Webhook rework (`WEBHOOKS_REWORK` flag, 6.7.12.0 opt-in → 6.8 default)

- DB-backed outbox before the HTTP attempt.
- Retry backoff: 5s → 30s → 5min → 30min → 4h (max 4 hours).
- In-flight deliveries survive worker crashes.
- Identity headers: `X-Shopware-Event-Id`, `X-Shopware-Sequence`, `X-Shopware-Attempt`.
- New `webhook` messenger transport: `bin/console messenger:consume webhook async low_priority`.
- Rollback: `bin/console webhook:drain-to-async`.

### Further app changes

- **App requirements** (`<requirements>` in the manifest, 6.7.10.0): e.g. `<public-access/>` validates HTTPS and reachability.
- **`app.system_heartbeat`** (6.7.8.0): weekly heartbeat webhook.
- **App script caching**: `response.cache.sharedMaxAge()` / `clientMaxAge()` (6.7.6.0).

---

## Hosting & Configuration

- **Google Storage application default credentials**: `keyFile`/`keyFilePath` optional.
- **Local filesystem**: `config.enforce_file_permissions: false` possible.
- **Staging mode**: `system_config` overrides configurable; extensions can be disabled.
- **`sales-channel:replace:url`** command (6.7.5.0).
- **Configurable order deep link expiry**: `shopware.order.deep_link.expire_days`.
- **Long-running MySQL connections**: `doctrine-mysql-come-back` support; `wrapperClass` in `DATABASE_URL`.
- **S3**: custom HTTP client via DI (`shopware.filesystem.s3.client`).
- **HTML sanitizer**: `custom_tags` configuration for custom HTML elements.
- **Deprecated HTTP cache reverse proxy configuration** (since 6.7.0.0, removed in 6.8):
  `shopware.http_cache.reverse_proxy.use_varnish_xkey` etc.

---

## Important deprecations (removal in 6.8)

| Deprecated | Replacement |
|---|---|
| `product.states` / `order_line_item.states` | `product.type` / `order_line_item.payload.product_type` |
| `LineItemProductStatesRule` | `LineItemProductTypeRule` |
| `NumberRangeValueGeneratorInterface` | `AbstractNumberRangeValueGenerator` |
| `--json` / `--output json` (CLI) | `--format json` |
| `AbstractNewsletterSubscribeRoute::subscribe()` etc. | `subscribeWithResponse()` etc. |
| `/api/_info/queue.json` | `/api/_info/message-stats.json` |
| `/api/_action/mail-template/validate` | (removed without replacement) |
| `mail_template_type.template_data` column | direct `templateData` in the API payload |
| `CookieProviderInterface` and implementations | `CookieGroupCollectEvent` |
| `TemplateGroup` | (removed without replacement) |
| `RuleComparison` (inheritance) | `final` in 6.8 |
| Increment-based message queue stats | `message-stats.json` endpoint |
| `shopware.admin_worker.enable_queue_stats_worker` | disable via config |
| Type-based number range preview (`/preview-pattern/{type}`) | `/preview-pattern` by ID |
| OpenSearch multi-host CSV config | single LB endpoint |

---

## Breaking changes (active since 6.7)

- **`controllerName`/`controllerAction`** → `activeRoute` in Twig/CSS/JS (6.7.3.0).
- **`context.token`** no longer available in the Twig rendering context (6.7.5.0).
- **OpenSearch 3.x**: empty `properties: []` no longer allowed → `{}` or omit (6.7.3.1).
- **Custom fields no longer searchable by default** (6.7.7.0); opt-in required.
- **`sw-select-base`**: `showClearableButton` now depends on `required` (6.7.8.0).
- **`EntityDefinitionQueryHelper::columnExists/tableExists`** deprecated → `TableHelper`.
- **`CookieProviderInterface`**: deprecated, replace via `CookieGroupCollectEvent` (6.7.7.0+).
- **`migration.generator`**: foreign key format `fk.<table>.<col>` → `fk__<table>__<col>` (6.7.8.0).
