# API-Client-Architektur & Methoden

## Vererbungshierarchie

```
OctoApiClientInterface
  └── AbstractOctoApiClient        (HTTP, Auth, Headers, Config)
      └── OctoApiClient            (OCTO API Methoden)
          └── CachedOctoApiClient  (PSR-6 Caching Decorator)
              ├── GoldenToursClient
              ├── GoCityClient
              ├── RheinKurierClient (OFFLINE = true)
              └── DemoClient
```

## AbstractOctoApiClient

**Datei:** `src/Core/Api/Octo/AbstractOctoApiClient.php`
**Namespace:** `FfOctoApi\Core\Api\Octo`

### Konstanten (werden von konkreten Clients überschrieben)

```php
public const string IDENTIFIER = '';
public const bool OFFLINE = false;
public const string DESTINATION_ID = '';
public const string SUPPLIER_ID = '';
protected const string API_KEY_CONFIG_KEY = '';
protected const string API_ENV_KEY = '';
protected const string BASE_URL = '';
protected const string COLOR = '';
```

### Konstruktor

```php
public function __construct(
    private readonly SystemConfigService $systemConfigService,
    private readonly HttpClientInterface $httpClient,
    protected readonly LoggerInterface $logger,
    protected readonly CacheItemPoolInterface $cache,
)
```

### API-Key-Resolution (Env hat Vorrang)

```php
public function getApiKey(?string $salesChannelId = null): string
// 1. Prüft Environment-Variable (z.B. OCTO_API_KEY_GOLDEN_TOURS)
// 2. Fallback auf SystemConfig (z.B. FfOctoApi.config.goldentoursApiKey)
```

### HTTP Headers

Jeder Request enthält:
```
Authorization: Bearer {API_KEY}
Accept-Language: de-DE, en-GB
Octo-Available-Languages: de, en
Content-Type: application/json
Octo-Env: test|live
Octo-Capabilities: octo/content,octo/pricing  (konfigurierbar)
```

**WICHTIG:** `Octo-Capabilities` Header ist Pflicht! Ohne ihn gibt die API HTTP 400.

### Kern-Methode: request()

```php
public function request(
    string $method,
    string $uri,
    ?HttpOptions $options = null,
    bool $origin = false,    // true = nur URI ohne BASE_URL
    bool $returnError = false // true = OctoErrorResponse statt Exception
): array|ResponseInterface|OctoErrorResponse
```

- Offline-Clients (`OFFLINE = true`) geben sofort `[]` zurück
- Baut HTTP-Client mit `getClientOptions()` (Auth-Headers, Base-URL)
- Setzt `Octo-Env` basierend auf `isTestEnv()` Config
- Bei Fehler: wirft Exception oder gibt `OctoErrorResponse` zurück

### Cache-Methode

```php
protected function getCachedItem(
    string $cacheKey,
    string $getter,         // Methodenname (z.B. 'getProducts')
    array $getterParams,    // Parameter für die Methode
    int|null $expireAfter   // null = Config-Wert
): mixed
```

Cache-Key-Pattern: `ff.octo-api.{resource}.{SUPPLIER_ID}[.{additional}]`

### Konfigurationsleser

```php
public function getCacheExpirationTime(?string $salesChannelId = null): int
// SystemConfig: FfOctoApi.config.expirationTime (default 10800s = 3h)

public function getBookingReservationTime(?string $salesChannelId = null): int
// SystemConfig: FfOctoApi.config.bookingReservationTime (Minuten, default 10, min 5)

public function isTestEnv(?string $salesChannelId = null): bool
// SystemConfig: FfOctoApi.config.testingEnvironment (default true)
```

### Getter/Setter für Sprache und Capabilities

```php
public function getAcceptLanguage(): string
public function setAcceptLanguage(string $acceptLanguage): static
public function getOctoAvailableLanguages(): string
public function setOctoAvailableLanguages(string $octoAvailableLanguages): static
public function getCapabilities(): array<string>
public function setCapabilities(array<string> $capabilities): static
```

Default Capabilities: `['octo/content', 'octo/pricing']`

---

## OctoApiClient — OCTO API Methoden

**Datei:** `src/Core/Api/Octo/OctoApiClient.php`

### Products

```php
public function getProducts(): array
// GET /products?destinationId={DESTINATION_ID}

public function getProduct(string $productId): array
// GET /products/{productId}?destinationId={DESTINATION_ID}
```

### Suppliers

```php
public function getSuppliers(): array
// GET /suppliers

public function getSupplier(?string $supplierId = null): array
// GET /supplier/{supplierId}

public function getSupplierDestinations(?string $supplierId = null): array
// Returns [] (nicht implementiert)
```

### Availability

```php
public function getAvailability(
    string $productId,
    string $optionId,
    DateTimeInterface $localStartDate,
    DateTimeInterface $localEndDate,
    array $units,
    string $dateFormat = 'Y-m-d H:i:s'
): array
// POST /availability
// Body: { productId, optionId, localDateStart, localDateEnd, units: [{id, quantity}] }

public function getAvailabilityCalendar(
    string $productId,
    string $optionId,
    DateTimeInterface $localStartDate,
    DateTimeInterface $localEndDate,
    array $units
): array
// POST /availability/calendar
// Body: { productId, optionId, localDateStart, localDateEnd, units }
```

**GoCity-Unterschied:** Nutzt `Y-m-d` statt `Y-m-d H:i:s` für Datumsformat.

### Bookings

```php
public function bookingReservation(
    ?string $uuid,
    ?int $expirationMinutes,
    string $productId,
    string $optionId,
    string $availabilityId,
    array $unitItems          // [{unitId: string, uuid?: string}]
): array
// POST /bookings
// Body: { uuid, productId, optionId, availabilityId, expirationMinutes, unitItems }

public function bookingUpdate(
    ?string $uuid,
    ?int $expirationMinutes,
    string $productId,
    string $optionId,
    string $availabilityId,
    array $unitItems
): array
// PATCH /bookings/{uuid}

public function bookingConfirm(
    string $uuid,
    string $fullName,
    string $emailAddress,
    array $locales = ['de-DE'],
    string $country = 'de',
    bool $emailReceipt = false,
    ?string $resellerReference = null
): array|OctoErrorResponse
// POST /bookings/{uuid}/confirm
// Body: { contact: {fullName, emailAddress, locales, country}, emailReceipt, resellerReference }
// returnError = true (gibt OctoErrorResponse bei Fehler)

public function bookingCancellation(string $uuid): array
// DELETE /bookings/{uuid}

public function bookingReservationExtend(string $uuid, int $expirationMinutes): array
// POST /bookings/{uuid}/extend

public function getBooking(string $uuid): array
// GET /bookings/{uuid}

public function getBookings(
    ?string $resellerReference = null,
    ?string $supplierReference = null,
    ?DateTimeInterface $localDate = null,
    ?DateTimeInterface $localDateStart = null,
    ?DateTimeInterface $localDateEnd = null,
    ?string $productId = null,
    ?string $optionId = null
): array
// GET /bookings?{filters}
```

### Convenience-Booking-Methoden

```php
public function getBookingsByResellerReference(string $resellerReference, ?string $productId, ?string $optionId): array
public function getBookingsBySupplierReference(string $supplierReference, ?string $productId, ?string $optionId): array
public function getBookingsByLocalDateReference(DateTimeInterface $localDate, ?string $productId, ?string $optionId): array
public function getBookingsByDateRangeReference(DateTimeInterface $localDateStart, DateTimeInterface $localDateEnd, ?string $productId, ?string $optionId): array
```

### Webhooks

```php
public function getWebhooks(): array
// GET /webhooks

public function registerWebhook(string $url, string $event): array
// POST /webhooks { url, event }
// Events: booking_update, availability_update

public function deleteWebhook(string $webhookId): int
// DELETE /webhooks/{webhookId}
```

---

## CachedOctoApiClient

**Datei:** `src/Core/Api/Octo/CachedOctoApiClient.php`

Alle Methoden folgen dem Muster `getCached{MethodName}()`:

```php
public function getCachedProducts(int|null $expireAfter = null): array
// Cache-Key: ff.octo-api.products.{SUPPLIER_ID}

public function getCachedProduct(string $productId): array
// Cache-Key: ff.octo-api.product.{productId}.{SUPPLIER_ID}

public function getCachedAvailability(...): array
// Cache-Key: ff.octo-api.availability.{productId}.{optionId}.{startDate}.{endDate}.{SUPPLIER_ID}
```

**NICHT gecacht** (müssen immer live sein):
- `bookingReservation()`, `bookingConfirm()`, `bookingCancellation()`
- `bookingUpdate()`, `bookingReservationExtend()`

---

## Konkrete Client-Implementierungen

### GoldenToursClient

**Datei:** `src/Client/Octo/GoldenToursClient.php`

```php
public const string IDENTIFIER = 'goldentours';
public const string DESTINATION_ID = '8affd1a6-0c7b-4da6-aff8-c8e6a4bc4247';
public const string SUPPLIER_ID = '0c7060de-d196-40dd-9f35-42880db8cd6c';
protected const string API_KEY_CONFIG_KEY = 'FfOctoApi.config.goldentoursApiKey';
protected const string API_ENV_KEY = 'OCTO_API_KEY_GOLDEN_TOURS';
protected const string BASE_URL = 'https://api.ventrata.com/octo/';
protected const string COLOR = '#FFE082';
```

- 278 Produkte aus London
- Availability-Typen: START_TIME, OPENING_HOURS
- 8 Unit-Typen: ADULT, YOUTH, CHILD, INFANT, FAMILY, SENIOR, STUDENT, OTHER
- Dual-Currency: GBP + EUR
- Delivery-Formate: QRCODE, PNG_URL, PKPASS_URL, GOOGLE_WALLET_URL, PDF_URL, AZTECCODE

### GoCityClient

**Datei:** `src/Client/Octo/GoCityClient.php`

```php
public const string IDENTIFIER = 'gocity';
public const string DESTINATION_ID = '3293bf46-050c-424d-b29f-4dd1de7300f7';
public const string SUPPLIER_ID = 'b565b694-18e3-488f-88c2-829c3150d4a4';
protected const string API_KEY_CONFIG_KEY = 'FfOctoApi.config.gocityApiKey';
protected const string API_ENV_KEY = 'OCTO_API_KEY_GO_CITY';
protected const string BASE_URL = 'https://api.staging.gocity.tech/octo/';
protected const string COLOR = '#90dde3';
```

**Override:**
```php
public function getCachedSupplier(?string $supplierId = null): array
// Ruft /supplier statt /supplier/{id} auf (GoCity-API-Unterschied)
```

- 49 Produkte in 25 Städten (Europa, Nordamerika, Naher Osten)
- Nur 2 Unit-Typen: ADULT (ab 13), CHILD (3-12)
- Booking-Status: `ON_HOLD` statt `PENDING`
- Datum-Format: `Y-m-d` statt `Y-m-d H:i:s`
- Availability immer FREESALE

### RheinKurierClient

**Datei:** `src/Client/Octo/RheinKurierClient.php`

```php
public const string IDENTIFIER = 'rheinkurier';
public const bool OFFLINE = true;
protected const string COLOR = '#6699CC';
```

- **OFFLINE** — Keine API-Calls!
- Preise aus `pricingFrom` im gespeicherten Produkt-JSON
- Keine Reservierungen, Bestätigungen oder Stornierungen

### DemoClient

**Datei:** `src/Client/Octo/DemoClient.php`

```php
public const string IDENTIFIER = 'demo';
public const string DESTINATION_ID = '05327791-626d-433c-8c65-0f436f1b92c6';
public const string SUPPLIER_ID = '697e3ce8-1860-4cbf-80ad-95857df1f640';
protected const string API_KEY_CONFIG_KEY = 'FfOctoApi.config.demoApiKey';
protected const string API_ENV_KEY = 'OCTO_API_KEY_DEMO';
protected const string BASE_URL = 'https://api.ventrata.com/octo/';
protected const string COLOR = '#F8BBD0';
```

---

## OctoApiClientRegistry

**Datei:** `src/Core/Api/Octo/OctoApiClientRegistry.php`

```php
public function __construct(iterable<CachedOctoApiClientInterface> $clients)
// Tagged Iterator: Tag "octo.api.client" (definiert in clients.xml)

public function getClientByIdentifier(
    string $identifier,
    string $acceptLanguage = 'de-DE, en-GB',
    string $octoAvailableLanguages = 'de, en'
): CachedOctoApiClientInterface

public function getClientIdentifiers(): array          // ['goldentours', 'gocity', 'rheinkurier', 'demo']
public function getClientApiConfigKeys(): array        // API Config Keys aller Clients
public function getClients(): CachedOctoApiClientInterface[]
public function getOnlineClients(): CachedOctoApiClientInterface[]  // Filtert OFFLINE aus
public function getOfflineClients(): CachedOctoApiClientInterface[]
public function isOfflineClient(string $identifier): bool
```

---

## OctoErrorResponse

**Datei:** `src/Core/Api/Octo/OctoErrorResponse.php`

```php
public function __construct(private readonly ResponseInterface $response)
public function getMessage(): string   // Extrahiert errorMessage oder errorCode aus Response-JSON
public function getCode(): string      // Extrahiert errorCode oder error
public function getResponse(): TraceableResponse
```

---

## Service-Registrierung (clients.xml)

```xml
<service id="FfOctoApi\Core\Api\Octo\OctoApiClientRegistry">
    <argument type="tagged_iterator" tag="octo.api.client"/>
</service>

<service id="FfOctoApi\Client\Octo\GoldenToursClient">
    <tag name="octo.api.client"/>
    <!-- Arguments: SystemConfigService, http_client, logger (octo channel), cache.app -->
</service>
<!-- Analog für GoCityClient, RheinKurierClient, DemoClient -->
```

## Neuen Client hinzufügen

1. Erstelle Klasse in `src/Client/Octo/` die `CachedOctoApiClient` erweitert
2. Setze alle Konstanten: IDENTIFIER, SUPPLIER_ID, DESTINATION_ID, BASE_URL, COLOR, API_KEY_CONFIG_KEY, API_ENV_KEY
3. Registriere in `clients.xml` mit Tag `octo.api.client`
4. Füge API-Key-Config in `config.xml` hinzu
5. Füge Snippet für Admin-Supplier-Name hinzu
6. Bei OFFLINE: Setze `OFFLINE = true` und teste alle Code-Pfade