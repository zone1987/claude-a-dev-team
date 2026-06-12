---
name: sw-paas-build-deploy
description: >
  Shopware PaaS (Platform.sh/Upsun) Build & Deploy: .platform/-Konfiguration,
  Build-Hook, Deploy-Hook, Post-Deploy, Mounts, Worker, Automatic Env Vars,
  shopware/paas-meta Recipe, Composer Auth, Rebuild triggern. Trigger:
  "paas build hook", "shopware paas deploy", ".platform/applications.yaml",
  "paas worker konfigurieren", "paas mounts", "paas environment variables auto",
  "shopware paas-meta", "paas build trigger", "upsun shopware", "platform.sh
  shopware build".
---

# Shopware PaaS (Platform.sh/Upsun) — Build & Deploy

> Dieser Skill bezieht sich auf das **klassische Shopware PaaS** (Platform.sh/Upsun),
> nicht auf PaaS Native. Für PaaS Native → `sw-paas-fundamentals`.

## Setup

```bash
# PaaS CLI installieren
curl -sfS https://cli.shopware.com/installer | php
shopware     # Erster Start → Browser-Login

# paas-meta Recipe installieren
composer require shopware/paas-meta

# PaaS Remote hinzufügen
shopware project:set-remote <PROJECT_ID>
git push shopware main
```

## .platform/-Konfiguration

| Datei | Zweck |
|-------|-------|
| `applications.yaml` | App: PHP-Version, Hooks, Mounts, Worker, Vars |
| `services.yaml` | DB, Redis, RabbitMQ, Network-Storage |
| `routes.yaml` | HTTP-Routing |

## Build → Deploy Ablauf

```
BUILD:        Konfiguration validieren → Docker-Image → Dependencies → Build-Hook
DEPLOY:       App-Requests halten → Filesysteme mounten → Deploy-Hook → Requests freigeben
POST_DEPLOY:  Nach Verbindungsaufnahme ausgeführt
```

## Automatische Umgebungsvariablen

```bash
DATABASE_URL=mysql://user:pass@database.internal:3306/main
MESSENGER_TRANSPORT_DSN=amqp://guest:guest@rabbitmq.internal:5672/%2f/messages
CACHE_DSN=redis://rediscache.internal:6379
OPENSEARCH_URL=http://opensearch.internal:9200
APP_URL=https://main-abc123.eu-5.platformsh.site
```

## Rebuild erzwingen (ohne Code-Änderung)

```bash
shopware variable:create --environment main --level environment \
  --prefix env --name REBUILD_DATE --value "$(date)" --visible-build true
shopware variable:update --environment main --value "$(date)" "env:REBUILD_DATE"
```

## Vertiefung

[references/deep/build-deploy.md](references/deep/build-deploy.md)
