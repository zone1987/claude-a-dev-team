# Database Migrations

## Contents

- [Overview](#overview)
- [File Location & Naming](#file-location-naming)
- [MigrationStep Class](#migrationstep-class)
- [Key Rules](#key-rules)
- [Common Column Types](#common-column-types)
- [Foreign Keys](#foreign-keys)
- [Translation Tables](#translation-tables)
- [Running Migrations](#running-migrations)

## Overview

Plugins use `MigrationStep` classes to manage database schema changes. Migrations run automatically during `plugin:install` and `plugin:update`.

## File Location & Naming

Migrations go in `src/Migration/` and follow this naming convention:

```
src/Migration/Migration{TIMESTAMP}{Description}.php
```

Example: `src/Migration/Migration1709123456CreateCustomTable.php`

Generate a timestamp with: `date +%s`

## MigrationStep Class

```php
<?php declare(strict_types=1);

namespace FfContentPlus\Migration;

use Doctrine\DBAL\Connection;
use Shopware\Core\Framework\Log\Package;
use Shopware\Core\Framework\Migration\MigrationStep;

/**
 * @class Migration1709123456CreateCustomTable
 * @package FfContentPlus\Migration
 */
#[Package('custom-plugins')]
class Migration1709123456CreateCustomTable extends MigrationStep
{
    /**
     * @return int
     */
    public function getCreationTimestamp(): int
    {
        return 1709123456;
    }

    /**
     * @param Connection $connection
     * @return void
     */
    public function update(Connection $connection): void
    {
        $connection->executeStatement('
            CREATE TABLE IF NOT EXISTS `ff_content_plus_item` (
                `id`         BINARY(16)   NOT NULL,
                `name`       VARCHAR(255) NOT NULL,
                `active`     TINYINT(1)   NOT NULL DEFAULT 0,
                `created_at` DATETIME(3)  NOT NULL,
                `updated_at` DATETIME(3)  NULL,
                PRIMARY KEY (`id`)
            ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
        ');
    }

    /**
     * @param Connection $connection
     * @return void
     */
    public function updateDestructive(Connection $connection): void
    {
        // The core uses this for delayed, major-version destructive changes.
        // A plugin's install and update never call it — leave it empty.
    }
}
```

## Key Rules

1. **`getCreationTimestamp()`** must return the integer timestamp matching the filename
2. **`update()`** is for non-destructive changes: CREATE TABLE, ADD COLUMN, ADD INDEX
3. **`updateDestructive()` never runs for a plugin.** `MigrationStep` defines it, and the core uses
   it for delayed destructive changes at a major version — but plugin install and update do not call
   it, and in practice nobody runs `database:migrate-destructive` for a plugin. **Put every change
   your plugin needs in `update()`**, and clean up in the `uninstall()` lifecycle method
4. **Always use `IF NOT EXISTS`** for CREATE TABLE / ADD COLUMN to make migrations idempotent
5. **Always use `BINARY(16)`** for ID columns (Shopware uses binary UUIDs)
6. **Always include** `created_at DATETIME(3)` and `updated_at DATETIME(3) NULL`
7. **Migrations are immutable** — never modify an existing migration. Create a new one instead

## Common Column Types

| Shopware Type | MySQL Column |
|---------------|-------------|
| ID (UUID) | `BINARY(16) NOT NULL` |
| Foreign Key | `BINARY(16) NULL` or `NOT NULL` |
| String | `VARCHAR(255)` |
| Long text | `LONGTEXT` |
| Integer | `INT` |
| Float | `DOUBLE` |
| Boolean | `TINYINT(1)` |
| Date | `DATE` |
| DateTime | `DATETIME(3)` |
| JSON | `JSON` |
| Price | `JSON` (Shopware stores prices as JSON) |
| Created at | `DATETIME(3) NOT NULL` |
| Updated at | `DATETIME(3) NULL` |

## Foreign Keys

```sql
ALTER TABLE `ff_content_plus_item`
    ADD CONSTRAINT `fk.ff_content_plus_item.product_id`
        FOREIGN KEY (`product_id`)
            REFERENCES `product` (`id`)
            ON DELETE CASCADE ON UPDATE CASCADE;
```

## Translation Tables

For translatable entities, create a translation table:

```sql
CREATE TABLE IF NOT EXISTS `ff_content_plus_item_translation` (
    `ff_content_plus_item_id` BINARY(16)   NOT NULL,
    `language_id`             BINARY(16)   NOT NULL,
    `name`                    VARCHAR(255) NOT NULL,
    `description`             LONGTEXT     NULL,
    `created_at`              DATETIME(3)  NOT NULL,
    `updated_at`              DATETIME(3)  NULL,
    PRIMARY KEY (`ff_content_plus_item_id`, `language_id`),
    CONSTRAINT `fk.ff_content_plus_item_translation.item_id`
        FOREIGN KEY (`ff_content_plus_item_id`)
            REFERENCES `ff_content_plus_item` (`id`)
            ON DELETE CASCADE ON UPDATE CASCADE,
    CONSTRAINT `fk.ff_content_plus_item_translation.language_id`
        FOREIGN KEY (`language_id`)
            REFERENCES `language` (`id`)
            ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
```

## Running Migrations

```bash
# Run all pending migrations for a plugin
bin/console database:migrate --all FfContentPlus

# Run destructive migrations
bin/console database:migrate --all --destructive FfContentPlus

# Migrations also run automatically on:
bin/console plugin:install FfContentPlus
bin/console plugin:update FfContentPlus
```

## Contents

- [File naming](#file-naming)
- [Generating a migration](#generating-a-migration)
- [Running migrations](#running-migrations)
- [Advanced control](#advanced-control)
- [Relocating the migration directory](#relocating-the-migration-directory)

## File naming

Shopware looks for migrations in a `Migration` directory relative to the plugin's base class:
`<plugin root>/src/Migration/Migration1546422281ExampleDescription.php`.

| Part | Meaning |
|---|---|
| `Migration` | every migration file starts with it |
| `1546422281` | a timestamp, which is what makes migrations incremental |
| `ExampleDescription` | a descriptive name |

## Generating a migration

```bash
./bin/console database:create-migration -p SwagBasicExample --name ExampleDescription
```

| Part | Meaning |
|---|---|
| `-p your_plugin_name` | creates the migration for that plugin |
| `--name your_descriptive_name` | appended after the timestamp |

**There is no rollback.** A migration class holds no instructions to reverse itself; database cleanup
on removal belongs in the plugin's `uninstall()` lifecycle method.

Shopware can also generate the SQL from your entity definitions:

```bash
./bin/console dal:migration:create --bundle=SwagBasicExample --entities=your_entity,your_other_entity
```

It writes the `CREATE TABLE` or `ALTER TABLE` statements needed to bring the schema in line with the
definitions — **one migration file per entity**.

| Option | Meaning |
|---|---|
| `--bundle` | the plugin name; omitted, the migration is generated in the core |
| `--entities` | comma-separated list of entities |

**The plugin has to be active**, or its entity definitions cannot be found.

## Running migrations

Installing a plugin adds its migration directory to a `MigrationCollection` and runs every
`update()`. Updating through the Plugin Manager runs the new ones the same way.

```bash
./bin/console database:migrate SwagBasicExample --all
```

The identifier argument selects which migrations run. **It defaults to the Shopware core**, so a
plugin's own migrations need its bundle name passed explicitly.

A migration created after the plugin was installed can be run by hand, since the directory is already
registered.

## Advanced control

A plugin that wants to decide which migrations run has to refuse the automatic execution first.
`MigrationCollection` — filled with that plugin's migrations only — is reachable from `InstallContext`
and its subclasses (`UpdateContext`, `ActivateContext`, …):

```php
public function update(UpdateContext $updateContext): void
{
    $updateContext->setAutoMigrate(false);   // disable automatic execution

    $migrationCollection = $updateContext->getMigrationCollection();

    // run UPDATE migrations up to and including 2019-12-12T09:30:51+00:00
    $migrationCollection->migrateInPlace(1576143014);
}
```

A plugin not using the migration system finds an empty collection (a `NullObject`) in the context.

## Relocating the migration directory

Most plugins should keep `src/Migration` — the tooling assumes it. Where there is a reason to move
it, override `getMigrationNamespace()` in the plugin base class:

```php
public function getMigrationNamespace(): string
{
    return 'Swag\BasicExample\MyMigrationNamespace';
}
```

**The path is derived from the namespace**, so the directory has to be renamed to match —
`MyMigrationNamespace` here.

## Source

[developer.shopware.com/docs/guides/plugins/plugins/database/database-migrations.html](https://developer.shopware.com/docs/guides/plugins/plugins/database/database-migrations.html),
Shopware 6.7, retrieved 2026-08-21.
