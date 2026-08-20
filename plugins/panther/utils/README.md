# Panther Utils

Ready-to-use templates for Symfony Panther — copy them and adapt them to your project. All values (paths, ports,
driver versions) are examples; real credentials/secrets do **not** belong here, but in `.env.test`/CI secrets.

| File | Purpose |
|---|---|
| `phpunit.panther.xml` | PHPUnit configuration (PHPUnit 10+) with the Panther `ServerExtension` registered and sensible `PANTHER_*` env vars. |
| `AbstractPantherTestCase.php` | Base test case with helpers: headless client, `waitForVisibility` wrapper, error screenshot. |
| `Dockerfile.panther` | Image with PHP + Chrome + ChromeDriver for headless Panther tests (no-sandbox, `--disable-dev-shm-usage`). |
| `docker-compose.selenium.yml` | Selenium Grid (standalone Chrome) for testing against a remote WebDriver via `PANTHER_*`. |
| `github-actions-panther.yml` | GitHub Actions workflow: drivers, AssetMapper build, headless Panther tests. |

Details/all options: skills `panther-installation`, `panther-config-env`, `panther-docker-ci`, `panther-selenium-remote`.
