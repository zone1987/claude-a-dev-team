# Shopware 6 — version highlights at a glance

Compact summary of the most important new features per major version. Details on upgrade paths and
breaking changes: skills `sw-upgrade-overview` (strategy) and `shopware-6.7-migration` (concrete steps 6.6→6.7).

---

## Contents

- [6.5 (EOL)](#65-eol)
- [6.6](#66)
- [6.7 (current LTS candidate)](#67-current-lts-candidate)
- [6.8 (upcoming / breaking change major)](#68-upcoming--breaking-change-major)
- [Version overview at a glance](#version-overview-at-a-glance)

## 6.5 (EOL)

**PHP & framework**
- PHP 8.1+ mandatory; Symfony 6.x.
- Flow Builder introduced (event-based automations instead of rigid email events).
- New app scripting feature (Twig-based app scripts).

**API**
- Store API stabilized as the primary headless interface.
- API versioning (v1/v2/…) abolished; versionless `/api`.

**Storefront**
- Bootstrap 5 migration completed.
- Webpack as build tool.

**Administration**
- Vue 3 migration started (step by step).

**Deprecations important for 6.6**
- `setTwig()` in `StorefrontController`.
- Various `address-editor.*` → `address-manager.*`.

---

## 6.6

**PHP & framework**
- PHP 8.2+ mandatory.
- Symfony 7.x.

**DAL / entities**
- `BulkEntityExtension`: fields for multiple entities in one class.
- `EntityExtension::getEntityName()` instead of `getDefinitionClass()`.
- `EnumField` for PHP `BackedEnum` types.
- External URL as media path (`path: https://...`).

**Messenger**
- `messenger.bus.shopware` deprecated → `messenger.default_bus`.

**HTTP cache**
- MySQL-based cache invalidator (Redis no longer mandatory for delayed invalidation).
- `ReverseProxyCacheClearer` deprecated.

**Storefront**
- Reworked address manager (new `address-manager.plugin.js`).
- New `window.activeNavigationPathIdList`.
- Cookie consent dialog: toggle switches instead of checkboxes.

**Administration**
- Axios 0.30.2 still the standard; double opt-in form.

**Upgrade skill**: `sw-upgrade-overview` → section 6.5→6.6.

---

## 6.7 (current LTS candidate)

Full details: `references/deep/release-notes-6.7.md`.

**PHP & framework**
- PHP 8.2+ mandatory (PHP 8.5 fully supported).
- Symfony 7.4 (since 6.7.7.0); php-redis ≥ 6.1 for cache.

**Core / DAL**
- `product.type` (`digital`/`physical`) replaces `product.states`.
- DAL: EXISTS subqueries instead of LEFT JOINs, `Immutable` flag, `Choice` flag for OpenAPI enums.
- Pluggable thumbnail processor (GD or Imagick).
- `product.descriptionTeaser`: HTML-free 512-character teaser for listings.
- SHA-256 for `product.display_group` (64 characters instead of 32).

**Storefront**
- Twig UX component system + Vite dev server.
- CSS custom properties for theme configuration.
- Global JS event system (`window.Shopware.emit/on`).
- JSON-LD structured data (replaces microdata).
- Google Analytics 4 extension; Google Ads Enhanced Conversions.

**Administration**
- SFC codemod + Composition API extension system.
- MCP server (experimental, `MCP_SERVER` flag).
- Agentic commerce sales channel (experimental).
- 3D model viewer and editor in media.

**API**
- Store API HTTP caching (`CACHE_REWORK` flag).
- Sync API foreign key resolvers (7 new resolvers).
- New mail template preview routes.
- Shipping cost endpoints without cart mutation.

**App System**
- Webhook rework with DB outbox and retry backoff (`WEBHOOKS_REWORK` flag; 6.8 default).
- App requirements validation (`<requirements>` element in the manifest).

**Important deprecations for 6.8**
- `--json` → `--format json` (CLI)
- `product.states` → `product.type`
- Newsletter route signatures (method renames)
- Type-based number range preview
- `CookieProviderInterface` → `CookieGroupCollectEvent`

**Upgrade skills**:
- `sw-upgrade-overview`: strategy overview
- `shopware-6.7-migration`: concrete migration steps 6.6 → 6.7
- `sw-deprecation-handling`: resolving deprecations
- `sw-meteor-component-map`: `sw-*` → `mt-*` admin components
- `sw-vite-migration`: Webpack → Vite
- `sw-vuex-to-pinia`: state management migration
- `sw-php-migration-patterns`: PHP signatures and API changes

---

## 6.8 (upcoming / breaking change major)

**Breaking changes compared to 6.7** (source: `UPGRADE-6.8.md`):

**Messenger / webhooks**
- `webhook` messenger transport mandatory (no longer opt-in via `WEBHOOKS_REWORK`).
- `bin/console messenger:consume webhook async low_priority` must be listed explicitly.

**API**
- Type-based number range preview `/preview-pattern/{type}` removed.
- `/api/_info/queue.json` removed → `/api/_info/message-stats.json`.
- `/api/_action/mail-template/validate` removed.
- Newsletter routes: `subscribe()`/`confirm()`/`unsubscribe()` removed, only `*WithResponse()` remains.
- Mail payload: custom top-level keys no longer forwarded; only the `extensions` field.
- `/store-api/document/download/` returns `404` instead of `204` when there is no document.

**Core**
- `product.states` / `order_line_item.states` removed.
- `LineItemProductStatesRule` removed → `LineItemProductTypeRule`.
- `StatesUpdater` removed.
- `--json`/`--output json` CLI flags removed → `--format json`.
- `mail_template_type.template_data` column removed.
- `NumberRangeValueGeneratorInterface` removed → `AbstractNumberRangeValueGenerator`.
- `CategoryDefinition::cmsPageIdSwitched` removed.
- Debit payment method removed.
- `RuleComparison` becomes `final` (no more inheritance).
- Increment-based message queue stats removed.
- `MetricTransportInterface::flush()` mandatory.

**Administration**
- Axios 1.x as the default.
- Composition API extension system stable (no more feature flag).
- Options API `Shopware.Component.override()` → deprecation warnings and gradual removal.

**Storefront**
- Cache also for logged-in customers / filled cart (`CACHE_REWORK` → default).
- `context.token` permanently removed from Twig.
- Old microdata blocks removed (JSON-LD is the new standard).

**Upgrade skills for 6.8** (once available):
- `sw-upgrade-overview`: section 6.7→6.8
- New `sw-migrate-68` skill (in preparation)

---

## Version overview at a glance

| Version | PHP min. | Symfony | Build tool | Admin state | HTTP cache |
|---|---|---|---|---|---|
| 6.5 | 8.1 | 6.x | Webpack | Vue 2/3 mix | classic |
| 6.6 | 8.2 | 7.x | Webpack | Vue 3 | MySQL invalidator |
| 6.7 | 8.2 | 7.4 | Webpack + Vite (new) | Vue 3 + Composition API | policy-based (opt-in) |
| 6.8 | 8.3 (expected) | 7.x | Vite (primary) | Composition API | policy-based (default) |
