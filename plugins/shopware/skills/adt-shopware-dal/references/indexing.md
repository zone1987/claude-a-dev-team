# Indexing System

## EntityIndexer (abstract)

Contract for all entity indexers. Supports full reindexing and incremental updates.

### Abstract Methods

| Method | Returns | Description |
|---|---|---|
| `getName()` | `string` | Unique indexer identifier |
| `iterate(?array $offset)` | `?EntityIndexingMessage` | Full-index: batched messages, returns null when done |
| `update(EntityWrittenContainerEvent $event)` | `?EntityIndexingMessage` | Incremental: reacts to write events |
| `handle(EntityIndexingMessage $message)` | `void` | Processes index messages |
| `getTotal()` | `int` | Total record count for progress |
| `getDecorated()` | `EntityIndexer` | Decorator pattern |

`getOptions(): array` returns sub-indexer names for selective skip/only logic.

## EntityIndexerRegistry

Central orchestrator. Message handler for `EntityIndexingMessage`, `IterateEntityIndexerMessage`, `FullEntityIndexerMessage`.

### Context States

| Constant | Purpose |
|---|---|
| `EXTENSION_INDEXER_SKIP` | Skip specific indexers |
| `EXTENSION_INDEXER_ONLY` | Run only specific indexers |
| `USE_INDEXING_QUEUE` | Force queue mode |
| `DISABLE_INDEXING` | Completely disable indexing |

### Key Methods

- `index(bool $useQueue, array $skip, array $only, bool $postUpdate)` - full reindex
- `refresh(EntityWrittenContainerEvent $event)` - incremental update (called by EntityIndexingSubscriber)

### Integration

`EntityIndexingSubscriber` listens to `EntityWrittenContainerEvent` with priority 1000 and calls `refresh()`.

## Built-in Updaters

### ChildCountUpdater

Updates `child_count` column on parent entities. SQL: COUNT children per parent_id.

### InheritanceUpdater

Updates inheritance columns. For ToMany associations: `IFNULL` to child's own data or parent. For ManyToOne: cascade FK from parent if child is null.

### ManyToManyIdFieldUpdater

Maintains denormalized `ManyToManyIdField` JSON columns with IDs from the many-to-many relation.

### TreeUpdater

Maintains tree data: materialized `path` (pipe-delimited) and `level` (depth integer, 1-based). Recursive parent loading up to 100 levels.

## PostUpdateIndexer

Abstract. Never reacts to individual writes (`update()` returns null). Runs only during full reindex with `$postUpdate = true`.

## SynchronousPostUpdateIndexer

Extends `PostUpdateIndexer`. Marker class that runs synchronously instead of through message queue.
