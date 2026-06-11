# OrderSubscriber (`src/Subscriber/OrderSubscriber.php`)

## Zweck
Verbindet den Shopware-Order-Lebenszyklus mit der OCTO-Buchungslogik: bestätigt Buchungen bei Zahlungseingang, storniert bei Order-Cancel und reichert die Account-Order-Seite um die Stornierbarkeit (`cancellable`) je LineItem an. `readonly`, `declare(strict_types=1)`.

## Typ & Vererbung
- Namespace: `FfOctoApi\Subscriber`
- `readonly class OrderSubscriber implements EventSubscriberInterface`
- Registriert in `subscribers.xml`.

## Konstruktor / DI
`CheckoutService $checkoutService`, `EntityRepository $orderTransactionRepository`, `EntityRepository $orderLineItemRepository`, `OctoApiClientRegistry $clientRegistry`.

## Abonnierte Events (`getSubscribedEvents`)
| Event | Handler |
|-------|---------|
| `state_machine.order.state_changed` | `onStateMachineStateChanged` |
| `state_machine.order_transaction.state_changed` | `onStateMachineStateTransactionChanged` |
| `AccountOrderPageLoadedEvent` | `onAccountOrderPageLoadedEvent` |
| `CancelOrderRouteRequestEvent` | `onCancelOrderRouteRequestEvent` |

## Methoden
- `onCancelOrderRouteRequestEvent(event)`: bei `transition === 'cancel'` → `checkoutService->cancelOrder(orderId, context)`.
- `onAccountOrderPageLoadedEvent(event)`: für nicht-stornierte Orders je LineItem `cancellable=false`; für online + `reservationUuid`: `client->getBooking(uuid)['cancellable']`; aktualisiert LineItems.
- `onStateMachineStateChanged(event)`: wenn Übergang nach `cancelled` (leave-Seite, vorher nicht cancelled) → `cancelOrder`.
- `onStateMachineStateTransactionChanged(event)`: wenn Transaction nach `paid` (enter) → lädt Transaction, prüft State `paid` → `checkoutService->confirmOrder(orderId, context)`.

## Besonderheiten / Fallstricke
- **Zahlungseingang triggert die OCTO-Bestätigung** (`confirmOrder`) → bei Fehlschlag Wiedervorlage (siehe `CheckoutService`).
- Offline-Clients: `getBooking` wird übersprungen (cancellable bleibt false).
- Die präzisen Transition-Side-/State-Checks verhindern Doppelausführung.

## Bezüge
`Service/CheckoutService.php`, `OctoApiClientRegistry`, `subscribers.xml`, `../scheduled-tasks-subscribers.md`, `../booking-flow.md`.
