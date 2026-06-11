# Migration1757686022CreateProductExtension (`src/Migration/Migration1757686022CreateProductExtension.php`)

## Zweck
Fügt der `product`-Tabelle die Inheritance-Spalten für die `ffOctoProduct`-Association hinzu (FK `ff_octo_product_id` + Association `ffOctoProduct`).

## Typ & Vererbung
- Namespace: `FfOctoApi\Migration`
- `class … extends MigrationStep`, nutzt `InheritanceUpdaterTrait`, `@internal`.

## Methoden
- `getCreationTimestamp(): int` → `1757686022`.
- `update(Connection): void` → `updateInheritance(connection, 'product', 'ff_octo_product_id')` und `updateInheritance(connection, 'product', 'ffOctoProduct')`.

## Besonderheiten
- Korrespondiert mit `ProductExtension` (Inherited-Flags → Varianten erben die Zuordnung).

## Bezüge
`Extension/Content/Product/ProductExtension.php`, `../database-entities.md`.
