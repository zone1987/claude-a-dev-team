# BuyBoxPluginRegistry (`src/Resources/app/storefront/src/struct/buy-box-plugin-registry.struct.js`)

## Zweck
Verwaltet die Child-Plugins der Buy-Box (Registrierung, Initialisierung, Deregistrierung). Bindet Selektoren an den CMS-Block, damit nur die korrekte (sichtbare) Buy-Box adressiert wird.

## Typ
- `export default class BuyBoxPluginRegistry`

## Felder
- `#_plugins` (BuyBoxPlugin[]), `#_cmsBlock`.

## Methoden
- `constructor(cmsBlock)`.
- `add(name, plugin, selector, options={})` — präfixt den Selector mit den CMS-Block-Klassen, legt `BuyBoxPlugin` an.
- `initializePlugins()` — pro Plugin: registriert oder (falls vorhanden) initialisiert über PluginManager.
- `deregisterPlugins()` — räumt Instanzen ab + `PluginManager.deregister`.
- `#_initializePlugin/#_registerPlugin` — PluginManager-Wrapper (+ octoDebug-Logs).
- `#_destroyInstancesForSelector(plugin)` — entfernt Instanzen aus `el.__plugins` und der Instanzliste (sonst nur No-Op `_update()` beim Re-Init).

## Besonderheiten
- Sauberes Instanz-Cleanup ist nötig für korrekte Re-Inits bei Viewport-Wechsel (vgl. `BuyBoxLoader`).

## Bezüge
`buy-box-plugin.struct.js`, `buy-box.plugin.js`, `loader/buy-box.loader.js`.
