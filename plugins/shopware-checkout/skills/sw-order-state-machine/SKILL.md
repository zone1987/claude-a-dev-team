---
name: sw-order-state-machine
description: >
  Order-/Transaction-/Delivery-StateMachine in Shopware 6: Zustände & Übergänge, StateMachineRegistry.transition,
  eigene States/Transitions, mail/flow bei Statuswechsel. Trigger: "Order State", "StateMachine", "Statuswechsel Bestellung",
  "StateMachineRegistry transition", "order_transaction state", "eigener Bestellstatus", "state_machine_state". Shopware 6.7.
---

# Shopware 6 — StateMachine (Order/Payment/Delivery)

Bestellungen haben drei State-Machines: `order.state`, `order_transaction.state` (Zahlung), `order_delivery.state` (Versand).
Übergänge laufen über die `StateMachineRegistry` (nicht direktes Setzen des Status).

```php
$this->stateMachineRegistry->transition(
    new Transition('order_transaction', $transactionId, 'paid', 'stateId'),
    $context
);
```

Verfügbare Transitions ergeben sich aus der State-Machine-Definition (z.B. `open → in_progress → completed`).
Eigene States/Transitions per Migration in `state_machine_state`/`state_machine_transition`. Statuswechsel feuern Events
(→ Flow Builder, Mail). Über die Admin-API: `shopware-api` (`sw-admin-api-actions`). Lifecycle-Events: `sw-order-events`.
