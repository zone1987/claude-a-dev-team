# CheckoutOrderCommentTest (`tests/E2E/Storefront/Order/CheckoutOrderCommentTest.php`)

## Zweck
E2E: Checkout schreibt den internen Order-Kommentar (Audit-Trail) — einzelnes GoldenTours-Ticket und gemischter Provider-Warenkorb. Suite **e2e-order**.

## Testfälle
- `testSingleGoldenToursTicketCheckoutWritesInternalComment`
- `testMixedProviderCartCheckoutWritesCommentsForAllItems`

## Besonderheiten
- Checkout-Tests mit **Vorkasse** (Projektregel). Prüft `CheckoutService::confirmOrder` → `addInternalComments`.

## Bezüge
`Service/CheckoutService.php`, `Subscriber/OrderSubscriber.php`, `feedback_test_payment_method`.
