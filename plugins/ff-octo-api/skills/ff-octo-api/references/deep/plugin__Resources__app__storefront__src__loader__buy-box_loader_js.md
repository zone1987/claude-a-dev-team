# BuyBoxLoader (`src/Resources/app/storefront/src/loader/buy-box.loader.js`)

## Zweck
Stellt sicher, dass `FfBuyBoxPlugin` **nur auf der aktuell sichtbaren** BuyBox läuft. Auf der PDP existieren zwei CMS-Blöcke (Mobile / Tablet+Desktop) parallel im DOM — ohne diesen Loader würden beide instanziiert und doppelte Requests absetzen. Reagiert auf `window.resize` und deregistriert bei Viewport-Wechsel sauber die alte Instanz.

## Typ
- `export default class BuyBoxLoader`

## Statische Felder
- `#pluginName = 'FfBuyBox'`, `#activeBuyBoxEl = null`, `#pluginRegistered = false`.

## Methoden
- `static load()` — registriert `resize`-Listener, ruft `#syncActiveBuyBox()`.
- `static #syncActiveBuyBox()` — findet sichtbares Element; wenn neu, deaktiviert altes, aktiviert neues.
- `static #findVisibleBuyBoxElement()` — `[data-ff-buy-box]`, deren `.cms-block` `display !== none`.
- `static #activate(el)` — baut Selektor aus den CMS-Block-Klassen, ermittelt `viewports` aus `hidden-*`-Klassen, instanziiert `StateService`, registriert (einmalig) + initialisiert das Plugin.
- `static #deactivate(el)` — entfernt die Plugin-Instanz aus `el.__plugins` und aus der PluginManager-Instanzliste, damit eine frische Instanz erzeugt werden kann.

## Besonderheiten / Fallstricke
- **Doppel-Init-Vermeidung** ist der Kernzweck — bei Änderungen an der Buy-Box-Struktur (CMS-Block-Klassen, `data-ff-buy-box`) hier nachziehen.
- Deaktivierung greift in PluginManager-Interna (`getPluginInstancesFromElement`, `plugin.get('instances')`).

## Bezüge
`plugin/buy-box.plugin.js`, `service/state.service.js`, Twig `buy-widget.html.twig` (CMS-Block + `data-ff-buy-box`), `../storefront-javascript.md`.
