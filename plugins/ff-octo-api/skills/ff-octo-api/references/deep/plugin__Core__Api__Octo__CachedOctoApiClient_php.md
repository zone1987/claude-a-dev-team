# CachedOctoApiClient (`src/Core/Api/Octo/CachedOctoApiClient.php`)

## Zweck
PSR-6-Cache-Decorator über `OctoApiClient`: bietet zu jeder API-Methode eine `getCached…`-Variante, die das Ergebnis über `getCachedItem()` (geerbt) zwischenspeichert. Basisklasse aller konkreten Supplier-Clients. (`/** @noinspection DuplicatedCode */`; PHPDoc-`@class OctoApiClient` ist Copy-Paste-Rest.)

## Typ & Vererbung
- Namespace: `FfOctoApi\Core\Api\Octo`
- `class CachedOctoApiClient extends OctoApiClient implements CachedOctoApiClientInterface`

## Methoden (Cache-Key → delegierter Getter)
- `getCachedProducts(expireAfter=null)` → `ff.octo-api.products.{SUPPLIER_ID}` → `getProducts`.
- `getCachedProduct(productId)` → `ff.octo-api.product.{productId}.{SUPPLIER_ID}` → `getProduct`.
- `getCachedSuppliers()` → `…suppliers.{SUPPLIER_ID}` → `getSuppliers`.
- `getCachedSupplier(supplierId?)` → `…supplier.{SUPPLIER_ID}` → `getSupplier`.
- `getCachedSupplierDestinations(supplierId?)` → `…supplier-destinations.{SUPPLIER_ID}` → `getSupplierDestinations` (No-Op).
- `getCachedAvailabilityCalendar(productId, optionId, start, end, units=[])` → Key mit Produkt/Option/Datumsspanne → `getAvailabilityCalendar`.
- `getCachedAvailability(productId, optionId, localDate, localTime=null, units=[])` → Key ohne localTime, **TTL fest 300 s (5 min)** → `getAvailability`.
- `getCachedBooking(uuid)` → `…booking.{uuid}.{SUPPLIER_ID}` → `getBooking`.
- `getCachedBookings(...)` → `…bookings.{SUPPLIER_ID}` → `getBookings`.
- `getCachedBookingsByResellerReference(...)`, `…BySupplierReference(...)`, `…ByLocalDateReference(...)`, `…ByDateRangeReference(...)` → jeweils referenz-/datumsspezifischer Key.

## Besonderheiten / Fallstricke
- Default-TTL = `getCacheExpirationTime()` (Config `expirationTime`); `getCachedAvailability` weicht mit fixen 300 s ab.
- `expireAfter === 0` (in `getCachedItem`) löscht den Cache-Eintrag (Force-Refresh) — genutzt vom Warm-Cache-/Price-Updater-Task.
- **Cache-Key-Tippfehler:** `getCachedBookingsByLocalDateReference` und `…ByDateRangeReference` nutzen beide das Prefix `bookings-by-supplier.…` (Copy-Paste) — kann mit `getCachedBookingsBySupplierReference`-Keys nicht kollidieren (andere Werte), aber semantisch irreführend.
- Offline-Gate sitzt in `request()` (über `getProducts` etc.).

## Bezüge
`OctoApiClient`, `AbstractOctoApiClient`, `CachedOctoApiClientInterface`, Supplier-Clients (`Client/Octo/*`), `OctoApiClientRegistry`.
