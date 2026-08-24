---
name: sw-write
description: Shopware DAL writes: write events and their payloads, database migrations. Use when the request names a Shopware write event or database migration.
---

# Shopware DAL writes and migrations

Changing data and changing schema. Write events fire around every persist and are the hook for side effects.

## Reference map

- **[DATABASE-MIGRATION.md](references/DATABASE-MIGRATION.md)**: Schema changes run through `MigrationStep` in `src/Migration/`. [DATABASE-MIGRATION-MIGRATIONS](references/DATABASE-MIGRATION-MIGRATIONS.md).
- **[WRITING-DATA.md](references/WRITING-DATA.md)**: create, update, upsert, delete and assigning associations through a repository.
- **[EVENTS.md](references/EVENTS.md)**: Every write passes through the `EntityWriter` and dispatches events — the clean way to react to data changes…. [EVENTS-SYSTEM](references/EVENTS-SYSTEM.md).

## Source

Distilled from [developer.shopware.com](https://developer.shopware.com) (Data Abstraction Layer guides and reference) plus the Shopware 6.7 source, retrieved 2026-08-20.
