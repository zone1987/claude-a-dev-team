# Database Migrations

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
        // Destructive changes (column drops, table drops)
        // Only runs with: bin/console dal:migration:run --destructive
    }
}
```

## Key Rules

1. **`getCreationTimestamp()`** must return the integer timestamp matching the filename
2. **`update()`** is for non-destructive changes: CREATE TABLE, ADD COLUMN, ADD INDEX
3. **`updateDestructive()`** is for destructive changes: DROP TABLE, DROP COLUMN. Only runs explicitly with `--destructive` flag
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
