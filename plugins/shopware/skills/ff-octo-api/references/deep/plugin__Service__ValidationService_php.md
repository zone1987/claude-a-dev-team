# ValidationService (`src/Service/ValidationService.php`)

## Zweck
Führt die Eingabe-Validierung durch: holt die `Assert\Collection` der angefragten Kategorie aus der Registry und validiert die Daten mit dem Symfony-Validator. `readonly`, `declare(strict_types=1)`.

## Typ & Vererbung
- Namespace: `FfOctoApi\Service`
- `readonly class ValidationService`

## Konstruktor / DI
| Parameter | Typ | Zweck |
|-----------|-----|-------|
| `$validator` | `ValidatorInterface` | Symfony-Validator. |
| `$constraintCollectionRegistry` | `ConstraintCollectionRegistry` | Liefert die Constraints je Kategorie. |

## Methoden
### `validate(array $args, ConstraintCollectionEnum): ValidationResponse`
Holt `getConstraints(enum->value)`, validiert `$args`, gibt `ValidationResponse` (Wrapper um die Violation-Liste).

## Bezüge
`Constraint/ConstraintCollectionRegistry.php`, `Constraint/ValidationResponse.php`, `Enum/ConstraintCollectionEnum.php`, `Controller/AvailbilityController.php`, `Service/BookingService.php`.
