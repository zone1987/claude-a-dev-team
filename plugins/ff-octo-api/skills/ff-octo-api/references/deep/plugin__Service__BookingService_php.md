# BookingService (`src/Service/BookingService.php`)

## Zweck
Dünner, validierender Wrapper um die OCTO-Reservierung (`bookingReservation`). Validiert die Parameter gegen die `booking_reservation`-Constraints und delegiert an den (Online-)Client; Offline-Clients liefern `[]`.

## Typ & Vererbung
- Namespace: `FfOctoApi\Service`
- `readonly class BookingService`, `declare(strict_types=1)`

## Konstruktor / DI
| Parameter | Typ | Zweck |
|-----------|-----|-------|
| `$clientRegistry` | `OctoApiClientRegistry` | Client-Auflösung. |
| `$validationService` | `ValidationService` | Parameter-Validierung. |

## Methoden
### `bookingReservation(identifier, uuid?, expirationMinutes?, productId?, optionId?, availabilityId?, unitItems=[]): array`
- Validiert **`ClassHelper::getMethodArgs()`** (alle eigenen Methodenargumente per Reflection) gegen `Constraint::BOOKING_RESERVATION`; bei Fehler `ValidationFailedException`.
- Holt Client; **offline → `[]`** (keine Reservierung).
- Sonst `client->bookingReservation(uuid, expirationMinutes, productId, optionId, availabilityId, unitItems)`.
- Wirft `ValidationFailedException`.

## Besonderheiten / Fallstricke
- Die Validierung basiert auf `ClassHelper::getMethodArgs()` → die Parameternamen müssen exakt zu den Constraint-Feldern passen (`identifier`, `uuid`, `productId`, …).
- Aufgerufen vom `CartController` beim Warenkorb-Add.

## Bezüge
`OctoApiClientRegistry`, `ValidationService`, `Helper/ClassHelper.php`, `Constraint/Booking/ReservationConstraintCollection.php`, `Controller/CartController.php`.
