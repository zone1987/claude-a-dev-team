# subscribers.xml (`src/Resources/config/subscribers.xml`)

## Zweck
Registriert die vier Event-Subscriber (Tag `kernel.event_subscriber`).

## Definierte Services
- `ProductDeleteSubscriber` — `Doctrine\DBAL\Connection`, `ff_octo_product.repository`.
- `ProductDetailSubscriber` — (keine Args).
- `ProductSaveSubscriber` — `PriceService`, `product.repository`.
- `OrderSubscriber` — `CheckoutService`, `order_transaction.repository`, `order_line_item.repository`, `OctoApiClientRegistry`.

## Bezüge
`Subscriber/*`, `../scheduled-tasks-subscribers.md`.
