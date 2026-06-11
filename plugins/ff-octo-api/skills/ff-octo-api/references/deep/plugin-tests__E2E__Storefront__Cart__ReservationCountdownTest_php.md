# ReservationCountdownTest (`tests/E2E/Storefront/Cart/ReservationCountdownTest.php`)

## Zweck
E2E: Reservierungs-Countdown wird für Online-Provider gezeigt, für Offline (RheinKurier) verborgen. Suite **e2e-cart**.

## Testfälle
- `testCountdownIsShownForOnlineProvider`
- `testCountdownIsHiddenForOfflineProvider`

## Bezüge
`reservation-countdown.plugin.js`, `line-item/type/product.html.twig` (offlineClient-Bedingung).
