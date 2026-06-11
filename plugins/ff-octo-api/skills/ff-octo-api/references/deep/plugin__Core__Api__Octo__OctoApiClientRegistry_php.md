# OctoApiClientRegistry (`src/Core/Api/Octo/OctoApiClientRegistry.php`)

## Zweck
Zentrale Registry aller Supplier-Clients (Service Locator). Wird per Tagged Iterator (`octo.api.client`) befüllt und liefert Clients per Identifier sowie gefilterte Online-/Offline-Listen. Zentrale Stelle für `isOfflineClient`.

## Typ & Vererbung
- Namespace: `FfOctoApi\Core\Api\Octo`
- `class OctoApiClientRegistry`

## Properties
| Property | Typ | Bedeutung |
|----------|-----|-----------|
| `$clients` | `CachedOctoApiClientInterface[]` | Map Identifier → Client. |

## Konstruktor / DI
| Parameter | Typ | Zweck |
|-----------|-----|-------|
| `$clients` | `iterable<CachedOctoApiClientInterface>` | Alle getaggten Clients; indexiert nach `getIdentifier()`. `@internal`. |

## Methoden
- `getClientIdentifiers(): array` — alle Identifier.
- `getClientApiConfigKeys(): array` — alle `API_KEY_CONFIG_KEY`.
- `getClientByIdentifier(identifier, acceptLanguage='de-DE, en-GB', octoAvailableLanguages='de, en'): CachedOctoApiClientInterface` — wirft `InvalidArgumentException` bei unbekanntem Identifier; setzt Sprache/Languages am Client und gibt ihn zurück.
- `getClients(): array` — alle.
- `getOnlineClients(): array` — `!isOffline()`.
- `getOfflineClients(): array` — `isOffline()`.
- `isOfflineClient(identifier): bool` — true wenn vorhanden UND offline.

## Besonderheiten / Fallstricke
- **Shared State:** `getClientByIdentifier` mutiert den (Singleton-)Client (`setAcceptLanguage`/`setCapabilities` an anderer Stelle) — innerhalb eines Requests können sich Aufrufe beeinflussen. Bei nebenläufiger/mehrfacher Nutzung Capabilities explizit setzen.
- Fehlender Identifier (z.B. leerer String aus dem Request) → `InvalidArgumentException`/`TypeError` (siehe `OctoProductController::getProduct` fängt `\Throwable`).

## Bezüge
`CachedOctoApiClientInterface`, Supplier-Clients (`Client/Octo/*`), `clients.xml`, Controller + Services, die Clients beziehen.
