---
name: sw-write
description: Shopware DAL writes: write events and their payloads, database migrations. Use when the request names a Shopware write event or database migration.
---

# Shopware DAL writes and migrations

Changing data and changing schema. Write events fire around every persist and are the hook for side effects.

## Reference map

- **[DATABASE-MIGRATION.md](DATABASE-MIGRATION.md)**: Schema-Änderungen laufen über `MigrationStep` in `src/Migration/`. [DATABASE-MIGRATION-MIGRATIONS](DATABASE-MIGRATION-MIGRATIONS.md).
- **[EVENTS.md](EVENTS.md)**: Jeder Write durchläuft den `EntityWriter` und dispatcht Events — der saubere Weg, um auf Datenänderungen zu r…. [EVENTS-SYSTEM](EVENTS-SYSTEM.md).

## Source

Distilled from [developer.shopware.com](https://developer.shopware.com) (Data Abstraction Layer guides and reference) plus the Shopware 6.7 source, retrieved 2026-08-20.
