# Migration1768988700AddOctoProductIdentifierIndex (`src/Migration/Migration1768988700AddOctoProductIdentifierIndex.php`)

## Zweck
Performance-Indizes auf `ff_octo_product` (Filterung nach Supplier/Identifier, z.B. RheinKurier-Filter im AppServer; Sortierung nach Erstellung).

## Typ & Vererbung
- Namespace: `FfOctoApi\Migration`
- `class … extends MigrationStep`, `@internal`, `declare(strict_types=1)`

## Methoden
- `getCreationTimestamp(): int` → `1768988700`.
- `update(Connection): void` → `ALTER TABLE ff_octo_product ADD INDEX`:
  - `idx_identifier (identifier)`, `idx_identifier_uuid (identifier, uuid)`, `idx_created_at (created_at)`.

## Besonderheiten
- Unterstützt u.a. die `ffOctoProduct.identifier='rheinkurier'`-Filterung (AppServer) und Listen-Sortierung.

## Bezüge
`Core/Content/OctoProduct/OctoProductDefinition.php`, `../appserver-integration.md`, `../database-entities.md`.
