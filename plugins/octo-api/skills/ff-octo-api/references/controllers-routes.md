# Controller & Routen

## Übersicht

| Route | Methode | Controller | Scope | Beschreibung |
|-------|---------|-----------|-------|-------------|
| `/api/octo/products` | GET | OctoProductController | Admin | Alle API-Produkte aller Supplier |
| `/api/octo/product` | POST | OctoProductController | Admin | Einzelnes API-Produkt |
| `/api/property-group/create` | POST | PropertyController | Admin | Property Group aus API-Optionen |
| `/api/product-variants/create` | POST | VariantController | Admin | Varianten aus API-Optionen |
| `/api/product-media/assign` | POST | MediaController | Admin | Medien aus API importieren |
| `/api/product-price/update` | POST | PriceController | Admin | Preise aus API aktualisieren |
| `/octo-api/availability/check` | POST | AvailbilityController | Storefront | Verfügbarkeitsprüfung |
| `/octo-api/availability/calendar` | POST | AvailbilityController | Storefront | Monatskalender |
| `/octo-api/session/set` | POST | SessionController | Storefront | Session-Wert setzen |
| `/octo-api/session/get-item` | POST | SessionController | Storefront | Session-Wert lesen |
| `/octo-api/session/remove-item` | POST | SessionController | Storefront | Session-Wert löschen |
| `/checkout/line-item/add` | POST | CartController | Storefront | **Priority 100!** |
| `/notification/notify` | POST | NotificationController | Storefront | Flash-Message senden |

---

## Admin-Controller

### OctoProductController

**Datei:** `src/Controller/OctoProductController.php`

```php
#[Route(path: '/api/octo/products', name: 'api.octo-product.list', methods: ['GET'],
    defaults: ['_routeScope' => ['administration']])]
public function listProducts(): JsonResponse
```
- Iteriert alle Online-Clients
- Filtert GoCity-Produkte ohne 'LON'-Prefix
- Markiert bereits verwendete Produkte als `disabled: true`
- Generiert deterministische IDs: `Uuid::fromStringToHex("{productId}-{reference}-{identifier}")`
- Response: `[{ id, identifier, color, product: {...}, disabled }]`

```php
#[Route(path: '/api/octo/product', name: 'api.octo-product.product', methods: ['POST'],
    defaults: ['_routeScope' => ['administration']])]
public function getProduct(Request $request, Context $context): JsonResponse
```
- Params: `uuid` (string), `identifier` (string)
- Response: `{ id, identifier, product: {...} }`

### PropertyController

**Datei:** `src/Controller/PropertyController.php`

```php
#[Route(path: '/api/property-group/create', name: 'api.property-group.create', methods: ['POST'],
    defaults: ['_routeScope' => ['administration']])]
public function createPropertyGroup(Request $request, Context $context): JsonResponse
```
- Param: `apiProduct` (array) — komplettes API-Produkt
- Delegiert an `PropertyService::createPropertyGroup()`
- Response: `{ propertyGroup: { id, name, options: [...] } }`

### VariantController

**Datei:** `src/Controller/VariantController.php`

```php
#[Route(path: '/api/product-variants/create', name: 'api.product-variants.create', methods: ['POST'],
    defaults: ['_routeScope' => ['administration']])]
public function createProductVariants(Request $request, Context $context): JsonResponse
```
- Params: `apiProduct`, `propertyGroup`, `product`
- Erstellt/aktualisiert Varianten mit Configurator-Settings
- Löscht alte Varianten die nicht mehr in der API sind
- Setzt Manufacturer aus API-Product Brand
- Response: `{ success: true }`

### MediaController

**Datei:** `src/Controller/MediaController.php`

```php
#[Route(path: '/api/product-media/assign', name: 'api.product-media.assign', methods: ['POST'],
    defaults: ['_routeScope' => ['administration']])]
public function assignProductMedia(Request $request, Context $context): JsonResponse
```
- Params: `apiProduct`, `product`
- Importiert Banner, Gallery und Cover-Bilder
- Response: `{ success: true }` oder Fehler

### PriceController

**Datei:** `src/Controller/PriceController.php`

```php
#[Route(path: '/api/product-price/update', name: 'api.product-price.update', methods: ['POST'],
    defaults: ['_routeScope' => ['administration']])]
public function updateProductPrices(Request $request, Context $context): JsonResponse
```
- Params: `apiProduct`, `identifier`, `productId`
- Delegiert an `PriceService::updatePrices()`
- Response: `{ success: true }`

---

## Storefront-Controller

### AvailbilityController

**Datei:** `src/Controller/AvailbilityController.php`
**Hinweis:** Typo im Dateinamen (`Availbility` statt `Availability`)

```php
#[Route(path: '/octo-api/availability/check', name: 'frontend.octo-api.availability.check',
    methods: ['POST'], defaults: ['XmlHttpRequest' => true, '_httpCache' => false,
    '_routeScope' => ['storefront']])]
public function checkAvailability(Request $request, SalesChannelContext $context): Response
```
- Validiert via `AvailabilityCheckConstraintCollection`
- Merged Units aus Request mit Session-Daten
- Ruft API-Availability auf (oder Fake für Offline-Clients)
- Schreibt Session-Daten (beide Keys)
- **Gibt HTML zurück** (gerendert via `octo-configurator.html.twig`)

```php
#[Route(path: '/octo-api/availability/calendar', name: 'frontend.octo-api.availability.calendar',
    methods: ['POST'], defaults: ['XmlHttpRequest' => true, '_httpCache' => false,
    '_routeScope' => ['storefront']])]
public function availabilityCalendar(Request $request, SalesChannelContext $context): JsonResponse
```
- Validiert via `AvailabilityCalendarConstraintCollection`
- Offline-Clients: `return new JsonResponse([])`
- Response: JSON-Array mit Tagesverfügbarkeiten

### CartController

**Datei:** `src/Controller/CartController.php`

```php
#[Route(path: '/checkout/line-item/add', name: 'frontend.checkout.line-item.add',
    methods: ['POST'], defaults: ['XmlHttpRequest' => true, '_routeScope' => ['storefront']],
    priority: 100)]
public function addLineItems(Cart $cart, RequestDataBag $requestDataBag, Request $request,
    SalesChannelContext $context): Response
```

**Priority 100** — überschreibt den Standard-Shopware-CartController!

- Handhabt sowohl normale als auch OCTO-Produkte
- Für OCTO: Liest Session, erstellt Reservierung, setzt Payload
- Siehe `references/booking-flow.md` Phase 3 für Details

### SessionController

**Datei:** `src/Controller/SessionController.php`

```php
#[Route(path: '/octo-api/session/set', name: 'frontend.octo-api.session.set',
    methods: ['POST'], defaults: ['XmlHttpRequest' => true, '_httpCache' => false,
    '_routeScope' => ['storefront']])]
public function setItem(Request $request): Response

#[Route(path: '/octo-api/session/get-item', name: 'frontend.octo-api.session.get-item',
    methods: ['POST'], defaults: ['XmlHttpRequest' => true, '_httpCache' => false,
    '_routeScope' => ['storefront']])]
public function getItem(Request $request): JsonResponse

#[Route(path: '/octo-api/session/remove-item', name: 'frontend.octo-api.session.remove-item',
    methods: ['POST'], defaults: ['XmlHttpRequest' => true, '_httpCache' => false,
    '_routeScope' => ['storefront']])]
public function removeItem(Request $request): JsonResponse
```

### NotificationController

**Datei:** `src/Controller/NotificationController.php`

```php
#[Route(path: '/notification/notify', name: 'frontend.notification.send',
    methods: ['POST'], defaults: ['XmlHttpRequest' => true, '_routeScope' => ['storefront']])]
public function notify(Request $request, SalesChannelContext $context): Response
```
- Params: `message` (string), `snippet` (string, optional), `parameters` (array, optional), `type` (string, default 'info')
- Nutzt `addFlash()` für Storefront-Benachrichtigungen

---

## Validierung

### AvailabilityCheckConstraintCollection

**Datei:** `src/Constraint/Availability/AvailabilityCheckConstraintCollection.php`
**Category:** `availability_check`
**Datumsformat:** `Y-m-d\TH:i:s.v\Z`

| Feld | Typ | Pflicht | Zusatz |
|------|-----|---------|--------|
| identifier | string | Ja | NotBlank |
| productUuid | string | Ja | NotBlank |
| productId | string | Ja | NotBlank |
| localDateStart | DateTime | Ja | Format: `Y-m-d\TH:i:s.v\Z` |
| localDateEnd | DateTime | Ja | Format: `Y-m-d\TH:i:s.v\Z` |
| localTimeStart | string | Nein | Regex: `/^([01]\d|2[0-3]):([0-5]\d)$/` |
| product | array | Nein | — |
| units | array | Nein | Collection mit id + quantity |

### AvailabilityCalendarConstraintCollection

**Category:** `availability_calendar`

| Feld | Typ | Pflicht |
|------|-----|---------|
| identifier | string | Ja |
| productId | string | Ja |
| optionId | string | Ja |
| date | DateTime | Ja |
| units | array | Nein |

### ReservationConstraintCollection

**Datei:** `src/Constraint/Booking/ReservationConstraintCollection.php`
**Category:** `booking_reservation`

| Feld | Typ | Pflicht |
|------|-----|---------|
| identifier | string | Ja |
| uuid | string | Ja |
| productId | string | Ja |
| optionId | string | Ja |
| availabilityId | string | Ja |
| expirationMinutes | integer | Nein |
| unitItems | array | Nein |

---

## Route-Konfiguration

**Datei:** `src/Resources/config/routes.xml`

```xml
<import resource="../../Controller/*Controller.php" type="attribute" />
```

Alle Controller nutzen PHP-Attribute für Routing. Die XML-Datei importiert sie automatisch.

## Controller-Registrierung

**Datei:** `src/Resources/config/controllers.xml`

Alle Controller sind als public Services registriert mit `setContainer` Call-Methode und ihren jeweiligen Dependencies (Services, Repositories, etc.).
