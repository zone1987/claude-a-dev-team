# ProductSaveSubscriberTest (`tests/Integration/Subscriber/ProductSaveSubscriberTest.php`)

## Zweck
Integration-Tests für `ProductSaveSubscriber` (Preis-Update + Rekursionsschutz). Testsuite **integration**.

## Testfälle
- `testSubscribesToProductWrittenEvent`
- `testRecursionGuardSkipsWhenExtensionPresent` — `octo_price_update`-Guard.
- `testNoActionWhenProductIsNotOcto`

## Bezüge
`Subscriber/ProductSaveSubscriber.php`, `Service/PriceService.php`.
