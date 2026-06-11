# controllers.xml (`src/Resources/config/controllers.xml`)

## Zweck
DI-Registrierung aller Controller (jeweils `public=true`, mit `setContainer(service_container)`).

## Definierte Services (Controller → wichtigste Argumente)
- `OctoProductController` — `OctoApiClientRegistry`, `LoggerService`, `product.repository`, `ff_octo_product.repository`.
- `PropertyController` — `PropertyService`.
- `VariantController` — `LoggerService`, `property_group.repository`, `product.repository`, `MediaService`.
- `MediaController` — `product.repository`, `MediaService`.
- `PriceController` — `PriceService`.
- `AvailbilityController` — `LoggerService`, `OctoApiClientRegistry`, `PriceService`, `PropertyService`, `SessionService`, `ValidationService`, `CalendarService`.
- `SessionController` — `LoggerService`, `SessionService`.
- `CartController` — `LineItemFactoryRegistry`, `CartService`, `BookingService`, `OctoApiClientRegistry`, `SystemConfigService`, `product.repository`, `LoggerService`.
- `NotificationController`, `WidgetController` — nur `setContainer`.

## Besonderheiten
- Alle Controller `public` (für Routing). Routen selbst via PHP-Attribute + `routes.xml`.

## Bezüge
`Controller/*`, `routes.xml`.
