# configurator.html.twig (`src/Resources/views/storefront/component/buy-widget/configurator.html.twig`)

## Zweck
Kern-Template der OCTO-Buy-Box. Rendert für OCTO-Produkte den kompletten Konfigurator (Datum, Availability-State, Units, Startzeiten, Preis, Buy-Btn, Capacity-Limit) und stellt `data-ff-buy-box` + Optionen (Routen) bereit. Definiert die vom Backend per `widgets`-Replace adressierten Blöcke.

## Typ
- `{% extends '@Storefront/storefront/component/buy-widget/configurator.html.twig' %}`

## Überschriebene/definierte Blöcke
- `buy_widget_configurator_group` — bei OCTO: Core-`select.html.twig` in `.product-detail-configurator-group`; sonst `parent()`.
- `buy_widget_configurator` — bei OCTO: `parent()` + `data-ff-buy-box`-Box mit `ffBuyBoxOptions` (apiProduct, product, selector, **routes**: `checkAvailability`, session get/set/remove). Enthält die inneren Blöcke:
  - `buy_widget_configurator_detail__booking_date` (booking-date-widget), `__availability_state(_inner)` (Alert `OctoApi.availability.state.{status}`), `__empty_units`, `__capacity_limit` (`data-ff-capacity-limit` + `…-template` `OctoApi.capacity.limitReached`), `__units(_inner)` (unit-widget), `__start_times` (`data-ff-time-select`), `__empty_start_times` (`data-ff-empty-start-times`), `__price(_inner)` (price-widget; berechnet `listingPriceFrom`/`price` aus `ff_octo_listing_price`), `__buy_btn` (Core `buy-widget-form.html.twig`), Loading-Spinner.

## Vom Backend nachgeladene Block-Selektoren (`AvailbilityController`)
`buy_widget_configurator_detail__units_inner`, `__price_inner`, `__availability_state_inner` → DOM `.product-detail-configurator-details-units` / `-total` / `-availability-state-slot`.

## Besonderheiten / Fallstricke
- **Override-Konflikt:** FfLondonBase fügt im selben Core-Template einen `departure_date`/`arrivalDate`-Block hinzu; FfOctoApi wrappt den ganzen Group-Block in die OCTO-Bedingung → für OCTO-Produkte wird der FfLondonBase-Block evtl. nicht gerendert.
- Block-/Klassennamen müssen mit `buy-box.plugin.js` und SCSS übereinstimmen.

## Bezüge
`buy-widget.html.twig`, `widget/{booking-date,unit,price}-widget.html.twig`, `plugin/buy-box.plugin.js`, `Controller/AvailbilityController.php`, FfLondonBase `configurator.html.twig`.
