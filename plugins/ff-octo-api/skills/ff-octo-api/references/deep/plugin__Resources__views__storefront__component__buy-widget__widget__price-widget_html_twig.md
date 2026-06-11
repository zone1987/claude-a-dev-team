# price-widget.html.twig (`.../buy-widget/widget/price-widget.html.twig`)

## Zweck
Rendert den Gesamtpreis der Buy-Box (mit optionalem „Ab"-Prefix + Tooltip) und die Steuer-Info mit Link. Wird vom Backend per `widgets`-Replace (`buy_widget_configurator_detail__price_inner`) nachgeladen.

## Block
- `octo_configurator__price` (+ `buy_widget_tax_link`).

## Inhalt
- Preis `price.retail|currency`; bei `listingPriceFrom`: Prefix `listing.listingTextFrom` + Tooltip `OctoApi.priceHint`.
- Steuer-Info (`general.grossTaxInformation`/`netTaxInformation`), Link auf Versand-/Zahlungs-CMS-Seite (AjaxModal).

## Bezüge
`plugin/buy-box.plugin.js` (`_performDomReset` stellt diesen Markup wieder her), `configurator.html.twig`, `Controller/AvailbilityController.php`.
