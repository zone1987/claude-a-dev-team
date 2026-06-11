---
name: sw-database-migration
description: >
  Datenbank-Migrations in Shopware 6: MigrationStep (getCreationTimestamp, update, updateDestructive),
  Namens-/Verzeichniskonvention Migration/MigrationV{major}, destructive vs. non-destructive.
  Trigger: "Migration", "MigrationStep", "Tabelle anlegen Migration", "getCreationTimestamp", "updateDestructive",
  "Schema ändern", "database migration shopware". Shopware 6.7. Scaffolder: /sw-migration.
---

# Shopware 6 — Datenbank-Migration

Schema-Änderungen laufen über `MigrationStep` in `src/Migration/` (bzw. `Migration/V6_7/`). Dateiname/Klasse
`Migration{Timestamp}{Beschreibung}`; `getCreationTimestamp()` = Unix-Timestamp (eindeutige Reihenfolge).

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
    public function updateDestructive(Connection $connection): void { /* Spalten/Tabellen droppen */ }
}
```

`update()` = additiv/non-destructive (läuft immer); `updateDestructive()` = löschend (separater, späterer Lauf).
IDs als `BINARY(16)`, Zeit als `DATETIME(3)`. Ausführen: `bin/console database:migrate --all`.

→ Migration-Patterns & Beispiele: [references/migrations.md](references/migrations.md)
→ Gerüst: [examples/MigrationStep.php](examples/MigrationStep.php)
