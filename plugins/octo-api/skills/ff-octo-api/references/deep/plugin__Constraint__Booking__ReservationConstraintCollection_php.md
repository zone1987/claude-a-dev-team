# ReservationConstraintCollection (`src/Constraint/Booking/ReservationConstraintCollection.php`)

## Zweck
Validierungsregeln für den **Buchungs-Reservierungs-Request** (Reservierung einer Verfügbarkeit für bestimmte Units). Kategorie `booking_reservation`.

## Typ & Vererbung
- Namespace: `FfOctoApi\Constraint\Booking`
- `class ReservationConstraintCollection implements ConstraintCollectionInterface`
- Tag `octo.validation.constraint-collection`.

## Methoden
### `static getCategory(): string`
Liefert `'booking_reservation'`. `#[\Override]`.

### `static getConstraint(): Assert\Collection`
Felder:
- `identifier`, `uuid`, `productId`, `optionId`, `availabilityId`: NotBlank + string (Pflicht).
- `expirationMinutes`: Optional, integer (Reservierungsdauer; sonst Config `bookingReservationTime`).
- `unitItems`: array, `All` → Collection mit `unitId` (NotBlank string) + `uuid` (Optional, NotBlank string).

## Besonderheiten
- `availabilityId` stammt aus dem vorausgehenden Availability-Check.
- `unitItems` referenziert Units einzeln (pro Person/Ticket), nicht aggregiert mit quantity.

## Bezüge
`Interface/ConstraintCollectionInterface.php`, `Constraint/ConstraintCollectionRegistry.php`, `Service/BookingService.php`.
