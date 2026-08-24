# Shopware 6 — entity indexers

An indexer precomputes what would be expensive to compute on read. The core's own example is the
`cheapest_price` column on a product: a product can have variants and advanced pricing rules, so
deriving that price is complex — far too slow to do while reading 25 products for a listing. The
indexer recalculates it whenever the DAL writes the product, and reading stays cheap.

## Contents

- [The four methods](#the-four-methods)
- [Registration](#registration)
- [Synchronous or queued](#synchronous-or-queued)
- [Why not to use the DAL inside an indexer](#why-not-to-use-the-dal-inside-an-indexer)
- [Indexing through existing events](#indexing-through-existing-events)

**Prefer subscribing to an existing indexer's event over writing your own** when you only need to
react to changes of a core entity — see the last section.

## The four methods

```php
// <plugin root>/src/Core/Framework/DataAbstractionLayer/Indexing/ExampleIndexer.php
public function getName(): string
{
    return 'swag.basic.example.indexer';
}

public function iterate($offset): ?EntityIndexingMessage
{
    $iterator = $this->iteratorFactory->createIterator($this->repository->getDefinition(), $offset);

    $ids = $iterator->fetch();

    if (empty($ids)) {
        return null;
    }

    return new EntityIndexingMessage(array_values($ids), $iterator->getOffset());
}

public function update(EntityWrittenContainerEvent $event): ?EntityIndexingMessage
{
    $updates = $event->getPrimaryKeys(CustomerDefinition::ENTITY_NAME);

    if (empty($updates)) {
        return null;
    }

    return new EntityIndexingMessage(array_values($updates), null, $event->getContext());
}

public function handle(EntityIndexingMessage $message): void
{
    $ids = $message->getData();

    if (!$ids) {
        return;
    }

    foreach ($ids as $id) {
        $this->writeLog($id);
    }
}
```

| Method | When it runs |
|---|---|
| `getName` | identifies the indexer in `EntityIndexerRegistry`, deciding which messages it handles — **must be unique** |
| `iterate` | a **full** index was requested: `bin/console dal:refresh:index`, or an admin triggering an index update in the settings |
| `update` | entities were written through the DAL |
| `handle` | processes the messages `iterate` or `update` produced |

`iterate` uses `Shopware\Core\Framework\DataAbstractionLayer\Dbal\Common\IteratorFactory` to fetch
ids in batches; the offset is what keeps the amount processed at once bounded.

`update` reads the affected keys from the event. **`EntityWrittenContainerEvent` can filter by
changed column** — index only customers whose `firstname` actually changed, for instance. Narrow as
far as possible; every id that reaches `handle` costs work. `update()` is also the place for data
that must change synchronously.

Writing in `handle` goes through the connection directly:

```php
private function writeLog($customerId)
{
    $this->connection->executeStatement(
        'INSERT INTO `log_entry` (`id`, `message`, `level`, `channel`, `created_at`)
         VALUES (:id, :message, :level, :channel, now())',
        [
            'id' => Uuid::randomBytes(),
            'message' => 'Indexed customer with id: ' . $customerId,
            'level' => 1,
            'channel' => 'debug',
        ]
    );
}
```

## Registration

**The `shopware.entity_indexer` tag is what makes it run.**

```php
// <plugin root>/src/Resources/config/services.php
$services->set(ExampleIndexer::class)
    ->args([
        service(IteratorFactory::class),
        service('customer.repository'),
        service(Connection::class),
    ])
    ->tag('shopware.entity_indexer');
```

## Synchronous or queued

**Messages from `update()` are handled synchronously by default** — `handle()` runs directly
afterwards. `EntityIndexingMessage`'s fourth constructor parameter, **`$forceQueue`**, defaults to
`false`; setting it to `true` hands the message to the message queue instead.

## Why not to use the DAL inside an indexer

Indexing stays active while an indexer runs, so writing through the DAL dispatches
`EntityWrittenContainerEvent` again, which triggers the indexers again — **an infinite loop**. That
is why `handle()` should use the connection directly. The ADR on when to use plain SQL rather than
the DAL covers the reasoning.

Where the DAL is genuinely needed, disable indexing through a context state:

```php
public function update(EntityWrittenContainerEvent $event): ?EntityIndexingMessage
{
    $updates = $event->getPrimaryKeys(CustomerDefinition::ENTITY_NAME);

    if (empty($updates)) {
        return null;
    }

    $context = $event->getContext();
    $context->addState(EntityIndexerRegistry::DISABLE_INDEXING);

    return new EntityIndexingMessage(array_values($updates), null, $context);
}
```

## Indexing through existing events

Several core indexers dispatch an event from their `handle` method, and **subscribing to that is the
preferred route for the main entities** — no indexer of your own, no loop to avoid:

| Indexer | | Indexer | |
|---|---|---|---|
| `CustomerIndexer` | | `MediaIndexer` | |
| `CategoryIndexer` | | `MediaFolderIndexer` | |
| `LandingPageIndexer` | | `MediaFolderConfigurationIndexer` | |
| `ProductIndexer` | | `SalesChannelIndexer` | |
| `ProductStreamIndexer` | | `BreadcrumpIndexer` | spelled this way in the core |
| `PromotionIndexer` | | | |
| `RuleIndexer` | | | |

### Subscribing to an indexer event

```php
// <plugin root>/src/Service/Subscriber.php
public static function getSubscribedEvents(): array
{
    return [
        CustomerIndexerEvent::class => 'onCustomerIndexerHandle',
    ];
}

public function onCustomerIndexerHandle(CustomerIndexerEvent $customerIndexerEvent)
{
    $queue = new MultiInsertQueryQueue($this->connection);

    foreach ($customerIndexerEvent->getIds() as $id) {
        $this->addLog($id, $queue);
    }

    $queue->execute();
}

private function addLog($customerId, MultiInsertQueryQueue $queue)
{
    $queue->addInsert('log_entry', [
        'id' => Uuid::randomBytes(),
        'message' => 'Updated customer with id: ' . $customerId,
        'level' => 1,
        'channel' => 'debug',
    ]);
}
```

```php
$services->set(Subscriber::class)
    ->args([service(Connection::class)])
    ->tag('kernel.event_subscriber');
```

**`MultiInsertQueryQueue` batches the writes** — one statement instead of one per id, which matters
at indexer volumes.

The same rule as inside an indexer applies here, and for the same reason: the event is dispatched in
an indexer's context, so writing through the DAL would dispatch `EntityWrittenContainerEvent` and
trigger the indexer again — an infinite loop. Using `Connection` directly avoids that, and plain SQL
is considerably faster, which is what indexers need.

## Related

For the indexing system itself, incremental against full, see
[INDEXER-INDEXING.md](INDEXER-INDEXING.md). To move heavy computation onto the queue, call the Skill
tool with `sw-messaging`.

## Source

[developer.shopware.com/docs/guides/plugins/plugins/framework/data-handling/add-data-indexer.html](https://developer.shopware.com/docs/guides/plugins/plugins/framework/data-handling/add-data-indexer.html),
Shopware 6.7, retrieved 2026-08-21.
