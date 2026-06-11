# scheduledTasks.xml (`src/Resources/config/scheduledTasks.xml`)

## Zweck
Registriert die geplanten Tasks und ihre Handler.

## Definierte Services
- `OctoApiWarmCacheTask` — Tag `shopware.scheduled.task`.
- `OctoApiWarmCacheHandler` — `scheduled_task.repository`, `LoggerService`, `OctoApiClientRegistry`, `cache.system`; Tag `messenger.message_handler`.
- `OctoApiPriceUpdaterTask` — Tag `shopware.scheduled.task`.
- `OctoApiPriceUpdaterHandler` — `scheduled_task.repository`, `LoggerService`, `PriceService`, `product.repository`; Tag `messenger.message_handler`.

## Bezüge
`Service/ScheduledTask/*`.
