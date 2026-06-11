# OctoApiWarmCacheHandler (`src/Service/ScheduledTask/OctoApiWarmCacheHandler.php`)

## Zweck
Handler des Warm-Cache-Tasks: invalidiert und füllt den Produkt-Cache aller **Online**-Clients neu (alle 3h).

## Typ & Vererbung
- Namespace: `FfOctoApi\Service\ScheduledTask`
- `#[AsMessageHandler(handles: OctoApiWarmCacheTask::class)]`
- `class OctoApiWarmCacheHandler extends ScheduledTaskHandler`

## Konstruktor / DI
`EntityRepository $scheduledTaskRepository`, `OctoLoggerInterface $exceptionLogger` (an parent: dessen PSR-Logger), `OctoApiClientRegistry $clientRegistry`, `CacheItemPoolInterface $cache`.

## Methoden
### `run(): void`
Pro Client-Identifier: **Offline überspringen**; Capability `octo/content`; löscht Cache-Key `ff.octo-api.products.{SUPPLIER_ID}`; ruft `getCachedProducts(cacheExpirationTime)` (neu befüllen); loggt Anzahl. `\Throwable` → error pro Client (bricht nicht ab).

## Besonderheiten
- Bewusster Cache-Bust (`deleteItem`) vor dem Neuladen.

## Bezüge
`OctoApiWarmCacheTask`, `OctoApiClientRegistry`, `CachedOctoApiClient`, `scheduledTasks.xml`.
