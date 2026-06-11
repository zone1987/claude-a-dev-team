# Migration1755686022CreateOctoProductTable (`src/Migration/Migration1755686022CreateOctoProductTable.php`)

## Zweck
Erstellt die Tabelle `ff_octo_product`.

## Typ & Vererbung
- Namespace: `FfOctoApi\Migration`
- `class … extends MigrationStep`, `@internal`, `declare(strict_types=1)`

## Methoden
- `getCreationTimestamp(): int` → `1755686022`.
- `update(Connection): void` → `CREATE TABLE IF NOT EXISTS ff_octo_product`:
  - `id` BINARY(16) PK, `uuid` VARCHAR(36) NOT NULL (UNIQUE `uniq.uuid`), `identifier` VARCHAR(50) NOT NULL,
    `product` JSON NULL DEFAULT `JSON_ARRAY()`, `created_at` DATETIME(3) NOT NULL, `updated_at` DATETIME(3) NULL,
    CHECK `JSON_VALID(product)`. InnoDB / utf8mb4 / utf8mb4_general_ci.

## Besonderheiten
- `uuid` ist unique → ein API-Produkt nur einmal.

## Bezüge
`Core/Content/OctoProduct/OctoProductDefinition.php`, `../database-entities.md`.
