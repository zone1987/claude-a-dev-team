# OctoApiClientInterface (`src/Core/Api/Octo/OctoApiClientInterface.php`)

## Zweck
Vertrag für OCTO-API-Clients: definiert alle API-Operationen (Products, Suppliers, Availability, Bookings, Webhooks) sowie die Konfig-/Metadaten-Getter und Sprach-/Capability-Setter.

## Typ
- Namespace: `FfOctoApi\Core\Api\Octo`
- `interface OctoApiClientInterface` (implementiert von `AbstractOctoApiClient`).

## Methoden (Auswahl, vollständige Liste = API-Oberfläche)
- Produkte/Supplier: `getProduct(productId)`, `getProducts()`, `getSupplier()`, `getSupplierId()`, `getSuppliers()`, `getSupplierDestinations()`.
- Sprache/Capabilities: `get/setAcceptLanguage`, `get/setOctoAvailableLanguages`, `get/setCapabilities` (Setter `static`).
- Availability: `getAvailabilityCalendar(...)`, `getAvailability(...)`.
- Bookings: `bookingReservation(...)`, `bookingUpdate(...)`, `bookingConfirm(...): array|OctoErrorResponse`, `bookingCancellation(uuid)`, `bookingReservationExtend(uuid, min)`, `getBooking(uuid)`, `getBookings(...)` + 4 Referenz-Wrapper.
- Webhooks: `getWebhooks()`, `registerWebhook(url, event)`, `deleteWebhook(webhookId): int`.
- Metadaten: `getColor()`, `getIdentifier()`, `isOffline()`, `getTargetDestination()`, `getApiEnvKey()`, `getApiConfigKey()`, `getCacheExpirationTime(?salesChannelId)`.

## Bezüge
`AbstractOctoApiClient`, `OctoApiClient`, `CachedOctoApiClientInterface`, `OctoErrorResponse`.
