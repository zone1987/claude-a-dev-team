# OctoLoggerInterface (`src/Interface/OctoLoggerInterface.php`)

## Zweck
Vertrag für den OCTO-spezifischen Logger. Kapselt Exception-orientiertes Logging mit konfigurierbarer Trace-Tiefe auf dem Log-Channel `octo`.

## Typ
- Namespace: `FfOctoApi\Interface`
- `interface OctoLoggerInterface`

## Methoden
Alle Log-Level nehmen eine `Exception`, optionalen `array $context` und eine `TraceSizeEnum` (Default `TRACE_SIZE_SHORT`):
### `debug(Exception $e, array $context = [], TraceSizeEnum $traceSize = TRACE_SIZE_SHORT): void`
### `info(Exception $e, array $context = [], TraceSizeEnum $traceSize = TRACE_SIZE_SHORT): void`
### `warning(Exception $e, array $context = [], TraceSizeEnum $traceSize = TRACE_SIZE_SHORT): void`
### `error(Exception $e, array $context = [], TraceSizeEnum $traceSize = TRACE_SIZE_SHORT): void`
### `getLogger(): LoggerInterface`
Gibt den darunterliegenden PSR-3-Logger zurück.

## Besonderheiten
- Logging ist **Exception-zentriert** (kein freier String) — `TraceSizeEnum` steuert, wie viel Stacktrace mitgeschrieben wird.
- Implementiert von `Service/LoggerService.php`; Trait-Helfer in `Core/Framework/Config/PluginLoggerTrait.php`.

## Bezüge
`Enum/TraceSizeEnum.php`, `Service/LoggerService.php`, `Core/Framework/Config/PluginLoggerTrait.php`.
