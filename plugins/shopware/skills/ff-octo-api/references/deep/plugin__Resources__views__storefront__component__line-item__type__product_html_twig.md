# line-item/type/product.html.twig (`src/Resources/views/storefront/component/line-item/type/product.html.twig`)

## Zweck
Override der Warenkorb-Line-Item-Darstellung für OCTO-Produkte: zeigt Besuchsdatum, Einlasszeit, gebuchte Units und einen Reservierungs-Countdown; ersetzt die Standard-Mengensteuerung.

## Typ
- `{% sw_extends '@Storefront/storefront/component/line-item/type/product.html.twig' %}`

## Überschriebene Blöcke
- `component_line_item_type_product_number` — `parent()` + `OctoApi.visitingDate` (payload.visitingDate), `OctoApi.entryTime` (payload.localTime), Units-Liste (`OctoApi.units.{type}`), **Reservierungs-Countdown** (`data-ff-reservation-countdown` mit `reservation.utcExpiresAt`, Notify-Route) — nur wenn nicht `offlineClient`.
- `component_line_item_type_product_col_quantity` — bei OCTO: nur Anzeige der Menge (`is-octo-product`, keine Steuerung); sonst `parent()`.

## Besonderheiten / Fallstricke
- **Override-Parallelität:** FfLondonBase überschreibt dasselbe Core-Template in einem anderen Block (`departure_date`) → mögliches doppeltes/verwirrendes Rendering bei OCTO+Departure-Date.
- Countdown entfernt das Item bei Ablauf (siehe `reservation-countdown.plugin.js`).

## Bezüge
`plugin/reservation-countdown.plugin.js`, `scss/component/_line-item.scss`, `Controller/NotificationController.php`, FfLondonBase `line-item/type/product.html.twig`.
