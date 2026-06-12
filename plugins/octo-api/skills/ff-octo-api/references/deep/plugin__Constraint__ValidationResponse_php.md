# ValidationResponse (`src/Constraint/ValidationResponse.php`)

## Zweck
Immutable Wrapper um eine Symfony-`ConstraintViolationList`. Kapselt das Validierungsergebnis: Gültigkeit, Roh-Violations und aufbereitete Fehlermeldungen für die API-/Storefront-Antwort.

## Typ & Vererbung
- Namespace: `FfOctoApi\Constraint`
- `readonly class ValidationResponse`

## Konstruktor / DI
| Parameter | Typ | Zweck |
|-----------|-----|-------|
| `$violationList` | `ConstraintViolationListInterface` | Die Verstöße aus der Validierung. |

## Methoden
### `isValid(): bool`
`true`, wenn die Violation-Liste leer ist (`count() === 0`).

### `getViolations(): ConstraintViolationListInterface`
Gibt die rohe Violation-Liste zurück.

### `getViolationMessages(): array`
Mappt jede Violation auf einen String `"<propertyPath> <message>"`. Bei `Assert\DateTime`-Constraints wird zusätzlich das erwartete Format angehängt (`(<format>)`). Nutzt `iterator_to_array` über den Listen-Iterator.

## Besonderheiten
- Reine Lese-/Aufbereitungsklasse, keine Seiteneffekte.
- Die DateTime-Sonderbehandlung hilft im Storefront, dem Nutzer das erwartete Datumsformat zu zeigen.

## Bezüge
`Service/ValidationService.php`, `Controller/AvailbilityController.php`, `Controller/CartController.php`.
