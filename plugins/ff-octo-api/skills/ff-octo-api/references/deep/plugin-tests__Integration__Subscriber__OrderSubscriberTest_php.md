# OrderSubscriberTest (`tests/Integration/Subscriber/OrderSubscriberTest.php`)

## Zweck
Integration-Tests für `OrderSubscriber` (Order-Lifecycle-Events). Testsuite **integration**.

## Testfälle
- `testSubscribesToExpectedEvents`
- `testOrderStateTransitionToCancelledTriggersCancelOrder`
- `testOrderStateTransitionToOpenDoesNotCancel`
- `testCancelOrderRouteRequestWithCancelTransitionTriggersCancel`
- `testCancelOrderRouteRequestWithOtherTransitionDoesNothing`

## Bezüge
`Subscriber/OrderSubscriber.php`, `Service/CheckoutService.php`.
