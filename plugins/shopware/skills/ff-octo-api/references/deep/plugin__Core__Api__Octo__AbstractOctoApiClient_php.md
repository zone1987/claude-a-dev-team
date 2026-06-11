# AbstractOctoApiClient (`src/Core/Api/Octo/AbstractOctoApiClient.php`)

## Zweck
Abstrakte Basis aller OCTO-API-Clients. Kapselt Konfigurations-/Key-/Base-URL-Auflösung (Config + Env, Test/Sandbox vs. Live), HTTP-Request-Ausführung mit Header-Aufbau und Fehlerbehandlung, sowie generisches PSR-6-Caching. Implementiert das Offline-Konzept (`OFFLINE`).

## Typ & Vererbung
- Namespace: `FfOctoApi\Core\Api\Octo`
- `abstract class AbstractOctoApiClient implements OctoApiClientInterface`

## Konstanten (von Subklassen überschrieben)
`IDENTIFIER`(''), `OFFLINE`(false), `DESTINATION_ID`(''), `SUPPLIER_ID`(''), `API_KEY_CONFIG_KEY`(''), `API_ENV_KEY`(''), `API_BASE_URL_CONFIG_KEY`(''), `API_ENV_BASE_URL`(''), `API_BASE_URL_CONFIG_KEY_SANDBOX`(''), `API_ENV_BASE_URL_SANDBOX`(''). (`COLOR` wird in Subklassen definiert, hier via `getColor()` referenziert.)

## Properties
| Property | Typ | Default | Bedeutung |
|----------|-----|---------|-----------|
| `$acceptLanguage` | string | `de-DE, en-GB` | `Accept-Language`-Header. |
| `$octoAvailableLanguages` | string | `de, en` | `Octo-Available-Languages`-Header. |
| `$capabilities` | array<string> | `['octo/content','octo/pricing']` | `Octo-Capabilities`-Header. |

## Konstruktor / DI
| Parameter | Typ | Zweck |
|-----------|-----|-------|
| `$systemConfigService` | `SystemConfigService` | Config-/Key-Auflösung. |
| `$httpClient` | `HttpClientInterface` | HTTP-Requests. |
| `$logger` | `OctoLoggerInterface` | Logging. |
| `$cache` | `CacheItemPoolInterface` | PSR-6-Cache. |

## Methoden
- `getBaseUrl(?salesChannelId): string` — wählt Sandbox- vs. Live-Config-/Env-Key abhängig von `isTestEnv()`; Env ergänzt leere Config.
- `getApiKey(?salesChannelId): string` — Config-Key `API_KEY_CONFIG_KEY`, sonst Env `API_ENV_KEY`.
- `getCacheExpirationTime(?salesChannelId): int` — `FfOctoApi.config.expirationTime`.
- `getBookingReservationTime(?salesChannelId): int` — `FfOctoApi.config.bookingReservationTime`; **Mindestwert 10** (wenn leer/<5). (Hinweis: liest die Config als Sekunden; der CartController behandelt `bookingReservationTime` als Minuten — Einheiten-Diskrepanz beachten.)
- `isTestEnv(?salesChannelId): bool` (protected) — `FfOctoApi.config.testingEnvironment`.
- Getter: `getDestinationId()`, `getSupplierId()`, `getColor()`, `getIdentifier()`, `getTargetDestination()`, `getApiEnvKey()`, `getApiConfigKey()`.
- `isOffline(): bool` — gibt `static::OFFLINE` zurück (zentral fürs Offline-Konzept).
- Language/Capabilities: `get/setAcceptLanguage`, `get/setOctoAvailableLanguages`, `get/setCapabilities` (Fluent `static`).
- `getClientOptions(): HttpOptions` (protected) — BaseUri, Bearer, Header (`Accept-Language`, `Octo-Available-Languages`, `Content-Type: application/json`, **`Octo-Env: test|live`** je `isTestEnv()`, `Octo-Capabilities`).
- `getClient(HttpOptions): HttpClientInterface` (protected) — `httpClient->withOptions`.
- `request(method, uri, options?, origin=false, returnError=false): array|ResponseInterface|OctoErrorResponse` (protected) — **wenn `isOffline()` → `[]`** (kein Call). Sonst Request; bei `origin` rohe Response; bei Status≠200 Log (Unauthorized=warning, sonst error) und `[]` bzw. `OctoErrorResponse`; sonst `toArray()`. Fängt diverse HTTP-Client-Exceptions → `['message','code']`.
- `getCachedItem(cacheKey, getter, getterParams=[], expireAfter=null): mixed` (protected) — PSR-6-Caching: `expireAfter===0` löscht den Eintrag; ruft sonst dynamisch `$this->$getter(...$params)` und speichert. TTL = `expireAfter` oder `getCacheExpirationTime()`.

## Besonderheiten / Fallstricke
- **`Octo-Env`**: Header wird aus `testingEnvironment` abgeleitet — in der Praxis/Skill gilt `test` als Pflicht; produktiv niemals versehentlich `live`.
- **Offline-Gate** sitzt in `request()` — Subklassen-Methoden, die NICHT über `request()` gehen, müssen `isOffline()` selbst prüfen.
- `getCachedItem` nutzt String-Getter (`call_user_func`) — Tippfehler im Getter-Namen schlägt erst zur Laufzeit fehl.

## Bezüge
`OctoApiClient`, `CachedOctoApiClient`, `OctoApiClientInterface`, `OctoErrorResponse`, `../configuration-services.md`.
