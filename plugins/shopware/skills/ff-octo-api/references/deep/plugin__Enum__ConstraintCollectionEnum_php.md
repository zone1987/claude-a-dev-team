# ConstraintCollectionEnum (`src/Enum/ConstraintCollectionEnum.php`)

## Zweck
String-Backed-Enum der Validierungs-Kategorien. Bildet die Schlüssel, unter denen die `ConstraintCollectionRegistry` ihre Collections verwaltet.

## Typ
- Namespace: `FfOctoApi\Enum`
- `enum ConstraintCollectionEnum: string`

## Cases
| Case | Wert | Bedeutung |
|------|------|-----------|
| `BOOKING_RESERVATION` | `booking_reservation` | Validierung der Reservierungs-Requests (BookingService). |
| `AVAILABILITY_CHECK` | `availability_check` | Validierung des Availability-Check-Requests. |
| `AVAILABILITY_CALENDAR` | `availability_calendar` | Validierung des Availability-Calendar-Requests. |

## Bezüge
`Constraint/ConstraintCollectionRegistry.php`, `Constraint/Availability/AvailabilityCheckConstraintCollection.php`, `Constraint/Availability/AvailabilityCalendarConstraintCollection.php`, `Constraint/Booking/ReservationConstraintCollection.php`.
