# DatabaseTrait (`src/Core/Framework/Migration/DatabaseTrait.php`)

## Zweck
Trait mit Schema-/Migrations-Hilfsfunktionen für die Plugin-Lifecycle-Methoden: Tabellen/Spalten/Foreign-Keys prüfen und entfernen, Inheritance abbauen und Plugin-Migrationen versioniert in-place ausführen.

## Typ
- Namespace: `FfOctoApi\Core\Framework\Migration`
- `trait DatabaseTrait` (nutzt `InheritanceUpdaterTrait`)

## Methoden
- `removeTables(Connection, array $tables): void` (protected) — droppt existierende Tabellen (FK-Checks temporär aus).
- `tableExists(Connection, table): bool` (private) — via SchemaManager.
- `columnExists(Connection, table, column): bool` (private).
- `hasForeignKey(Connection, table, foreignKey): bool` (private) — prüft referencing columns.
- `getForeignKey(Connection, table, foreignKey): ?string` (private) — Name des FK.
- `removeForeignKey(Connection, table, foreignKey): void` (protected) — `ALTER TABLE … DROP FOREIGN KEY`.
- `removeInheritance(Connection, table, column): void` (protected) — entfernt FK + Spalte.
- `removeTableInheritances(Connection, table, columns): void` (protected) — mehrere Spalten.
- `updateMigrations(InstallContext|UpdateContext): void` (protected) — setzt AutoMigrate=false, sammelt + `migrateInPlace()`.
- `getMigrationPaths(InstallContext|UpdateContext): array` (protected) — sammelt versionierte Migrationsverzeichnisse ≤ aktueller Plugin-Version (`version_compare`).
- `createMigrationCollection(InstallContext|UpdateContext): MigrationCollection` (protected) — baut `MigrationSource` + `collect` + `sync`.

## Besonderheiten / Fallstricke
- `removeTables` schaltet `FOREIGN_KEY_CHECKS` ab/an — destruktiv (Uninstall).
- Versionsvergleich wandelt `vX_Y`-Verzeichnisnamen in `X.Y` um.
- Nutzt `$this->container`/`$this->getPath()` etc. → nur in der Plugin-Hauptklasse einsetzbar.

## Bezüge
`FfOctoApi.php`, `Migration/*`.
