# SessionServiceTest (`tests/Unit/Service/SessionServiceTest.php`)

## Zweck
Unit-Tests für `SessionService`. Testsuite **unit**.

## Getestete Klasse
`FfOctoApi\Service\SessionService`.

## Testfälle
- `testSetAndGetItemRoundtrip`
- `testGetItemThrowsWhenKeyMissing`
- `testGetItemRemovesEmptyValueAndThrows` — leerer Wert wird entfernt + Exception.
- `testRemoveItemRemovesExistingKey`
- `testRemoveItemReturnsNullWhenKeyMissing`
- `testSetItemReturnsAllSessionData`

## Bezüge
`Service/SessionService.php`.
