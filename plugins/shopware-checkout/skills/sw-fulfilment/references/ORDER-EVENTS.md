# Shopware 6 — Order Events

Key order-related events (subscribers, `shopware-core` → `sw-events-subscriber`):

| Event | When |
|---|---|
| `CheckoutOrderPlacedEvent` | Order completed (order exists) |
| `StateMachineStateChangeEvent` / `*StateMachineStateChangeEvent` | State transition (before/after) |
| `order.written` / `order_transaction.written` | DAL write |
| `CheckoutOrderPlacedCriteriaEvent` | Criteria used when loading the placed order |

## Contents

- [Reacting to a written order](#reacting-to-a-written-order)
- [Reading the changeset](#reading-the-changeset)

```php
public static function getSubscribedEvents(): array {
    return [ CheckoutOrderPlacedEvent::class => 'onOrderPlaced' ];
}
```

For reactive business processes the **Flow Builder** is often the better choice (`shopware-framework` → `sw-flow-action`/`sw-flow-trigger`),
because it stays configurable. For triggering state changes see `ORDER-STATE-MACHINE.md`. To map every event in a project, run `/sw-event-map`.

## Reacting to a written order

`OrderEvents` holds the constants for every order-related write event; `ORDER_WRITTEN_EVENT` is the
one for general changes to the order itself.

```php
// <plugin root>/src/Service/ListenToOrderChanges.php
use Symfony\Component\EventDispatcher\EventSubscriberInterface;

public static function getSubscribedEvents(): array
{
    return [
        OrderEvents::ORDER_WRITTEN_EVENT => 'onOrderWritten',
    ];
}

public function onOrderWritten(EntityWrittenEvent $event): void
{
    // only react to the live version
    if ($event->getContext()->getVersionId() !== Defaults::LIVE_VERSION) {
        return;
    }

    // ...
}
```

**The version check is not optional.** Editing an order in the administration creates a new draft
version, merged into the live version on save. Without the check a subscriber fires on the draft
too — usually not the state you want to react to.

## Reading the changeset

**A changeset is not on the event by default**, for performance reasons: nothing records what
changed unless something asks for it. Requesting one takes a second subscriber on
`PreWriteValidationEvent`, which fires before the write result set is generated.

```php
public static function getSubscribedEvents(): array
{
    return [
        PreWriteValidationEvent::class => 'triggerChangeSet',
        OrderEvents::ORDER_WRITTEN_EVENT => 'onOrderWritten',
    ];
}

public function triggerChangeSet(PreWriteValidationEvent $event): void
{
    if ($event->getContext()->getVersionId() !== Defaults::LIVE_VERSION) {
        return;
    }

    foreach ($event->getCommands() as $command) {
        if (!$command instanceof ChangeSetAware) {
            continue;
        }

        if ($command->getEntityName() !== OrderDefinition::ENTITY_NAME) {
            continue;
        }

        $command->requestChangeSet();
    }
}
```

Both narrowing steps matter, and both are about cost:

- **`ChangeSetAware`** — an insert command cannot produce a changeset, since nothing changed; a whole
  entity is new.
- **The entity check** — generating a changeset costs performance, so request it for the one entity
  the subscriber cares about, never broadly.

The changeset is then available on each write result:

```php
public function onOrderWritten(EntityWrittenEvent $event): void
{
    if ($event->getContext()->getVersionId() !== Defaults::LIVE_VERSION) {
        return;
    }

    foreach ($event->getWriteResults() as $result) {
        $changeSet = $result->getChangeSet();
        // ...
    }
}
```

## Source

[developer.shopware.com/docs/guides/plugins/plugins/checkout/order/listen-to-order-changes.html](https://developer.shopware.com/docs/guides/plugins/plugins/checkout/order/listen-to-order-changes.html),
Shopware 6.7, retrieved 2026-08-21.
