# CapacityLimitTest (`tests/E2E/Storefront/BuyBox/CapacityLimitTest.php`)

## Zweck
E2E: bei erreichtem `capacity`-Limit werden Plus-Buttons disabled und der Limit-Alert sichtbar. Suite **e2e-buybox**.

## Testfälle
- `testCapacityLimitDisablesPlusAndShowsAlert`

## Bezüge
`buy-box.plugin.js` (`_enforceCapacityLimit`), `quantity-select.plugin.js`, `configurator.html.twig` (`data-ff-capacity-limit`).
