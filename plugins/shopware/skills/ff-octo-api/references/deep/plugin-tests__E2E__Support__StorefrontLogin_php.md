# StorefrontLogin (`tests/E2E/Support/StorefrontLogin.php`)

## Zweck
Test-Helfer zum Einloggen eines Test-Kunden in der Storefront (für Checkout-/Order-E2E-Tests).

## Typ
- `final class StorefrontLogin`.
- Methode: `static loginAsTestCustomer(Client $client, string $baseUri): void`.

## Besonderheiten / Fallstricke
- **Session-Regeneration bei Login:** Beim Login verwirft Shopware die Session inkl. `octo-product-session-*`. Checkout-Tests müssen die OCTO-Auswahl nach dem Login (neu) setzen — siehe Memory `octo_session_login_problem`.

## Bezüge
`E2E/Storefront/Order/CheckoutOrderCommentTest.php`, `E2E/Storefront/Cart/*`, `SessionService`.
