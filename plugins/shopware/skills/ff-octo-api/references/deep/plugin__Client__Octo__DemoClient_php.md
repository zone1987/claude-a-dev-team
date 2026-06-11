# DemoClient (`src/Client/Octo/DemoClient.php`)

## Zweck
Konkreter OCTO-API-Client für den **Demo-Supplier** (Ventrata-Test-Produkte). Dient zum Testen der Integration ohne echte GoldenTours-/GoCity-Daten. Online-Client (kein `OFFLINE`), erbt sämtliche HTTP-/Caching-Logik von `CachedOctoApiClient`.

## Typ & Vererbung
- Namespace: `FfOctoApi\Client\Octo`
- `class DemoClient extends CachedOctoApiClient` (→ `OctoApiClient` → `AbstractOctoApiClient`).
- Registriert über `clients.xml` mit Tag `octo.api.client`; wird via `OctoApiClientRegistry` (Tagged Iterator) aufgelöst.
- Hinweis: PHPDoc-`@class GoCityClient` ist ein Copy-Paste-Fehler im Kommentar (Klasse heißt `DemoClient`).

## Konstanten
| Konstante | Sichtbarkeit | Wert | Bedeutung |
|-----------|--------------|------|-----------|
| `IDENTIFIER` | public string | `demo` | Eindeutiger Supplier-Identifier (Filter in `ff_octo_product.identifier`, Registry-Lookup). |
| `DESTINATION_ID` | public string | `05327791-626d-433c-8c65-0f436f1b92c6` | OCTO Destination-ID. |
| `SUPPLIER_ID` | public string | `697e3ce8-1860-4cbf-80ad-95857df1f640` | OCTO Supplier-ID. |
| `API_KEY_CONFIG_KEY` | protected string | `FfOctoApi.config.demoApiKey` | Plugin-Config-Schlüssel für den API-Key. |
| `API_ENV_KEY` | protected string | `OCTO_API_KEY_DEMO` | Env-Variable für den API-Key (hat Vorrang vor Config). |
| `API_BASE_URL_CONFIG_KEY` | protected string | `FfOctoApi.config.demoBaseUrl` | Config-Schlüssel für die Live-Base-URL. |
| `API_ENV_BASE_URL` | protected string | `OCTO_API_BASE_URL_DEMO` | Env-Variable für die Live-Base-URL. |
| `API_BASE_URL_CONFIG_KEY_SANDBOX` | protected string | `FfOctoApi.config.demoBaseUrlSandbox` | Config-Schlüssel für die Sandbox-Base-URL. |
| `API_ENV_BASE_URL_SANDBOX` | protected string | `OCTO_API_BASE_URL_DEMO_SANDBOX` | Env-Variable für die Sandbox-Base-URL. |
| `COLOR` | protected string | `#F8BBD0` | Anzeigefarbe (Admin-Supplier-Badge). |

## Methoden
Keine eigenen — alle Funktionalität (HTTP, Auth, Caching, Header) wird von `CachedOctoApiClient`/`OctoApiClient`/`AbstractOctoApiClient` geerbt.

## Besonderheiten / Fallstricke
- Online-Client → echte Requests; Header `Octo-Env: test` ist Pflicht (gesteuert über `testingEnvironment`-Config in der Basisklasse).
- Sandbox- vs. Live-Base-URL-Auflösung erfolgt in `AbstractOctoApiClient` anhand obiger Konstanten (Env vor Config).

## Bezüge
`CachedOctoApiClient`, `OctoApiClientRegistry`, `clients.xml`, Geschwister-Clients `GoCityClient`, `GoldenToursClient`, `RheinKurierClient`.
