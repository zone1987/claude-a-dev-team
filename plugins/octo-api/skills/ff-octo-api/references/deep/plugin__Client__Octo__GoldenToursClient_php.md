# GoldenToursClient (`src/Client/Octo/GoldenToursClient.php`)

## Zweck
Konkreter OCTO-API-Client für den Supplier **GoldenTours** (London-Touren, Ventrata-API `api.ventrata.com/octo/`, ~278 Produkte). Wichtigster Online-Supplier. Erbt die gesamte HTTP-/Caching-Logik von `CachedOctoApiClient`.

## Typ & Vererbung
- Namespace: `FfOctoApi\Client\Octo`
- `class GoldenToursClient extends CachedOctoApiClient`
- Registriert in `clients.xml` mit Tag `octo.api.client`.

## Konstanten
| Konstante | Sichtbarkeit | Wert | Bedeutung |
|-----------|--------------|------|-----------|
| `IDENTIFIER` | public string | `goldentours` | Supplier-Identifier. |
| `DESTINATION_ID` | public string | `8affd1a6-0c7b-4da6-aff8-c8e6a4bc4247` | OCTO Destination-ID. |
| `SUPPLIER_ID` | public string | `0c7060de-d196-40dd-9f35-42880db8cd6c` | OCTO Supplier-ID. |
| `API_KEY_CONFIG_KEY` | protected string | `FfOctoApi.config.goldentoursApiKey` | Config-Key API-Key. |
| `API_ENV_KEY` | protected string | `OCTO_API_KEY_GOLDEN_TOURS` | Env API-Key (Vorrang). |
| `API_BASE_URL_CONFIG_KEY` | protected string | `FfOctoApi.config.goldentoursBaseUrl` | Config Live-Base-URL. |
| `API_ENV_BASE_URL` | protected string | `OCTO_API_BASE_URL_GOLDEN_TOURS` | Env Live-Base-URL. |
| `API_BASE_URL_CONFIG_KEY_SANDBOX` | protected string | `FfOctoApi.config.goldentoursBaseUrlSandbox` | Config Sandbox-Base-URL. |
| `API_ENV_BASE_URL_SANDBOX` | protected string | `OCTO_API_BASE_URL_GOLDEN_TOURS_SANDBOX` | Env Sandbox-Base-URL. |
| `COLOR` | protected string | `#FFE082` | Anzeigefarbe. |

## Methoden
Keine eigenen — vollständig von `CachedOctoApiClient`/`OctoApiClient`/`AbstractOctoApiClient` geerbt.

## Besonderheiten
- Online-Client → `Octo-Env: test` Pflicht.
- Produktfelder/Preise siehe `../goldentours-products.md`, IDs in `../api/ids/goldentours.json`.

## Bezüge
`CachedOctoApiClient`, `OctoApiClientRegistry`, `../goldentours-products.md`, `../api/ids/goldentours.json`.
