# Shopware PaaS Native — Fundamentals (Deep Reference)

Sources: `products/paas/shopware/fundamentals/` (account.md, organization.md, project.md,
applications.md, application-yaml.md, environment-variables.md, secrets.md,
php-settings.md, plugins-store-authentication.md, k8s-meta.md)

---

## Contents

- [1. Account & Identity](#1-account-identity)
- [2. Organizations](#2-organizations)
- [3. Projects](#3-projects)
- [4. Applications](#4-applications)
- [5. application.yaml — complete reference](#5-applicationyaml-complete-reference)
- [6. Environment variables — priority](#6-environment-variables-priority)
- [7. Vault Secrets](#7-vault-secrets)
- [8. PHP settings](#8-php-settings)
- [9. Plugin Store Authentication](#9-plugin-store-authentication)
- [10. k8s-meta package](#10-k8s-meta-package)

## 1. Account & Identity

```bash
sw-paas account whoami                     # current user + roles
sw-paas account whoami --output json | jq ".sub"  # determine the sub ID
sw-paas account context set               # store org+project
sw-paas account context show
sw-paas account context delete
```

The context is stored in `context-production.yaml`:

| OS     | Path |
|--------|------|
| Unix   | `~/.config/sw-paas` |
| macOS  | `~/Library/Application Support/sw-paas` |
| Windows| `%LOCALAPPDATA%` |

### Managing users

```bash
sw-paas account user list
sw-paas account user add --sub "<sub-id>"
sw-paas account user remove
sw-paas account user request
sw-paas account user requests list
sw-paas account user requests resolve   # account-admin only
```

### Service accounts (CI/CD)

```bash
sw-paas account service-account create
sw-paas account service-account list
sw-paas account service-account update
sw-paas account service-account delete
sw-paas account service-account grant add
sw-paas account service-account grant list
sw-paas account service-account grant policies
sw-paas account service-account grant revoke
```

### Tokens

```bash
# Personal token
sw-paas account token create --name "ci-token"
export SW_PAAS_TOKEN=<token>
sw-paas --token <token> account whoami
sw-paas account token revoke --token-id abcd-1234

# Service account token
sw-paas account token create --service-account-id <id>
sw-paas account token list --service-account-id <id>
sw-paas account token revoke --service-account-id <id>
```

---

## 2. Organizations

- Top-level unit (company/entity)
- Long-lived, do not expire automatically
- Roles: `read-only`, `developer`, `project-admin`, `account-admin`

```bash
sw-paas organization create
```

---

## 3. Projects

- Represent a Git repo (GitHub/GitLab/Bitbucket)
- Can contain many applications

```bash
sw-paas project create
sw-paas project list
```

---

## 4. Applications

### Resource profile (default)

| Component    | Replicas | CPU req | Memory req | Memory limit |
|--------------|----------|---------|------------|--------------|
| `storefront` | 2        | 50m     | 256Mi      | 2Gi          |
| `admin`      | 1        | 25m     | 128Mi      | 2Gi          |
| `worker`     | 1        | 50m     | 256Mi      | 1Gi          |

Scaling is primarily horizontal. Limits depend on the booked plan.

### Application lifecycle

```bash
sw-paas application create
sw-paas application build start
sw-paas application build logs
sw-paas application update           # build + deploy (with commit SHA)
sw-paas application deploy create    # deploy a specific build
sw-paas application deploy list
sw-paas application deploy get
sw-paas application logs
sw-paas application deploy logs
```

### Deployment behavior

- Zero downtime via Kubernetes rolling updates
- DB migrations run **first**
- After that: [Deployment Helper](https://developer.shopware.com/docs/guides/hosting/installation-updates/deployments/deployment-helper)
- Pre/post-deployment hooks are configurable through the Deployment Helper

### Running commands

```bash
sw-paas exec --new      # interactive shell in the container (TTL: 1h)
sw-paas command create  # non-interactive, own container
```

### Domain management

Automatic `shopware.shop` domain on first provisioning.

```bash
sw-paas domain create               # create a custom domain
```

DNS target: `cdn.shopware.shop` (CNAME for subdomains).
After creating the domain, `sw-paas application deploy create` is required.

### Plugin management

**Only via Composer** (no UI plugin manager):
```bash
composer require vendor/plugin
```

Private packages via the `COMPOSER_AUTH` vault secret (`buildenv`).

---

## 5. application.yaml — complete reference

```yaml
app:
  php:
    version: "8.3"              # PHP version
    extensions:                 # PHP extensions (mlocati/docker-php-extension-installer)
      - imagick
  environment_variables:
    - name: MY_RUNTIME_VAR
      value: "runtime-value"
      scope: RUN                # RUN = runtime
    - name: MY_BUILD_VAR
      value: "build-value"
      scope: BUILD              # BUILD = build phase only
services:
  mysql:
    version: "8.0"
  opensearch:
    enabled: true
cronJobs:
  - name: guest-cleanup
    schedule: "0 3 * * *"
    command: "bin/console customer:delete-unused-guests"
    timezone: Europe/Berlin
```

---

## 6. Environment variables — priority

| Source             | Priority   |
|--------------------|------------|
| `.env` file        | Lowest     |
| `application.yaml` | Medium     |
| Vault secrets      | Highest    |

---

## 7. Vault Secrets

Secrets are valid organization-wide and reusable.

```bash
sw-paas vault create                        # interactive
sw-paas vault create --type env --key NAME  # runtime variable
sw-paas vault create --type buildenv --key NAME  # build variable
sw-paas vault create --type ssh             # generate an SSH key pair
sw-paas vault list
sw-paas vault get --secret-id SECRET-ID
sw-paas vault delete --secret-id SECRET-ID
sw-paas vault edit                          # edit an existing secret
```

### System-managed secrets (do NOT delete!)

| Secret | Purpose |
|--------|-------|
| `STOREFRONT_CREDENTIALS` | Storefront authentication |
| `GRAFANA_CREDENTIALS` | Grafana access |
| `NATS_USER_CREDENTIALS` | NATS messaging |
| `STOREFRONT_PROXY_KEY` | Routing |

### User-managed secrets

| Secret | Type | Purpose |
|--------|-----|-------|
| `SSH_PRIVATE_KEY` | ssh | Git deployment |
| `SHOPWARE_PACKAGES_TOKEN` | buildenv | Shopware Plugin Store |
| `COMPOSER_AUTH` | buildenv | Third-party repos |

### COMPOSER_AUTH format

```json
{
  "http-basic": {
    "git.mycompany.com": {
      "username": "user",
      "password": "pass"
    }
  }
}
```

```json
{
  "bearer": {
    "git.mycompany.com": "mytoken"
  }
}
```

### Housekeeping / best practices

```bash
# Back up before deleting
sw-paas vault get --secret-id SECRET-ID > $(date +%Y%m%d)-backup.txt

# Audit
sw-paas vault list --application-id YOUR-APP-ID
```

- No version history — changes are permanent
- Regular rotation recommended (every 90 days)

---

## 8. PHP settings

Configurable via environment variables:

| Variable | PHP setting |
|----------|----------------|
| `PHP_MAX_UPLOAD_SIZE` | `upload_max_filesize` + `post_max_size` |
| `PHP_MAX_EXECUTION_TIME` | `max_execution_time` |

Base image: [shopware/docker](https://github.com/shopware/docker)
All parameters: [docker.ini](https://github.com/shopware/docker/blob/main/fpm/rootfs/usr/local/etc/php/conf.d/docker.ini)

**Do not override:** `PHP_SESSION_HANDLER` (managed by the platform)

---

## 9. Plugin Store Authentication

```bash
# Shopware Plugin Store (usually created automatically)
sw-paas vault create --type buildenv --key SHOPWARE_PACKAGES_TOKEN

# Third-party store
sw-paas vault create --type buildenv --key COMPOSER_AUTH
```

---

## 10. k8s-meta package

Prepares Shopware for PaaS Native.

| Shopware | k8s-meta |
|----------|----------|
| 6.6      | `^1.0`   |
| 6.7      | `^2.0`   |

```bash
composer require shopware/k8s-meta --ignore-platform-reqs
```

### Installed configuration

`config/packages/operator.yaml` configures:
- **S3 object storage** (public/private/theme/sitemap filesystems)
- **Redis** (application cache + session)
- **Cluster mode** (`cluster_setup: true`, `runtime_extension_management: false`)
- **Admin worker** disabled (external queue processing)
- **Elasticsearch/OpenSearch** replica/shard settings
- **Monolog** → stderr as JSON

`config/packages/prod/`:
| File | Purpose |
|-------|-------|
| `fastly.yaml` | Fastly CDN reverse proxy + cache purging |
| `monolog.yaml` | Error-level logging → stderr JSON |
| `opentelemetry.yaml` | OpenTelemetry profiler |

### Overriding the configuration

```yaml
# config/packages/prod/shopware.yaml
shopware:
    http_cache:
        stale_while_revalidate: 300
        stale_if_error: 3600
```

**Warning:** The default config is optimized for the PaaS infra — change it only with care.
