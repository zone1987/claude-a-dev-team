# StateService (`src/Service/StateService.php`)

## Zweck
Navigiert die Order-State-Machine: ermittelt erreichbare Folge-/Vorgänger-Zustände (Entities + technische Namen) und setzt den Order-Status. `readonly`, `declare(strict_types=1)`.

## Typ & Vererbung
- Namespace: `FfOctoApi\Service`
- `readonly class StateService`

## Konstruktor / DI
`EntityRepository $orderRepository`, `EntityRepository $stateMachineTransitionRepository`, `OctoLoggerInterface $logger`.

## Methoden
- `getNextAvailableStateMachineStateById(stateMachineStateId, ?context): StateMachineStateCollection` — Transitions mit `fromStateId == id`, gemappt auf `toStateMachineState`.
- `getPreviousAvailableStateMachineStateById(...)` — analog über `toStateId` → `fromStateMachineState`.
- `getNextAvailableStateMachineStateNamesById(...): array<string>` — technische Namen der Folgezustände.
- `getPreviousAvailableStateMachineStateNamesById(...): array<string>` — technische Namen der Vorgänger.
- `setOrderStateMachineState(order, technicalStateName, ?context): bool` — prüft, ob `technicalStateName` erreichbar; sonst `InvalidArgumentException`. Ermittelt `nextStateId = array_search(name, availableStates)`, upsert `stateId`. Bei Exception error + `false`.

## Besonderheiten / Fallstricke
- **Index-/ID-Fallstrick:** `getNextAvailableStateMachineStateNamesById` liefert ein per `map` erzeugtes Array (Schlüssel = ursprüngliche Collection-Keys/IDs → technische Namen). `array_search(name, ...)` gibt diesen Schlüssel zurück und wird als `stateId` verwendet — funktioniert nur, solange der Map-Key die State-ID ist. Bei Änderungen an der Collection-Indizierung kann hier ein falscher/leerer `stateId` entstehen. Sorgfältig testen.

## Bezüge
`Subscriber/OrderSubscriber.php`, `Service/CheckoutService.php`, Shopware StateMachine.
