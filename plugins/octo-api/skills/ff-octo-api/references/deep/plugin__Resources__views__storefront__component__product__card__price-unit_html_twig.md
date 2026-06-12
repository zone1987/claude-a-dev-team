# product/card/price-unit.html.twig (`src/Resources/views/storefront/component/product/card/price-unit.html.twig`)

## Zweck
Override des Listing-Preises auf Produktkarten: zeigt für OCTO-Produkte den `ff_octo_listing_price` („Ab"-Preis) statt des Standard-Unit-Preises.

## Typ
- `{% sw_extends '@Storefront/storefront/component/product/card/price-unit.html.twig' %}`

## Überschriebene Blöcke
- `component_product_box_from_price` — bei `ffOctoProduct`-Extension: `displayFrom = true`, dann `parent()`.
- `component_product_box_main_price` — `listingPrice = price.unitPrice`; bei OCTO `ff_octo_listing_price(octoProduct.product)`; rendert `|currency`; behält die Standard-List-Price-Logik.

## Besonderheiten / Fallstricke
- `ff_octo_listing_price` liefert `null` bei 0/keinem Preis → Template/`|currency` muss das vertragen (0,00-€-Schutz).

## Bezüge
`Twig/TwigFunctions.php`, `Service/PriceService.php::getLowestPriceFrom`.
