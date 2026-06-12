# Shopware PaaS (Platform.sh/Upsun) — Build & Deploy (Deep Reference)

Quellen: `products/paas/shopware-paas/build-deploy.md`,
`products/paas/shopware-paas/repository.md`,
`products/paas/shopware-paas/setup-template.md`,
`products/paas/shopware-paas/cli-setup.md`

> **Hinweis:** Platform.sh ist jetzt **Upsun**. Referenzen auf Platform.sh sind äquivalent.

---

## CLI Setup

```bash
# Installation
curl -sfS https://cli.shopware.com/installer | php

# SSH-Key (alternativ manuell in PaaS Console: My Profile → SSH Keys)
shopware     # Erster Start → Browser-Authentifizierung
```

---

## Repository-Einrichtung

### Neues Projekt

```bash
composer create-project shopware/production <folder-name>
cd <folder-name>
composer require shopware/paas-meta
```

### paas-meta Recipe aktualisieren

```bash
composer recipes:update
```

**Warnung:** Jedes Recipe-Update kann Breaking Changes enthalten! Manuell prüfen,
besonders bei `.platform`-Datei-Änderungen (z.B. local → service mount).

### Git-Remotes konfigurieren

```bash
# Projekt-ID ermitteln
shopware projects

# Remote hinzufügen
shopware project:set-remote <PROJECT_ID>

# Ergebnis: zwei Remotes
git remote -v
# origin   git@github.com:company/repo.git (fetch/push)
# shopware <paas-url>.git (fetch/push)
```

---

## Build & Deploy Prozess

### Deployment triggern

```bash
git add .
git commit -m "Applied new configuration"
git push -u shopware main
```

### Build-Schritte

| Phase | Aktion |
|-------|--------|
| Build | Konfiguration validieren |
| Build | Container-Image erstellen |
| Build | Dependencies installieren (Composer + Assets) |
| Build | Build-Hook ausführen |
| Deploy | App-Requests halten |
| Deploy | Laufende Container unmounten |
| Deploy | Filesysteme mounten |
| Deploy | Deploy-Hook ausführen |
| Deploy | Requests freigeben |

### Erstes Deployment

Shopware-CLI-Installer läuft automatisch, erstellt Admin-Account:

| Username | Password |
|----------|----------|
| `admin`  | `shopware` |

**Sofort nach Deployment Passwort ändern!**
`install.lock` nicht löschen — sonst läuft Installer erneut.

---

## Setup Template — .platform/applications.yaml

```yaml
name: app
type: php:8.3

# Umgebungsvariablen und Server-Settings
variables:
  env:
    N_PREFIX: /app/.global
    APP_ENV: prod
    # Custom Variables hier

# Lifecycle Hooks
hooks:
  build: |
    # Build-Phase: Filesystem ist schreibbar, keine Services verfügbar
    # Composer + shopware-cli + Assets bauen
  deploy: |
    # Deploy-Phase: Traffic ist gehalten, Services verfügbar
    # DB-Migrationen, Theme-Config, Cache leeren
    # MINIMIEREN — jede Sekunde = Downtime
  post_deploy: |
    # Nach Verbindungsaufnahme: Theme kompilieren etc.

# Service-Mapping
relationships:
  database: "db:mysql"
  cacheredis: "cacheredis:redis"
  rabbitmqqueue: "rabbitmq:rabbitmq"
  redissession: "redissession:redis"

# Schreibbare Verzeichnisse
mounts:
  # Local Mounts (pro Instanz)
  "/var/cache": { source: local, source_path: cache }
  "/var/log": { source: local, source_path: log }
  # Service Mounts (geteilt zwischen Instanzen)
  "/public/media": { source: service, service: fileshare, source_path: media }
  "/public/thumbnail": { source: service, service: fileshare, source_path: thumbnail }
  "/public/bundles": { source: service, service: fileshare, source_path: bundles }
  "/public/sitemap": { source: service, service: fileshare, source_path: sitemap }

# HTTP-Routing
web:
  locations:
    "/":
      root: "public"
      expires: 1h
      passthru: "/index.php"

# Worker-Konfiguration
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

## Automatische Umgebungsvariablen

Werden automatisch von Platform.sh gesetzt basierend auf `relationships`:

### Global

| Variable | Beispielwert |
|----------|-------------|
| `APP_SECRET` | `a3c45d78e91f2b3c4d5e...` |
| `APP_ENV` | `prod` |
| `APP_URL` | `https://main-abc123.eu-5.platformsh.site` |
| `MAILER_DSN` | `smtp://localhost:25` |

### Database

| Variable | Beispielwert |
|----------|-------------|
| `DATABASE_URL` | `mysql://user:password@database.internal:3306/main` |
| `DATABASE_REPLICA_0_URL` | `mysql://user:password@database-replica.internal:3306/main` |

### RabbitMQ

| Variable | Beispielwert |
|----------|-------------|
| `MESSENGER_TRANSPORT_DSN` | `amqp://guest:guest@rabbitmq.internal:5672/%2f/messages` |
| `MESSENGER_TRANSPORT_DSN_PREFIX` | `amqp://guest:guest@rabbitmq.internal:5672/%2f/` |

### Redis Cache

| Variable | Beispielwert |
|----------|-------------|
| `CACHE_DSN` | `redis://rediscache.internal:6379` |
| `CACHE_URL` | `redis://rediscache.internal:6379` |

### Redis Session

| Variable | Beispielwert |
|----------|-------------|
| `SESSION_REDIS_HOST` | `redissession.internal` |
| `SESSION_REDIS_PORT` | `6379` |
| `SESSION_REDIS_URL` | `redis://redissession.internal:6379` |

### OpenSearch/Elasticsearch

| Variable | Beispielwert |
|----------|-------------|
| `OPENSEARCH_URL` | `http://opensearch.internal:9200` |
| `ADMIN_OPENSEARCH_URL` | `http://opensearch.internal:9200` |
| `ELASTICSEARCH_URL` | `http://elasticsearch.internal:9200` |
| `ELASTICSEARCH_HOST` | `elasticsearch.internal` |
| `ELASTICSEARCH_PORT` | `9200` |

---

## Composer Authentication

```bash
# Shopware Plugin Store Auth für CI
shopware variable:create \
  --level project \
  --name env:COMPOSER_AUTH \
  --json true \
  --visible-runtime false \
  --sensitive true \
  --visible-build true \
  --value '{"bearer": {"packages.shopware.com": "<YOUR_TOKEN>"}}'
```

Token aus Shopware Account → "Install with Composer".

---

## Rebuild ohne Code-Änderung

```bash
# Variable erstellen (triggert sofortigen Build)
shopware variable:create \
  --environment main \
  --level environment \
  --prefix env \
  --name REBUILD_DATE \
  --value "$(date)" \
  --visible-build true

# Variable updaten (triggert erneuten Build)
shopware variable:update --environment main --value "$(date)" "env:REBUILD_DATE"
```

---

## Migration von altem Template

Von `shopwareArchive/paas` auf neues Flex-Template:

```bash
# Flex-Migration durchführen
# .platform.app.yml → .platform/applications.yaml
# Services umbenannt:
# queuerabbit → rabbitmq
# searchelastic → opensearch
```

Optionen bei Service-Umbenennung:
1. Services zurückbenennen
2. Neuen Service starten + ES reindexieren
3. Paralleler Betrieb beider Services während Übergangszeit

---

## files/theme-config

Theme-Konfiguration in Git committen (Empfehlung):
```text
files/
└─ theme-config/
   └─ ...
```

Ermöglicht Builds ohne Datenbank-Zugriff auf Theme-Konfiguration.
Details: [Build without Database](https://developer.shopware.com/docs/guides/hosting/installation-updates/deployments/build-w-o-db)
