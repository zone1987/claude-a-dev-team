# Contao migrations framework (5.x)

## Contents

- [Overview](#overview)
- [Service registration](#service-registration)
- [MigrationInterface – 3 mandatory methods](#migrationinterface-3-mandatory-methods)
- [AbstractMigration (recommended)](#abstractmigration-recommended)
- [Complete example](#complete-example)
- [Best Practices](#best-practices)

## Overview

The migration framework enables data compatibility during updates. Migrations are executed via:
- Install tool → database update
- `vendor/bin/contao-console contao:migrate`

---

## Service registration

```yaml
# config/services.yaml
services:
    App\Migration\MyMigration:
        tags:
            - { name: contao.migration, priority: 0 }
```

---

## MigrationInterface – 3 mandatory methods

| Method | Description |
|---------|-------------|
| `getName(): string` | Descriptive name (shown to the user) |
| `shouldRun(): bool` | Checks whether the prerequisites are met and the migration is necessary |
| `run(): MigrationResult` | Runs the migration, returns the result |

---

## AbstractMigration (recommended)

Implements `MigrationInterface` and provides:
- `getName()` (automatically from the class name)
- `createResult(bool $successful, string $message = ''): MigrationResult`

---

## Complete example

```php
namespace App\Migration;

use Contao\CoreBundle\Migration\AbstractMigration;
use Contao\CoreBundle\Migration\MigrationResult;
use Doctrine\DBAL\Connection;

class CustomerNameMigration extends AbstractMigration
{
    public function __construct(private readonly Connection $connection) {}

    public function shouldRun(): bool
    {
        $schemaManager = $this->connection->createSchemaManager();

        // Does the table exist?
        if (!$schemaManager->tablesExist(['tl_customers'])) {
            return false;
        }

        $columns = $schemaManager->listTableColumns('tl_customers');

        // Only run if the source columns exist and the target column is missing
        return isset($columns['firstname'])
            && isset($columns['lastname'])
            && !isset($columns['name']);
    }

    public function run(): MigrationResult
    {
        // Create the target column
        $this->connection->executeQuery("
            ALTER TABLE tl_customers
            ADD name varchar(255) NOT NULL DEFAULT ''
        ");

        // Migrate the data
        $stmt = $this->connection->prepare("
            UPDATE tl_customers
            SET name = CONCAT(firstName, ' ', lastName)
        ");
        $stmt->execute();

        return $this->createResult(
            true,
            'Combined ' . $stmt->rowCount() . ' customer names.'
        );
    }
}
```

---

## Best Practices

- Always check for table existence and column structure in `shouldRun()` (defensively)
- `shouldRun()` must return `false` after execution (idempotence)
- Use Doctrine DBAL for schema changes, do not hardcode raw SQL strings
- Communicate errors with `$this->createResult(false, 'Error description')`

---

*Source: https://docs.contao.org/5.x/dev/framework/migrations/*
