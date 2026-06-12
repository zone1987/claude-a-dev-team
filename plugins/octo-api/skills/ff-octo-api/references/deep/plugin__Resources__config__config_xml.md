# config.xml (`src/Resources/config/config.xml`)

## Zweck
Plugin-Konfiguration (Admin-Settings, `FfOctoApi.config.*`).

## Felder (Karten)
**Grundeinstellungen:**
- `expirationTime` (single-select: 0/3600/7200/10800 s, **Default 10800**) — Cache-TTL.
- `bookingReservationTime` (single-select: 5/10/15/20/25/30/60, **kein Default** → Code-Fallback 30 bzw. 10) — Reservierungsdauer (Minuten).

**API Keys (password):** `goldentoursApiKey`, `gocityApiKey`, `demoApiKey`.

**API Base Urls (Live, url):** `goldentoursBaseUrl` (`https://api.ventrata.com/octo/`), `gocityBaseUrl` (`https://api.gocity.com/octo/`), `demoBaseUrl` (`https://api.ventrata.com/octo/`).

**API Base Urls (Sandbox, url):** `goldentoursBaseUrlSandbox` (`https://api.ventrata.com/octo/`), `gocityBaseUrlSandbox` (`https://api.staging.gocity.tech/octo/`), `demoBaseUrlSandbox` (`https://api.ventrata.com/octo/`).

**Provision:** `provisionValue` (float, **Default 10** %).

**Testing:** `testingEnvironment` (checkbox, **Default false**) — steuert `Octo-Env: test|live` und Sandbox- vs. Live-Base-URL.

## Besonderheiten / Fallstricke
- **Sandbox-/Live-Base-URLs** sind getrennt konfigurierbar (vom `AbstractOctoApiClient` je `testingEnvironment` gewählt); Env-Vars haben Vorrang.
- `testingEnvironment` Default `false` → produktiv `live`! Für Tests/Skill gilt `test` als Pflicht → in der Praxis aktivieren.
- `bookingReservationTime` ohne XML-Default; `AbstractOctoApiClient::getBookingReservationTime` erzwingt min. 10, `CartController` Default '30'.

## Bezüge
`Core/Api/Octo/AbstractOctoApiClient.php`, `Client/Octo/*`, `../configuration-services.md`.
