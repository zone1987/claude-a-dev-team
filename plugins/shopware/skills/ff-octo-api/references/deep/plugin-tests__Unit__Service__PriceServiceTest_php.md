# PriceServiceTest (`tests/Unit/Service/PriceServiceTest.php`)

## Zweck
Pure Unit-Tests für `PriceService` (mockt DAL/OCTO-Clients/SystemConfig via StaticEntityRepository). Reproduziert Produktions-Bugs (0,00 €, GBP-Umrechnung, RheinKurier-Fallback). Testsuite **unit**.

## Getestete Klasse
`FfOctoApi\Service\PriceService`.

## Helfer
`makeCurrency(iso, factor)`, `buildPriceService()` (EUR 1.0 / GBP 0.8744 / USD 1.1).

## Testfälle
- `testGetLowestPriceFromEmptyUnitsReturnsEmptyArray`
- `testGetLowestPriceFromFiltersChildAndInfant` — CHILD/INFANT raus.
- `testGetLowestPriceFromFiltersAccompaniedByUnits` — Begleit-Units raus.
- `testGetLowestPriceFromPicksGbpWhenAvailableAndConvertsToEur` — GBP→EUR.
- `testGetLowestPriceFromFallsBackWhenAllNetAreZero` — 0-Fallback.
- `testGetLowestPriceFromAcrossRheinKurierFixturePicksLowestNonChild` — Offline-Fixture.
- `testGetLowestPriceWithStaticPriceFormatPicksLowest`.
- `testConstructorLoadsCurrencies`.

## Besonderheiten
- Deckt die 0,00-€-/Currency-/Begleit-Logik ab (vgl. `feedback_zero_price_never_ok`).

## Bezüge
`Service/PriceService.php`, `Unit/Fixtures/FixtureLoader.php`.
