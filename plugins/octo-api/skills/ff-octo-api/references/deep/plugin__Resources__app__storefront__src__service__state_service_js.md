# StateService (Storefront) (`src/Resources/app/storefront/src/service/state.service.js`)

## Zweck
Verwaltet die Lade-States der Buy-Box (calendar/availability/date) und schaltet die `is-loading`-CSS-Klasse am Element. Reagiert auf `octo-state-change`-Events.

## Typ
- `export default class StateService`

## Felder
- `#_loadingStates` (availability/calendar/date: false), `#_el`, `#_loading` (Proxy), `#_isLoading` (Proxy).

## Methoden
- `constructor(element)` — baut zwei Proxies: `#_isLoading` toggelt `is-loading`-Klasse; `#_loading` validiert Keys und berechnet `isLoading` als OR aller States. Abonniert `octo-state-change`.
- `#_onLoadPartial(event)` — setzt `#_loading[key] = value` (wirft bei ungültigem Key).

## Besonderheiten
- Pro sichtbarer Buy-Box wird im Loader eine eigene Instanz erzeugt.

## Bezüge
`loader/buy-box.loader.js`, `octo-api.service.js` (publisht `octo-state-change`).
