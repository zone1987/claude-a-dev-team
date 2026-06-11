# OctoErrorResponse (`src/Core/Api/Octo/OctoErrorResponse.php`)

## Zweck
Wrapper um eine fehlerhafte OCTO-API-Response. Extrahiert `errorMessage`/`errorCode` (bzw. `error`) aus dem Body, damit der aufrufende Code (v.a. `CheckoutService`) gezielt auf Fehlercodes wie `ALREADY_CONFIRMED` reagieren kann.

## Typ & Vererbung
- Namespace: `FfOctoApi\Core\Api\Octo`
- `class OctoErrorResponse`, `declare(strict_types=1)`

## Properties
| Property | Typ | Bedeutung |
|----------|-----|-----------|
| `$message` | string | `errorMessage` aus dem Body (sonst `''`). |
| `$code` | string | `errorCode` bzw. `error` aus dem Body (sonst `''`). |
| `$response` | `ResponseInterface` (readonly, ctor) | Die rohe Response. |

## Konstruktor / DI
`__construct(ResponseInterface $response)` — dekodiert den Body (`getContent(false)`); bei HTTP-Client-Exceptions leeres Array. Setzt `message`/`code`.

## Methoden
- `getMessage(): string`
- `getCode(): string`
- `getResponse(): TraceableResponse`

## Besonderheiten
- Wird nur erzeugt, wenn `request(..., returnError: true)` aufgerufen wird (aktuell `bookingConfirm`).
- Code-Vergleich gegen `OctoErrorCode::ALREADY_CONFIRMED` im `CheckoutService`.

## Bezüge
`AbstractOctoApiClient::request`, `OctoApiClient::bookingConfirm`, `Constant/OctoErrorCode.php`, `Service/CheckoutService.php`.
