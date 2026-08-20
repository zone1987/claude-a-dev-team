# shopware-cli — Complete Command Reference

All commands of the official Shopware CLI (`github.com/shopware/shopware-cli`).
Source: Shopware Developer Documentation (product area `tools/cli`, as of 2026).

---

## Contents

- [Installation](#installation)
- [Global Flags](#global-flags)
- [extension — Extension Commands](#extension-extension-commands)
- [project — Project Commands](#project-project-commands)
- [account — Account Commands](#account-account-commands)
- [Environment Variables](#environment-variables)
- [Compatibility Date](#compatibility-date)
- [Typical Workflows](#typical-workflows)

## Installation

### macOS / Linux (Homebrew)
```bash
brew install --cask shopware/tap/shopware-cli
```

### Debian / Ubuntu (APT)
```bash
curl -1sLf 'https://dl.cloudsmith.io/public/friendsofshopware/stable/setup.deb.sh' | sudo -E bash
sudo apt install shopware-cli
```

### Fedora / CentOS / RHEL (YUM/DNF)
```bash
curl -1sLf 'https://dl.cloudsmith.io/public/friendsofshopware/stable/setup.rpm.sh' | sudo -E bash
sudo dnf install shopware-cli
```

### Arch Linux (AUR)
```bash
yay -S shopware-cli-bin
```

### Nix
```bash
nix profile install nixpkgs#shopware-cli
# or from FriendsOfShopware:
nix profile install github:FriendsOfShopware/nur-packages#shopware-cli
```

### Docker (binary copy into your own image)
```dockerfile
COPY --from=ghcr.io/shopware/shopware-cli:bin /shopware-cli /usr/local/bin/shopware-cli
```

### Docker (direct usage)
```bash
docker run --rm -v $(pwd):$(pwd) -w $(pwd) -u $(id -u) \
  ghcr.io/shopware/shopware-cli extension build FroshPlatformAdminer
```

### GitHub Actions
```yaml
- name: Install shopware-cli
  uses: shopware/shopware-cli-action@v3
```

### GitLab CI
```yaml
build:
  image:
    name: ghcr.io/shopware/shopware-cli:latest
    entrypoint: ["/bin/sh", "-c"]
  script:
    - shopware-cli --version
```

### From source (Go 1.20+)
```bash
git clone https://github.com/shopware/shopware-cli
cd shopware-cli
go mod tidy
go build -o shopware-cli .
```

---

## Global Flags

| Flag | Short | Default | Description |
|------|-------|---------|-------------|
| `--verbose` | | `false` | Enable debug output |
| `--no-interaction` | `-n` | `false` | No interactive input (CI-safe) |
| `--version` | | | Print version and exit |
| `--help` | `-h` | | Show help for the command |

---

## extension — Extension Commands

### `extension build <path>`

Build the assets of an extension (Administration + Storefront). Reads the Shopware version from `composer.json` or `manifest.xml` and uses the lowest compatible version.

```bash
shopware-cli extension build path/to/MyPlugin
```

**Configuration via `.shopware-extension.yml`:**
```yaml
build:
  shopwareVersionConstraint: '6.6.9.0'  # version override
  extraBundles:
    - path: src/Foo                      # additional bundles
    - path: src/Bar
      name: BarBundle                    # optional name override
  zip:
    assets:
      enable_es_build_for_admin: true    # ESBuild for admin (standalone, faster)
      enable_es_build_for_storefront: true
      npm_strict: true                   # install runtime deps only
      enabled: true
      before_hooks: []
      after_hooks: []
      disable_sass: false
```

**SHOPWARE_PROJECT_ROOT:** For full control over the build, an existing Shopware installation can be used:
```bash
SHOPWARE_PROJECT_ROOT=/path/to/shopware shopware-cli extension build path/to/MyPlugin
```

**Bundle type (no plugin):** Composer type `shopware-bundle` + `shopware-bundle-name` in `extra`:
```json
{
  "type": "shopware-bundle",
  "extra": { "shopware-bundle-name": "MyBundle" }
}
```

---

### `extension zip <path>`

Create a release zip: copies the extension, builds assets, removes unnecessary files, creates the archive in the current directory.

```bash
shopware-cli extension zip path/to/MyPlugin
shopware-cli extension zip path/to/MyPlugin --disable-git
shopware-cli extension zip path/to/MyPlugin --git-commit abc123
shopware-cli extension zip path/to/MyPlugin --release
shopware-cli extension zip path/to/MyPlugin --overwrite-version=1.0.0
shopware-cli extension zip path/to/MyPlugin --overwrite-app-backend-url=https://example.com
shopware-cli extension zip path/to/MyPlugin --overwrite-app-backend-secret=MySecret
```

| Flag | Default | Description |
|------|---------|-------------|
| `--disable-git` | `false` | Do not use a git tag, use the current source code |
| `--git-commit` | | Specify a particular tag or commit |
| `--release` | `false` | Release mode: remove app secret, generate changelog |
| `--overwrite-version` | | Override the version in `composer.json`/`manifest.xml` |
| `--overwrite-app-backend-url` | | Replace all external URLs in `manifest.xml` |
| `--overwrite-app-backend-secret` | | Replace the app secret in `manifest.xml` |

**Default:** uses the last git tag. `--disable-git` uses the current code.

**Composer dependencies (< SW 6.5):** Automatic `composer install` + removal of duplicates.
```yaml
build:
  zip:
    composer:
      enabled: false  # disable
```

**Exclude files:**
```yaml
build:
  zip:
    pack:
      excludes:
        paths:
          - tests/
          - .github/
```

**Checksum generation:** Automatic. Exclusions are configurable:
```yaml
build:
  zip:
    checksum:
      ignore:
        - src/Resources/config/services.php
```

**Changelog generation (with `--release`):**
```yaml
changelog:
  enabled: true
  pattern: '^NEXT-\d+'
  variables:
    ticket: '^(NEXT-\d+)\s'
  template: |
    {{range .Commits}}- [{{ .Message }}](https://issues.shopware.com/issues/{{ .Variables.ticket }})
    {{end}}
```

---

### `extension validate <path>`

Validate an extension — useful in CI/CD pipelines before a release.

```bash
shopware-cli extension validate path/to/MyPlugin
shopware-cli extension validate --full path/to/MyPlugin
shopware-cli extension validate --full path/to/MyPlugin --check-against lowest
shopware-cli extension validate --full path/to/MyPlugin --check-against highest
shopware-cli extension validate --full path/to/MyPlugin --only phpstan
shopware-cli extension validate --full path/to/MyPlugin --only "phpstan,eslint,stylelint"
shopware-cli extension validate --full path/to/MyPlugin --reporter github
```

| Flag | Description |
|------|-------------|
| `--full` | Run all tools (PHPStan, ESLint, Stylelint, ...) |
| `--check-against` | `lowest` or `highest` — Shopware version for the checks |
| `--only` | Specific tools (comma-separated) |
| `--reporter` | Output format: `summary` (default), `json`, `junit`, `github`, `markdown` |

**Basic checks (without `--full`):**
- `composer.json` has a `shopware/core` requirement
- Extension metadata: `name`, `label` (DE+EN), `description` (DE+EN, 150–185 characters)
- PHP linting with the minimum PHP version (7.3, 7.4, 8.1, 8.2 — via WebAssembly, no local PHP required)
- `theme.json` parsing and assets
- Snippet files have identical keys

**Available tools with `--only`:**

| Tool | Description |
|------|-------------|
| `phpstan` | PHP static analysis |
| `sw-cli` | Shopware CLI native checks |
| `stylelint` | CSS/SCSS linting |
| `admin-twig` | Admin Twig template checks |
| `php-cs-fixer` | PHP code style |
| `prettier` | Code formatting |
| `eslint` | JavaScript/TypeScript linting |
| `rector` | PHP code refactoring |

**Configure ignores (`.shopware-extension.yaml`):**
```yaml
validation:
  ignore:
    - identifier: 'Shopware.XXXXXX'
    - identifier: 'Shopware.XXXXXX'
      path: 'path/to/file.php'
    - message: 'Some error message'
      path: 'path/to/file.php'
    - message: 'Some error message'
```

**Project scan (all extensions at once):**
```bash
shopware-cli extension validate --full /path/to/project-root
```
Ignores via `.shopware-project.yaml` with the same syntax.

---

### `extension fix <path>`

Automatic refactoring: Rector (PHP), ESLint (JavaScript), custom rules (Admin Twig). Changes files in place!

```bash
shopware-cli extension fix path/to/MyPlugin
docker run --rm -v "$(pwd)":/ext ghcr.io/shopware/shopware-cli extension fix /ext
```

Shopware version for the Rector rules: from `composer.json` → `shopware/core` constraint.

---

### `extension format <path>`

Format code: PHP (PHP-CS-Fixer following the Shopware coding standard), JavaScript/CSS/SCSS (Prettier), Admin Twig.

```bash
shopware-cli extension format path/to/MyPlugin
shopware-cli extension format path/to/MyPlugin --dry-run
docker run --rm -v "$(pwd)":/ext ghcr.io/shopware/shopware-cli extension format /ext
docker run --rm -v "$(pwd)":/ext ghcr.io/shopware/shopware-cli extension format /ext --dry-run
```

| Flag | Description |
|------|-------------|
| `--dry-run` | Preview without changing files |

**Configuration:** `.php-cs-fixer.dist.php` in the extension root (PHP), `.prettierrc` (JS/CSS/SCSS).

---

### `extension admin-watch <path-to-extension> <url-to-shopware>`

Standalone admin watcher: injects only changed extension files into the existing admin build. Starts in milliseconds (unlike the regular watcher).

```bash
shopware-cli extension admin-watch path/to/MyPlugin http://localhost
shopware-cli extension admin-watch path/to/MyPlugin1 path/to/MyPlugin2 http://localhost
shopware-cli extension admin-watch path/to/shopware-project http://localhost  # auto-detect
shopware-cli extension admin-watch path/to/MyPlugin http://localhost --listen :9000
shopware-cli extension admin-watch path/to/MyPlugin http://localhost --external-url https://dev.example.com
```

| Flag | Description |
|------|-------------|
| `--listen` | Change the port (default: random) |
| `--external-url` | URL for reverse proxy setups (SSL etc.) |

Multiple extensions: provide all paths, the last argument is the Shopware URL.

---

### `extension get-version <path>`

Print the version of the extension.

```bash
shopware-cli extension get-version path/to/MyPlugin
```

---

### `extension get-changelog <path>`

Print the English changelog of the extension.

```bash
shopware-cli extension get-changelog path/to/MyPlugin
```

---

## project — Project Commands

### `project create <folder-name> [version]`

Create a new Shopware project.

```bash
shopware-cli project create my-shop
shopware-cli project create my-shop 6.6.0.0
shopware-cli project create my-shop latest     # latest stable
shopware-cli project create my-shop dev-trunk  # latest dev
```

---

### `project ci <path>`

Full CI/CD build pipeline: `composer install`, asset build (only missing ones), cleanup, snippet merging.

```bash
shopware-cli project ci .
shopware-cli project ci /path/to/shopware --with-dev-dependencies
```

| Flag | Description |
|------|-------------|
| `--with-dev-dependencies` | Also install Composer dev dependencies |

**What happens:**
1. `composer install` (production deps)
2. Compile missing extension assets
3. Delete `node_modules` and other unnecessary files
4. Delete extension asset source code
5. Merge admin snippets

**Private Composer repositories:**
```bash
SHOPWARE_PACKAGES_TOKEN=xxx shopware-cli project ci .
# or
COMPOSER_AUTH='{"http-basic": {...}}' shopware-cli project ci .
```

**Build hooks in `.shopware-project.yml`:**
```yaml
build:
  hooks:
    pre:
      - 'echo "Starting build"'
    pre-composer:
      - 'cp .env.ci .env'
    post-composer:
      - 'bin/console secrets:decrypt-to-local --force'
    pre-assets:
      - 'npm install --prefix custom/plugins/MyPlugin'
    post-assets:
      - 'rm -rf node_modules'
    post:
      - 'echo "Build complete"'
```

**Available hooks:** `pre`, `pre-composer`, `post-composer`, `pre-assets`, `post-assets`, `post`.
The variable `PROJECT_ROOT` is available in all hooks.

**Complete `.shopware-project.yml` configuration:**
```yaml
compatibility_date: '2026-02-11'

build:
  browserslist: 'defaults'
  cleanup_paths:
    - 'node_modules'
  disable_asset_copy: false
  exclude_extensions:
    - 'SwagExample'
  keep_extension_source: false
  keep_source_maps: false
  remove_extension_assets: false
  force_extension_build:
    - name: 'SomePlugin'
  bundles:
    - path: src/MyBundle
    - path: src/MyFancyBundle
      name: MyGreatFancyBundle
  mjml:
    enabled: false
    searchPaths:
      - custom/plugins
      - custom/static-plugins
  hooks:
    pre: []
    post: []
    pre-composer: []
    post-composer: []
    pre-assets: []
    post-assets: []
```

**MJML email template compilation (from v0.6.32, with FroshPlatformTemplateMail):**
```yaml
build:
  mjml:
    enabled: true
    searchPaths:
      - custom/plugins
      - custom/static-plugins
```
Compiles `.html.mjml` → `.html.twig` and removes the `.mjml` files.

**Declare bundles (recommended via `.shopware-project.yml`):**
```yaml
build:
  bundles:
    - path: src/MyBundle
    - path: src/MyFancyBundle
      name: MyGreatFancyBundle
```

**Docker example:**
```dockerfile
#syntax=docker/dockerfile:1.4
FROM ghcr.io/shopware/docker-base:8.3 AS base-image
FROM ghcr.io/shopware/shopware-cli:latest-php-8.3 AS shopware-cli

FROM shopware-cli AS build
ARG SHOPWARE_PACKAGES_TOKEN
ADD . /src
WORKDIR /src
RUN --mount=type=secret,id=composer_auth,dst=/src/auth.json \
    --mount=type=cache,target=/root/.composer \
    --mount=type=cache,target=/root/.npm \
    /usr/local/bin/entrypoint.sh shopware-cli project ci /src

FROM base-image
COPY --from=build --chown=82 --link /src /var/www/html
```

---

### `project admin-build <path>`

Build the administration assets for all extensions.

```bash
shopware-cli project admin-build .
shopware-cli project admin-build . --only-custom-static-extensions
```

| Flag | Description |
|------|-------------|
| `--only-custom-static-extensions` | Only build extensions in `custom/static-plugins/` |

Equivalent to `bin/build-administration.sh`.

---

### `project storefront-build <path>`

Build storefront assets + `theme:compile`.

```bash
shopware-cli project storefront-build .
shopware-cli project storefront-build . --only-custom-static-extensions
```

| Flag | Description |
|------|-------------|
| `--only-custom-static-extensions` | Only build extensions in `custom/static-plugins/` |

Equivalent to `bin/build-storefront.sh`.

---

### `project admin-watch <path>`

Start the admin webpack dev server.

```bash
shopware-cli project admin-watch .
shopware-cli project admin-watch . --only-extensions MyPlugin,OtherPlugin
shopware-cli project admin-watch . --skip-extensions ThirdPartyPlugin
```

| Flag | Description |
|------|-------------|
| `--only-extensions` | Watch only certain extensions (comma-separated) |
| `--skip-extensions` | Exclude certain extensions |

Equivalent to `bin/watch-administration.sh`.

---

### `project storefront-watch <path>`

Start the storefront webpack hot reload proxy.

```bash
shopware-cli project storefront-watch .
```

Equivalent to `bin/watch-storefront.sh`.

---

### `project dump [flags]`

Create a MySQL dump (native Go implementation, no `mysqldump` required).

```bash
shopware-cli project dump
shopware-cli project dump --host 127.0.0.1 --username root --password root --database sw6
shopware-cli project dump --clean
shopware-cli project dump --anonymize
shopware-cli project dump --compression=gzip
shopware-cli project dump --compression=zstd
shopware-cli project dump --skip-lock-tables
```

| Flag | Description |
|------|-------------|
| `--host` | Database host |
| `--username` | Database user |
| `--password` | Database password |
| `--database` | Database name |
| `--clean` | Log/temporary tables without content (cart, log_entry, message_queue_stats, ...) |
| `--anonymize` | Anonymize known user data |
| `--compression` | `gzip` or `zstd` |
| `--skip-lock-tables` | Skip the table lock |

**Data rewriting:**
```yaml
# .shopware-project.yml
dump:
  rewrite:
    customer:
      email: "faker.Internet().Email()"
      firstName: "'Anonymized'"
```

**Tables without content:**
```yaml
dump:
  nodata:
    - log_entry
    - dead_message
```

**Ignore tables completely:**
```yaml
dump:
  ignore:
    - some_temp_table
```

**WHERE clause:**
```yaml
dump:
  where:
    order: 'createdAt > "2024-01-01"'
```

**Cleaned by default (`--clean`):** `cart`, `customer_recovery`, `dead_message`, `enqueue`, `messenger_messages`, `increment`, `elasticsearch_index_task`, `log_entry`, `message_queue_stats`, `notification`, `payment_token`, `refresh_token`, `version`, `version_commit`, `version_commit_data`, `webhook_event_log`.

---

### `project worker <amount>`

Start multiple messenger consumers at the same time.

```bash
shopware-cli project worker 2
shopware-cli project worker 4
```

For production: prefer supervisord or systemd.

---

### `project clear-cache`

Clear the cache (shortcut for `bin/console cache:clear`).

```bash
shopware-cli project clear-cache
```

If an API connection is configured in `.shopware-project.yml`, the remote cache is cleared.

---

### `project console <command>`

Passthrough to `bin/console` without having to change into the project directory.

```bash
shopware-cli project console cache:clear
shopware-cli project console plugin:list
```

---

### `project admin-api [method] [path]`

Admin API requests with automatic JWT authentication.

```bash
shopware-cli project admin-api --output-token        # print JWT token
shopware-cli project admin-api GET /_info/version
shopware-cli project admin-api POST /product -d '{"name": "Test"}'
shopware-cli project admin-api GET /order -H "sw-language-id: xxx"
```

| Flag | Description |
|------|-------------|
| `--output-token` | Print the JWT token instead of making a request |
| `-d` | Request body (like curl) |
| `-H` | Additional headers (like curl) |

---

### `project image-proxy`

Start a local HTTP server that serves static files from `public/` and forwards missing files to an upstream server (with cache).

```bash
shopware-cli project image-proxy
shopware-cli project image-proxy --url https://production.example.com
shopware-cli project image-proxy --port 3000
shopware-cli project image-proxy --clear
shopware-cli project image-proxy --external-url https://dev.example.com
shopware-cli project image-proxy --skip-config
```

| Flag | Default | Description |
|------|---------|-------------|
| `--url` | from config | Upstream server URL |
| `--port` | `8080` | Listen port |
| `--clear` | `false` | Clear the cache before start |
| `--external-url` | `http://localhost:{port}` | External URL for the Shopware config (reverse proxy) |
| `--skip-config` | `false` | Do not create the Shopware config file |

**Configuration in `.shopware-project.yml`:**
```yaml
image_proxy:
  url: https://production.example.com
```

**Flow:** local `public/` files → cache (`var/cache/image-proxy/`) → upstream proxy → store in cache.

Automatically creates `config/packages/zzz-sw-cli-image-proxy.yml` and removes it on stop.

---

### `project extension list`

List all installed extensions via the Admin API.

```bash
shopware-cli project extension list
```

### `project extension install <name>`

Install an extension.

```bash
shopware-cli project extension install MyPlugin
```

### `project extension uninstall <name>`

Uninstall an extension.

```bash
shopware-cli project extension uninstall MyPlugin
```

### `project extension update <name>`

Update an extension.

```bash
shopware-cli project extension update MyPlugin
```

### `project extension outdated`

Show extensions with available updates.

```bash
shopware-cli project extension outdated
```

### `project extension upload <zip-path>`

Upload an extension zip to a Shopware instance.

```bash
shopware-cli project extension upload MyPlugin-1.0.0.zip
```

### `project extension delete <name>`

Delete an extension from a Shopware instance.

```bash
shopware-cli project extension delete MyPlugin
```

---

### `project autofix flex`

Migrate a project to Symfony Flex (< SW 6.5 → 6.5+). Moves configuration files, updates `composer.json` and `bin/console`.

```bash
shopware-cli project autofix flex
```

A backup before running is recommended!

---

### `project autofix composer-plugins`

Migrate locally installed plugins to Composer (via Shopware Packagist).

```bash
shopware-cli project autofix composer-plugins
```

Requires a Shopware Packages token from the Shopware Account.

---

### `project fix <path>`

Apply automatic refactoring to the whole project.

```bash
shopware-cli project fix path/to/project
docker run --rm -v "$(pwd)":/project ghcr.io/shopware/shopware-cli project fix /project
```

---

### `project format <path>`

Apply code formatting to the whole project.

```bash
shopware-cli project format path/to/project
shopware-cli project format path/to/project --dry-run
```

---

## account — Account Commands

### `account login`

OIDC/OAuth2 browser login to Shopware Account.

```bash
shopware-cli account login
```

**CI/CD (no browser):** set environment variables:
```bash
SHOPWARE_CLI_ACCOUNT_CLIENT_ID=xxx
SHOPWARE_CLI_ACCOUNT_CLIENT_SECRET=yyy
```

Client ID and secret: Shopware Account → Extension Partner → Development → [Generate].

---

### `account logout`

Invalidate the local token cache.

```bash
shopware-cli account logout
```

---

### `account merchant shop list`

List all accessible shops.

```bash
shopware-cli account merchant shop list
```

---

### `account merchant shop configure-composer <domain>`

Configure the Composer repository (create `auth.json` + update `composer.json`).

```bash
shopware-cli account merchant shop configure-composer my-shop.example.com
```

Tab completion for available domains is supported.

---

### `account producer extension list`

List all of your own store extensions.

```bash
shopware-cli account producer extension list
shopware-cli account producer extension list --search MyPlugin
```

| Flag | Description |
|------|-------------|
| `--search` | Filter by name |

---

### `account producer extension upload <zip-path>`

Upload an extension zip to the Shopware Store + trigger the automatic code review.

```bash
shopware-cli account producer extension upload MyPlugin-1.0.0.zip
shopware-cli account producer extension upload MyPlugin-1.0.0.zip --skip-for-review-result
```

| Flag | Description |
|------|-------------|
| `--skip-for-review-result` | Do not wait for the code review result |

**Prerequisites:**
- Login via `account login`
- Zip with all assets (via `extension zip --release`)
- `CHANGELOG*.md` in the zip with a changelog entry for the new version
- Validated via `extension validate`

Checks first whether the version already exists. Compatibility from `composer.json`/`manifest.xml`.

---

### `account producer extension info pull <path>`

Download the current store page data (description, images, metadata) into the local `.shopware-extension.yml` and `src/Resources/store/`.

```bash
shopware-cli account producer extension info pull path/to/MyPlugin
```

---

### `account producer extension info push <path>`

Upload local store page data (`.shopware-extension.yml`, images) to Shopware Account.

```bash
shopware-cli account producer extension info push path/to/MyPlugin
```

**Image configuration in `.shopware-extension.yml`:**
```yaml
store:
  images:
    - file: src/Resources/store/screenshot1.png
      priority: 1
      activate:
        de: true
        en: true
      preview:
        de: false
        en: false
  # or a directory:
  image_directory: src/Resources/store/images/
  automatic_bugfix_version_compatibility: true
```

**Directory structure (by language):**
```
src/Resources/store/images/
├── de/
│   ├── 0.png
│   ├── 1.png
│   └── 2.png  # preview
└── en/
    ├── 0.png
    ├── 1.png
    └── 2.png  # preview
```

---

## Environment Variables

| Variable | Description |
|----------|-------------|
| `CI` | Detect a CI environment |
| `SHOPWARE_CLI_PREVIOUS_TAG` | Override the previous git tag for the changelog |
| `CI_PROJECT_URL` | GitLab CI project URL for the changelog |
| `SHOPWARE_CLI_NO_SYMFONY_CLI` | Disable usage of the Symfony CLI |
| `APP_ENV` | Application environment |
| `SHOPWARE_PROJECT_ROOT` | Use a Shopware project for the extension build |
| `SHOPWARE_CLI_DISABLE_WASM_CACHE` | Disable the WASM cache for PHP linting |
| `SHOPWARE_PACKAGES_TOKEN` | Token for packages.shopware.com (private Composer repos) |
| `COMPOSER_AUTH` | Content of `auth.json` as an environment variable |
| `SHOPWARE_CLI_ACCOUNT_CLIENT_ID` | CI/CD: account client ID |
| `SHOPWARE_CLI_ACCOUNT_CLIENT_SECRET` | CI/CD: account client secret |

---

## Compatibility Date

Both `.shopware-extension.yml` and `.shopware-project.yml` support:

```yaml
compatibility_date: '2026-02-11'
```

Enables new behavior changes from the given date onwards. If the field is missing, `2026-02-11` is used as a fallback (with a warning).

Format: `YYYY-MM-DD`.

---

## Typical Workflows

### Extension release (complete)

```bash
# 1. Build assets
shopware-cli extension build MyPlugin/

# 2. Validate
shopware-cli extension validate --full MyPlugin/
shopware-cli extension validate --full MyPlugin/ --check-against lowest

# 3. Create zip
shopware-cli extension zip MyPlugin/ --release

# 4. Update the store page
shopware-cli account login
shopware-cli account producer extension info push MyPlugin/

# 5. Upload the extension
shopware-cli account producer extension upload MyPlugin-1.0.0.zip
```

### CI/CD with GitHub Actions

```yaml
- name: Install shopware-cli
  uses: shopware/shopware-cli-action@v3

- name: Build extension
  run: shopware-cli extension build .

- name: Validate extension
  run: shopware-cli extension validate --full . --reporter github

- name: Create zip
  run: shopware-cli extension zip . --release

- name: Upload to Store
  env:
    SHOPWARE_CLI_ACCOUNT_CLIENT_ID: ${{ secrets.SW_CLIENT_ID }}
    SHOPWARE_CLI_ACCOUNT_CLIENT_SECRET: ${{ secrets.SW_CLIENT_SECRET }}
  run: shopware-cli account producer extension upload *.zip
```

### Project deployment

```bash
shopware-cli project ci /var/www/shopware
```
