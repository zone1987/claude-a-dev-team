# Shopware 6 — Versions-Highlights im Überblick

Kompakte Zusammenfassung der wichtigsten Neuerungen je Major-Version. Details zu Upgrade-Pfaden und
Breaking Changes: Skills `sw-upgrade-overview` (Strategie) und `shopware-6.7-migration` (konkrete Schritte 6.6→6.7).

---

## 6.5 (EOL)

**PHP & Framework**
- PHP 8.1+ Pflicht; Symfony 6.x.
- Flow Builder eingeführt (ereignisbasierte Automatisierungen statt starrer E-Mail-Events).
- Neue App-Scripting-Funktion (Twig-basierte App-Scripts).

**API**
- Store API als primäre Headless-Schnittstelle stabilisiert.
- API-Versionierung (v1/v2/…) abgeschafft; versionsloses `/api`.

**Storefront**
- Bootstrap 5-Migration abgeschlossen.
- Webpack als Build-Tool.

**Administration**
- Vue 3-Migration begonnen (schrittweise).

**Deprecations wichtig für 6.6**
- `setTwig()` in `StorefrontController`.
- Diverse `address-editor.*` → `address-manager.*`.

---

## 6.6

**PHP & Framework**
- PHP 8.2+ Pflicht.
- Symfony 7.x.

**DAL / Entities**
- `BulkEntityExtension`: Felder für mehrere Entities in einer Klasse.
- `EntityExtension::getEntityName()` statt `getDefinitionClass()`.
- `EnumField` für PHP-`BackedEnum`-Typen.
- Externe URL als Media-Pfad (`path: https://...`).

**Messenger**
- `messenger.bus.shopware` deprecated → `messenger.default_bus`.

**HTTP-Cache**
- MySQL-basierter Cache-Invalidator (kein Redis mehr zwingend für Delayed Invalidation).
- `ReverseProxyCacheClearer` deprecated.

**Storefront**
- Überarbeiteter Address-Manager (neues `address-manager.plugin.js`).
- Neues `window.activeNavigationPathIdList`.
- Cookie-Consent-Dialog: Toggle-Switches statt Checkboxen.

**Administration**
- Axios 0.30.2 weiter Standard; Doppel-Opt-In-Formular.

**Upgrade-Skill**: `sw-upgrade-overview` → Abschnitt 6.5→6.6.

---

## 6.7 (aktuell LTS-Kandidat)

Vollständige Details: `references/deep/release-notes-6.7.md`.

**PHP & Framework**
- PHP 8.2+ Pflicht (PHP 8.5 vollständig supported).
- Symfony 7.4 (seit 6.7.7.0); php-redis ≥ 6.1 für Cache.

**Core / DAL**
- `product.type` (`digital`/`physical`) ersetzt `product.states`.
- DAL: EXISTS-Subqueries statt LEFT JOINs, `Immutable`-Flag, `Choice`-Flag für OpenAPI-Enums.
- Pluggable Thumbnail-Processor (GD oder Imagick).
- `product.descriptionTeaser`: HTML-freier 512-Zeichen-Teaser für Listings.
- SHA-256 für `product.display_group` (64 Zeichen statt 32).

**Storefront**
- Twig-UX-Komponenten-System + Vite-Dev-Server.
- CSS Custom Properties für Theme-Konfiguration.
- Globales JS-Event-System (`window.Shopware.emit/on`).
- JSON-LD Structured Data (ersetzt Microdata).
- Google Analytics 4-Erweiterung; Google Ads Enhanced Conversions.

**Administration**
- SFC-Codemod + Composition-API-Extension-System.
- MCP-Server (experimentell, `MCP_SERVER`-Flag).
- Agentic Commerce Sales-Channel (experimentell).
- 3D-Modell-Viewer und -Editor in Media.

**API**
- Store-API HTTP-Caching (`CACHE_REWORK`-Flag).
- Sync-API Foreign-Key-Resolver (7 neue Resolver).
- Neue Mail-Template-Preview-Routen.
- Shipping-Cost-Endpunkte ohne Cart-Mutation.

**App System**
- Webhook-Rework mit DB-Outbox und Retry-Backoff (`WEBHOOKS_REWORK`-Flag; 6.8-Default).
- App Requirements Validierung (`<requirements>`-Element in Manifest).

**Wichtige Deprecations für 6.8**
- `--json` → `--format json` (CLI)
- `product.states` → `product.type`
- Newsletter-Route-Signaturen (Methodenumbenennungen)
- Typ-basierter Number-Range-Preview
- `CookieProviderInterface` → `CookieGroupCollectEvent`

**Upgrade-Skills**:
- `sw-upgrade-overview`: Strategie-Überblick
- `shopware-6.7-migration`: konkrete Migrationsschritte 6.6 → 6.7
- `sw-deprecation-handling`: Deprecations auflösen
- `sw-meteor-component-map`: `sw-*` → `mt-*` Admin-Komponenten
- `sw-vite-migration`: Webpack → Vite
- `sw-vuex-to-pinia`: State-Management-Migration
- `sw-php-migration-patterns`: PHP-Signaturen und API-Änderungen

---

## 6.8 (upcoming / Breaking-Change-Major)

**Breaking Changes gegenüber 6.7** (Quelle: `UPGRADE-6.8.md`):

**Messenger / Webhooks**
- `webhook`-Messenger-Transport Pflicht (kein Opt-in mehr via `WEBHOOKS_REWORK`).
- `bin/console messenger:consume webhook async low_priority` muss explizit gelistet sein.

**API**
- Typ-basierter Number-Range-Preview `/preview-pattern/{type}` entfernt.
- `/api/_info/queue.json` entfernt → `/api/_info/message-stats.json`.
- `/api/_action/mail-template/validate` entfernt.
- Newsletter-Routen: `subscribe()`/`confirm()`/`unsubscribe()` entfernt, nur noch `*WithResponse()`.
- Mail-Payload: Custom Top-Level-Keys nicht mehr weitergeleitet; nur noch `extensions`-Feld.
- `/store-api/document/download/` gibt `404` statt `204` wenn kein Dokument.

**Core**
- `product.states` / `order_line_item.states` entfernt.
- `LineItemProductStatesRule` entfernt → `LineItemProductTypeRule`.
- `StatesUpdater` entfernt.
- `--json`/`--output json` CLI-Flags entfernt → `--format json`.
- `mail_template_type.template_data`-Spalte entfernt.
- `NumberRangeValueGeneratorInterface` entfernt → `AbstractNumberRangeValueGenerator`.
- `CategoryDefinition::cmsPageIdSwitched` entfernt.
- Debit-Payment-Methode entfernt.
- `RuleComparison` wird `final` (keine Vererbung mehr).
- Increment-basierte Message-Queue-Stats entfernt.
- `MetricTransportInterface::flush()` Pflicht.

**Administration**
- Axios 1.x als Default.
- Composition API Extension System stabil (kein Feature-Flag mehr).
- Options API `Shopware.Component.override()` → Deprecation-Warnings und schrittweise Entfernung.

**Storefront**
- Cache auch für eingeloggte Kunden / gefüllten Warenkorb (`CACHE_REWORK` → Default).
- `context.token` in Twig dauerhaft entfernt.
- Alte Microdata-Blöcke entfernt (JSON-LD ist neuer Standard).

**Upgrade-Skills für 6.8** (sobald verfügbar):
- `sw-upgrade-overview`: Abschnitt 6.7→6.8
- Neuer `sw-migrate-68`-Skill (in Vorbereitung)

---

## Versions-Übersicht auf einen Blick

| Version | PHP min. | Symfony | Build-Tool | Admin State | HTTP-Cache |
|---|---|---|---|---|---|
| 6.5 | 8.1 | 6.x | Webpack | Vue 2/3 Mix | klassisch |
| 6.6 | 8.2 | 7.x | Webpack | Vue 3 | MySQL-Invalidator |
| 6.7 | 8.2 | 7.4 | Webpack + Vite (neu) | Vue 3 + Composition API | Policy-basiert (opt-in) |
| 6.8 | 8.3 (erwartet) | 7.x | Vite (primary) | Composition API | Policy-basiert (default) |
