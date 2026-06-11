# FfTimeSelectPlugin (`src/Resources/app/storefront/src/plugin/time-select.plugin.js`)

## Zweck
Reicht die Auswahl eines Zeitslots als Event weiter. Publiziert beim Init und bei Änderung `octo-time-changed`.

## Typ & Vererbung
- `export default class FfTimeSelectPlugin extends OctoBasePlugin`
- Registriert auf `[data-ff-time-select]`. Option `route` (null).

## Methoden
- `init()` — `_registerEvents()`.
- `_registerEvents()` — `change`-Listener auf dem Select; publisht initial `octo-time-changed` mit aktuellem Wert.
- `_onTimeChange(event)` — publisht `octo-time-changed {time}`.

## Bezüge
`buy-box.plugin.js` (`_onTimeChanged`, `_loadTimeWidget`), `octo-base.plugin.js`.
