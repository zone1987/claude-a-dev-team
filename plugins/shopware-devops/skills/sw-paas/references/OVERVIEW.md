# Shopware PaaS

Shopware PaaS is based on **Platform.sh**. The configuration is applied to the project via a
Symfony Flex recipe (`shopware/paas-meta`) and consists of three
`.platform/` files plus helper scripts.

```bash
# Install the sw-paas CLI
curl -L https://install.sw-paas-cli.shopware.systems | sh
sw-paas auth
```

```bash
# Install the recipe
composer require shopware/paas-meta
```

## Configuration files

| File | Purpose |
|-------|-------|
| `.platform/applications.yaml` | App definition: PHP version, hooks, mounts, worker, crons |
| `.platform/services.yaml` | Services: MariaDB, Redis (cache+session), RabbitMQ, network storage |
| `.platform/routes.yaml` | HTTP routing with cache policy |
| `config/packages/paas.yaml` | Symfony configuration: Redis session/cache, cluster mode |
| `.environment` | Shell env vars on every request (`APP_CACHE_DIR`) |
| `.shopware-project.yaml` | shopware-cli project config: `deployment.cache.always_clear: true` |

## Build → Deploy → Post-Deploy

```
BUILD:    install Node + shopware-cli → shopware-cli project ci .
DEPLOY:   rsync cache/var from build → shopware-deployment-helper run → domain update
POST_DEPLOY: bin/console theme:compile --sync
```

## Deep dive

- [CONFIG.md](CONFIG.md) — Complete applications.yaml, services.yaml, routes.yaml with explanations
- [WORKFLOW.md](WORKFLOW.md) — Deploy workflow, sw-paas CLI, environment variables
