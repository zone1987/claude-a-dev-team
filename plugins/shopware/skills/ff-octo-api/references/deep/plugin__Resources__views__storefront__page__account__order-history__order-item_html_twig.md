# order-item.html.twig (`.../page/account/order-history/order-item.html.twig`)

## Zweck
Override der Account-Bestellhistorie: aktiviert den „Bestellung stornieren"-Button nur, wenn mindestens ein LineItem `cancellable` ist (von `OrderSubscriber::onAccountOrderPageLoadedEvent` gesetzt).

## Typ
- `{% sw_extends '@Storefront/storefront/page/account/order-history/order-item.html.twig' %}`

## Überschriebener Block
- `page_account_order_item_context_menu_cancel_order` — `isCancellable` = es gibt ein LineItem mit `payload.cancellable === true`; Button `disabled` wenn nicht stornierbar; nur bei nicht-cancelled Order + `core.cart.enableOrderRefunds`.

## Besonderheiten
- `cancellable` stammt aus dem OCTO-`getBooking`-Call im `OrderSubscriber`.

## Bezüge
`Subscriber/OrderSubscriber.php` (`onAccountOrderPageLoadedEvent`), `Service/CheckoutService.php::cancelOrder`.
