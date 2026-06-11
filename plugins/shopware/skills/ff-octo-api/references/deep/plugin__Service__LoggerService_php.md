# LoggerService (`src/Service/LoggerService.php`)

## Zweck
Implementiert `OctoLoggerInterface`: Exception-/String-orientiertes Logging auf den `octo`-Channel mit konfigurierbarer Trace-Tiefe (`TraceSizeEnum`). `declare(strict_types=1)`.

## Typ & Vererbung
- Namespace: `FfOctoApi\Service`
- `class LoggerService implements OctoLoggerInterface`

## Konstruktor / DI
| Parameter | Typ | Zweck |
|-----------|-----|-------|
| `$logger` | `LoggerInterface` (PSR-3, Channel `octo`) | Darunterliegender Monolog-Logger. |

## Methoden
- `debug/info/warning/error(Exception|string $e, array $context=[], TraceSizeEnum $traceSize=TRACE_SIZE_SHORT): void` — delegieren an `log(...)` mit entsprechendem Level (warning ist Default-Level in `log`).
- `private log(e, context, traceSize, Level $logLevel=Warning): void` — bei Exception ohne Context: `TRACE_SIZE_LONG` → voller Trace, `TRACE_SIZE_SHORT` → file/line. Message = Exception-Message oder String. `match` auf Level → entsprechende Logger-Methode. Fängt eigene Exceptions ab (loggt file/line).
- `getLogger(): LoggerInterface`.

## Besonderheiten / Fallstricke
- Akzeptiert **`Exception|string`** (Interface deklariert nur `Exception`) — Aufrufer übergeben teils Strings (z.B. AbstractOctoApiClient).
- Default-Level in `log` ist `Warning` → `warning()` ohne explizites Level.

## Bezüge
`Interface/OctoLoggerInterface.php`, `Enum/TraceSizeEnum.php`, `Resources/config/packages/*.yaml` (Channel `octo`).
