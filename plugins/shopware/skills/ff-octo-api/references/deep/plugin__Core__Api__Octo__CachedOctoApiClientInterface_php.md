# CachedOctoApiClientInterface (`src/Core/Api/Octo/CachedOctoApiClientInterface.php`)

## Zweck
Erweitert `OctoApiClientInterface` um die gecachten Varianten aller relevanten API-Methoden. Typ, den die Registry und Controller als Client-Vertrag verwenden.

## Typ
- Namespace: `FfOctoApi\Core\Api\Octo`
- `interface CachedOctoApiClientInterface extends OctoApiClientInterface`

## Methoden
Gecachte Pendants: `getCachedProducts(expireAfter=null)`, `getCachedProduct(productId)`, `getCachedSuppliers()`, `getCachedSupplier(supplierId?)`, `getCachedSupplierDestinations(supplierId?)`, `getCachedAvailabilityCalendar(...)`, `getCachedAvailability(...)`, `getCachedBooking(uuid)`, `getCachedBookings(...)`, `getCachedBookingsByResellerReference(...)`, `…BySupplierReference(...)`, `…ByLocalDateReference(...)`, `…ByDateRangeReference(...)`.
Zusätzlich (wiederholt): `getColor()`, `getIdentifier()`, `isOffline()`, `getTargetDestination()`, `getApiEnvKey()`, `getApiConfigKey()`.

## Bezüge
`OctoApiClientInterface`, `CachedOctoApiClient`, `OctoApiClientRegistry`.
