# ConstraintCollectionRegistryTest (`tests/Unit/Constraint/ConstraintCollectionRegistryTest.php`)

## Zweck
Unit-Tests für `ConstraintCollectionRegistry`. Testsuite **unit**.

## Getestete Klasse
`FfOctoApi\Constraint\ConstraintCollectionRegistry` (nutzt Fakes unter `Unit/Constraint/Fakes/`).

## Testfälle
- `testGetConstraintsReturnsRegisteredCollection`
- `testGetConstraintsThrowsForUnknownCategory`
- `testConstructorThrowsOnDuplicateCategory`
- `testSupportsMultipleCategories`

## Bezüge
`Constraint/ConstraintCollectionRegistry.php`, `Unit/Constraint/Fakes/*`.
