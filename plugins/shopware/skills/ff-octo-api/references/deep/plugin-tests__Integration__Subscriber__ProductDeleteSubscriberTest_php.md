# ProductDeleteSubscriberTest (`tests/Integration/Subscriber/ProductDeleteSubscriberTest.php`)

## Zweck
Integration-Tests für `ProductDeleteSubscriber` (Orphan-Cleanup). Testsuite **integration**.

## Testfälle
- `testSubscribesToEntityDeleteEvent`
- `testDeletingProductRemovesAttachedOctoProduct`
- `testDeletingNonOctoProductDoesNotAffectOctoProducts`

## Bezüge
`Subscriber/ProductDeleteSubscriber.php`.
