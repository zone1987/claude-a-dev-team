# OctoCartCollectorTest (`tests/Integration/Cart/OctoCartCollectorTest.php`)

## Zweck
Integration-Tests für `OctoCartCollector` (Cart-Preisberechnung). Testsuite **integration**.

## Getestete Klasse
`FfOctoApi\Core\Checkout\Cart\OctoCartCollector`.

## Testfälle
- `testNonOctoLineItemsAreLeftUntouched`
- `testOctoLineItemWithMatchingSessionGetsPriceRecalculated`
- `testOctoLineItemWithoutSessionFallsBackToPayloadUnits`
- `testIsDefaultVariantWithParentLabelRenamesLineItem`

## Bezüge
`Core/Checkout/Cart/OctoCartCollector.php`.
