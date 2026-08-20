# Shopware PaaS (Platform.sh/Upsun) — Build & Deploy

> This skill covers **classic Shopware PaaS** (Platform.sh/Upsun),
> not PaaS Native. For PaaS Native → `sw-paas-fundamentals`.

## Setup

```bash
# Install the PaaS CLI
curl -sfS https://cli.shopware.com/installer | php
shopware     # First start → browser login

# Install the paas-meta recipe
composer require shopware/paas-meta

# Add the PaaS remote
shopware project:set-remote <PROJECT_ID>
git push shopware main
```

## .platform/ configuration

| File | Purpose |
|-------|-------|
| `applications.yaml` | App: PHP version, hooks, mounts, workers, vars |
| `services.yaml` | DB, Redis, RabbitMQ, network storage |
| `routes.yaml` | HTTP routing |

## Build → Deploy sequence

```
BUILD:        Validate configuration → Docker image → dependencies → build hook
DEPLOY:       Hold app requests → mount filesystems → deploy hook → release requests
POST_DEPLOY:  Runs after connections are accepted
```

## Automatic environment variables

```bash
DATABASE_URL=mysql://user:pass@database.internal:3306/main
MESSENGER_TRANSPORT_DSN=amqp://guest:guest@rabbitmq.internal:5672/%2f/messages
CACHE_DSN=redis://rediscache.internal:6379
OPENSEARCH_URL=http://opensearch.internal:9200
APP_URL=https://main-abc123.eu-5.platformsh.site
```

## Force a rebuild (without a code change)

```bash
shopware variable:create --environment main --level environment \
  --prefix env --name REBUILD_DATE --value "$(date)" --visible-build true
shopware variable:update --environment main --value "$(date)" "env:REBUILD_DATE"
```

## Deep dive

[BUILD-DEPLOY-DETAIL.md](BUILD-DEPLOY-DETAIL.md)
