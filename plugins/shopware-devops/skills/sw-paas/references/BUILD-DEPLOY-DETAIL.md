# Shopware PaaS (Platform.sh/Upsun) — Build & Deploy (Deep Reference)

Sources: `products/paas/shopware-paas/build-deploy.md`,
`products/paas/shopware-paas/repository.md`,
`products/paas/shopware-paas/setup-template.md`,
`products/paas/shopware-paas/cli-setup.md`

> **Note:** Platform.sh is now **Upsun**. References to Platform.sh are equivalent.

---

## Contents

- [CLI Setup](#cli-setup)
- [Repository setup](#repository-setup)
- [Build & Deploy process](#build-deploy-process)
- [Setup Template — .platform/applications.yaml](#setup-template-platformapplicationsyaml)
- [.platform/services.yaml](#platformservicesyaml)
- [Automatic environment variables](#automatic-environment-variables)
- [Composer Authentication](#composer-authentication)
- [Rebuild without a code change](#rebuild-without-a-code-change)
- [Migration from the old template](#migration-from-the-old-template)
- [files/theme-config](#filestheme-config)

## CLI Setup

```bash
# Installation
curl -sfS https://cli.shopware.com/installer | php

# SSH key (alternatively add it manually in the PaaS Console: My Profile → SSH Keys)
shopware     # First start → browser authentication
```

---

## Repository setup

### New project

```bash
composer create-project shopware/production <folder-name>
cd <folder-name>
composer require shopware/paas-meta
```

### Update the paas-meta recipe

```bash
composer recipes:update
```

**Warning:** Every recipe update can contain breaking changes! Review manually,
especially with `.platform` file changes (e.g. local → service mount).

### Configure Git remotes

```bash
# Determine the project ID
shopware projects

# Add the remote
shopware project:set-remote <PROJECT_ID>

# Result: two remotes
git remote -v
# origin   git@github.com:company/repo.git (fetch/push)
# shopware <paas-url>.git (fetch/push)
```

---

## Build & Deploy process

### Trigger a deployment

```bash
git add .
git commit -m "Applied new configuration"
git push -u shopware main
```

### Build steps

| Phase | Action |
|-------|--------|
| Build | Validate configuration |
| Build | Create container image |
| Build | Install dependencies (Composer + assets) |
| Build | Run build hook |
| Deploy | Hold app requests |
| Deploy | Unmount running containers |
| Deploy | Mount filesystems |
| Deploy | Run deploy hook |
| Deploy | Release requests |

### First deployment

The Shopware CLI installer runs automatically and creates an admin account:

| Username | Password |
|----------|----------|
| `admin`  | `shopware` |

**Change the password immediately after deployment!**
Do not delete `install.lock` — otherwise the installer runs again.

---

## Setup Template — .platform/applications.yaml

```yaml
name: app
type: php:8.3

# Environment variables and server settings
variables:
  env:
    N_PREFIX: /app/.global
    APP_ENV: prod
    # Custom variables go here

# Lifecycle hooks
hooks:
  build: |
    # Build phase: filesystem is writable, no services available
    # Composer + shopware-cli + build assets
  deploy: |
    # Deploy phase: traffic is held, services available
    # DB migrations, theme config, clear cache
    # MINIMIZE — every second = downtime
  post_deploy: |
    # After connections are accepted: compile theme etc.

# Service mapping
relationships:
  database: "db:mysql"
  cacheredis: "cacheredis:redis"
  rabbitmqqueue: "rabbitmq:rabbitmq"
  redissession: "redissession:redis"

# Writable directories
mounts:
  # Local mounts (per instance)
  "/var/cache": { source: local, source_path: cache }
  "/var/log": { source: local, source_path: log }
  # Service mounts (shared between instances)
  "/public/media": { source: service, service: fileshare, source_path: media }
  "/public/thumbnail": { source: service, service: fileshare, source_path: thumbnail }
  "/public/bundles": { source: service, service: fileshare, source_path: bundles }
  "/public/sitemap": { source: service, service: fileshare, source_path: sitemap }

# HTTP routing
web:
  locations:
    "/":
      root: "public"
      expires: 1h
      passthru: "/index.php"

# Worker configuration
workers:
  queue:
    commands:
      start: php bin/console messenger:consume --memory-limit=256M --time-limit=60 async
  scheduled_task:
    commands:
      start: php bin/console scheduled-task:run --memory-limit=256M --time-limit=60
```

---

## .platform/services.yaml

```yaml
db:
  type: mariadb:10.6
  disk: 2048

cacheredis:
  type: redis:7.0

redissession:
  type: redis:7.0

rabbitmq:
  type: rabbitmq:3.8
  disk: 1024

fileshare:
  type: network-storage:2.0
  disk: 5000

# Optional
elasticsearch:
  type: opensearch:2
  disk: 256

# Optional
opensearch:
  type: opensearch:2
  disk: 256
```

---

## Automatic environment variables

Set automatically by Platform.sh based on `relationships`:

### Global

| Variable | Example value |
|----------|-------------|
| `APP_SECRET` | `a3c45d78e91f2b3c4d5e...` |
| `APP_ENV` | `prod` |
| `APP_URL` | `https://main-abc123.eu-5.platformsh.site` |
| `MAILER_DSN` | `smtp://localhost:25` |

### Database

| Variable | Example value |
|----------|-------------|
| `DATABASE_URL` | `mysql://user:password@database.internal:3306/main` |
| `DATABASE_REPLICA_0_URL` | `mysql://user:password@database-replica.internal:3306/main` |

### RabbitMQ

| Variable | Example value |
|----------|-------------|
| `MESSENGER_TRANSPORT_DSN` | `amqp://guest:guest@rabbitmq.internal:5672/%2f/messages` |
| `MESSENGER_TRANSPORT_DSN_PREFIX` | `amqp://guest:guest@rabbitmq.internal:5672/%2f/` |

### Redis Cache

| Variable | Example value |
|----------|-------------|
| `CACHE_DSN` | `redis://rediscache.internal:6379` |
| `CACHE_URL` | `redis://rediscache.internal:6379` |

### Redis Session

| Variable | Example value |
|----------|-------------|
| `SESSION_REDIS_HOST` | `redissession.internal` |
| `SESSION_REDIS_PORT` | `6379` |
| `SESSION_REDIS_URL` | `redis://redissession.internal:6379` |

### OpenSearch/Elasticsearch

| Variable | Example value |
|----------|-------------|
| `OPENSEARCH_URL` | `http://opensearch.internal:9200` |
| `ADMIN_OPENSEARCH_URL` | `http://opensearch.internal:9200` |
| `ELASTICSEARCH_URL` | `http://elasticsearch.internal:9200` |
| `ELASTICSEARCH_HOST` | `elasticsearch.internal` |
| `ELASTICSEARCH_PORT` | `9200` |

---

## Composer Authentication

```bash
# Shopware Plugin Store auth for CI
shopware variable:create \
  --level project \
  --name env:COMPOSER_AUTH \
  --json true \
  --visible-runtime false \
  --sensitive true \
  --visible-build true \
  --value '{"bearer": {"packages.shopware.com": "<YOUR_TOKEN>"}}'
```

Token from the Shopware Account → "Install with Composer".

---

## Rebuild without a code change

```bash
# Create a variable (triggers an immediate build)
shopware variable:create \
  --environment main \
  --level environment \
  --prefix env \
  --name REBUILD_DATE \
  --value "$(date)" \
  --visible-build true

# Update the variable (triggers another build)
shopware variable:update --environment main --value "$(date)" "env:REBUILD_DATE"
```

---

## Migration from the old template

From `shopwareArchive/paas` to the new Flex template:

```bash
# Perform the Flex migration
# .platform.app.yml → .platform/applications.yaml
# Services renamed:
# queuerabbit → rabbitmq
# searchelastic → opensearch
```

Options when a service is renamed:
1. Rename the services back
2. Start a new service + reindex ES
3. Run both services in parallel during the transition period

---

## files/theme-config

Commit the theme configuration to Git (recommended):
```text
files/
└─ theme-config/
   └─ ...
```

Enables builds without database access to the theme configuration.
Details: [Build without Database](https://developer.shopware.com/docs/guides/hosting/installation-updates/deployments/build-w-o-db)
