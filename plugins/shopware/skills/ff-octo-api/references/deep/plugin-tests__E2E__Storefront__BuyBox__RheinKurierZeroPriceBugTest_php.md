# RheinKurierZeroPriceBugTest (`tests/E2E/Storefront/BuyBox/RheinKurierZeroPriceBugTest.php`)

## Zweck
E2E-Regressionstest für den RheinKurier-0,00-€-Bug: PDP zeigt nach JS-Init keinen Nullpreis; Availability-Check-Response enthält Nicht-Null-Preis. Suite **e2e-buybox**.

## Testfälle
- `testInitialPdpDoesNotShowZeroPriceAfterJsInit`
- `testAvailabilityCheckResponseContainsNonZeroPrice`

## Besonderheiten
- Direkter Regressionsschutz für den Offline-Fallback in `PriceService`.

## Bezüge
`Service/PriceService.php`, `Client/Octo/RheinKurierClient.php`, `../appserver-integration.md`, `feedback_zero_price_never_ok`.
