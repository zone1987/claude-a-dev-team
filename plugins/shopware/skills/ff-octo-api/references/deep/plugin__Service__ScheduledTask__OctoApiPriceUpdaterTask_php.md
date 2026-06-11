# OctoApiPriceUpdaterTask (`src/Service/ScheduledTask/OctoApiPriceUpdaterTask.php`)

## Zweck
Definiert den geplanten Task zur Preisaktualisierung aller OCTO-Produkte.

## Typ & Vererbung
- Namespace: `FfOctoApi\Service\ScheduledTask`
- `class OctoApiPriceUpdaterTask extends ScheduledTask`
- Registriert in `scheduledTasks.xml`.

## Methoden
- `static getTaskName(): string` → `ff.octoapi.price-updater`.
- `static getDefaultInterval(): int` → `10800` (3 Stunden).

## Bezüge
`OctoApiPriceUpdaterHandler`, `scheduledTasks.xml`, `PriceService`.
