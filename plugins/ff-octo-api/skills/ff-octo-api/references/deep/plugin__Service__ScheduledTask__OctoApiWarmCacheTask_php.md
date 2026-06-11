# OctoApiWarmCacheTask (`src/Service/ScheduledTask/OctoApiWarmCacheTask.php`)

## Zweck
Definiert den geplanten Task zum Aufwärmen des OCTO-Produkt-Caches.

## Typ & Vererbung
- Namespace: `FfOctoApi\Service\ScheduledTask`
- `class OctoApiWarmCacheTask extends ScheduledTask`
- Registriert in `scheduledTasks.xml`.

## Methoden
- `static getTaskName(): string` → `ff.octoapi.warm_cache`.
- `static getDefaultInterval(): int` → `10800` (3 Stunden).

## Bezüge
`OctoApiWarmCacheHandler`, `scheduledTasks.xml`.
