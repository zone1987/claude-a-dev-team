---
name: sw-plain-sql-vs-dal
description: >
  Entscheidung in Shopware 6: wann DAL (Criteria/Repository) und wann plain SQL via Doctrine\DBAL\Connection.
  Trigger: "plain SQL oder DAL", "Connection executeStatement", "raw SQL shopware", "DAL vs SQL", "wann SQL benutzen",
  "Performance DAL SQL". Shopware 6.7.
---

# Shopware 6 — Plain SQL vs. DAL

**Standard ist DAL** (Events, Translations, Rechte, Cache, Indexer). Plain SQL nur in begründeten Fällen.

| DAL nutzen | Plain SQL (`Connection`) vertretbar |
|---|---|
| CRUD mit Geschäftsobjekten | Migrations (Schema) |
| API-/Store-relevante Daten | Massen-Reports / read-only Aggregate über viele Zeilen |
| alles, was Events/Cache/Indexer braucht | Performance-kritische Pfade ohne DAL-Semantik |

```php
// SQL bewusst & parametrisiert (UUID als Binary)
$rows = $this->connection->fetchAllAssociative(
    'SELECT LOWER(HEX(id)) AS id, name FROM ff_example WHERE active = 1'
);
```

Risiko bei SQL: keine Write-Events, kein Cache-Invalidation, keine Translation-/Inheritance-Logik, UUID-Binary-Handling
selbst. Schreiben fast immer über DAL (ADR „when to use plain SQL or DAL").
