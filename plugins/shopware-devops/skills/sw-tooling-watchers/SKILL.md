---
name: sw-tooling-watchers
description: >
  Shopware 6 Hot Module Replacement (HMR) — Watchers für Admin und Storefront.
  Build-Commands (composer run / shopware-cli), APP_ENV=dev für Debug-Toolbar,
  IPV4FIRST für NodeJS v17+. Trigger: "shopware watcher", "hot module replacement shopware",
  "hmr shopware", "watch storefront", "watch admin", "composer run watch:admin",
  "composer run watch:storefront", "shopware-cli project admin-watch",
  "storefront dev server", "js build shopware", "JS änderungen shopware". Shopware 6.7.
---

# Shopware 6 — Watchers & Hot Module Replacement

## JS/CSS bauen (ohne Watcher)

| Befehl | Zweck |
|---|---|
| `composer run build:js:admin` | Admin (Source-Code) |
| `shopware-cli project admin-build` | Admin (Production Template) |
| `composer run build:js:storefront` | Storefront (Source-Code) |
| `shopware-cli project storefront-build` | Storefront (Production Template) |

## Watchers (HMR) starten

| Befehl | Zweck |
|---|---|
| `composer run watch:admin` | Admin-Watcher (Source-Code) |
| `composer run storefront:dev-server` | Storefront-Watcher ≥ 6.7.11.0 |
| `composer run watch:storefront` | Storefront-Watcher < 6.7.11.0 |
| `shopware-cli project admin-watch` | Admin-Watcher (Production Template) |
| `shopware-cli project storefront-watch` | Storefront-Watcher (Production Template) |

Watcher **ersetzen nicht** den finalen Build-Schritt!

## Umgebungsvariablen

```bash
# Production-Mode (kein Symfony-Toolbar im Storefront):
APP_ENV=prod composer run watch:storefront

# IPv6-Probleme mit NodeJS >= 17 beheben:
IPV4FIRST=1 composer run watch:storefront
```

- `APP_ENV=dev` → Development Mode: Symfony Toolbar im Storefront, bessere Fehlermeldungen
- `APP_ENV=prod` → Production Mode: Kein Debugging-Toolbar
- `IPV4FIRST=1` → NodeJS v17+ bevorzugt IPv6; dieses Flag erzwingt IPv4
