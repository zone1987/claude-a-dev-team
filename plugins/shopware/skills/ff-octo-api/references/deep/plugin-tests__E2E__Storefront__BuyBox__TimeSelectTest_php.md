# TimeSelectTest (`tests/E2E/Storefront/BuyBox/TimeSelectTest.php`)

## Zweck
E2E: zukünftiger Tag zeigt alle Startzeiten; Markup für „keine Startzeiten"-Hinweis existiert. Suite **e2e-buybox**.

## Testfälle
- `testFutureDayShowsAllStartTimes`
- `testEmptyStartTimesHintMarkupExists`

## Bezüge
`time-select.plugin.js`, `buy-box.plugin.js` (`_loadTimeWidget`), `configurator.html.twig` (`data-ff-empty-start-times`).
