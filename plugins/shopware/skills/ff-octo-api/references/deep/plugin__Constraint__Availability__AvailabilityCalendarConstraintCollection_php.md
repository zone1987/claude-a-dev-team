# AvailabilityCalendarConstraintCollection (`src/Constraint/Availability/AvailabilityCalendarConstraintCollection.php`)

## Zweck
Validierungsregeln für den **Availability-Calendar-Request** (Kalender-Verfügbarkeit einer Option über einen Zeitraum). Kategorie `availability_calendar`.

## Typ & Vererbung
- Namespace: `FfOctoApi\Constraint\Availability`
- `class AvailabilityCalendarConstraintCollection implements ConstraintCollectionInterface`
- Tag `octo.validation.constraint-collection`.
- Hinweis: PHPDoc-`@class AvailabilityCheckConstraintCollection` ist ein Copy-Paste-Fehler.

## Konstanten
| Konstante | Wert | Bedeutung |
|-----------|------|-----------|
| `DATE_FORMAT` | `Y-m-d\TH:i:s.v\Z` | Erwartetes Format für `date`. |

## Methoden
### `static getCategory(): string`
Liefert `'availability_calendar'`. `#[\Override]`.

### `static getConstraint(): Assert\Collection`
Felder:
- `identifier`, `productId`, `optionId`: NotBlank + string (Pflicht).
- `date`: NotBlank + DateTime(`DATE_FORMAT`) (Pflicht).
- `units`: array, `All` → Collection mit `id` (NotBlank string) + `quantity` (NotBlank integer).

## Besonderheiten
- Im Gegensatz zum Check-Request ist hier `optionId` Pflicht und es gibt nur ein einzelnes `date`.

## Bezüge
`Interface/ConstraintCollectionInterface.php`, `Constraint/ConstraintCollectionRegistry.php`, `Service/CalendarService.php`, `Controller/AvailbilityController.php`.
