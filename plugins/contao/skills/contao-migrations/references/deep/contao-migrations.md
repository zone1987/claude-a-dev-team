# Contao Migrations-Framework (5.x)

## Überblick

Das Migration-Framework ermöglicht Datenkompatibilität bei Updates. Migrationen werden ausgeführt via:
- Install Tool → Datenbankaktualisierung
- `vendor/bin/contao-console contao:migrate`

---

## Service-Registrierung

```yaml
# config/services.yaml
services:
    App\Migration\MyMigration:
        tags:
            - { name: contao.migration, priority: 0 }
```

---

## MigrationInterface – 3 Pflichtmethoden

| Methode | Beschreibung |
|---------|-------------|
| `getName(): string` | Beschreibender Name (wird dem Benutzer angezeigt) |
| `shouldRun(): bool` | Prüft ob Voraussetzungen erfüllt und Migration nötig ist |
| `run(): MigrationResult` | Führt Migration aus, gibt Ergebnis zurück |

---

## AbstractMigration (empfohlen)

Implementiert `MigrationInterface` und stellt bereit:
- `getName()` (automatisch aus Klassenname)
- `createResult(bool $successful, string $message = ''): MigrationResult`

---

## Vollständiges Beispiel

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

        // Tabelle existiert?
        if (!$schemaManager->tablesExist(['tl_customers'])) {
            return false;
        }

        $columns = $schemaManager->listTableColumns('tl_customers');

        // Nur ausführen wenn Quellspalten vorhanden und Zielspalte fehlt
        return isset($columns['firstname'])
            && isset($columns['lastname'])
            && !isset($columns['name']);
    }

    public function run(): MigrationResult
    {
        // Zielspalte anlegen
        $this->connection->executeQuery("
            ALTER TABLE tl_customers
            ADD name varchar(255) NOT NULL DEFAULT ''
        ");

        // Daten migrieren
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

- In `shouldRun()` immer auf Tabellenexistenz und Spaltenstruktur prüfen (defensiv)
- `shouldRun()` muss nach Ausführung `false` zurückgeben (Idempotenz)
- Für Schema-Änderungen Doctrine DBAL nutzen, nicht rohe SQL-Strings hardcoden
- Fehler mit `$this->createResult(false, 'Fehlerbeschreibung')` kommunizieren

---

*Quelle: https://docs.contao.org/5.x/dev/framework/migrations/*
