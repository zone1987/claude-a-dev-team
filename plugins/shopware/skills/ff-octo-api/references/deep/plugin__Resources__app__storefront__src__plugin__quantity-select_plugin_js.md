# FfQuantitySelectPlugin (`src/Resources/app/storefront/src/plugin/quantity-select.plugin.js`)

## Zweck
Mengensteuerung pro Unit (Plus/Minus). Publiziert synchron `octo-quantity-dom-changed` (für sofortiges Capacity-Enforcement) und debounced `octo-quantity-changed` (löst `availability/check` aus).

## Typ & Vererbung
- `export default class FfQuantitySelectPlugin extends OctoBasePlugin`
- Registriert auf `[data-ff-quantity-select]`. Optionen `unit`, `units`, `debounce` (500).

## Methoden
- `init()` — Buttons/Count-Element, debounced `_onChange`, `_toggleSubstractButton`, Events, `_publish(false)`.
- `get/set count` — liest/setzt DOM-Count (min 0); im Setter: Minus-Button toggeln, **synchron** `octo-quantity-dom-changed` publishen, debounced `_onChange`.
- `_toggleSubstractButton()` — Minus disabled bei 0.
- `_onMinusClick()` — `count -= 1`.
- `_onAddClick()` — **ignoriert Klick, wenn Plus-Button disabled** (Capacity-Limit von buy-box gesetzt); sonst `count += 1`.
- `_onChange()` → `_publish()`.
- `_publish(reload=true)` — `octo-quantity-changed {count, unit, reload}`.

## Besonderheiten / Fallstricke
- **Synchroner DOM-Event vs. debounced Server-Call:** Capacity greift sofort (DOM), `availability/check` erst nach 500ms.
- Plus-Disabled wird extern (buy-box) gesetzt → der Klick-Guard hier verhindert Überschreiten.

## Bezüge
`buy-box.plugin.js` (`_onQuantityChanged`, `_enforceCapacityLimit`), `octo-base.plugin.js`.
