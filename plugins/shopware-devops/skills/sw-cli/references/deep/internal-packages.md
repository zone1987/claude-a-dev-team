# shopware-cli — Interne Go-Packages

Quelle: `github.com/shopware/shopware-cli/internal/`

| Package | Pfad | Zweck |
|---------|------|-------|
| `account-api` | `internal/account-api/` | Shopware Account REST API Client: Login/OIDC/OAuth2, Producer-Endpoints, Extension-Binaries |
| `admin-api` | `internal/admin-api/` | Shopware Admin API Client: Extension-Manager, Cache-Manager, Info-Endpoint |
| `extension` | `internal/extension/` | Kern-Extension-Handling: Asset-Build (ESBuild/Webpack), Configs, Zip, Cleanup, Changelog, Checksums, Manifest, Icon-Resizing |
| `esbuild` | `internal/esbuild/` | ESBuild-Wrapper mit Sass-Plugin und Vite-Config-Support |
| `verifier` | `internal/verifier/` | Validation/Fix/Format-Toolchain: PHPStan, PHP-CS-Fixer, ESLint, Stylelint, Prettier, Rector, Twig-Linter |
| `shop` | `internal/shop/` | Projekt-Config (`.shopware-project.yml`) lesen, SW-Version erkennen, Shop-Client |
| `packagist` | `internal/packagist/` | Shopware Packagist API, composer.json/auth.json-Helpers, Deployment-Recipe-Generierung |
| `phpexec` | `internal/phpexec/` | PHP/composer/bin-console Ausführungs-Helpers |
| `envfile` | `internal/envfile/` | Symfony `.env`/`.env.local` Loader |
| `mysqldump` | `internal/mysqldump/` | Pure-Go MySQL-Dumper: parallel, Anonymisierung, Kompression (gzip/zstd) |
| `ci` | `internal/ci/` | CI-Section-Output für GitHub Actions und GitLab CI |
| `flexmigrator` | `internal/flexmigrator/` | Symfony Flex Migrations-Helpers |
| `mjml` | `internal/mjml/` | MJML-Template-Compiler |
| `validation` | `internal/validation/` | Reporter-Typen und Ausgabe-Formatierung |
| `tui` | `internal/tui/` | Terminal UI (lipgloss Styles, huh Forms, Banner) |
| `tracking` | `internal/tracking/` | Anonyme Telemetrie (Command, Ergebnis, Dauer, OS, Version) |

## Telemetrie

shopware-cli sendet anonyme Nutzungstelemetrie (Command-Name, Erfolg/Fehler, Dauer, OS/Arch, CLI-Version).
Deaktivieren: `SHOPWARE_CLI_DISABLE_TRACKING=1` als Umgebungsvariable setzen.

## `.shopware-project.yml` — Wichtige Felder

```yaml
# Shopware-URL und Admin-Credentials (für Admin-API-Calls)
url: "https://my-shop.example.com"
admin_api:
  client_id: "SWIATEST..."
  client_secret: "..."

# Extension-Build-Konfiguration
build:
  disable_asset_copy: false
  keep_extension_source: false

# Deployment-Konfiguration
deployment:
  cache:
    always_clear: true

# Extensions: welche beim Build einbeziehen
extensions:
  - name: MyPlugin
```

## `.shopware-extension.yml` — Store-Metadaten

```yaml
store:
  icon: src/Resources/store/icon.png
  localizations:
    - de_DE
    - en_GB
  categories:
    - Storefront
  automatic_bugfix_version_compatibility: true
  info:
    de:
      name: "Mein Plugin"
      summary: "Kurzbeschreibung"
      description: "Lange Beschreibung"
      installation_manual: "Installationsanleitung"
      highlights: []
      features: []
      faq: []
    en:
      name: "My Plugin"
      summary: "Short description"
      description: "Long description"
      installation_manual: "Installation instructions"
```
