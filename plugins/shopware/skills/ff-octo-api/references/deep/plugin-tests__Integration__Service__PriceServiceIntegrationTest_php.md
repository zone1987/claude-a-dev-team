# PriceServiceIntegrationTest (`tests/Integration/Service/PriceServiceIntegrationTest.php`)

## Zweck
Integration-Tests für `PriceService` gegen echte DAL/Container. Testsuite **integration**.

## Testfälle
- `testUpdatePricesSetsProductPriceFromApiProduct`
- `testUpdatePricesHandlesMissingTopLevelIdViaFallback` — RheinKurier-Fallback.
- `testGetLowestPriceExcludesChildAndInfantUnits`
- `testGetLowestPriceSkipsZeroPriceUnits` — 0,00-€-Schutz.
- `testGetLowestPriceExcludesAccompaniedUnits`

## Bezüge
`Service/PriceService.php`.
