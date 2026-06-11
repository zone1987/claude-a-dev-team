# E2E Support AdminApiClient (`tests/E2E/Support/AdminApiClient.php`)

## Zweck
Test-Helfer: schlanker Shopware-Admin-API-Client für E2E-Tests (Daten-Setup/Verifikation, z.B. Order-Transaktionsstatus für Checkout-Tests).

## Typ
- `final class AdminApiClient`.
- Methoden: `get(endpoint, query=[])`, `search(entity, body)`, `postAction(endpoint, body=[])`, `transitionTransactionState(transactionId, actionName)`.

## Besonderheiten
- `transitionTransactionState` wird genutzt, um z.B. eine Zahlung auf „paid" zu setzen (triggert `OrderSubscriber::confirmOrder`).

## Bezüge
`E2E/Storefront/Order/CheckoutOrderCommentTest.php`, Shopware Admin API.
