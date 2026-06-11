---
name: sw-paas
description: >
  Shopware PaaS — Platform.sh-basiertes Managed Hosting. Konfiguration via
  .platform/-Dateien (applications.yaml, services.yaml, routes.yaml), Build-Hook
  mit shopware-cli, Deploy-Hook mit deployment-helper, Mounts, Worker, Crons,
  sw-paas CLI. Trigger: "shopware paas", "sw-paas", "shopware platform.sh",
  "paas deploy", ".platform/applications.yaml", "paas-meta recipe",
  "shopware paas cli", "paas build hook", "paas worker".
---

# Shopware PaaS

Shopware PaaS basiert auf **Platform.sh**. Die Konfiguration wird via Symfony Flex
Recipe (`shopware/paas-meta`) ins Projekt eingespielt und besteht aus drei
`.platform/`-Dateien sowie Hilfsskripten.

```bash
# sw-paas CLI installieren
curl -L https://install.sw-paas-cli.shopware.systems | sh
sw-paas auth
```

```bash
# Recipe installieren
composer require shopware/paas-meta
```

## Konfigurations-Dateien

| Datei | Zweck |
|-------|-------|
| `.platform/applications.yaml` | App-Definition: PHP-Version, Hooks, Mounts, Worker, Crons |
| `.platform/services.yaml` | Services: MariaDB, Redis (Cache+Session), RabbitMQ, Network-Storage |
| `.platform/routes.yaml` | HTTP-Routing mit Cache-Policy |
| `config/packages/paas.yaml` | Symfony-Konfiguration: Redis-Session/Cache, Cluster-Mode |
| `.environment` | Shell-Env-Vars bei jedem Request (`APP_CACHE_DIR`) |
| `.shopware-project.yaml` | shopware-cli Projekt-Config: `deployment.cache.always_clear: true` |

## Build → Deploy → Post-Deploy

```
BUILD:    Node + shopware-cli installieren → shopware-cli project ci .
DEPLOY:   rsync cache/var aus Build → shopware-deployment-helper run → domain update
POST_DEPLOY: bin/console theme:compile --sync
```

## Vertiefung

- [references/deep/paas-config.md](references/deep/paas-config.md) — Vollständige applications.yaml, services.yaml, routes.yaml mit Erklärungen
- [references/deep/paas-workflow.md](references/deep/paas-workflow.md) — Deploy-Workflow, sw-paas CLI, Umgebungsvariablen
