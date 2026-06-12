# Shopware 6.7 — Vollständige Release Notes

Quelle: `RELEASE_INFO-6.7.md` (Trunk/Main). Versions-Highlights kumulativ ab 6.7.0 bis 6.7.12 (upcoming).

---

## Core

### Symfony & PHP

- **Symfony 7.4** (seit 6.7.7.0): alle Pakete aktualisiert; php-redis ≥ 6.1 Pflicht für Cache.
- **PHP 8.5**-Support vollständig (seit 6.7.6.0); `symfony/polyfill-php85` (`array_first`/`array_last`).

### Produkt-Typ statt `product.states`

Neues Feld `product.type` (`digital` / `physical` + erweiterbar via `shopware.product.allowed_types`).
- `order_line_item.states` → `order_line_item.payload.product_type`
- `LineItemProductStatesRule` → `LineItemProductTypeRule`
- `StatesUpdater` und `ProductStatesBeforeChangeEvent`/`ProductStatesChangedEvent` deprecated

### DAL-Optimierungen

- **EXISTS-Subqueries** statt LEFT JOINs für verschachtelte Filtergruppen → massive Performance-Gewinne bei komplexen Criteria (z.B. mehrere `lineItems.type`-Filter).
- Neues `Immutable`-DAL-Flag: `custom_field.name`, `custom_field.type`, `custom_field_set.name` sind nach Erstellung unveränderlich.
- `#[Field]`-Attribut: `maxLength`-Parameter für STRING- und EMAIL-Felder.
- `#[ListField]`, `#[Password]`, `FieldType::EMAIL`, `FieldType::PRICE` als neue Attribut-Feldtypen.
- `OpenAPI enum`-Unterstützung via `Choice`-Flag.
- Primary-Key-Validierung in `dal:validate`.

### HTTP-Cache-Rework (`CACHE_REWORK`-Flag / 6.7.6+)

- HTTP-Caching-Policies: benannte Policies pro Route und Area (`storefront`/`store_api`).
- `sw-states`- und `sw-currency`-Handling deprecated; Cache künftig auch für eingeloggte Kunden / gefüllten Warenkorb aktiv.
- `sw-cache-hash` enthält nur noch preisrelevante Rule-IDs.
- `SHOPWARE_HTTP_DEFAULT_TTL`, `shopware.http_cache.stale_while_revalidate` etc. deprecated.

### Elasticsearch / OpenSearch

- **Dediziertes `completion`-Feld** für Admin-Suche-Autocomplete (ngram aus `text`/`textBoosted` entfernt).
- **BM25 ohne Feldlängen-Normalisierung** (`b=0`) als Index-Default; Prose-Felder behalten Standard-BM25.
- **`dis_max`-`tie_breaker`** konfigurierbar via `elasticsearch.search.dismax_tie_breaker` (default 0.2).
- **Configurable `min_score`**: `core.search.minScore` (float, per Sales Channel).
- **`TokenQueryBuilder` refaktoriert**: `AbstractFieldQueryBuilder` und `AbstractTokenQueryBuilder` als Dekorations-Extension-Points.
- **OpenSearch PHP Client 2.6** (6.7.8.0): Mehrfach-Host-Konfiguration via CSV deprecated; → Single-LB-Endpoint.
- **`ENABLE_OPENSEARCH_FOR_ADMIN_API`-Flag** (experimentell, 6.7.8.0): Admin-API-Suchen via OpenSearch.
- **Konfigurierbare Shard/Replica-Counts**: `SHOPWARE_ES_NUMBER_OF_SHARDS` / `SHOPWARE_ES_NUMBER_OF_REPLICAS` etc.
- **`SHOPWARE_ES_USE_LANGUAGE_ANALYZER`**: Sprachanalyzer für Suchanfragen steuerbar.

### Weitere Core-Änderungen

- **`product.display_group`** nutzt jetzt SHA-256 (64 Zeichen statt MD5 32 Zeichen).
- **Produkt-`descriptionTeaser`**: neues read-only-Feld, HTML-freier 512-Zeichen-Teaser; `core.listing.partialDataLoading` reduziert Listing-Payload.
- **Varianten nach Eltern-Produktname suchen**: `parent.name`-Suchfeld (deaktiviert by default).
- **Thumbnail-Processor pluggable**: `ThumbnailProcessorInterface`; `GdImageThumbnailProcessor` (default) und `ImagickThumbnailProcessor` wählbar via `shopware.media.thumbnail_processor`.
- **`product.main_category` Vererbung** von Eltern-Produkt.
- **Salutation `position`-Feld**: sortierbare Anreden in Formularen.
- **Produkt Open Graph-Felder**: `og:title`, `og:description`, `og:image` pro Produkt (6.7.9.0).
- **Default CMS-Page-ID** wird jetzt in DB persistiert (kein Runtime-Only mehr).
- **Interner Kommentar** bei State-Machine-Übergängen.
- **State-Machine-Transitions** gesperrt per Entity (Lock gegen Race Conditions).
- **Plugin-Snippet-Lader**: Locale-spezifische statt plugin-weite Prüfung.
- **`RegisterScheduleTaskMessage`** deprecated.
- **`IgnoreInUnusedMediaSearch`-Flag**: technische Media-Associations von `media:delete-unused` ausschließen.
- **Doppeltes Opt-In**: Auto-Resend nach konfigurierbarem Interval (`core.loginRegistration.doubleOptInResendInterval`).
- **CLI JSON-Output**: `--json`/`--output json` → `--format json` (deprecated, entfernt in 6.8).
- **Standardisierter `sha256`-Twig-Filter**.
- **`translation:list`**-Command und `translation:install` interaktiv mit Locales.
- **Requirement-aware Plugin-Installationsreihenfolge** bei `plugin:install`.
- **`TestBootstrapper`**: Composer-managed Plugins aus `vendor/` unterstützt.
- **JSONL-Produktexport** (`ProductExportEntity::FILE_FORMAT_JSONL`).
- **`product.search_keyword.indexing`** deaktivierbar; `relevant_keyword_count` konfigurierbar.
- **Konfigurierbare Elasticsearch-Shard-/Replica-Counts** via Env-Vars.
- **Telemetrie-Metriken** (hinter `TELEMETRY_METRICS`-Flag): `MetricTransportInterface::flush()`, Per-Label-Validation, `Telemetry`-Facade, `PeriodicMetricCollectorInterface`.
- **SVG-Upload-Allowlist** (6.7.10.1): strikte passive Allowlist, konfigurierbar via `shopware.media.svg.*`.

---

## Storefront

### Neues Komponenten-System (6.7.11.0)

- Basiert auf **Twig UX Components** + eigene SCSS/JS-Behandlung.
- Dokumentation: https://developer.shopware.com/docs/concepts/framework/storefront-components.html

### Vite Dev-Server (6.7.11.0)

```bash
composer storefront:dev-server
```
`composer watch:storefront` deprecated (nächste Major).

### CSS Custom Properties für Theme-Config (6.7.11.0)

Theme-Konfigurationswerte als native CSS Custom Properties verfügbar:
```css
.btn-primary { background: var(--sw-color-brand-primary); }
```

### Globales JS-Event-System (6.7.11.0)

Neues `window.Shopware`-Objekt mit Node-EventEmitter-basiertem System:
```js
window.Shopware.emit('Filter:Change', { foo: 'bar' });
window.Shopware.on('Filter:Change', ({ foo }) => { /* ... */ });
```

### JSON-LD Structured Data (6.7.9.0, `JSON_LD_DATA`-Flag)

Microdata ersetzt durch JSON-LD in `<head>`:
- `WebSite` + `SearchAction`, `Organization`, `WebPage`/`ProductPage`, `BreadcrumbList`, `Product`, `ItemList`
- Eigene Templates unter `storefront/layout/structured-data/`; je Template 2 überschreibbare Blöcke.

### Weitere Storefront-Features

- **Single-file-References in `theme.json`**: `@BundleName/path/to/file` für Style und Script.
- **PluginManager.callPluginMethod()**: Methode auf allen Plugin-Instanzen aufrufen.
- **GLTF-Animationen** in 3D-Modellen (6.7.10.0).
- **Live-Kauf-Limits** für Closeout-Produkte via neuem Store-API-Endpunkt `GET /store-api/product/purchase-limit`.
- **Single-Hit-Suche-Redirect** auch für EAN und Hersteller-Nr. (konfigurierbar via `shopware.storefront.redirect_on_single_hit_fields`).
- **Cookie Consent sprachabhängig** (6.7.7.0).
- **Google Analytics 4**: erweiterte E-Commerce-Events (`add_to_wishlist`, `view_cart`, `add_shipping_info` etc.), neue Konfiguration "Track Offcanvas Cart".
- **IDN-E-Mail-Validierung** im Storefront.
- **`list-price-affix.html.twig`**: zentraler Extension-Point für Content vor/nach Listenpreisen (6.7.12.0).
- **`sizes`-Attribut für XXL-Breakpoint** (6.7.12.0).
- **XHR-Login-Failures**: HTTP 403 statt Redirect (6.7.12.0).
- **Mail-Templates**: `theme_config()` in Mails via temporären `salesChannelContext` (6.7.12.0).
- **Google Ads Enhanced Conversions** (6.7.12.0).
- **Checkout-Gateway-Fallback-Methode** für blockierte Zahlungs-/Versandmethoden (6.7.12.0).
- **Kunden-Adressen** werden beim Speichern getrimmt (6.7.12.0).
- **Cookie-Bar früher fokussiert** (Accessibility) und an `<body>`-Anfang verschoben (6.7.10.0).
- **Bestellstornierung** nur noch für Bestellungen im Status `open` (6.7.10.0).
- **Robots.txt** konfigurierbar mit eigenen `User-agent`-Blöcken (6.7.5.0).
- **Steuer-Berechnung B2B/B2C** getrennt (6.7.5.0).

---

## Administration

### SFC-Migration & Composition API

- **SFC-Codemod** (`npm run codemod:sfc-migration`): `.html.twig + index.js` → `.vue`; Options API → Composition API.
- **Composition API Extension System** (`ADMIN_COMPOSITION_API_EXTENSION_SYSTEM`-Flag): `Options-API`-Overrides automatisch auf Composition-API-Komponenten gemappt (Compat-Shim); `Shopware.Component.overrideComponentSetup()` als neuer Weg.
- **Native `<sw-block>`-Runtime**: Legacy-Twig-Overrides weiter kompatibel, Deprecation-Warning im Browser.

### MCP-Server (experimentell, 6.7.11.0, `MCP_SERVER`-Flag)

- Endpunkt `/api/_mcp` (Streamable HTTP Transport).
- Tools für Entity-Management, State-Machine-Transitions, Cache, Storefront-Suche.
- Ressourcen: Entity-List, Sales-Channels, State-Machines, Business-Events, Flow-Actions.
- Plugins via `mcp.tool`/`mcp.prompt`/`mcp.resource`-Tags erweiterbar.

### Agentic Commerce (experimentell, 6.7.10.0)

- Neuer Sales-Channel-Typ "Agentic Commerce"; OpenAI Merchant Center als erster Provider.
- Dedizierte Admin-Views für Konfiguration, Produkt-Mapping, Usage-Insights.

### Weitere Admin-Änderungen

- **`sw-date-filter`**: 15 Zeitraum-Optionen (6.7.11.0), Bug-Fix "Last Quarter" falsches Jahr (6.7.11.0).
- **Mail-Template-Preview** Sales-Channel-aware, sandboxed iframe (6.7.11.0).
- **Interne Bestellkommentare** in der Bestellliste (Tooltip-Icon, 6.7.10.0).
- **`sw-entity-multi-id-select`**: Varianten in Labels unterscheidbar (6.7.12.0).
- **Rule-Builder-Labels** für Warenkorbsummen-Bedingungen präziser (6.7.12.0).
- **Icon-Cache und Speculation-Rules** per Sales-Channel konfigurierbar (6.7.12.0).
- **Analytics-Settings** in Configuration- und Tracking-Karten aufgeteilt (6.7.12.0).
- **Axios 1.x** neben 0.30.2 (Dual-Client, `useAxiosV1: true`; Default in 6.8).
- **Suche im Settings-Modul** (6.7.6.0).
- **3D-Modell-Viewer und -Editor** in der Media-Verwaltung (6.7.7.0).
- **Media umbenennen** löst URL-Aktualisierung aus (6.7.12.0).

---

## API

### Store API

- **HTTP-Caching** für zahlreiche Store-API-Routes (hinter `CACHE_REWORK`-Flag, 6.7.6.0):
  `/store-api/product`, `/store-api/category`, `/store-api/navigation/*`, `/store-api/search`, `/store-api/cms/*`, u.v.m.
- **Gzip/Base64url-kodierte Criteria** als Query-Parameter (Alternative für lange URLs).
- **Neue Versand-Kosten-Endpunkte** (6.7.10.0):
  - `GET /store-api/shipping-cost/product/{productId}`
  - `GET /store-api/shipping-cost/cart`
- **Per-User- und Per-IP-Rate-Limiter** für Login und OAuth (`shopware.api.rate_limiter`).
- **Newsletter-Routen** geben jetzt `200 OK` + Body statt `204 No Content` zurück; `subscribe()`/`confirm()`/`unsubscribe()` deprecated → `*WithResponse()`.
- **Store API: Cookie-Groups-Route** `/store-api/cookie-groups` (inkl. `languageId`).
- **`/store-api/product/purchase-limit`**: Live-Kauf-Limits für Closeout-Produkte.

### Admin API

- **Sync API**: 7 neue Foreign-Key-Resolver (z.B. `currency.iso_code`, `payment_method.technical_name`, `salutation.salutation_key`).
- **Mail-Template-Routen** (6.7.11.0): `/api/_action/mail-template/simulate`, `/preview`, `/get-data-and-send`, `/available-variables`.
- **Number-Range-Preview by ID**: `/api/_action/number-range/{numberRangeId}/preview-pattern` (neu); Typ-basierter Route deprecated (→ 6.8 entfernt).
- **Leere `sw-*`-ID-Header** werden wie fehlende Header behandelt (6.7.12.0).
- **Plain JSON API**: Extension-Felder bleiben in `extensions`-Objekt bei `includes` (6.7.12.0).
- **Video-Cover-Management**: `POST /api/_action/media/{mediaId}/video-cover`.
- **Externe Media-Thumbnails**: `POST/DELETE /api/_action/media/{id}/external-thumbnails`.
- **`/api/_info/queue.json` deprecated** → `/api/_info/message-stats.json`.
- **`/api/_action/mail-template/validate` deprecated** (entfernt in 6.8).

---

## App System

### Webhook-Rework (`WEBHOOKS_REWORK`-Flag, 6.7.12.0 opt-in → 6.8 default)

- DB-gestützter Outbox vor HTTP-Versuch.
- Retry-Backoff: 5s → 30s → 5min → 30min → 4h (max 4 Stunden).
- In-Flight-Deliveries überleben Worker-Crashes.
- Identity-Headers: `X-Shopware-Event-Id`, `X-Shopware-Sequence`, `X-Shopware-Attempt`.
- Neuer `webhook`-Messenger-Transport: `bin/console messenger:consume webhook async low_priority`.
- Rollback: `bin/console webhook:drain-to-async`.

### Weitere App-Änderungen

- **App Requirements** (`<requirements>` in Manifest, 6.7.10.0): z.B. `<public-access/>` validiert HTTPS und Erreichbarkeit.
- **`app.system_heartbeat`** (6.7.8.0): wöchentlicher Heartbeat-Webhook.
- **App Script Caching**: `response.cache.sharedMaxAge()` / `clientMaxAge()` (6.7.6.0).

---

## Hosting & Konfiguration

- **Google Storage Application Default Credentials**: `keyFile`/`keyFilePath` optional.
- **Local Filesystem**: `config.enforce_file_permissions: false` möglich.
- **Staging-Modus**: `system_config`-Overrides konfigurierbar; Extensions deaktivierbar.
- **`sales-channel:replace:url`**-Command (6.7.5.0).
- **Konfigurierbare Order-Deep-Link-Ablaufzeit**: `shopware.order.deep_link.expire_days`.
- **Long-running MySQL-Connections**: `doctrine-mysql-come-back`-Support; `wrapperClass` in `DATABASE_URL`.
- **S3**: Custom HTTP-Client via DI (`shopware.filesystem.s3.client`).
- **HTML-Sanitizer**: `custom_tags`-Konfiguration für eigene HTML-Elemente.
- **Deprecierte HTTP-Cache-Reverse-Proxy-Konfiguration** (since 6.7.0.0, entfernt in 6.8):
  `shopware.http_cache.reverse_proxy.use_varnish_xkey` etc.

---

## Wichtige Deprecations (Entfernung in 6.8)

| Deprecated | Ersatz |
|---|---|
| `product.states` / `order_line_item.states` | `product.type` / `order_line_item.payload.product_type` |
| `LineItemProductStatesRule` | `LineItemProductTypeRule` |
| `NumberRangeValueGeneratorInterface` | `AbstractNumberRangeValueGenerator` |
| `--json` / `--output json` (CLI) | `--format json` |
| `AbstractNewsletterSubscribeRoute::subscribe()` etc. | `subscribeWithResponse()` etc. |
| `/api/_info/queue.json` | `/api/_info/message-stats.json` |
| `/api/_action/mail-template/validate` | (entfernt ohne Ersatz) |
| `mail_template_type.template_data`-Spalte | Direkte `templateData` in API-Payload |
| `CookieProviderInterface` und Implementierungen | `CookieGroupCollectEvent` |
| `TemplateGroup` | (entfernt ohne Ersatz) |
| `RuleComparison` (Vererbung) | `final` in 6.8 |
| Increment-basierte Message-Queue-Stats | `message-stats.json`-Endpoint |
| `shopware.admin_worker.enable_queue_stats_worker` | Deaktivieren via Config |
| Typ-basierter Number-Range-Preview (`/preview-pattern/{type}`) | `/preview-pattern` by ID |
| OpenSearch Multi-Host-CSV-Config | Single LB-Endpoint |

---

## Breaking Changes (aktiv seit 6.7)

- **`controllerName`/`controllerAction`** → `activeRoute` in Twig/CSS/JS (6.7.3.0).
- **`context.token`** nicht mehr in Twig-Rendering-Context verfügbar (6.7.5.0).
- **OpenSearch 3.x**: leere `properties: []` nicht mehr erlaubt → `{}` oder weglassen (6.7.3.1).
- **Custom Fields nicht mehr searchable by default** (6.7.7.0); Opt-in nötig.
- **`sw-select-base`**: `showClearableButton` jetzt abhängig von `required` (6.7.8.0).
- **`EntityDefinitionQueryHelper::columnExists/tableExists`** deprecated → `TableHelper`.
- **`CookieProviderInterface`**: deprecated, via `CookieGroupCollectEvent` ersetzen (6.7.7.0+).
- **`migration.generator`**: Fremdschlüssel-Format `fk.<table>.<col>` → `fk__<table>__<col>` (6.7.8.0).
