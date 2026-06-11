# clients.xml (`src/Resources/config/clients.xml`)

## Zweck
DI-Konfiguration der Supplier-Clients und der Registry. Alle Clients werden mit Tag `octo.api.client` registriert und über den Tagged Iterator in die `OctoApiClientRegistry` injiziert.

## Definierte Services
- `OctoApiClientRegistry` (`public=true`) — Argument: `tagged_iterator` Tag `octo.api.client`.
- `GoldenToursClient`, `GoCityClient`, `RheinKurierClient`, `DemoClient` (alle `public=true`, Tag `octo.api.client`).
  - Argumente je Client: `SystemConfigService`, `http_client`, `LoggerService`, `cache.system`, `service_container`.

## Besonderheiten
- **Neuen Supplier registrieren:** hier einen `<service>`-Block mit Tag `octo.api.client` und den 5 Argumenten ergänzen.
- Alle Clients teilen denselben `cache.system`-Pool und `http_client`.

## Bezüge
`Client/Octo/*`, `Core/Api/Octo/OctoApiClientRegistry.php`, `Core/Api/Octo/AbstractOctoApiClient.php`.
