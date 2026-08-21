# Shopware 6 — Plain SQL vs. DAL

**The DAL is the default** (events, translations, permissions, cache, indexers). Use plain SQL only in justified cases.

| Use the DAL | Plain SQL (`Connection`) is defensible |
|---|---|
| CRUD on business objects | migrations (schema) |
| API/Store-relevant data | bulk reports / read-only aggregates across many rows |
| anything that needs events/cache/indexers | performance-critical paths without DAL semantics |

```php
// SQL used deliberately and parameterized (UUID as binary)
$rows = $this->connection->fetchAllAssociative(
    'SELECT LOWER(HEX(id)) AS id, name FROM ff_example WHERE active = 1'
);
```

The risk with SQL: no write events, no cache invalidation, no translation/inheritance logic, and UUID binary handling
is on you. Almost always write through the DAL (ADR "when to use plain SQL or DAL").
