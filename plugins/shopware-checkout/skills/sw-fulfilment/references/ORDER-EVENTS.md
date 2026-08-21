# Shopware 6 — Order Events

Key order-related events (subscribers, `shopware-core` → `sw-events-subscriber`):

| Event | When |
|---|---|
| `CheckoutOrderPlacedEvent` | Order completed (order exists) |
| `StateMachineStateChangeEvent` / `*StateMachineStateChangeEvent` | State transition (before/after) |
| `order.written` / `order_transaction.written` | DAL write |
| `CheckoutOrderPlacedCriteriaEvent` | Criteria used when loading the placed order |

```php
public static function getSubscribedEvents(): array {
    return [ CheckoutOrderPlacedEvent::class => 'onOrderPlaced' ];
}
```

For reactive business processes the **Flow Builder** is often the better choice (`shopware-framework` → `sw-flow-action`/`sw-flow-trigger`),
because it stays configurable. Triggering state changes: `sw-order-state-machine`. All events in the project: `sw-event-catalog`.
