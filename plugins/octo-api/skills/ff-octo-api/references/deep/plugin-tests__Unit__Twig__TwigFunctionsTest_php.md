# TwigFunctionsTest (`tests/Unit/Twig/TwigFunctionsTest.php`)

## Zweck
Unit-Tests für `TwigFunctions` (`ff_octo_listing_price`). Testsuite **unit**.

## Getestete Klasse
`FfOctoApi\Twig\TwigFunctions`.

## Testfälle
- `testReturnsNullForNullInput`, `testReturnsNullForEmptyArray`, `testReturnsNullWhenNoOptions`, `testReturnsNullWhenOptionsHaveNoUnits`
- `testReturnsNullWhenPriceServiceReturnsZeroRetail` — 0,00-€-Schutz.
- `testReturnsRetailInMajorUnits`, `testReturnsRetailWithDefaultPrecisionWhenMissing`
- `testFlattensUnitsAcrossMultipleOptions`
- `testIntegratesWithRheinKurierFixture`
- `testRegistersFfOctoListingPriceFunction`

## Bezüge
`Twig/TwigFunctions.php`, `Service/PriceService.php`.
