# ConstraintCollectionRegistry (`src/Constraint/ConstraintCollectionRegistry.php`)

## Zweck
Registry, die alle Validierungs-Constraint-Collections nach Kategorie verwaltet und auf Anfrage die passende Symfony-`Assert\Collection` liefert. Zentrale Stelle, über die Controller (Availability/Booking) ihre Eingabe-Validierung beziehen.

## Typ & Vererbung
- Namespace: `FfOctoApi\Constraint`
- `class ConstraintCollectionRegistry`
- Befüllt via **Tagged Iterator** `octo.validation.constraint-collection` (DI, siehe `validations.xml`).

## Properties
| Property | Typ | Bedeutung |
|----------|-----|-----------|
| `$constraintCollections` | `ConstraintCollectionInterface[]` | Map Kategorie → Collection. |

## Konstruktor / DI
| Parameter | Typ | Zweck |
|-----------|-----|-------|
| `$constraintCollections` | `iterable<ConstraintCollectionInterface>` | Alle getaggten Collections. Wirft `InvalidArgumentException`, wenn zwei Collections dieselbe Kategorie (`getCategory()`) beanspruchen. |

## Methoden
### `private getConstraintCollection(string $category): ConstraintCollectionInterface`
Liefert die Collection zur Kategorie; wirft `InvalidArgumentException`, wenn keine existiert.

### `public getConstraints(string $category): Assert\Collection`
Gibt die `Assert\Collection` der Kategorie zurück (delegiert an `getConstraint()` der Collection). Wird vom `ValidationService`/Controllern genutzt.

## Besonderheiten
- Kategorien stammen aus `ConstraintCollectionEnum` (booking_reservation, availability_check, availability_calendar).
- Doppelte Kategorie = harter Fehler beim Container-Build/Erstaufruf.

## Bezüge
`Interface/ConstraintCollectionInterface.php`, `Enum/ConstraintCollectionEnum.php`, `Constraint/Availability/*`, `Constraint/Booking/*`, `Service/ValidationService.php`, `validations.xml`.
