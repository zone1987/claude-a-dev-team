# GoCityClient (`src/Client/Octo/GoCityClient.php`)

## Zweck
Konkreter OCTO-API-Client für den Supplier **GoCity** (City-Pässe, GoCity-Staging-API, ~49 Produkte / 25 Städte). Online-Client, erbt HTTP/Caching von `CachedOctoApiClient`. Bietet als einziger Client eine Zusatzmethode für den `supplier`-Endpunkt.

## Typ & Vererbung
- Namespace: `FfOctoApi\Client\Octo`
- `class GoCityClient extends CachedOctoApiClient`
- Registriert in `clients.xml` mit Tag `octo.api.client`.

## Konstanten
| Konstante | Sichtbarkeit | Wert | Bedeutung |
|-----------|--------------|------|-----------|
| `IDENTIFIER` | public string | `gocity` | Supplier-Identifier. |
| `DESTINATION_ID` | public string | `3293bf46-050c-424d-b29f-4dd1de7300f7` | OCTO Destination-ID. |
| `SUPPLIER_ID` | public string | `b565b694-18e3-488f-88c2-829c3150d4a4` | OCTO Supplier-ID. |
| `API_KEY_CONFIG_KEY` | protected string | `FfOctoApi.config.gocityApiKey` | Config-Key API-Key. |
| `API_ENV_KEY` | protected string | `OCTO_API_KEY_GO_CITY` | Env API-Key (Vorrang vor Config). |
| `API_BASE_URL_CONFIG_KEY` | protected string | `FfOctoApi.config.gocityBaseUrl` | Config Live-Base-URL. |
| `API_ENV_BASE_URL` | protected string | `OCTO_API_BASE_URL_GO_CITY` | Env Live-Base-URL. |
| `API_BASE_URL_CONFIG_KEY_SANDBOX` | protected string | `FfOctoApi.config.gocityBaseUrlSandbox` | Config Sandbox-Base-URL. |
| `API_ENV_BASE_URL_SANDBOX` | protected string | `OCTO_API_BASE_URL_GO_CITY_SANDBOX` | Env Sandbox-Base-URL. |
| `COLOR` | protected string | `#90dde3` | Anzeigefarbe. |

## Methoden
### `getCachedSupplier(?string $supplierId = null): array`
- **Zweck:** Holt die Supplier-Daten vom OCTO-`supplier`-Endpunkt.
- **Parameter:** `$supplierId` — optional, wird im aktuellen Code **nicht** an den Request weitergereicht (der Aufruf geht immer auf den generischen `supplier`-Pfad).
- **Rückgabe:** `array` (dekodierte API-Antwort).
- **Seiteneffekt:** HTTP GET über die geerbte `request()`-Methode (mit Caching gemäß `CachedOctoApiClient`).
- **Fallstrick:** Der `$supplierId`-Parameter ist derzeit wirkungslos — beim Erweitern beachten.

## Besonderheiten
- GoCity-spezifisches Datumsformat / Produktstruktur siehe `../gocity-api.md`.
- Online-Client → `Octo-Env: test` Pflicht.

## Bezüge
`CachedOctoApiClient`, `OctoApiClientRegistry`, `../gocity-api.md`, `../api/ids/gocity.json`.
