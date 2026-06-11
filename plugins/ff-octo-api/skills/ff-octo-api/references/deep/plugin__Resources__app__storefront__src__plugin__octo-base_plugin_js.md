# OctoBasePlugin (`src/Resources/app/storefront/src/plugin/octo-base.plugin.js`)

## Zweck
Basis-Plugin für die OCTO-Storefront-Plugins. Stellt farbcodierte Debug-Logging-Helfer bereit (Events, Methodenaufrufe, Plugin-Load, Info), aktiv nur bei `window.octoDebug`.

## Typ & Vererbung
- `export default class OctoBasePlugin extends Plugin` (Shopware `plugin.class`).

## Statische Felder
- `_colors` (Object, eingefroren in `init()`): `events`, `methodCalls`, `pluginLoaded`, `info`.

## Methoden
- `init()` — friert `_colors` ein.
- `logEvent(event)` — `[EVENT]`-Log bei octoDebug.
- `logMethodCall(method, ...args)` — `[METHOD]`-Log bei octoDebug.
- `logPluginLoaded(viewports)` — `[PLUGIN]`-Log bei octoDebug.
- `logInfo(...)` — `[INFO]`-Log (immer).

## Besonderheiten
- Wird von den Buy-Box-(Child-)Plugins erweitert; Debug über `window.octoDebug` (in `main.js` default false).

## Bezüge
`plugin/buy-box.plugin.js`, `plugin/*-select.plugin.js`, `main.js`.
