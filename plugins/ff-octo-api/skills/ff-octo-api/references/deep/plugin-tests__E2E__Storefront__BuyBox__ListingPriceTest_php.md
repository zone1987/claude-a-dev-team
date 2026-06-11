# ListingPriceTest (`tests/E2E/Storefront/BuyBox/ListingPriceTest.php`)

## Zweck
E2E: Listing zeigt für ein Referenzprodukt einen Nicht-Null-Preis (0,00-€-Schutz). Suite **e2e-buybox**.

## Testfälle
- `testListingShowsNonZeroPriceForReferenceProduct`

## Bezüge
`price-unit.html.twig`, `TwigFunctions::ff_octo_listing_price`, `feedback_zero_price_never_ok`.
