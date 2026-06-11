# AvailabilityCheckConstraintCollection (`src/Constraint/Availability/AvailabilityCheckConstraintCollection.php`)

## Zweck
Definiert die Symfony-Validierungsregeln für den **Availability-Check-Request** (Verfügbarkeitsprüfung einer Option/eines Tickets). Wird über die `ConstraintCollectionRegistry` unter der Kategorie `availability_check` bereitgestellt.

## Typ & Vererbung
- Namespace: `FfOctoApi\Constraint\Availability`
- `class AvailabilityCheckConstraintCollection implements ConstraintCollectionInterface`
- Registriert mit Tag `octo.validation.constraint-collection` (`validations.xml`).

## Konstanten
| Konstante | Wert | Bedeutung |
|-----------|------|-----------|
| `DATE_TIME_FORMAT` | `Y-m-d\TH:i:s.v\Z` | Erwartetes Format für `localDateStart`/`localDateEnd` (ISO mit ms + Z). |
| `DATE_FORMAT` | `Y-m-d` | Format für `localDate`. |
| `TIME_FORMAT` | `h:i` | (Konstante vorhanden; `localTime` wird de facto per Regex `H:i` validiert.) |

## Methoden
### `static getCategory(): string`
Liefert `'availability_check'`. `#[\Override]`.

### `static getConstraint(): Assert\Collection`
Baut die `Assert\Collection`. Felder:
- `identifier`, `productUuid`, `productId`: NotBlank + string (Pflicht).
- `localDateStart`, `localDateEnd`: Optional, NotBlank + DateTime(`DATE_TIME_FORMAT`).
- `localDate`: Optional, NotBlank + DateTime(`DATE_FORMAT`).
- `localTime`: Optional, Regex `^([01]\d|2[0-3]):([0-5]\d)$` (H:i).
- `product`: array.
- `units`: array, `All` → je Element Collection mit `id` (NotBlank string) + `quantity` (NotBlank integer).

## Besonderheiten
- `quantity` muss echtes `integer` sein (nicht numerischer String) → Frontend muss korrekt typisieren.
- Datumsfelder sind optional (verschiedene Availability-Typen: Datumsbereich, Einzeltag, Zeitslot).

## Bezüge
`Interface/ConstraintCollectionInterface.php`, `Constraint/ConstraintCollectionRegistry.php`, `Controller/AvailbilityController.php`, `Enum/ConstraintCollectionEnum.php`.
