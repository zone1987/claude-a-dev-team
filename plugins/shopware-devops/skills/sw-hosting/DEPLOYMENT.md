# Shopware Hosting — Deployment

Refer to `DEPLOYMENT-DETAIL.md` for full deploy.php, GitLab CI, and GitHub Actions examples.

## Deployment Helper (recommended)

```bash
composer require shopware/deployment-helper
vendor/bin/shopware-deployment-helper run
```

Handles: install/update detection, DB wait, plugin management, theme compile, one-time tasks, maintenance mode.

### .shopware-project.yml

```yaml
deployment:
    hooks:
        pre: 'echo before'
        post: 'echo after'
    extension-management:
        enabled: true
        exclude:
            - SomeManagedByStorePlugin
    one-time-tasks:
        - id: my-migration
          when: after
          script: '%php.bin% bin/console my:command'
    store:
        license-domain: 'example.com'
```

Use `.shopware-project.local.yml` (gitignored) for local overrides. Supports `!reset` and `!override` YAML tags.

### Environment variables for initial setup

```dotenv
INSTALL_LOCALE=de-DE
INSTALL_CURRENCY=EUR
INSTALL_ADMIN_USERNAME=admin
INSTALL_ADMIN_PASSWORD=secure
SALES_CHANNEL_URL=https://myshop.com
SHOPWARE_DEPLOYMENT_STAGING=1
```

## Deployer (classic SFTP/SSH)

```bash
composer require deployer/deployer shopware/deployment-helper
dep deploy env=prod
```

Webserver docroot: `/var/www/shopware/current/public` (symlink!)

## Build without database (CI)

```bash
# Set CI=1 to use ComposerPluginLoader
CI=1 shopware-cli project ci /src
```

For Storefront theme without DB, dump variables first:
```bash
bin/console theme:dump   # on a running instance
```

Then configure StaticFileConfigLoader:
```yaml
# config/packages/storefront.yaml
storefront:
    theme:
        config_loader_id: Shopware\Storefront\Theme\ConfigLoader\StaticFileConfigLoader
        available_theme_provider: Shopware\Storefront\Theme\ConfigLoader\StaticFileAvailableThemeProvider
        theme_path_builder_id: Shopware\Storefront\Theme\MD5ThemePathBuilder
```

Use `cache:clear:all` instead of `cache:clear` in deployment scripts when mixing `bin/ci` and `bin/console`.

## Blue-Green Deployment

```dotenv
BLUE_GREEN_DEPLOYMENT=1
```

Requires super-privilege to create DB triggers. Enables schema-safe rollbacks.

## Health Check

```
GET /api/_info/health-check
```

Returns `200` when healthy, `50x` when not.

See also: `sw-cli` (project ci, build commands), `sw-hosting-installation` (Docker setup).

Full reference: `DEPLOYMENT-DETAIL.md`
