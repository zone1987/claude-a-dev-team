# ConstraintCollectionInterface (`src/Interface/ConstraintCollectionInterface.php`)

## Zweck
Vertrag für alle Validierungs-Constraint-Collections. Jede Collection liefert ihre Kategorie und die zugehörige Symfony-`Assert\Collection`.

## Typ
- Namespace: `FfOctoApi\Interface`
- `interface ConstraintCollectionInterface`

## Methoden
### `static getCategory(): string`
Eindeutige Kategorie (Schlüssel in der `ConstraintCollectionRegistry`).

### `static getConstraint(): Assert\Collection`
Die Validierungsregeln als `Assert\Collection`.

## Besonderheiten
- Beide Methoden sind **statisch**.
- Implementierungen werden per Tag `octo.validation.constraint-collection` registriert.

## Bezüge
`Constraint/ConstraintCollectionRegistry.php`, `Constraint/Availability/*`, `Constraint/Booking/ReservationConstraintCollection.php`.
