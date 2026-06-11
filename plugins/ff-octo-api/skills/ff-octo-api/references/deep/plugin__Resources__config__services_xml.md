# services.xml (`src/Resources/config/services.xml`)

## Zweck
Haupt-DI-Datei: importiert alle anderen Config-Dateien und registriert die Service-Schicht.

## Imports
`definitions.xml`, `extensions.xml`, `controllers.xml`, `clients.xml`, `subscribers.xml`, `scheduledTasks.xml`, `twig.xml`, `checkout.xml`, `validations.xml`, `commands.xml`.

## Definierte Services (Service → Argumente)
- `PriceService` — LoggerService, product.repository, currency.repository, OctoApiClientRegistry, PropertyService, SystemConfigService.
- `PropertyService` — LoggerService, property_group.repository, property_group_option.repository.
- `MediaService` — product.repository, media.repository, media_folder.repository, MediaUploadService.
- `SessionService` — (keine Args).
- `BookingService` — OctoApiClientRegistry, ValidationService.
- `ValidationService` — validator, ConstraintCollectionRegistry.
- `StateService` — order.repository, state_machine_transition.repository, LoggerService.
- `CheckoutService` — order.repository, product.repository, customer.repository, LoggerService, OctoApiClientRegistry.
- `CalendarService` — LoggerService, OctoApiClientRegistry, ff_octo_product.repository.
- `LoggerService` — `monolog.logger.octo` (eigener Channel `octo`).

## Bezüge
Alle `Service/*`, importierte Config-Dateien.
