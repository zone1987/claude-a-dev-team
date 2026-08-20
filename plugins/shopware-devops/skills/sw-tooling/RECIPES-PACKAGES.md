# Symfony Flex recipes — available packages

Source: `github.com/shopware/recipes` (all `manifest.json` files analyzed).

## Contents

- [Shopware packages](#shopware-packages)
- [Symfony packages](#symfony-packages)
- [Third-party packages](#third-party-packages)
- [Configuring the Flex endpoint](#configuring-the-flex-endpoint)

## Shopware packages

| Package | Versions | Alias | Description |
|---------|-----------|-------|--------------|
| `shopware/core` | 6.4, 6.6, 6.7 | — | Core scaffolding: bin/, config/, custom/, files/, public/, var/ |
| `shopware/administration` | 6.4, 6.6, 6.7 | — | Admin build scripts |
| `shopware/storefront` | 6.4, 6.6, 6.7 | — | Storefront build scripts |
| `shopware/elasticsearch` | 6.4, 6.6, 6.7 | — | OpenSearch/ES configuration |
| `shopware/platform` | 6.4, 6.6, 6.7 | — | Auto-merge of core+admin+storefront+es (legacy) |
| `shopware/docker` | 0.1, 0.2, 0.3 | — | Docker Compose setup for production |
| `shopware/docker-dev` | 0.1 | — | Docker Compose + Makefile for development |
| `shopware/dev-tools` | 1.0 | — | Aliases for development tools |
| `shopware/fastly-meta` | 6.4, 6.5, 6.6, 6.7, 6.8 | `fastly` | Fastly CDN: VCL snippets + Shopware configuration |
| `shopware/k8s-meta` | 1.0, 2.0 | `k8s` | Kubernetes configuration |
| `shopware/paas-meta` | 6.4, 6.5, 6.6, 6.7 | `paas` | Shopware PaaS (Platform.sh): .platform/, config/packages/paas.yaml |
| `shopware/opentelemetry` | 0.1 | — | OpenTelemetry configuration |
| `shopware/fixture-bundle` | 0.1 | — | Fixture bundle registration |

### shopware/core — copied files (6.7)

```
bin/console          → bin/console
bin/ci               → bin/ci
config/              → config/
custom/plugins/      → custom/plugins/
custom/static-plugins/ → custom/static-plugins/
files/.htaccess      → files/.htaccess
public/index.php     → public/index.php
public/.htaccess     → public/.htaccess
var/.gitignore       → var/.gitignore
```

**bundles (6.7):**
- `Shopware\Core\Framework\Framework` — all
- `Shopware\Core\Content\Content` — all
- `Shopware\Core\DevOps\DevOps` — e2e
- `Shopware\Core\Maintenance\Maintenance` — all
- `Symfony\Bundle\FrameworkBundle\FrameworkBundle` — all
- `Symfony\Bundle\MonologBundle\MonologBundle` — all
- `Symfony\Bundle\TwigBundle\TwigBundle` — all
- and many more

**env (6.7):**
```
APP_ENV=prod
APP_URL=http://127.0.0.1:8000
APP_SECRET=%generate(secret)%
INSTANCE_ID=%generate(secret)%
DATABASE_URL=mysql://root:root@localhost/shopware
```

### shopware/paas-meta — copied files (6.7)

```
.platform/applications.yaml  → .platform/applications.yaml
.platform/services.yaml       → .platform/services.yaml
.platform/routes.yaml         → .platform/routes.yaml
config/packages/paas.yaml     → config/packages/paas.yaml
root/.environment             → .environment
root/.shopware-project.yaml   → .shopware-project.yaml
```

**container (6.7):**
```
default_redis_database: "0"
default_redis_host: "rediscache.internal"
default_redis_port: "6379"
env(CACHE_URL): "redis://localhost"
env(MESSENGER_TRANSPORT_DSN_PREFIX): "doctrine://default?auto_setup=false&queue_name="
env(MESSENGER_TRANSPORT_DSN): "%env(MESSENGER_TRANSPORT_DSN_PREFIX)%messages"
env(MESSENGER_TRANSPORT_LOW_PRIORITY_DSN): "%env(MESSENGER_TRANSPORT_DSN_PREFIX)%low_priority"
```

---

## Symfony packages

| Package | Versions | Alias | Description |
|---------|-----------|-------|--------------|
| `symfony/framework-bundle` | 5.4, 6.4, 7.4 | — | Symfony framework base configuration |
| `symfony/console` | 5.4 | — | Console component registration |
| `symfony/routing` | 5.4, 6.4, 7.4 | — | Routing configuration |
| `symfony/messenger` | 5.4, 6.0 | `messenger` | Messenger: config/packages/messenger.yaml |
| `symfony/amqp-messenger` | 5.4 | — | AMQP Messenger: docker-compose LavinMQ service |
| `symfony/monolog-bundle` | 3.3 | — | Monolog logging configuration |
| `symfony/debug-bundle` | 5.3 | — | Debug bundle (dev env only) |
| `symfony/mailer` | 4.3 | `mail`, `mailer` | Mailer: docker-compose.override Mailpit service |
| `symfony/twig-bundle` | 5.4 | — | Twig configuration |
| `symfony/translation` | 5.4 | — | Translation configuration |
| `symfony/validator` | 5.3 | — | Validator configuration |
| `symfony/lock` | 5.3 | — | Lock component |
| `symfony/scheduler` | 7.2 | — | Scheduler: src/Scheduler/ stub |
| `symfony/property-info` | 7.3 | — | PropertyInfo configuration |
| `symfony/ux-twig-component` | 2.13 | — | Twig Components |

---

## Third-party packages

| Package | Versions | Alias | Description |
|---------|-----------|-------|--------------|
| `doctrine/annotations` | 1.0 | — | Annotations registration |
| `enqueue/dbal` | 0.10 | — | DBAL Enqueue transport |
| `enqueue/enqueue-bundle` | 0.10 | — | Enqueue bundle |
| `enqueue/redis` | 0.10 | — | Redis Enqueue transport |
| `sroze/messenger-enqueue-transport` | 0.4 | — | Messenger Enqueue transport adapter |
| `nyholm/psr7` | 1.0 | — | PSR-7 HTTP message implementation |
| `open-telemetry/opentelemetry-logger-monolog` | 1.0 | — | OpenTelemetry Monolog handler |
| `pentatrion/vite-bundle` | 6.5 | — | Vite bundle configuration |
| `frosh/code-quality-meta` | 0.1–0.5 | `code-quality` | vendor-bin: cs-fixer, phpstan, rector |
| `frosh/devenv-meta` | 0.1–0.3 | `devenv` | Nix/devenv.sh: .envrc, devenv.nix, devenv.yaml |

---

## Configuring the Flex endpoint

```json
{
    "extra": {
        "symfony": {
            "endpoint": [
                "https://raw.githubusercontent.com/shopware/recipes/flex/main/index.json",
                "flex://defaults"
            ]
        }
    }
}
```

Order: Shopware recipes first, then the Symfony standard server.
