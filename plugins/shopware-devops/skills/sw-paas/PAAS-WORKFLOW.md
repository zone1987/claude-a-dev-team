# Shopware PaaS — Deploy workflow, sw-paas CLI and environment variables

## Contents

- [sw-paas CLI](#sw-paas-cli)
- [Full deploy workflow](#full-deploy-workflow)
- [Enabling Elasticsearch/OpenSearch](#enabling-elasticsearchopensearch)
- [Multi-environment (staging vs. production)](#multi-environment-staging-vs-production)
- [shopware-deployment-helper](#shopware-deployment-helper)
- [Initial installation after deployment](#initial-installation-after-deployment)
- [Important environment variables for PaaS](#important-environment-variables-for-paas)

## sw-paas CLI

### Installation

```bash
# Recommended: installer
curl -L https://install.sw-paas-cli.shopware.systems | sh

# Specific version
curl -L https://install.sw-paas-cli.shopware.systems | sh -s 0.0.57

# Manual: binary from GitHub Releases
# https://github.com/shopware/sw-paas/releases
chmod +x sw-paas_linux_amd64
mv sw-paas_linux_amd64 /usr/local/bin/sw-paas
```

**Installer behavior:**
- Installs to `~/.sw-paas/bin/sw-paas`
- Adds `SW_PAAS_INSTALL` and a `PATH` extension to `~/.zshrc` or `~/.bash_profile`
- Respects the `SW_PAAS_DIR` environment variable for a custom path

**Uninstall:**
```bash
rm -rf ~/.sw-paas
# Then remove from the shell profile:
# export SW_PAAS_INSTALL="$HOME/.sw-paas"
# export PATH="$SW_PAAS_INSTALL/bin:$PATH"
```

### Supported platforms
- macOS (Darwin): x86_64, arm64
- Linux: x86_64, arm64, i386

### First command after installation

```bash
sw-paas auth
```

Authenticates against the Shopware PaaS API.

---

## Full deploy workflow

### 1. Set up the project

```bash
# Create a new project with PaaS configuration
shopware-cli project create my-shop latest --deployment shopware-paas --ci github

# OR: add PaaS to an existing project
composer require shopware/paas-meta
```

### 2. Local development

```bash
# Development without PaaS
shopware-cli project admin-watch .
shopware-cli project storefront-watch .

# Local dump for data
shopware-cli project dump --clean --anonymize
```

### 3. Build phase (on Platform.sh)

Platform.sh runs the `build` hook from `applications.yaml`:

```
┌─────────────────────────────────────────────────────┐
│ BUILD HOOK (no network, no mount access)             │
│                                                      │
│ 1. Install Node.js (from the nodejs.org CDN)         │
│ 2. Install shopware-cli (from GitHub Releases)       │
│ 3. Run shopware-cli project ci .:                   │
│    a. composer install --no-dev --optimize           │
│    b. Build extension assets (admin + storefront)   │
│    c. Symfony cache warmup                          │
│    d. assets:install                               │
│    e. Compile MJML (if present)                    │
│    f. Generate checksums                           │
│ 4. Back up localCache → RO-localCache               │
│ 5. Back up var/ → RO-var                           │
└─────────────────────────────────────────────────────┘
```

**Important build environment variables:**
```bash
export APP_CACHE_DIR=$PLATFORM_APP_DIR/localCache
export SHOPWARE_SKIP_ASSET_INSTALL_CACHE_INVALIDATION=1
```

### 4. Deploy phase (on Platform.sh)

```
┌─────────────────────────────────────────────────────┐
│ DEPLOY HOOK (network + mounts available)             │
│                                                      │
│ 1. rsync RO-localCache → /localCache (mount)        │
│ 2. rsync RO-var → /var (mount)                      │
│ 3. Create Dompdf directories                        │
│ 4. shopware-deployment-helper run:                  │
│    a. Database migrations                           │
│    b. Plugin updates                                │
│    c. Set up scheduled tasks                        │
│    (--skip-asset-install --skip-theme-compile)      │
│ 5. Non-prod: update the sales channel domain        │
└─────────────────────────────────────────────────────┘
```

### 5. Post-deploy phase

```
┌─────────────────────────────────────────────────────┐
│ POST_DEPLOY HOOK                                     │
│                                                      │
│ bin/console theme:compile --sync                    │
│ (after all deploy hooks of all instances)           │
└─────────────────────────────────────────────────────┘
```

### 6. Worker (permanently running)

```
┌─────────────────────────────────────────────────────┐
│ WORKER: queue                                        │
│                                                      │
│ pre_start:                                          │
│   export APP_CACHE_DIR=$PLATFORM_APP_DIR/localCache │
│   rm -rf $APP_CACHE_DIR/var                         │
│   php bin/console  (warm-up)                        │
│                                                      │
│ start:                                              │
│   bin/console messenger:consume async low_priority  │
│   failed                                           │
│   --memory-limit=<container-memory>M               │
│   --time-limit=295                                 │
└─────────────────────────────────────────────────────┘
```

### 7. Cron

```
*/5 * * * *   APP_CACHE_DIR=/app/localCache php bin/console scheduled-task:run --no-wait
```

---

## Enabling Elasticsearch/OpenSearch

In `applications.yaml`:
```yaml
variables:
    env:
        SHOPWARE_ES_ENABLED: 1
        SHOPWARE_ES_INDEXING_ENABLED: 1
relationships:
    opensearch: "opensearch:opensearch"
```

Uncomment in `services.yaml`:
```yaml
opensearch:
    type: opensearch:2
    disk: 256
```

---

## Multi-environment (staging vs. production)

The deploy hook distinguishes them automatically:

```bash
if [ "$PLATFORM_ENVIRONMENT_TYPE" != production ]; then
    # Staging/dev: point the sales channel domain at the current URL
    export FRONTEND_URL=$(echo $PLATFORM_ROUTES | base64 --decode | \
      jq -r 'to_entries[] | select(.value.id=="shopware") | .key')
    export FRONTEND_DOMAIN=$(php -r 'echo parse_url($_SERVER["FRONTEND_URL"], PHP_URL_HOST);')
    bin/console sales-channel:update:domain "$FRONTEND_DOMAIN"
fi
```

---

## shopware-deployment-helper

`vendor/bin/shopware-deployment-helper` is part of `shopware/deployment-helper` (Composer package).

```bash
# Default (with asset install and theme compile)
php vendor/bin/shopware-deployment-helper run

# PaaS: assets are installed in the build hook, the theme is compiled after deploy
php vendor/bin/shopware-deployment-helper run \
  --skip-asset-install \
  --skip-theme-compile
```

**What `deployment-helper run` does:**
1. Run database migrations
2. Plugin lifecycle (install/update/activate)
3. Register scheduled tasks
4. (Optional) Install assets
5. (Optional) Compile the theme

---

## Initial installation after deployment

```bash
# After the first push: download the theme config files
platform mount:download --mount 'files' --target 'files' -A app

# Commit and push these files so the theme compiles correctly
git add files/theme-config/
git commit -m "chore: add initial theme config from PaaS"
git push
```

---

## Important environment variables for PaaS

| Variable | Origin | Purpose |
|----------|----------|-------|
| `PLATFORM_APP_DIR` | Platform.sh | App root path (`/app`) |
| `PLATFORM_ENVIRONMENT_TYPE` | Platform.sh | `production` or `development` |
| `PLATFORM_ROUTES` | Platform.sh | JSON of all routes (base64) |
| `PLATFORM_RELATIONSHIPS` | Platform.sh | JSON of all services (base64) |
| `APP_CACHE_DIR` | `.environment` | Local cache path (`/app/localCache`) |
| `APP_LOG_DIR` | `applications.yaml` | Log path (`/app/localLog`) |
| `NODE_VERSION` | `applications.yaml` | Node.js version for the build |
| `SHOPWARE_CLI_VERSION` | `applications.yaml` | shopware-cli version for the build |
| `SHOPWARE_HTTP_CACHE_ENABLED` | `applications.yaml` | Enable the HTTP cache (→ Cache-Control header) |
| `SHOPWARE_SKIP_WEBINSTALLER` | `applications.yaml` | Disable the web installer |
| `SHOPWARE_ES_ENABLED` | `applications.yaml` | Enable OpenSearch |
| `SHOPWARE_SKIP_ASSET_INSTALL_CACHE_INVALIDATION` | Build hook | Skip asset install cache invalidation |
| `SW_PAAS_DIR` | Local | sw-paas CLI install path |
