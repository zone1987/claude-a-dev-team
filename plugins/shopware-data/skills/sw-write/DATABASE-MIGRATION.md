# Shopware 6 — Database migration

Schema changes run through `MigrationStep` in `src/Migration/` (or `Migration/V6_7/`). File name/class
`Migration{Timestamp}{Description}`; `getCreationTimestamp()` = Unix timestamp (unique ordering).

```php
class Migration1700000000FfExample extends MigrationStep
{
    public function getCreationTimestamp(): int { return 1700000000; }
    public function update(Connection $connection): void
    {
        $connection->executeStatement('CREATE TABLE IF NOT EXISTS `ff_example` (
            `id` BINARY(16) NOT NULL, `name` VARCHAR(255) NOT NULL,
            `created_at` DATETIME(3) NOT NULL, `updated_at` DATETIME(3) NULL,
            PRIMARY KEY (`id`)
        ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;');
    }
    public function updateDestructive(Connection $connection): void { /* drop columns/tables */ }
}
```

`update()` = additive/non-destructive (always runs); `updateDestructive()` = deleting (separate, later run).
IDs as `BINARY(16)`, time as `DATETIME(3)`. Execute: `bin/console database:migrate --all`.

→ Migration patterns & examples: [DATABASE-MIGRATION-MIGRATIONS.md](DATABASE-MIGRATION-MIGRATIONS.md)
→ Scaffold: [examples/MigrationStep.php](examples/MigrationStep.php)
