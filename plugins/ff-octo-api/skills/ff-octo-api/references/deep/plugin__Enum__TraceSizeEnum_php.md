# TraceSizeEnum (`src/Enum/TraceSizeEnum.php`)

## Zweck
Int-Backed-Enum zur Steuerung der Umfangs-/Detailtiefe von Trace-/Log-Ausgaben (wie viel Kontext beim Logging mitgeschrieben wird).

## Typ
- Namespace: `FfOctoApi\Enum`
- `enum TraceSizeEnum: int`

## Cases
| Case | Wert | Bedeutung |
|------|------|-----------|
| `TRACE_SIZE_ZERO` | `0` | Kein Trace. |
| `TRACE_SIZE_SHORT` | `1` | Kurzer Trace. |
| `TRACE_SIZE_LONG` | `2` | Ausführlicher Trace. |

## Bezüge
`Service/LoggerService.php`, `Core/Framework/Config/PluginLoggerTrait.php`, `Interface/OctoLoggerInterface.php`.
