# Shopware 6 — Order-Events

Wichtige Events rund um Bestellungen (Subscriber, `shopware-core` → `sw-events-subscriber`):

| Event | Wann |
|---|---|
| `CheckoutOrderPlacedEvent` | Bestellung abgeschlossen (Order existiert) |
| `StateMachineStateChangeEvent` / `*StateMachineStateChangeEvent` | Status-Übergang (vor/nach) |
| `order.written` / `order_transaction.written` | DAL-Write |
| `CheckoutOrderPlacedCriteriaEvent` | Criteria beim Laden der platzierten Bestellung |

```php
public static function getSubscribedEvents(): array {
    return [ CheckoutOrderPlacedEvent::class => 'onOrderPlaced' ];
}
```

Für reaktive Geschäftsabläufe oft besser der **Flow Builder** (`shopware-framework` → `sw-flow-action`/`sw-flow-trigger`),
da konfigurierbar. Statuswechsel auslösen: `sw-order-state-machine`. Alle Events im Projekt: `sw-event-catalog`.
