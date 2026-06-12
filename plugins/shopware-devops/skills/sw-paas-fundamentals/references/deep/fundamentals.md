# Shopware PaaS Native — Fundamentals (Deep Reference)

Quellen: `products/paas/shopware/fundamentals/` (account.md, organization.md, project.md,
applications.md, application-yaml.md, environment-variables.md, secrets.md,
php-settings.md, plugins-store-authentication.md, k8s-meta.md)

---

## 1. Account & Identity

```bash
sw-paas account whoami                     # Aktueller User + Rollen
sw-paas account whoami --output json | jq ".sub"  # Sub-ID ermitteln
sw-paas account context set               # Org+Project speichern
sw-paas account context show
sw-paas account context delete
```

Kontext gespeichert in `context-production.yaml`:

| OS     | Pfad |
|--------|------|
| Unix   | `~/.config/sw-paas` |
| macOS  | `~/Library/Application Support/sw-paas` |
| Windows| `%LOCALAPPDATA%` |

### Benutzer verwalten

```bash
sw-paas account user list
sw-paas account user add --sub "<sub-id>"
sw-paas account user remove
sw-paas account user request
sw-paas account user requests list
sw-paas account user requests resolve   # nur account-admin
```

### Service Accounts (CI/CD)

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
# Persönlicher Token
sw-paas account token create --name "ci-token"
export SW_PAAS_TOKEN=<token>
sw-paas --token <token> account whoami
sw-paas account token revoke --token-id abcd-1234

# Service Account Token
sw-paas account token create --service-account-id <id>
sw-paas account token list --service-account-id <id>
sw-paas account token revoke --service-account-id <id>
```

---

## 2. Organisationen

- Top-Level-Einheit (Firma/Entität)
- Langlebig, verfallen nicht automatisch
- Rollen: `read-only`, `developer`, `project-admin`, `account-admin`

```bash
sw-paas organization create
```

---

## 3. Projekte

- Repräsentieren ein Git-Repo (GitHub/GitLab/Bitbucket)
- Können viele Applications enthalten

```bash
sw-paas project create
sw-paas project list
```

---

## 4. Applications

### Ressourcen-Profil (Default)

| Komponente   | Replicas | CPU req | Memory req | Memory limit |
|--------------|----------|---------|------------|--------------|
| `storefront` | 2        | 50m     | 256Mi      | 2Gi          |
| `admin`      | 1        | 25m     | 128Mi      | 2Gi          |
| `worker`     | 1        | 50m     | 256Mi      | 1Gi          |

Skalierung primär horizontal. Limits abhängig vom gebuchten Plan.

### Application-Lifecycle

```bash
sw-paas application create
sw-paas application build start
sw-paas application build logs
sw-paas application update           # Build + Deploy (mit commit SHA)
sw-paas application deploy create    # Deploy eines spezifischen Builds
sw-paas application deploy list
sw-paas application deploy get
sw-paas application logs
sw-paas application deploy logs
```

### Deployment-Verhalten

- Zero-Downtime via Kubernetes Rolling Updates
- DB-Migrationen laufen **zuerst**
- Danach: [Deployment Helper](https://developer.shopware.com/docs/guides/hosting/installation-updates/deployments/deployment-helper)
- Pre/Post-Deployment Hooks über Deployment Helper konfigurierbar

### Befehle ausführen

```bash
sw-paas exec --new      # Interaktive Shell im Container (TTL: 1h)
sw-paas command create  # Nicht-interaktiv, eigener Container
```

### Domain-Verwaltung

Automatische `shopware.shop`-Domain bei Erstzustellung.

```bash
sw-paas domain create               # Custom Domain anlegen
```

DNS-Ziel: `cdn.shopware.shop` (CNAME für Subdomains).
Nach Domain-Anlage: `sw-paas application deploy create` nötig.

### Plugin-Management

**Nur via Composer** (kein UI-Plugin-Manager):
```bash
composer require vendor/plugin
```

Private Pakete via `COMPOSER_AUTH` Vault-Secret (`buildenv`).

---

## 5. application.yaml — Vollständige Referenz

```yaml
app:
  php:
    version: "8.3"              # PHP-Version
    extensions:                 # PHP-Erweiterungen (mlocati/docker-php-extension-installer)
      - imagick
  environment_variables:
    - name: MY_RUNTIME_VAR
      value: "runtime-value"
      scope: RUN                # RUN = Laufzeit
    - name: MY_BUILD_VAR
      value: "build-value"
      scope: BUILD              # BUILD = nur Build-Phase
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

## 6. Umgebungsvariablen — Priorität

| Quelle             | Priorität  |
|--------------------|------------|
| `.env`-Datei       | Niedrigste |
| `application.yaml` | Mittel     |
| Vault Secrets      | Höchste    |

---

## 7. Vault Secrets

Secrets sind organisationsweit gültig und wiederverwendbar.

```bash
sw-paas vault create                        # Interaktiv
sw-paas vault create --type env --key NAME  # Runtime-Variable
sw-paas vault create --type buildenv --key NAME  # Build-Variable
sw-paas vault create --type ssh             # SSH-Schlüsselpaar generieren
sw-paas vault list
sw-paas vault get --secret-id SECRET-ID
sw-paas vault delete --secret-id SECRET-ID
sw-paas vault edit                          # Existierenden Secret bearbeiten
```

### System-verwaltete Secrets (NICHT löschen!)

| Secret | Zweck |
|--------|-------|
| `STOREFRONT_CREDENTIALS` | Storefront-Authentifizierung |
| `GRAFANA_CREDENTIALS` | Grafana-Zugang |
| `NATS_USER_CREDENTIALS` | NATS-Messaging |
| `STOREFRONT_PROXY_KEY` | Routing |

### User-verwaltete Secrets

| Secret | Typ | Zweck |
|--------|-----|-------|
| `SSH_PRIVATE_KEY` | ssh | Git-Deployment |
| `SHOPWARE_PACKAGES_TOKEN` | buildenv | Shopware Plugin Store |
| `COMPOSER_AUTH` | buildenv | Third-Party Repos |

### COMPOSER_AUTH Format

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

### Housekeeping / Best Practices

```bash
# Vor Löschung sichern
sw-paas vault get --secret-id SECRET-ID > $(date +%Y%m%d)-backup.txt

# Audit
sw-paas vault list --application-id YOUR-APP-ID
```

- Kein Versions-History — Änderungen sind permanent
- Regelmäßige Rotation empfohlen (alle 90 Tage)

---

## 8. PHP-Einstellungen

Via Umgebungsvariablen konfigurierbar:

| Variable | PHP-Einstellung |
|----------|----------------|
| `PHP_MAX_UPLOAD_SIZE` | `upload_max_filesize` + `post_max_size` |
| `PHP_MAX_EXECUTION_TIME` | `max_execution_time` |

Basis-Image: [shopware/docker](https://github.com/shopware/docker)
Alle Parameter: [docker.ini](https://github.com/shopware/docker/blob/main/fpm/rootfs/usr/local/etc/php/conf.d/docker.ini)

**Nicht überschreiben:** `PHP_SESSION_HANDLER` (plattformseitig verwaltet)

---

## 9. Plugin Store Authentication

```bash
# Shopware Plugin Store (meist automatisch erstellt)
sw-paas vault create --type buildenv --key SHOPWARE_PACKAGES_TOKEN

# Third-Party Store
sw-paas vault create --type buildenv --key COMPOSER_AUTH
```

---

## 10. k8s-meta Package

Bereitet Shopware für PaaS Native vor.

| Shopware | k8s-meta |
|----------|----------|
| 6.6      | `^1.0`   |
| 6.7      | `^2.0`   |

```bash
composer require shopware/k8s-meta --ignore-platform-reqs
```

### Installierte Konfiguration

`config/packages/operator.yaml` konfiguriert:
- **S3 Object Storage** (public/private/theme/sitemap Filesysteme)
- **Redis** (Application Cache + Session)
- **Cluster Mode** (`cluster_setup: true`, `runtime_extension_management: false`)
- **Admin Worker** deaktiviert (externe Queue-Verarbeitung)
- **Elasticsearch/OpenSearch** Replica/Shard-Einstellungen
- **Monolog** → stderr als JSON

`config/packages/prod/`:
| Datei | Zweck |
|-------|-------|
| `fastly.yaml` | Fastly CDN Reverse Proxy + Cache Purging |
| `monolog.yaml` | Error-Level Logging → stderr JSON |
| `opentelemetry.yaml` | OpenTelemetry Profiler |

### Konfiguration überschreiben

```yaml
# config/packages/prod/shopware.yaml
shopware:
    http_cache:
        stale_while_revalidate: 300
        stale_if_error: 3600
```

**Warnung:** Default-Config ist für PaaS-Infra optimiert — nur mit Bedacht ändern.
