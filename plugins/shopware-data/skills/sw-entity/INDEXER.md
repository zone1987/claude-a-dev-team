# Shopware 6 — Entity-Indexer

Indexer berechnen abgeleitete Daten (z.B. Aggregate, Pfade) bei Writes — inkrementell und als Full-Index
(`bin/console dal:refresh:index`). Erweitert `EntityIndexer`.

```php
class FfStatsIndexer extends EntityIndexer
{
    public function getName(): string { return 'ff.stats.indexer'; }
    public function iterate($offset): ?EntityIndexingMessage { /* full index batches */ }
    public function update(EntityWrittenContainerEvent $event): ?EntityIndexingMessage { /* affected ids */ }
    public function handle(EntityIndexingMessage $message): void { /* recompute + persist */ }
}
```

Registrierung via `shopware.entity_indexer`-Tag. Schwere Berechnung asynchron über MessageQueue (`sw-message-queue`).
Für reine Reaktionen ohne Aggregat reicht oft ein Subscriber (`sw-events-subscriber`).

→ Indexing-System, inkrementell vs. full: [INDEXER-INDEXING.md](INDEXER-INDEXING.md)
