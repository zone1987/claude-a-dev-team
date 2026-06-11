# PantherTestCase (`tests/E2E/PantherTestCase.php`)

## Zweck
Basisklasse aller Panther-E2E-Tests: Setup/Teardown des (remote) Chrome-Clients, Capabilities, Base-URI und Selenium-Host.

## Typ
- `abstract class PantherTestCase extends BasePantherTestCase`.
- Methoden: `setUp()`, `buildChromeCapabilities()` (private), `tearDown()`, `getBaseUri()`, `getSeleniumHost()`.

## Besonderheiten
- Läuft gegen eine **echte** Storefront (DDEV) über Selenium/Chrome (remote), nicht gegen einen lokalen Test-Kernel.

## Bezüge
`NoopKernel.php`, `bootstrap.php`, alle `E2E/Storefront/**`, `Support/*`.
