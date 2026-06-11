# ListingSmokeTest (`tests/E2E/Storefront/Smoke/ListingSmokeTest.php`)

## Zweck
E2E-Smoke: **jedes** OCTO-Produkt im Listing hat einen Nicht-Null-Preis (harter 0,00-€-Regressionsschutz). Suite **e2e-smoke**.

## Testfälle
- `testEveryOctoProductInListingHasNonZeroPrice`

## Besonderheiten
- Direkte Umsetzung der „0,00 € ist nie ok"-Regel über das gesamte Listing.

## Bezüge
`TwigFunctions::ff_octo_listing_price`, `PriceService`, `feedback_zero_price_never_ok`.
