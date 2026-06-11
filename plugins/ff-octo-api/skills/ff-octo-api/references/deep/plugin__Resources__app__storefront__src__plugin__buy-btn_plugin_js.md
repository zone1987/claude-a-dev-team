# BuyBtnPlugin (`src/Resources/app/storefront/src/plugin/buy-btn.plugin.js`)

## Zweck
Steuert das Enable/Disable des „In den Warenkorb"-Buttons der Buy-Box anhand des Auswahl-States (Datum, ggf. Zeit, gültige Units). Nutzt einen Proxy, der bei jeder State-Änderung neu validiert.

## Typ & Vererbung
- `export default class BuyBtnPlugin extends OctoBasePlugin`
- Registriert auf `.buy-widget button.btn-buy` (Option `selected`, `timeRequired`).

## Methoden
- `init()` — `_registerProxies()`, `_registerEvents()`.
- `_registerProxies()` — `Proxy` auf `options.selected`; bei `set`: validiert
  - Datum gewählt,
  - Zeit gewählt **wenn** `timeRequired`,
  - mindestens eine **Standalone-Unit** (kein `restrictions.accompaniedBy`; CHILD/INFANT mit accompaniedBy-IDs zählen allein nicht). Fehlt `restrictions` → als standalone behandelt.
  - → `_show()`/`_hide()`.
- `_show()/_hide()` — toggelt `disabled`.
- `_registerEvents()` — `octo-date-changed`, `octo-time-changed`, `octo-units-changed`.
- `_onDateChanged` — akzeptiert `selectedDate` **oder** `date` (Kompatibilität).
- `_onTimeChanged`, `_onUnitsChanged` — setzen Proxy-Werte.

## Besonderheiten / Fallstricke
- **Begleitpersonen-Regel:** ohne Standalone-Unit bleibt der Button disabled (CHILD/INFANT brauchen Erwachsene).
- Reagiert auf `octo-units-changed` (von `buy-box.plugin.js` publiziert, inkl. `restrictions`).

## Bezüge
`buy-box.plugin.js`, `octo-base.plugin.js`, Twig `buy-widget.html.twig`.
