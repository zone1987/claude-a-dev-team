# OctoErrorCode (`src/Constant/OctoErrorCode.php`)

## Zweck
Konstanten-Container für OCTO-API-Fehlercodes, die im Booking-/Checkout-Flow ausgewertet werden (z.B. um eine bereits bestätigte Buchung idempotent zu behandeln).

## Typ & Vererbung
- Namespace: `FfOctoApi\Constant`
- `abstract class OctoErrorCode` (reine Konstanten-Klasse, nicht instanziierbar).

## Konstanten
| Konstante | Typ | Wert | Bedeutung |
|-----------|-----|------|-----------|
| `ALREADY_CONFIRMED` | public string | `ALREADY_CONFIRMED` | OCTO-Fehlercode: Buchung wurde bereits bestätigt. Wird in `CheckoutService` genutzt, um einen erneuten Bestätigungsversuch nicht als echten Fehler zu werten. |

## Methoden
Keine.

## Bezüge
`Service/CheckoutService.php`, `Core/Api/Octo/OctoErrorResponse.php`.
