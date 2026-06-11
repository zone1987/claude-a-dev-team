# Symfony Flex Recipes — Verfügbare Packages

Quelle: `github.com/shopware/recipes` (alle `manifest.json`-Dateien analysiert).

## Shopware-Packages

| Package | Versionen | Alias | Beschreibung |
|---------|-----------|-------|--------------|
| `shopware/core` | 6.4, 6.6, 6.7 | — | Kern-Scaffolding: bin/, config/, custom/, files/, public/, var/ |
| `shopware/administration` | 6.4, 6.6, 6.7 | — | Admin-Build-Skripte |
| `shopware/storefront` | 6.4, 6.6, 6.7 | — | Storefront-Build-Skripte |
| `shopware/elasticsearch` | 6.4, 6.6, 6.7 | — | OpenSearch/ES-Konfiguration |
| `shopware/platform` | 6.4, 6.6, 6.7 | — | Auto-Merge von core+admin+storefront+es (Legacy) |
| `shopware/docker` | 0.1, 0.2, 0.3 | — | Docker-Compose-Setup für Produktion |
| `shopware/docker-dev` | 0.1 | — | Docker-Compose + Makefile für Entwicklung |
| `shopware/dev-tools` | 1.0 | — | Aliases für Entwicklungs-Tools |
| `shopware/fastly-meta` | 6.4, 6.5, 6.6, 6.7, 6.8 | `fastly` | Fastly CDN: VCL-Snippets + Shopware-Konfiguration |
| `shopware/k8s-meta` | 1.0, 2.0 | `k8s` | Kubernetes-Konfiguration |
| `shopware/paas-meta` | 6.4, 6.5, 6.6, 6.7 | `paas` | Shopware PaaS (Platform.sh): .platform/, config/packages/paas.yaml |
| `shopware/opentelemetry` | 0.1 | — | OpenTelemetry-Konfiguration |
| `shopware/fixture-bundle` | 0.1 | — | Fixture-Bundle-Registrierung |

### shopware/core — Kopierte Dateien (6.7)

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
- u.v.m.

**env (6.7):**
```
APP_ENV=prod
APP_URL=http://127.0.0.1:8000
APP_SECRET=%generate(secret)%
INSTANCE_ID=%generate(secret)%
DATABASE_URL=mysql://root:root@localhost/shopware
```

### shopware/paas-meta — Kopierte Dateien (6.7)

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

## Symfony-Packages

| Package | Versionen | Alias | Beschreibung |
|---------|-----------|-------|--------------|
| `symfony/framework-bundle` | 5.4, 6.4, 7.4 | — | Symfony Framework Basis-Konfiguration |
| `symfony/console` | 5.4 | — | Console-Component-Registrierung |
| `symfony/routing` | 5.4, 6.4, 7.4 | — | Routing-Konfiguration |
| `symfony/messenger` | 5.4, 6.0 | `messenger` | Messenger: config/packages/messenger.yaml |
| `symfony/amqp-messenger` | 5.4 | — | AMQP Messenger: docker-compose LavinMQ-Service |
| `symfony/monolog-bundle` | 3.3 | — | Monolog Logging-Konfiguration |
| `symfony/debug-bundle` | 5.3 | — | Debug-Bundle (nur dev-Env) |
| `symfony/mailer` | 4.3 | `mail`, `mailer` | Mailer: docker-compose.override Mailpit-Service |
| `symfony/twig-bundle` | 5.4 | — | Twig-Konfiguration |
| `symfony/translation` | 5.4 | — | Translation-Konfiguration |
| `symfony/validator` | 5.3 | — | Validator-Konfiguration |
| `symfony/lock` | 5.3 | — | Lock-Component |
| `symfony/scheduler` | 7.2 | — | Scheduler: src/Scheduler/ Stub |
| `symfony/property-info` | 7.3 | — | PropertyInfo-Konfiguration |
| `symfony/ux-twig-component` | 2.13 | — | Twig Components |

---

## Drittanbieter-Packages

| Package | Versionen | Alias | Beschreibung |
|---------|-----------|-------|--------------|
| `doctrine/annotations` | 1.0 | — | Annotations-Registrierung |
| `enqueue/dbal` | 0.10 | — | DBAL Enqueue Transport |
| `enqueue/enqueue-bundle` | 0.10 | — | Enqueue Bundle |
| `enqueue/redis` | 0.10 | — | Redis Enqueue Transport |
| `sroze/messenger-enqueue-transport` | 0.4 | — | Messenger Enqueue Transport-Adapter |
| `nyholm/psr7` | 1.0 | — | PSR-7 HTTP Message Implementierung |
| `open-telemetry/opentelemetry-logger-monolog` | 1.0 | — | OpenTelemetry Monolog Handler |
| `pentatrion/vite-bundle` | 6.5 | — | Vite Bundle Konfiguration |
| `frosh/code-quality-meta` | 0.1–0.5 | `code-quality` | vendor-bin: cs-fixer, phpstan, rector |
| `frosh/devenv-meta` | 0.1–0.3 | `devenv` | Nix/devenv.sh: .envrc, devenv.nix, devenv.yaml |

---

## Flex-Endpoint konfigurieren

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

Reihenfolge: Shopware-Recipes zuerst, dann Symfony-Standard-Server.
