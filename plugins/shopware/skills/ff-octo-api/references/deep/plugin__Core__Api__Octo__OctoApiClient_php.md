# OctoApiClient (`src/Core/Api/Octo/OctoApiClient.php`)

## Zweck
Implementiert die konkreten OCTO-API-Methoden (Products, Suppliers, Availability, Bookings, Webhooks) auf Basis von `AbstractOctoApiClient::request()`. Erbt Auth/Header/Caching-Infrastruktur, fügt die fachlichen Endpunkte hinzu. (`/** @noinspection DuplicatedCode */`.)

## Typ & Vererbung
- Namespace: `FfOctoApi\Core\Api\Octo`
- `class OctoApiClient extends AbstractOctoApiClient`

## Methoden (alle ohne eigenes Caching — Caching liegt in `CachedOctoApiClient`)
**Produkte/Supplier:**
- `getProducts(): array` — GET `products` mit Query `destinationId`.
- `getProduct(productId): array` — GET `products/{id}` mit Query `destinationId`.
- `getSuppliers(): array` — GET `suppliers`.
- `getSupplier(?supplierId): array` — GET `supplier/{id}` (Default eigener `SUPPLIER_ID`).
- `getSupplierDestinations(?supplierId): array` — **gibt aktuell hart `[]` zurück** (echter Call auskommentiert).

**Availability:**
- `getAvailabilityCalendar(productId, optionId, localStartDate, localEndDate, units=[]): array` — POST `availability/calendar` (JSON mit `localDateStart/End` als `Y-m-d`).
- `getAvailability(productId, optionId, localDate, localTime=null, units=[]): array` — POST `availability` (JSON).

**Bookings:**
- `bookingReservation(uuid?, expirationMinutes?, productId?, optionId?, availabilityId?, unitItems=[]): array` — POST `bookings` (uuid default `Uuid::randomHex()`, expiration default `getBookingReservationTime()`).
- `bookingUpdate(...)` — PATCH `bookings/{uuid}`.
- `bookingConfirm(uuid, fullName, emailAddress, locales=['de-DE'], country='de', emailReceipt=false, resellerReference=null): array|OctoErrorResponse` — POST `bookings/{uuid}/confirm` (mit `returnError=true` → `OctoErrorResponse` bei Fehler, wichtig für `ALREADY_CONFIRMED`-Handling).
- `bookingCancellation(uuid): array` — POST `bookings/{uuid}/cancel` (`force=true`, leerer `reason`).
- `bookingReservationExtend(uuid, expirationMinutes): array` — POST `bookings/{uuid}/extend`.
- `getBooking(uuid): array` — GET `bookings/{uuid}`.
- `getBookings(resellerReference?, supplierReference?, localDate?, localDateStart?, localDateEnd?, productId?, optionId?): array` — GET `bookings` (Query, Datums als `Y-m-d`).
- Bequemlichkeits-Wrapper: `getBookingsByResellerReference`, `getBookingsBySupplierReference`, `getBookingsByLocalDateReference`, `getBookingsByDateRangeReference`.

**Webhooks:**
- `getWebhooks(): array` — setzt Capability `ventrata/webhooks`, GET `webhooks`.
- `deleteWebhook(webhookId): int` — Capability `ventrata/webhooks`, DELETE `webhooks/{id}`, gibt Statuscode (sonst 400).
- `registerWebhook(url, event): array` — Capability `ventrata/webhooks`, POST `webhooks` (event: `booking_update`, `availability_update`; Capabilities `octo/content,octo/pricing`).

## Besonderheiten / Fallstricke
- `getSupplierDestinations` ist ein No-Op (`[]`).
- `bookingConfirm` ist die einzige Methode mit `returnError=true` → kann `OctoErrorResponse` liefern (vom `CheckoutService` ausgewertet).
- Offline-Gate sitzt in `request()` (geerbt) — alle Methoden hier respektieren es automatisch.
- Nur dokumentierte OCTO-Requests verwenden; `Octo-Env: test` Pflicht.

## Bezüge
`AbstractOctoApiClient`, `CachedOctoApiClient`, `OctoErrorResponse`, `Service/CheckoutService.php`, `Service/BookingService.php`, `../ventrata-octo-api.md`.
