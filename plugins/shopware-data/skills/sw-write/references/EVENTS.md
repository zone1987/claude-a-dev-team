# Shopware 6 — Write system and events

Every write (`create/update/upsert/delete`) passes through the `EntityWriter` and dispatches events — the clean
way to react to data changes (instead of polling or decorators).

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
