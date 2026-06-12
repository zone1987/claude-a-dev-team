# Panther Utils

Einsatzfertige Vorlagen für Symfony Panther — kopieren und an dein Projekt anpassen. Alle Werte (Pfade, Ports,
Treiber-Versionen) sind Beispiele; echte Credentials/Secrets gehören **nicht** hierher, sondern in `.env.test`/CI-Secrets.

| Datei | Zweck |
|---|---|
| `phpunit.panther.xml` | PHPUnit-Konfiguration (PHPUnit 10+) mit registrierter Panther-`ServerExtension` und sinnvollen `PANTHER_*`-Env-Vars. |
| `AbstractPantherTestCase.php` | Basis-TestCase mit Helfern: headless-Client, `waitForVisibility`-Wrapper, Fehler-Screenshot. |
| `Dockerfile.panther` | Image mit PHP + Chrome + ChromeDriver für headless Panther-Tests (no-sandbox, `--disable-dev-shm-usage`). |
| `docker-compose.selenium.yml` | Selenium-Grid (Standalone Chrome) zum Testen gegen einen Remote-WebDriver via `PANTHER_*`. |
| `github-actions-panther.yml` | GitHub-Actions-Workflow: Treiber, AssetMapper-Build, headless Panther-Tests. |

Details/alle Optionen: Skills `panther-installation`, `panther-config-env`, `panther-docker-ci`, `panther-selenium-remote`.
