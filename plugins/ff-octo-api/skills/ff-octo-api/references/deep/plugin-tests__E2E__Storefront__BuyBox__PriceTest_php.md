# PriceTest (`tests/E2E/Storefront/BuyBox/PriceTest.php`)

## Zweck
E2E: PDP-Preis nie 0; „Ab"-Prefix ohne Units, Units erscheinen nach Datumswahl, „Ab"-Prefix verschwindet nach Unit-Auswahl. Suite **e2e-buybox**.

## Testfälle
- `testPdpPriceIsNotZero`
- `testFromPrefixShownWithoutUnits`
- `testUnitsAppearAfterDatePick`
- `testFromPrefixDisappearsAfterUnitSelection`

## Bezüge
`buy-box.plugin.js`, `price-widget.html.twig`, `Support/BuyBoxPage.php`.
