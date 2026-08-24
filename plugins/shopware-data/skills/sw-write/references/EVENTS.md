# Shopware 6 — Write system and events

Every write (`create/update/upsert/delete`) passes through the `EntityWriter` and dispatches events — the clean
way to react to data changes (instead of polling or decorators).

## Contents

- [Batch events](#batch-events)
- [EntityWriteEvent](#entitywriteevent)
- [EntityDeleteEvent](#entitydeleteevent)
- [Per-entity events](#per-entity-events)
- [Event classes](#event-classes)

Every event is nested inside a container event, so **a subscriber is called once per operation** —
one call for a search request rather than thirty.

```php
public static function getSubscribedEvents(): array
{
    return [
        'ff_example.written' => 'onWritten',          // EntityWrittenEvent (one entity)
        EntityWrittenContainerEvent::class => 'onAny', // all entities of one write
        'ff_example.deleted' => 'onDeleted',
    ];
}
public function onWritten(EntityWrittenEvent $event): void {
    foreach ($event->getWriteResults() as $r) { $id = $r->getPrimaryKey(); $payload = $r->getPayload(); }
}
```

Use `{entity}.written/.deleted` for targeted reactions; the container event for a transaction-wide view. Validate and
manipulate before the write via `PreWriteValidationEvent`/`BeforeWriteEvent`. Run heavy follow-up work async (`sw-message-queue`).

→ Write pipeline, commands, all events: [EVENTS-SYSTEM.md](EVENTS-SYSTEM.md)

## Batch events

Two events fire around batches of commands rather than a single entity:

| Event | When |
|---|---|
| `Shopware\Core\Framework\DataAbstractionLayer\Event\EntityWriteEvent` | before a batch of commands is written — inserted, updated or deleted |
| `Shopware\Core\Framework\DataAbstractionLayer\Event\EntityDeleteEvent` | before a batch of delete commands runs |

Both let you run code **before and after** the operation through `addSuccess` and `addError`, each
taking any PHP callable. That is what makes them the right place when you need the state *before* the
write — an old filename, for instance, to remove from a CDN.

## EntityWriteEvent

```php
// <plugin root>/src/Subscriber/EntityWriteSubscriber.php
use Psr\Log\LoggerInterface;
use Symfony\Component\EventDispatcher\EventSubscriberInterface;

class EntityWriteSubscriber implements EventSubscriberInterface
{
public function __construct(private readonly LoggerInterface $logger)
{
}

public static function getSubscribedEvents(): array
{
    return [EntityWriteEvent::class => 'beforeWrite'];
}

public function beforeWrite(EntityWriteEvent $event)
{
    // ids of one entity type — the event fires for batches, so filter
    $ids = $event->getIds(CmsPageDefinition::ENTITY_NAME);

    // or every id about to be written, whatever the type
    $ids = $event->getIds();

    // the payloads; note that a DeleteCommand has none
    $payloads = array_map(fn (WriteCommand $command) => $command->getPayload(), $event->getCommands());

    // or for one entity type
    $payloads = array_map(
        fn (WriteCommand $command) => $command->getPayload(),
        $event->getCommandsForEntity(CmsPageDefinition::ENTITY_NAME)
    );

    $event->addSuccess(function () use ($ids) {
        $this->logger->info(sprintf('Entities with ids: "%s" were written', implode(', ', $ids)));
    });

    $event->addError(function () use ($ids) {
        $this->logger->critical(sprintf('Entities with ids: "%s" were not written', implode(', ', $ids)));
    });
}
}
```

**A `DeleteCommand` carries no payload** — asking for one gets you nothing, which is easy to miss when
a batch mixes writes and deletes.

## EntityDeleteEvent

Same shape, delete only. Useful for capturing state before removal — collect a name, then use it
afterwards to remove the record from a third-party system:

```php
// <plugin root>/src/Subscriber/DeleteSubscriber.php
public function beforeDelete(EntityDeleteEvent $event)
{
    $ids = $event->getIds(CmsPageDefinition::ENTITY_NAME);

    $event->addSuccess(function () use ($ids) {
        $this->cache->purge($ids);
    });

    $event->addError(function () use ($ids) {
        // log, notify, whatever the failure needs
    });
}
```

Register either with `kernel.event_subscriber`:

```php
$services->set(ProductSubscriber::class)
    ->tag('kernel.event_subscriber');
```

## Per-entity events

Every entity dispatches these; the part before the dot is the entity name. Shown for `product`:

| Event | When | Class |
|---|---|---|
| `product.written` | after the data reached storage | `EntityWrittenEvent` |
| `product.deleted` | after the data was deleted in storage | `EntityDeletedEvent` |
| `product.loaded` | after the data was hydrated into objects | `EntityLoadedEvent` |
| `product.search.result.loaded` | after a search returned data | `EntitySearchResultLoadedEvent` |
| `product.aggregation.result.loaded` | after aggregations were loaded | `EntityAggregationResultLoadedEvent` |
| `product.id.search.result.loaded` | after an id-only search finished | `EntityIdSearchResultLoadedEvent` |

All live under `Shopware\Core\Framework\DataAbstractionLayer\Event\`. What each carries:

| Event | Provides |
|---|---|
| `written` | the definition's reference class, the data written, the context, the affected primary keys, any errors |
| `deleted` | the definition's reference class, the context, the affected primary keys, any errors |
| `loaded` | the definition's reference class, the context, the hydrated entities |
| `search.result.loaded` | the reference class, the context, and the search result object with its count, criteria and entities |
| `aggregation.result.loaded` | the aggregation results, the criteria searched with, the context |
| `id.search.result.loaded` | the reference class and the context |

## Event classes

**Every stock entity ships an event class of constants** — `ProductEvents` for the product. Using
them gives autocompletion, and it insulates the subscriber from an event name changing upstream:

```php
// <plugin root>/src/Subscriber/ProductSubscriber.php
public static function getSubscribedEvents(): array
{
    return [
        ProductEvents::PRODUCT_LOADED_EVENT => 'onLoad',
        ProductEvents::PRODUCT_WRITTEN_EVENT => 'afterWrite',
    ];
}

public function onLoad(EntityLoadedEvent $event)
{
    // ...
}

public function afterWrite(EntityWrittenEvent $event)
{
    // ...
}
```

Prefer the constant over the literal `'product.written'` string.

## Source

[developer.shopware.com/docs/guides/plugins/plugins/framework/data-handling/using-database-events.html](https://developer.shopware.com/docs/guides/plugins/plugins/framework/data-handling/using-database-events.html),
Shopware 6.7, retrieved 2026-08-21.
