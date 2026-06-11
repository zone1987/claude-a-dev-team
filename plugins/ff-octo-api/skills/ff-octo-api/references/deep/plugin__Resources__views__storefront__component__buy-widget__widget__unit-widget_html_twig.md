# unit-widget.html.twig (`.../buy-widget/widget/unit-widget.html.twig`)

## Zweck
Rendert pro Unit eine Zeile mit Titel/Untertitel (Altersangaben), Begleitpersonen-Hinweis, „Ab"-Preis und Mengensteuerung (`data-ff-quantity-select`). Wird vom Backend per `widgets`-Replace (`buy_widget_configurator_detail__units_inner`) nachgeladen.

## Block
- `octo_configurator__units` (importiert Macro `accompanied_by`).

## Inhalt (pro Unit)
- `quantitySelectOptions` (unit, units, productId, session-Routen).
- Titel `OctoApi.units.{type}` (bzw. `unit.title` bei `OTHER`); Subtitle aus `restrictions.minAge/maxAge` (Snippets `OctoApi.unit.subtitle`/`shortSubtitle`).
- `accompanied_by(units, unit)` (Begleitpersonen).
- Preis `OctoApi.configuratorDetails.from` + `unit.price.retail|currency`.
- Quantity-Box: `.detail-unit-quantity-subtract/-count/-add`.
- `data-ff-browser-translation` + `.translatable` (Browser-Übersetzung).

## Bezüge
`macros/accompanied-by.html.twig`, `plugin/quantity-select.plugin.js`, `plugin/browser-translation.plugin.js`, `Controller/AvailbilityController.php`.
