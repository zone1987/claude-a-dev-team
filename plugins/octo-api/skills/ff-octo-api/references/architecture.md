# Architektur & Design Patterns

## Verzeichnisstruktur

```
FfOctoApi/
├── src/
│   ├── FfOctoApi.php                          # Plugin Entry Point
│   ├── Client/Octo/                            # Konkrete API-Client-Implementierungen
│   │   ├── GoldenToursClient.php               # GoldenTours Supplier
│   │   ├── GoCityClient.php                    # GoCity Supplier
│   │   ├── RheinKurierClient.php               # RheinKurier (Offline-Client)
│   │   └── DemoClient.php                      # Demo/Test Supplier
│   ├── Command/                                # CLI-Befehle
│   │   ├── LogTestCommand.php                  # ff:log:test
│   │   ├── PriceUpdateCommand.php              # ff:price:update
│   │   ├── PropertyGroupCleanupCommand.php     # ff:property-group:cleanup
│   │   └── GoCityTradeApiTestCommand.php       # ff:gocity:trade-api-test (Sandbox-Trade-API-Evidenz)
│   ├── Constant/
│   │   └── OctoErrorCode.php                   # Fehlercodes (ALREADY_CONFIRMED)
│   ├── Constraint/                             # Validierung
│   │   ├── Availability/
│   │   │   ├── AvailabilityCalendarConstraintCollection.php
│   │   │   └── AvailabilityCheckConstraintCollection.php
│   │   ├── Booking/
│   │   │   └── ReservationConstraintCollection.php
│   │   ├── ConstraintCollectionRegistry.php
│   │   └── ValidationResponse.php
│   ├── Controller/                             # HTTP-Controller
│   │   ├── AvailbilityController.php           # Storefront: Verfügbarkeit
│   │   ├── CartController.php                  # Storefront: Warenkorb (überschreibt Default)
│   │   ├── SessionController.php               # Storefront: Session-Management
│   │   ├── NotificationController.php          # Storefront: Flash-Messages
│   │   ├── OctoProductController.php           # Admin API: Produkte
│   │   ├── PropertyController.php              # Admin API: Property Groups
│   │   ├── VariantController.php               # Admin API: Varianten
│   │   ├── MediaController.php                 # Admin API: Medien
│   │   └── PriceController.php                 # Admin API: Preise
│   ├── Core/
│   │   ├── Api/Octo/                           # API-Client-Kern
│   │   │   ├── OctoApiClientInterface.php
│   │   │   ├── CachedOctoApiClientInterface.php
│   │   │   ├── AbstractOctoApiClient.php       # Basis mit HTTP & Cache
│   │   │   ├── OctoApiClient.php               # Konkrete API-Methoden
│   │   │   ├── CachedOctoApiClient.php         # Cache-Decorator
│   │   │   ├── OctoApiClientRegistry.php       # Client-Registry
│   │   │   └── OctoErrorResponse.php           # Fehler-DTO
│   │   ├── Checkout/Cart/
│   │   │   └── OctoCartCollector.php           # Cart Processor
│   │   ├── Content/OctoProduct/                # Entity Definition
│   │   │   ├── OctoProductDefinition.php
│   │   │   ├── OctoProductEntity.php
│   │   │   └── OctoProductCollection.php
│   │   └── Framework/
│   │       ├── Config/PluginLoggerTrait.php
│   │       └── Migration/DatabaseTrait.php
│   ├── Enum/
│   │   └── ConstraintCollectionEnum.php
│   ├── Extension/Content/Product/
│   │   └── ProductExtension.php                # Erweitert SW Product Entity
│   ├── Helper/
│   │   └── ClassHelper.php                     # Reflection-Helper
│   ├── Interface/
│   │   └── ConstraintCollectionInterface.php
│   ├── Migration/                              # DB-Migrationen
│   │   ├── Migration1755686022CreateOctoProductTable.php
│   │   ├── Migration1757686022CreateProductExtension.php
│   │   └── Migration1768988700AddOctoProductIdentifierIndex.php
│   ├── Resources/
│   │   ├── app/administration/                 # Admin-JS
│   │   ├── app/storefront/                     # Storefront-JS
│   │   ├── config/                             # Service-Definitions (XML)
│   │   ├── snippet/                            # Übersetzungen (JSON)
│   │   └── views/                              # Twig-Templates
│   ├── Service/                                # Business Logic
│   │   ├── BookingService.php
│   │   ├── CheckoutService.php
│   │   ├── MediaService.php
│   │   ├── PriceService.php
│   │   ├── PropertyService.php
│   │   ├── SessionService.php
│   │   ├── StateService.php
│   │   ├── ValidationService.php
│   │   ├── ScheduledTask/                      # Scheduled Tasks
│   │   │   ├── OctoApiWarmCacheTask.php
│   │   │   ├── OctoApiWarmCacheHandler.php
│   │   │   ├── OctoApiPriceUpdaterTask.php
│   │   │   └── OctoApiPriceUpdaterHandler.php
│   │   └── Testing/                            # Test-/Zertifizierungs-Helper
│   │       └── TradeApiTestRunner.php          # Go City V2 Trade API Sandbox-Runner
│   ├── Struct/
│   │   └── MediaFile.php
│   ├── Subscriber/                             # Event Subscriber
│   │   ├── OrderSubscriber.php
│   │   ├── ProductDeleteSubscriber.php
│   │   ├── ProductDetailSubscriber.php
│   │   └── ProductSaveSubscriber.php
│   └── Twig/
│       └── TwigFilters.php                     # json_decode Filter
├── docs/                                       # Ausführliche Dokumentation
│   ├── architecture.md
│   ├── api-clients.md
│   ├── configuration.md
│   ├── database-entities.md
│   ├── flows-booking.md
│   ├── gocity-api.md
│   ├── goldentours-products.md
│   ├── price-calculation.md
│   ├── routes-controllers.md
│   ├── scheduled-tasks.md
│   ├── session-management.md
│   ├── storefront-javascript.md
│   ├── supplier-comparison.md
│   ├── twig-templates.md
│   ├── ventrata-octo-api.md
│   ├── administration.md
│   └── api/products/
│       ├── goldentours.json                    # Beispiel-Response (6.2 MB, 278 Produkte)
│       └── gocity.json                         # Beispiel-Response (344 KB, 49 Produkte)
├── requests/                                   # HTTP-Client Testdateien
│   ├── Octo-Api.http
│   ├── http-client.env.json
│   └── http-client.private.env.json.example
├── composer.json
├── CLAUDE.md
├── CHANGELOG.md
├── readme.md
└── (Quality-Tools: phpunit.xml, psalm.xml, ecs.php, rector.php, .phpcs.xml)
```

## Design Patterns

### Registry Pattern
`OctoApiClientRegistry` verwaltet alle API-Client-Instanzen. Clients werden via Tag `octo.api.client` in `clients.xml` registriert und per `identifier` abgerufen.

`ConstraintCollectionRegistry` sammelt Validierungs-Constraints via Tag `octo.validation.constraint-collection`, abrufbar per Enum-Key.

### Strategy Pattern
Verschiedene Supplier (`GoldenToursClient`, `GoCityClient`, `RheinKurierClient`, `DemoClient`) implementieren das gleiche Interface, aber mit unterschiedlichen Konfigurationen (API-URLs, Keys, Offline-Modus).

### Decorator Pattern (Cache)
`CachedOctoApiClient` erweitert `OctoApiClient` und umhüllt jede Methode mit Cache-Logik über `getCachedItem()`. Cache-Keys enthalten Supplier-ID, Produkt-ID, Datumsbereich etc.

### Service Layer Pattern
Alle Business-Logik liegt in Services (`BookingService`, `PriceService`, `CheckoutService` etc.), die via Dependency Injection bereitgestellt werden. Alle Services sind `readonly` deklariert.

### Constraint-basierte Validierung
`ConstraintCollectionRegistry` sammelt Symfony-Constraint-Collections, die per Enum-Key abrufbar sind. Jede Collection implementiert `ConstraintCollectionInterface`.

## Vererbungshierarchie API-Client

```
OctoApiClientInterface
    └── AbstractOctoApiClient (implements OctoApiClientInterface)
            └── OctoApiClient (extends AbstractOctoApiClient)
                    └── CachedOctoApiClient (extends OctoApiClient, implements CachedOctoApiClientInterface)
                            ├── GoldenToursClient
                            ├── GoCityClient
                            ├── RheinKurierClient (OFFLINE = true)
                            └── DemoClient
```

## Shopware-Integration

- **Entity Extension**: `ProductExtension` fügt dem Shopware-Product-Entity ein `ffOctoProduct`-Feld (ManyToOne-Relation) hinzu
- **Cart Processor**: `OctoCartCollector` implementiert `CartProcessorInterface` und berechnet dynamische Preise (Priority 6000)
- **Scheduled Tasks**: Zwei Tasks (`OctoApiWarmCacheTask`, `OctoApiPriceUpdaterTask`) laufen alle 3 Stunden über Symfony Messenger
- **Event Subscriber**: 4 Subscriber reagieren auf Produkt- und Order-Events
- **Route Override**: `CartController` überschreibt `/checkout/line-item/add` mit Priority 100
- **Twig Extension**: `TwigFilters` stellt `json_decode` Filter bereit

## Online vs. Offline Clients

Zentrales Architektur-Konzept: Clients mit `OFFLINE = true` (RheinKurier) machen **keine** HTTP-Requests. An folgenden Stellen muss das geprüft werden:

| Klasse | Verhalten bei Offline |
|--------|----------------------|
| `AbstractOctoApiClient::request()` | Returns `[]` |
| `AvailbilityController` | Fake-Availability aus `pricingFrom` |
| `CartController` | Keine Reservierung |
| `BookingService` | Returns `[]` |
| `CheckoutService::confirmTicket()` | Überspringt API-Call |
| `CheckoutService::cancelOrder()` | Überspringt API-Call |
| `OrderSubscriber::onAccountOrderPageLoadedEvent()` | Kein Cancellable-Check |
| `OctoApiPriceUpdaterHandler` | Überspringt RheinKurier |
| `OctoApiWarmCacheHandler` | Überspringt Offline |

## Deterministische UUID-Generierung

Das Plugin nutzt `Symfony\Component\Uid\Uuid::fromStringToHex()` für reproduzierbare IDs:

```php
// Property Group
Uuid::fromStringToHex("{apiProductId}-property-group")

// Property Group Option
Uuid::fromStringToHex("{apiProductId}-{reference}-{identifier}-property-group-option")

// Configurator Setting
Uuid::fromStringToHex("{apiProductId}-{reference}-{identifier}")

// Manufacturer
Uuid::fromStringToHex("{identifier}-manufacturer")

// Unique Line-Item ID (identisch in 3 Klassen!)
$unitString = implode('__', array_map(fn($u) => "{$u['id']}_q{$u['quantity']}", $units));
Uuid::fromStringToHex($productId . $unitString)
```
