# Shopware 6 — StateMachine (Order/Payment/Delivery)

Orders have three state machines: `order.state`, `order_transaction.state` (payment), `order_delivery.state` (shipping).
Transitions run through the `StateMachineRegistry` (never set the state directly).

```php
$this->stateMachineRegistry->transition(
    new Transition('order_transaction', $transactionId, 'paid', 'stateId'),
    $context
);
```

Available transitions follow from the state machine definition (e.g. `open → in_progress → completed`).
Add custom states/transitions via migration into `state_machine_state`/`state_machine_transition`. State changes fire events
(→ Flow Builder, mail). Through the Admin API: `shopware-api` (`sw-admin-api-actions`). Lifecycle events: `sw-order-events`.
