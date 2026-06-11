# validations.xml (`src/Resources/config/validations.xml`)

## Zweck
Registriert die `ConstraintCollectionRegistry` (Tagged Iterator) und die drei Constraint-Collections.

## Definierte Services
- `ConstraintCollectionRegistry` — `tagged_iterator` Tag `octo.validation.constraint-collection`.
- `Booking\ReservationConstraintCollection` — Tag `octo.validation.constraint-collection`.
- `Availability\AvailabilityCheckConstraintCollection` — Tag.
- `Availability\AvailabilityCalendarConstraintCollection` — Tag.

## Besonderheiten
- Neue Validierungskategorie: Collection mit `ConstraintCollectionInterface` + Tag hier ergänzen.

## Bezüge
`Constraint/*`, `Enum/ConstraintCollectionEnum.php`, `Service/ValidationService.php`.
