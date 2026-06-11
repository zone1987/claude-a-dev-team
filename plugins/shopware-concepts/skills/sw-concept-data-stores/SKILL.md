---
name: sw-concept-data-stores
description: >
  Shopware Framework-Konzepte: Flow Builder, HTTP Cache, Elasticsearch, Migrations, System Checks,
  Storefront Components (ab 6.7.11). Trigger: "Flow Builder Konzept", "wie funktioniert der Flow Builder",
  "HTTP Cache Shopware", "Cache Invalidierung", "Elasticsearch Shopware", "shopware migrations",
  "System Checks", "Storefront Components", "Twig Components Shopware", "Vite Storefront",
  "shopware http cache concept", "cache-hash", "sw-cache-hash Cookie", "shopware es:index",
  "shopware framework concepts", "wie funktioniert Caching in Shopware".
---

# Shopware Framework-Konzepte (weitere)

Vollständige Konzept-Doku: `references/deep/data-stores.md`

## Kurzüberblick

### Flow Builder

- **Trigger** → **Condition** → **Action** (visuelle Automatisierung, kein Code)
- `FlowDispatcher` → `FlowExecutor` → Sequenz mit Regel-Checks
- **Storer-Konzept**: `*Storer`-Klassen persistieren Flow-Daten; Lazy Loading bei sofortiger Ausführung,
  DB-Persistenz nur bei verzögerten Flows
- Flow Templates — vorgefertigte Flows (via Apps oder Plugins)

### HTTP Cache

- Reverse-Proxy-Ansatz; `_httpCache: true` in Route-Defaults aktiviert Caching
- **`sw-cache-hash` Cookie** — kodiert aktuellen Anwendungszustand (logged-in, Währung, Regeln, etc.)
- Cache Key = Request + cache-hash (maximale Trefferrate, minimale Permutationen)
- **Cache-Invalidierung** via Tags; Listen-Routen verlassen sich auf TTL statt entity-spezifische Invalidierung
- Caching Policies (Experimental → Standard ab 6.8): pro Route konfigurierbar

### Elasticsearch

- Nur explizit aktivierte Suchen nutzen ES (`STATE_ELASTICSEARCH_AWARE` im Context)
- `ElasticsearchDefinition` — definiert Felder und Aggregationen pro Entity
- Fallback auf MySQL bei ES-Fehler (deaktivierbar via `SHOPWARE_ES_THROW_EXCEPTION`)
- Commands: `es:index`, `es:reset`, `es:status`, `es:create:alias`

### Migrations

- PHP-Klassen mit `update()` (non-destructive) und `updateDestructive()` (destruktiv)
- Automatisch erkannt im `Migration/`-Verzeichnis des Plugins

### System Checks

- Typen: Readiness, Health, Long-running
- Kategorien: SYSTEM, FEATURE, EXTERNAL, AUXILIARY
- Status: OK, SKIPPED, UNKNOWN, WARNING, ERROR, FAILURE
- Kontext: WEB, CLI, PRE_ROLLOUT, RECURRENT

### Storefront Components (ab 6.7.11)

- Symfony UX Twig Components — atomic, wiederverwendbare Templates
- Anonymous (Template only) oder PHP-backed (Plugin only)
- JS-Component-System — auto-initialisiert via `data-component` Attribut, ES Module Loading (Vite)
- Event-System via `window.Shopware.emit/on/intercept`
- Build: `composer npm:storefront run build:components`

Technische Umsetzung: `shopware-framework`, `shopware-storefront` (Dev-Plugins)
