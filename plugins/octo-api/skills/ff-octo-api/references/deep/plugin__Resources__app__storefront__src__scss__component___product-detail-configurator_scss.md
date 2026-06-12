# SCSS component/_product-detail-configurator.scss (`.../scss/component/_product-detail-configurator.scss`)

## Zweck
Hauptstyling der Buy-Box / des Konfigurators auf der PDP (Container, Select-Input, Details-Box, Header, Datum/Zeit/Units/Preis-Bereiche, Capacity-Limit-Alert, Availability-State). ≈253 Zeilen — die umfangreichste SCSS-Datei.

## Typ
- SCSS.

## Wichtige Klassen
`.product-detail-configurator-details` (+ `-header/-date/-time/-units/-total/-availability-state-slot`), `.product-detail-configurator-select-input`, `.detail-unit-quantity-*`, `[data-ff-capacity-limit]`.

## Besonderheiten
- Die hier gestylten Selektoren werden vom `buy-box.plugin.js` per `widgets`-Replace befüllt — Klassennamen müssen mit JS/Twig übereinstimmen.

## Bezüge
`plugin/buy-box.plugin.js`, `views/storefront/component/buy-widget/*`, `variables/*`.
