# shopware-cli project — Complete reference

## Contents

- [project create](#project-create)
- [project ci](#project-ci)
- [project admin-build / storefront-build](#project-admin-build-storefront-build)
- [project worker](#project-worker)
- [project dump](#project-dump)
- [project console](#project-console)
- [project extension (via Admin API)](#project-extension-via-admin-api)
- [project admin-api](#project-admin-api)
- [project doctor](#project-doctor)
- [project validate](#project-validate)
- [project autofix](#project-autofix)
- [project generate-jwt](#project-generate-jwt)
- [project image-proxy](#project-image-proxy)
- [project upgrade-check](#project-upgrade-check)
- [project config-schema](#project-config-schema)
- [project clear-cache](#project-clear-cache)

## project create

Create a new Shopware 6 project. Interactive when called without flags.

```bash
# Interactive
shopware-cli project create

# With all flags
shopware-cli project create my-shop latest \
  --git \
  --docker \
  --with-elasticsearch \
  --with-amqp \
  --deployment shopware-paas \
  --ci github
```

| Flag | Default | Description |
|------|---------|-------------|
| `--docker` | false | Use Docker for composer install |
| `--with-elasticsearch` | false | Include OpenSearch/Elasticsearch support |
| `--with-amqp` | false | Include the AMQP queue (symfony/amqp-messenger) |
| `--no-audit` | false | Make `composer audit` non-blocking |
| `--git` | false | Initialize a git repository |
| `--version string` | | SW version: `6.6.0.0`, `6.7.0.0`, `latest` |
| `--deployment string` | | `none` \| `deployer` \| `platformsh` \| `shopware-paas` |
| `--ci string` | | `none` \| `github` \| `gitlab` |

**Deployment options:**
- `shopware-paas` → installs the `shopware/paas-meta` recipe (Platform.sh config)
- `platformsh` → generic Platform.sh config
- `deployer` → Deployer PHP configuration
- `none` → no deployment config

## project ci

Complete CI/CD build pipeline for production deployments:
1. `composer install --no-dev --optimize-autoloader`
2. Build extension assets (admin + storefront)
3. Symfony cache warmup
4. `assets:install`
5. Compile MJML (if present)
6. Generate checksums

```bash
shopware-cli project ci .
shopware-cli project ci . --with-dev-dependencies
shopware-cli project ci . --force   # outside CI
```

| Flag | Default | Description |
|------|---------|-------------|
| `--with-dev-dependencies` | false | Keep `require-dev` |
| `--force` | false | Also run outside CI / with a dirty git tree |

**Environment variables `project ci` reads:**
- `APP_CACHE_DIR` — cache directory (default: `var/cache`)
- `SHOPWARE_SKIP_ASSET_INSTALL_CACHE_INVALIDATION=1` — skip cache invalidation during the build (PaaS optimization)
- `CI` — must be set (or use `--force`)

## project admin-build / storefront-build

```bash
# Admin only
shopware-cli project admin-build .
shopware-cli project admin-build . --only-extensions MyPlugin,OtherPlugin
shopware-cli project admin-build . --skip-extensions LegacyPlugin

# Storefront only + theme:compile
shopware-cli project storefront-build .
shopware-cli project storefront-build . --skip-theme-compile
shopware-cli project storefront-build . --force-install-dependencies
```

**admin-build flags:**

| Flag | Default | Description |
|------|---------|-------------|
| `--skip-assets-install` | false | Do not run `assets:install` afterwards |
| `--force-install-dependencies` | false | Force npm install |
| `--only-extensions string` | | Comma-separated extension list |
| `--skip-extensions string` | | Exclusion list |
| `--only-custom-static-extensions` | false | Only `custom/static-plugins` |

**Additional storefront-build flags:**

| Flag | Default | Description |
|------|---------|-------------|
| `--skip-theme-compile` | false | Skip `theme:compile` |

## project worker

Start messenger consumers. Auto-restart on crash (rate-limited: 1 restart per 10s).
SIGTERM/SIGINT lead to a graceful stop.

```bash
# 1 worker
shopware-cli project worker

# 3 workers in parallel
shopware-cli project worker 3

# Custom queues
shopware-cli project worker --queue async,low_priority 2

# With graceful stop (wait 60s before SIGKILL)
shopware-cli project worker --graceful-stop-limit 60

# Verbose logging
shopware-cli project worker --verbose
```

| Flag | Default | Description |
|------|---------|-------------|
| `--verbose` | false | `-vvv` for all workers |
| `--queue string` | `async,failed,low_priority` (SW>=6.5.7) | Comma-separated queue names |
| `--memory-limit string` | `512M` | Memory limit per worker run |
| `--time-limit string` | `120` | Time limit per worker run (seconds) |
| `--graceful-stop-limit uint` | 0 | Seconds for a graceful SIGTERM before SIGKILL (0=immediately) |
| `--limit uint` | 0 | Max. messages per worker run (0=unlimited) |

## project dump

Pure Go MySQL dumper without an external `mysqldump` binary.

```bash
# Simple (DATABASE_URL from .env)
shopware-cli project dump

# With anonymization and compression
shopware-cli project dump --clean --anonymize --compression gzip

# To stdout (pipeline)
shopware-cli project dump --output -

# Explicit connection data
shopware-cli project dump -u shopware -p shopware --host localhost --database shopware

# Parallel (5 tables at a time)
shopware-cli project dump --parallel 5

# Compressed with zstd
shopware-cli project dump --compression zstd --output dump.sql.zst
```

| Flag | Short | Default | Description |
|------|-------|---------|-------------|
| `--host` | | (from DATABASE_URL) | MySQL host |
| `--database` | | (from DATABASE_URL) | Database name |
| `--username` | `-u` | (from DATABASE_URL) | MySQL user |
| `--password` | `-p` | (from DATABASE_URL) | MySQL password |
| `--port` | | (from DATABASE_URL) | MySQL port |
| `--output` | | `dump.sql` | Output file or `-` for stdout |
| `--clean` | | false | Skip tables: `cart`, `messenger_messages`, `message_queue_stats`, `dead_message`, `increment`, `log_entry`, `sales_channel_api_context` |
| `--skip-lock-tables` | | false | Skip `LOCK TABLES` (needed for limited permissions) |
| `--anonymize` | | false | Anonymize customer data: email, name, address, etc. |
| `--compression` | | | `gzip` (file gets `.gz`) \| `zstd` (file gets `.zst`) |
| `--quick` | | false | Quick option (disables the row-by-row buffer) |
| `--parallel` | | 0 | Dump tables in parallel (0=sequential) |
| `--insert-into-limit` | | 0 | Max. rows per INSERT statement (0=no limit) |

## project console

Passthrough to `bin/console`. Flag parsing is disabled (all arguments are passed through directly).
Tab completion is available for all Symfony Console commands.

```bash
shopware-cli project console cache:clear
shopware-cli project console plugin:install --activate MyPlugin
shopware-cli project console system:install --shop-name "My Shop" --shop-email info@example.com
```

## project extension (via Admin API)

These require a configured Admin API in `.shopware-project.yml`.

```bash
# List extensions
shopware-cli project extension list
shopware-cli project extension list --json

# Lifecycle
shopware-cli project extension install MyPlugin
shopware-cli project extension install --activate MyPlugin
shopware-cli project extension activate MyPlugin
shopware-cli project extension deactivate MyPlugin
shopware-cli project extension uninstall MyPlugin
shopware-cli project extension delete MyPlugin

# Updates
shopware-cli project extension update MyPlugin
shopware-cli project extension update all
shopware-cli project extension outdated
shopware-cli project extension outdated --json

# Upload a local extension
shopware-cli project extension upload path/to/MyPlugin --activate
shopware-cli project extension upload path/to/MyPlugin --increase-version
```

## project admin-api

```bash
# GET request
shopware-cli project admin-api GET /api/product?limit=5

# POST request
shopware-cli project admin-api POST /api/product \
  '{"name": "Test", "productNumber": "TEST-001", "stock": 10}'

# Print the token only (for curl pipelines)
shopware-cli project admin-api GET /api/product --output-token
```

## project doctor

Diagnostics without side effects:
- Read and validate `.shopware-project.yml`
- Detect the Shopware version
- List all extensions and bundles
- Report potential problems

```bash
shopware-cli project doctor .
```

## project validate

```bash
shopware-cli project validate .
shopware-cli project validate . --reporter github
shopware-cli project validate . --only phpstan
shopware-cli project validate . --local-only   # custom/* only
```

| Flag | Default | Description |
|------|---------|-------------|
| `--reporter string` | auto | `summary` \| `json` \| `github` \| `gitlab` \| `junit` \| `markdown` |
| `--only string` | | Comma-separated tool list |
| `--exclude string` | | Exclude tools |
| `--no-copy` | false | No tmp dir |
| `--local-only` | false | Scan only the `custom/*` folders |

## project autofix

```bash
# Migrate composer-based plugins to Composer/Packagist
shopware-cli project autofix composer-plugins

# Migrate to Symfony Flex
shopware-cli project autofix flex
```

`autofix flex` modifies:
- `composer.json`: add the Flex endpoint, adjust scripts
- `.env`: Flex-compatible structure
- `config/`: clean up according to the recipe pattern

## project generate-jwt

```bash
# Write files: config/jwt/private.pem + config/jwt/public.pem
shopware-cli project generate-jwt .

# Print as env vars (for CI/secrets)
shopware-cli project generate-jwt . --env
# → JWT_PRIVATE_KEY=<base64>
# → JWT_PUBLIC_KEY=<base64>
```

## project image-proxy

Local proxy for development with production media. Serves images from the local `public/`,
forwards misses to the upstream and caches responses.

```bash
shopware-cli project image-proxy --url https://production.example.com
shopware-cli project image-proxy --url https://production.example.com --port 8081
shopware-cli project image-proxy --url https://production.example.com --clear
```

On startup it creates a temporary Shopware filesystem config and removes it on exit.

## project upgrade-check

```bash
shopware-cli project upgrade-check .
# → Interactive version selection
# → Lists incompatible extensions with details
```

Uses the Admin API when configured, otherwise `composer.lock` for the version analysis.

## project config-schema

```bash
shopware-cli project config-schema > shopware-project-schema.json
```

## project clear-cache

```bash
shopware-cli project clear-cache
# → Uses the Admin API when configured
# → Fallback: delete var/cache
```
