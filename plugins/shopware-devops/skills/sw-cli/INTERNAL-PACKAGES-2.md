# shopware-cli — Internal Go packages

Source: `github.com/shopware/shopware-cli/internal/`

| Package | Path | Purpose |
|---------|------|---------|
| `account-api` | `internal/account-api/` | Shopware Account REST API client: login/OIDC/OAuth2, producer endpoints, extension binaries |
| `admin-api` | `internal/admin-api/` | Shopware Admin API client: extension manager, cache manager, info endpoint |
| `extension` | `internal/extension/` | Core extension handling: asset build (ESBuild/Webpack), configs, zip, cleanup, changelog, checksums, manifest, icon resizing |
| `esbuild` | `internal/esbuild/` | ESBuild wrapper with Sass plugin and Vite config support |
| `verifier` | `internal/verifier/` | Validation/fix/format toolchain: PHPStan, PHP-CS-Fixer, ESLint, Stylelint, Prettier, Rector, Twig linter |
| `shop` | `internal/shop/` | Read project config (`.shopware-project.yml`), detect SW version, shop client |
| `packagist` | `internal/packagist/` | Shopware Packagist API, composer.json/auth.json helpers, deployment recipe generation |
| `phpexec` | `internal/phpexec/` | PHP/composer/bin-console execution helpers |
| `envfile` | `internal/envfile/` | Symfony `.env`/`.env.local` loader |
| `mysqldump` | `internal/mysqldump/` | Pure Go MySQL dumper: parallel, anonymization, compression (gzip/zstd) |
| `ci` | `internal/ci/` | CI section output for GitHub Actions and GitLab CI |
| `flexmigrator` | `internal/flexmigrator/` | Symfony Flex migration helpers |
| `mjml` | `internal/mjml/` | MJML template compiler |
| `validation` | `internal/validation/` | Reporter types and output formatting |
| `tui` | `internal/tui/` | Terminal UI (lipgloss styles, huh forms, banner) |
| `tracking` | `internal/tracking/` | Anonymous telemetry (command, result, duration, OS, version) |

## Telemetry

shopware-cli sends anonymous usage telemetry (command name, success/failure, duration, OS/arch, CLI version).
To disable: set `SHOPWARE_CLI_DISABLE_TRACKING=1` as an environment variable.

## `.shopware-project.yml` — Important fields

```yaml
# Shopware URL and admin credentials (for Admin API calls)
url: "https://my-shop.example.com"
admin_api:
  client_id: "SWIATEST..."
  client_secret: "..."

# Extension build configuration
build:
  disable_asset_copy: false
  keep_extension_source: false

# Deployment configuration
deployment:
  cache:
    always_clear: true

# Extensions: which ones to include in the build
extensions:
  - name: MyPlugin
```

## `.shopware-extension.yml` — Store metadata

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
