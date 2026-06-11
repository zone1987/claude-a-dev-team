# OctoApiPriceUpdaterHandler (`src/Service/ScheduledTask/OctoApiPriceUpdaterHandler.php`)

## Zweck
Handler des Price-Updater-Tasks: aktualisiert die Preise aller Produkte mit `ffOctoProduct` — **außer RheinKurier** (offline; Preise werden über den AppServer/persistierte Daten gepflegt).

## Typ & Vererbung
- Namespace: `FfOctoApi\Service\ScheduledTask`
- `#[AsMessageHandler(handles: OctoApiPriceUpdaterTask::class)]`
- `class OctoApiPriceUpdaterHandler extends ScheduledTaskHandler`

## Konstruktor / DI
`EntityRepository $scheduledTaskRepository`, `OctoLoggerInterface $exceptionLogger`, `PriceService $priceService`, `EntityRepository $productRepository`.

## Methoden
### `run(): void`
Sucht Produkte mit gesetzter `ffOctoProduct.id` (NotFilter auf null). Pro Produkt: **RheinKurier überspringen**; sonst `priceService->updatePrices(productId, identifier)` (lädt apiProduct selbst nach). Info-Logs am Anfang/Ende.

## Besonderheiten / Fallstricke
- RheinKurier wird explizit übersprungen (Offline) — dessen Preise kommen aus dem persistierten `ff_octo_product.product` (AppServer).
- Lädt nur Parent? Nein — Filter ist nur `ffOctoProduct.id != null` (keine `parentId`-Einschränkung); `updatePrices` aktualisiert intern Parent + Children.

## Bezüge
`OctoApiPriceUpdaterTask`, `Service/PriceService.php`, `Client/Octo/RheinKurierClient.php`, `scheduledTasks.xml`, `../appserver-integration.md`.
