# Shopware 6 — Entity indexer

Indexers compute derived data (aggregates, paths, and so on) on writes — incrementally and as a full index
(`bin/console dal:refresh:index`). Extend `EntityIndexer`.

```php
class FfStatsIndexer extends EntityIndexer
{
    public function getName(): string { return 'ff.stats.indexer'; }
    public function iterate($offset): ?EntityIndexingMessage { /* full index batches */ }
    public function update(EntityWrittenContainerEvent $event): ?EntityIndexingMessage { /* affected ids */ }
    public function handle(EntityIndexingMessage $message): void { /* recompute + persist */ }
}
```

Register it with the `shopware.entity_indexer` tag. Move heavy computation to the message queue (`sw-message-queue`).
For plain reactions without an aggregate, a subscriber is often enough (`sw-events-subscriber`).

→ Indexing system, incremental vs. full: [INDEXER-INDEXING.md](INDEXER-INDEXING.md)
