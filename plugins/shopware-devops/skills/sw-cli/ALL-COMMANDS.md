# shopware-cli — All Commands (exhaustive)

Source: `github.com/shopware/shopware-cli` (Go, v0.6.x). Analyzed from `cmd/` and `internal/`.

## Contents

- [Global Flags (persistent, all commands)](#global-flags-persistent-all-commands)
- [account](#account)
- [extension](#extension)
- [project](#project)

## Global Flags (persistent, all commands)

| Flag | Short | Default | Description |
|------|-------|---------|-------------|
| `--verbose` | | false | Enable debug output |
| `--no-interaction` | `-n` | false | Disable all interactive questions (CI-safe) |
| `--version` | | | Print version and exit |

---

## account

### `account login`
OIDC/OAuth2 browser flow against Shopware Account.
No additional flags.

### `account logout`
Invalidate the local token cache.
No flags.

### `account producer extension list`
List all of your own store extensions.

| Flag | Description |
|------|-------------|
| `--search string` | Filter results by name |

### `account producer extension info pull [path]`
Pull store information (description HTML, installation manual, images, icon) from Shopware Account into the local `.shopware-extension.yml` and `src/Resources/store/`.

No additional flag.

### `account producer extension info push [zip-or-path]`
Upload local store info (`.shopware-extension.yml`, `src/Resources/store/`) to Shopware Account.

No additional flag.

### `account producer extension upload [zip]`
Upload an extension zip to the store, trigger a code review.

| Flag | Default | Description |
|------|---------|-------------|
| `--skip-for-review-result` | false | Do not wait for the code review result |

---

## extension

### `extension admin-watch [path...] [host]`
ESBuild dev proxy for the Shopware Administration. Compiles extensions live and proxies the admin.

| Flag | Default | Description |
|------|---------|-------------|
| `--listen string` | `:8080` | Listen address (host:port) |
| `--external-url string` | | External URL (reverse proxy setup) |

### `extension build [path...]`
Build admin and storefront JS/CSS assets for one or more extensions.
ESBuild/Webpack depending on the extension type. Respects `SHOPWARE_PROJECT_ROOT` for version constraints.
No flags.

### `extension get-changelog [path]`
Print the extension changelog to stdout.

| Flag | Description |
|------|-------------|
| `--language string` | Language key, comma-separated fallback list (e.g. `de_DE,en_GB`) |

### `extension config-schema`
JSON schema for `.shopware-extension.yml` to stdout. No flags.

### `extension fix [path]`
Run code fixers: PHPCSFixer, ESLint autofix, etc. Requires a git repository.

| Flag | Default | Description |
|------|---------|-------------|
| `--only string` | | Run only certain tools (comma-separated: `phpstan,eslint`) |
| `--allow-non-git` | false | Also run without a git repo |

### `extension format [path]`
Run formatters: Prettier, PHP-CS-Fixer, etc.

| Flag | Default | Description |
|------|---------|-------------|
| `--only string` | | Only certain tools |
| `--dry-run` | false | Only report, do not apply |

### `extension get-name [path]`
Print the technical name of the extension (from folder or zip). No flags.

### `extension get-version [path]`
Print the version of the extension (from folder or zip). No flags.

### `extension prepare [path]`
Install composer dependencies + clean up in preparation for zip creation.
Runs the same pre-zip pipeline as `extension zip`. No flags.

### `extension validate [path]`
Validate an extension. Default: only fast shopware-cli-native checks.

| Flag | Default | Description |
|------|---------|-------------|
| `--full` | false | Also run PHPStan, ESLint, Stylelint, PHP-CS-Fixer, Rector, Prettier, Twig |
| `--store-compliance` | false | Force store compliance checks (ignores custom ignore lists) |
| `--reporter string` | auto | Output format: `summary`, `json`, `github`, `gitlab`, `junit`, `markdown` |
| `--check-against string` | `highest` | Shopware version: `highest` or `lowest` |
| `--only string` | | Only certain tools |
| `--exclude string` | | Exclude tools |
| `--no-copy` | false | Do not copy the extension into a tmp dir |

### `extension zip [path] [branch]`
Create a release zip from an extension folder. By default via git export.

| Flag | Default | Description |
|------|---------|-------------|
| `--disable-git` | false | Use the source folder directly (no git export) |
| `--release` | false | Release mode (removes the app backend secret) |
| `--overwrite-app-backend-url string` | | Replace the backend URL in `manifest.xml` |
| `--overwrite-app-backend-secret string` | | Replace the app secret in `manifest.xml` |
| `--overwrite-version string` | | Override the version in the zip |
| `--use-git-tag-as-version` | false | Use the detected git tag as version |
| `--output-directory string` | | Output directory for the zip |
| `--git-commit string` | | Export a specific commit/tag |
| `--filename string` | | Explicit zip file name (default: `<name>-<tag>.zip`) |

---

## project

### `project admin-api [method] [path]`
Authenticated Admin REST API wrapper. Reads credentials from `.shopware-project.yml`.

| Flag | Default | Description |
|------|---------|-------------|
| `--output-token` | false | Only print the bearer token |
| `--no-default-headers` | false | No `Content-Type`/`Accept: application/json` |

### `project admin-build [project-dir]` (alias: `build-admin`)
Build admin JS/CSS for all extensions.

| Flag | Default | Description |
|------|---------|-------------|
| `--skip-assets-install` | false | Do not run `assets:install` afterwards |
| `--force-install-dependencies` | false | Force npm install (even if `node_modules` exists) |
| `--only-extensions string` | | Comma-separated extension list |
| `--skip-extensions string` | | Comma-separated exclusion list |
| `--only-custom-static-extensions` | false | Only `custom/static-plugins` |

### `project admin-watch [path]` (alias: `watch-admin`)
Start the admin webpack dev server.

| Flag | Description |
|------|-------------|
| `--only-extensions string` | Filter extensions |
| `--skip-extensions string` | Exclude extensions |
| `--only-custom-static-extensions bool` | Only `custom/static-plugins` |

### `project autofix composer-plugins`
Generates `composer require` commands to migrate plugins from `custom/plugins` to Composer/Packagist. Interactive.

### `project autofix flex`
Migrates a project from a manual layout to Symfony Flex. Changes `composer.json` and `.env`. Interactive confirmation.

### `project ci [project-dir]`
Full CI build pipeline: composer install, extension assets, cache warmup, assets install, MJML, checksums.

| Flag | Default | Description |
|------|---------|-------------|
| `--with-dev-dependencies` | false | Keep `require-dev` in composer install |
| `--force` | false | Also run outside CI / with a dirty git tree |

### `project clear-cache`
Clear the Shopware cache. Uses the Admin API if configured, otherwise deletes `var/cache`. No flags.

### `project config init`
Create `.shopware-project.yml` interactively. No flags (requires interaction).

### `project config-schema`
JSON schema for `.shopware-project.yml` to stdout. No flags.

### `project console [args...]`
`bin/console` passthrough. Flag parsing disabled on the CLI side. Tab completion for all console commands.

### `project create [name] [version]`
Create a new Shopware 6 project.

| Flag | Default | Description |
|------|---------|-------------|
| `--docker` | false | Use Docker for composer install |
| `--with-elasticsearch` | false | Include OpenSearch/ES support |
| `--with-amqp` | false | Include AMQP queue (symfony/amqp-messenger) |
| `--no-audit` | false | `composer audit` non-blocking |
| `--git` | false | Initialize a git repository |
| `--version string` | | SW version: `6.6.0.0`, `latest`, etc. |
| `--deployment string` | | Deployment: `none`, `deployer`, `platformsh`, `shopware-paas` |
| `--ci string` | | CI system: `none`, `github`, `gitlab` |

### `project doctor [project-dir]`
Check the project for problems: read config, detect SW version, list extensions/bundles. No flags.

### `project dump`
Dump the MySQL database. Auto-detects `DATABASE_URL` from `.env`/`.env.local`.

| Flag | Short | Default | Description |
|------|-------|---------|-------------|
| `--host` | | | MySQL host |
| `--database` | | | Database name |
| `--username` | `-u` | | MySQL user |
| `--password` | `-p` | | MySQL password |
| `--port` | | | MySQL port |
| `--output` | | `dump.sql` | Output file or `-` for stdout |
| `--clean` | | false | Skip cart, messenger_messages, etc. |
| `--skip-lock-tables` | | false | Skip `LOCK TABLES` |
| `--anonymize` | | false | Anonymize customer data |
| `--compression` | | | `gzip` (`.gz`) or `zstd` (`.zst`) |
| `--quick` | | false | Quick option (no row-by-row buffer) |
| `--parallel` | | 0 | Dump tables in parallel (0=disabled) |
| `--insert-into-limit` | | 0 | Max. rows per INSERT |

### `project extension activate [name...]`
Activate extensions (installs first if necessary). No flags.

### `project extension deactivate [name...]`
Deactivate extensions. No flags.

### `project extension delete [name...]`
Deactivate, uninstall and remove extensions. No flags.

### `project extension install [name...]`

| Flag | Default | Description |
|------|---------|-------------|
| `--activate` | false | Activate directly after install |

### `project extension list` (alias: `ls`)

| Flag | Default | Description |
|------|---------|-------------|
| `--json` | false | Output as a JSON array |

### `project extension outdated`
List extensions with available updates. Exit code != 0 if outdated extensions exist.

| Flag | Default | Description |
|------|---------|-------------|
| `--json` | false | Output as a JSON array |

### `project extension uninstall [name...]`
Deactivate + uninstall (files remain). No flags.

### `project extension update [name... | all]`

| Flag | Default | Description |
|------|---------|-------------|
| `--disable-store-update` | false | No download from store.shopware.com |

### `project extension upload [path]`
Zip a local extension and upload it to a remote shop.

| Flag | Default | Description |
|------|---------|-------------|
| `--activate` | false | Install + activate + update after upload |
| `--increase-version` | false | Increment the patch version before upload |

### `project fix [project-dir]`

| Flag | Default | Description |
|------|---------|-------------|
| `--only string` | | Only certain tools |
| `--allow-non-git` | false | Allow without a git repo |

### `project format [project-dir]`

| Flag | Default | Description |
|------|---------|-------------|
| `--only string` | | Only certain tools |
| `--dry-run` | false | Only report |

### `project generate-jwt [project-dir]`
Generate a 2048-bit RSA key pair.

| Flag | Default | Description |
|------|---------|-------------|
| `--env` | false | Print as `JWT_PRIVATE_KEY`/`JWT_PUBLIC_KEY` env vars instead of writing files |

### `project image-proxy`
Local HTTP proxy: serves images from `public/`, misses are forwarded upstream and cached.

| Flag | Default | Description |
|------|---------|-------------|
| `--port string` | `8080` | Port |
| `--url string` | | Upstream URL |
| `--clear` | false | Clear the cache before start |
| `--external-url string` | | External URL for the generated SW config |
| `--skip-config` | false | Do not write/remove a Shopware filesystem config |

### `project storefront-build [path]` (alias: `build-storefront`)

| Flag | Default | Description |
|------|---------|-------------|
| `--skip-assets-install` | false | Skip `assets:install` |
| `--skip-theme-compile` | false | Skip `theme:compile` |
| `--force-install-dependencies` | false | Force npm install |
| `--only-extensions string` | | Filter extensions |
| `--skip-extensions string` | | Exclude extensions |
| `--only-custom-static-extensions` | false | Only `custom/static-plugins` |

### `project storefront-watch [path]` (alias: `watch-storefront`)
Storefront webpack hot proxy.

| Flag | Description |
|------|-------------|
| `--only-extensions string` | Filter extensions |
| `--skip-extensions string` | Exclude extensions |
| `--only-custom-static-extensions bool` | Only `custom/static-plugins` |

### `project upgrade-check`
Check extensions for compatibility with a future SW version (interactive, version selection). No flags.

### `project validate [project-dir]`

| Flag | Default | Description |
|------|---------|-------------|
| `--reporter string` | auto | `summary`, `json`, `github`, `gitlab`, `junit`, `markdown` |
| `--only string` | | Only certain tools |
| `--exclude string` | | Exclude tools |
| `--no-copy` | false | No tmp dir |
| `--local-only` | false | Only scan `custom/*` folders |

### `project worker [amount]`
Start messenger consumers. Restart on error (rate-limited: 1x/10s). SIGTERM/SIGINT-safe.

| Flag | Default | Description |
|------|---------|-------------|
| `--verbose` | false | `-vvv` for the worker |
| `--queue string` | | Comma-separated queue names (default: `async,failed,low_priority` for SW >=6.5.7) |
| `--memory-limit string` | `512M` | Memory limit per worker |
| `--time-limit string` | `120` | Time limit per worker run (seconds) |
| `--graceful-stop-limit uint` | 0 | Seconds for graceful SIGTERM before SIGKILL |
| `--limit uint` | 0 | Max. messages per worker run |
