# Shopware 6 — the order state machine

An order carries **three independent states**, each its own state machine:

| State | Technical name | Answers |
|---|---|---|
| Order | `order` | is the order open, in progress, done? |
| Transaction | `order_transaction` | was it paid? |
| Delivery | `order_delivery` | was it shipped? |

## Contents

- [Transitioning a state](#transitioning-a-state)
- [Order state transitions](#order-state-transitions)
- [Transaction state transitions](#transaction-state-transitions)
- [Delivery state transitions](#delivery-state-transitions)
- [Finding the possible transitions](#finding-the-possible-transitions)
- [A full example](#a-full-example)
- [The transaction state helper](#the-transaction-state-helper)

States are connected by **transitions**, and you cannot jump from any state to any other: an order
transaction cannot go to `refunded` before it was `paid`.

## Transitioning a state

Inject `Shopware\Core\System\StateMachine\StateMachineRegistry` and call `transition()`. It takes a
`Shopware\Core\System\StateMachine\Transition` and a `Shopware\Core\Framework\Context`.

The `Transition` constructor takes four arguments:

| # | Argument | Notes |
|---|---|---|
| 1 | the entity whose state changes | `order`, `order_transaction` or `order_delivery` — use the definition's `ENTITY_NAME` constant, so a rename upstream does not break your code |
| 2 | the entity id | the id of the order, transaction or delivery, found through its repository |
| 3 | the transition to run | the **action** name, not the resulting state — `paid`, `ship`, `process` |
| 4 | the `StateMachineStateField` name | always `stateId` in the default definitions |

**The third argument is an action, not a state.** That distinction is where most mistakes happen:
`do_pay` results in `in_progress`, and `process` results in `in_progress` too — on a different
machine.

## Order state transitions

| Transition | Resulting state |
|---|---|
| `reopen` | `open` |
| `process` | `in_progress` |
| `cancel` | `cancelled` |
| `complete` | `completed` |

```php
$this->stateMachineRegistry->transition(new Transition(
    OrderDefinition::ENTITY_NAME,
    $orderId,
    'process',
    'stateId'
), $context);
```

## Transaction state transitions

| Transition | Resulting state |
|---|---|
| `reopen` | `open` |
| `fail` | `failed` |
| `authorize` | `authorized` |
| `do_pay` | `in_progress` |
| `paid` | `paid` |
| `paid_partially` | `paid_partially` |
| `refund_partially` | `refunded_partially` |
| `refund` | `refunded` |
| `remind` | `reminded` |
| `cancel` | `cancelled` |

```php
$this->stateMachineRegistry->transition(new Transition(
    OrderTransactionDefinition::ENTITY_NAME,
    $transactionId,
    'do_pay',
    'stateId'
), $context);
```

## Delivery state transitions

| Transition | Resulting state |
|---|---|
| `reopen` | `open` |
| `ship` | `shipped` |
| `ship_partially` | `shipped_partially` |
| `cancel` | `cancelled` |
| `retour` | `returned` |
| `retour_partially` | `returned_partially` |

```php
$this->stateMachineRegistry->transition(new Transition(
    OrderDeliveryDefinition::ENTITY_NAME,
    $deliveryId,
    'ship',
    'stateId'
), $context);
```

## Finding the possible transitions

Since not every transition is available from every state — an order that never started cannot be
`reopen`ed, a delivery that never shipped cannot be refunded — ask the registry:

```php
$transitions = $this->stateMachineRegistry->getAvailableTransitions(
    OrderDefinition::ENTITY_NAME,
    $orderId,
    'stateId',
    $context
);
```

It returns the actions available now. For an order still `open` that is two entries: `cancel` and
`process`.

## A full example

Setting the delivery of an order to shipped, knowing only the order id:

```php
public function setOrderDeliveryToShipped(string $orderId, Context $context): void
{
    $criteria = new Criteria();
    $criteria->addFilter(new EqualsFilter('orderId', $orderId));

    $orderDeliveryEntityId = $this->orderDeliveryRepository->searchIds($criteria, $context)->firstId();

    $this->stateMachineRegistry->transition(new Transition(
        OrderDeliveryDefinition::ENTITY_NAME,
        $orderDeliveryEntityId,
        'ship',
        'stateId'
    ), $context);
}
```

**Beware `first()` on deliveries or transactions.** An order can have more than one of either, so
`getDeliveries()->first()` is not reliably the delivery you mean. Where it matters — the most recent
delivery, say — add filters or a sorting instead of taking the first.

## The transaction state helper

For transaction states there is a helper that saves building a `Transition` at all. It has one method
per state and takes the transaction id plus the context:

```php
$this->orderTransactionStateHandler->cancel($transactionId, $context);
$this->orderTransactionStateHandler->refund($transactionId, $context);
$this->orderTransactionStateHandler->fail($transactionId, $context);
$this->orderTransactionStateHandler->paid($transactionId, $context);
$this->orderTransactionStateHandler->payPartially($transactionId, $context);
$this->orderTransactionStateHandler->process($transactionId, $context);
$this->orderTransactionStateHandler->refundPartially($transactionId, $context);
$this->orderTransactionStateHandler->remind($transactionId, $context);
$this->orderTransactionStateHandler->reopen($transactionId, $context);
```

There is no equivalent helper for the order or delivery machines — those go through
`StateMachineRegistry`.

## Source

[developer.shopware.com/docs/guides/plugins/plugins/checkout/order/using-the-state-machine.html](https://developer.shopware.com/docs/guides/plugins/plugins/checkout/order/using-the-state-machine.html),
Shopware 6.7, retrieved 2026-08-21.
