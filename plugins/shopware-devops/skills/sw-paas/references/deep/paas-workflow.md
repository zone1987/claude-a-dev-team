# Shopware PaaS — Deploy-Workflow, sw-paas CLI und Umgebungsvariablen

## sw-paas CLI

### Installation

```bash
# Empfohlen: Installer
curl -L https://install.sw-paas-cli.shopware.systems | sh

# Spezifische Version
curl -L https://install.sw-paas-cli.shopware.systems | sh -s 0.0.57

# Manuell: Binary von GitHub Releases
# https://github.com/shopware/sw-paas/releases
chmod +x sw-paas_linux_amd64
mv sw-paas_linux_amd64 /usr/local/bin/sw-paas
```

**Installer-Verhalten:**
- Installiert nach `~/.sw-paas/bin/sw-paas`
- Fügt `SW_PAAS_INSTALL` und `PATH`-Erweiterung in `~/.zshrc` oder `~/.bash_profile` ein
- Respektiert `SW_PAAS_DIR`-Umgebungsvariable für Custom-Pfad

**Deinstallation:**
```bash
rm -rf ~/.sw-paas
# Dann aus Shell-Profil entfernen:
# export SW_PAAS_INSTALL="$HOME/.sw-paas"
# export PATH="$SW_PAAS_INSTALL/bin:$PATH"
```

### Unterstützte Plattformen
- macOS (Darwin): x86_64, arm64
- Linux: x86_64, arm64, i386

### Erstes Kommando nach Installation

```bash
sw-paas auth
```

Authentifiziert gegen die Shopware PaaS API.

---

## Vollständiger Deploy-Workflow

### 1. Projekt einrichten

```bash
# Neues Projekt mit PaaS-Konfig erstellen
shopware-cli project create my-shop latest --deployment shopware-paas --ci github

# ODER: PaaS zu bestehendem Projekt hinzufügen
composer require shopware/paas-meta
```

### 2. Lokale Entwicklung

```bash
# Entwicklung ohne PaaS
shopware-cli project admin-watch .
shopware-cli project storefront-watch .

# Lokalen Dump für Daten
shopware-cli project dump --clean --anonymize
```

### 3. Build-Phase (auf Platform.sh)

Platform.sh führt den `build`-Hook aus dem `applications.yaml` aus:

```
┌─────────────────────────────────────────────────────┐
│ BUILD HOOK (kein Netzwerk, kein Mount-Zugriff)       │
│                                                      │
│ 1. Node.js installieren (von nodejs.org CDN)         │
│ 2. shopware-cli installieren (von GitHub Releases)   │
│ 3. shopware-cli project ci . ausführen:             │
│    a. composer install --no-dev --optimize           │
│    b. Extension Assets bauen (Admin + Storefront)   │
│    c. Symfony Cache warmup                          │
│    d. assets:install                               │
│    e. MJML kompilieren (falls vorhanden)           │
│    f. Checksums generieren                         │
│ 4. localCache → RO-localCache sichern               │
│ 5. var/ → RO-var sichern                           │
└─────────────────────────────────────────────────────┘
```

**Wichtige Build-Umgebungsvariablen:**
```bash
export APP_CACHE_DIR=$PLATFORM_APP_DIR/localCache
export SHOPWARE_SKIP_ASSET_INSTALL_CACHE_INVALIDATION=1
```

### 4. Deploy-Phase (auf Platform.sh)

```
┌─────────────────────────────────────────────────────┐
│ DEPLOY HOOK (Netzwerk + Mounts verfügbar)            │
│                                                      │
│ 1. rsync RO-localCache → /localCache (Mount)        │
│ 2. rsync RO-var → /var (Mount)                      │
│ 3. Dompdf-Verzeichnisse anlegen                     │
│ 4. shopware-deployment-helper run:                  │
│    a. Datenbank-Migrationen                         │
│    b. Plugin-Updates                                │
│    c. Scheduled Tasks einrichten                    │
│    (--skip-asset-install --skip-theme-compile)      │
│ 5. Nicht-Prod: Sales-Channel-Domain aktualisieren   │
└─────────────────────────────────────────────────────┘
```

### 5. Post-Deploy-Phase

```
┌─────────────────────────────────────────────────────┐
│ POST_DEPLOY HOOK                                     │
│                                                      │
│ bin/console theme:compile --sync                    │
│ (nach allen Deploy-Hooks aller Instanzen)           │
└─────────────────────────────────────────────────────┘
```

### 6. Worker (permanent laufend)

```
┌─────────────────────────────────────────────────────┐
│ WORKER: queue                                        │
│                                                      │
│ pre_start:                                          │
│   export APP_CACHE_DIR=$PLATFORM_APP_DIR/localCache │
│   rm -rf $APP_CACHE_DIR/var                         │
│   php bin/console  (warm-up)                        │
│                                                      │
│ start:                                              │
│   bin/console messenger:consume async low_priority  │
│   failed                                           │
│   --memory-limit=<container-memory>M               │
│   --time-limit=295                                 │
└─────────────────────────────────────────────────────┘
```

### 7. Cron

```
*/5 * * * *   APP_CACHE_DIR=/app/localCache php bin/console scheduled-task:run --no-wait
```

---

## Elasticsearch/OpenSearch aktivieren

In `applications.yaml`:
```yaml
variables:
    env:
        SHOPWARE_ES_ENABLED: 1
        SHOPWARE_ES_INDEXING_ENABLED: 1
relationships:
    opensearch: "opensearch:opensearch"
```

In `services.yaml` auskommentieren:
```yaml
opensearch:
    type: opensearch:2
    disk: 256
```

---

## Multi-Environment (Staging vs. Produktion)

Der Deploy-Hook unterscheidet automatisch:

```bash
if [ "$PLATFORM_ENVIRONMENT_TYPE" != production ]; then
    # Staging/Dev: Sales-Channel-Domain auf aktuelle URL setzen
    export FRONTEND_URL=$(echo $PLATFORM_ROUTES | base64 --decode | \
      jq -r 'to_entries[] | select(.value.id=="shopware") | .key')
    export FRONTEND_DOMAIN=$(php -r 'echo parse_url($_SERVER["FRONTEND_URL"], PHP_URL_HOST);')
    bin/console sales-channel:update:domain "$FRONTEND_DOMAIN"
fi
```

---

## shopware-deployment-helper

`vendor/bin/shopware-deployment-helper` ist Teil von `shopware/deployment-helper` (Composer-Paket).

```bash
# Standard (mit Asset-Install und Theme-Compile)
php vendor/bin/shopware-deployment-helper run

# PaaS: Assets werden im Build-Hook installiert, Theme nach Deploy kompiliert
php vendor/bin/shopware-deployment-helper run \
  --skip-asset-install \
  --skip-theme-compile
```

**Was `deployment-helper run` macht:**
1. Datenbank-Migrationen ausführen
2. Plugin-Lifecycle (install/update/activate)
3. Scheduled Tasks registrieren
4. (Optional) Assets installieren
5. (Optional) Theme kompilieren

---

## Erstinstallation nach Deployment

```bash
# Nach erstem Push: Theme-Config-Dateien herunterladen
platform mount:download --mount 'files' --target 'files' -A app

# Diese Dateien committen und pushen, damit Theme korrekt kompiliert wird
git add files/theme-config/
git commit -m "chore: add initial theme config from PaaS"
git push
```

---

## Wichtige Umgebungsvariablen für PaaS

| Variable | Herkunft | Zweck |
|----------|----------|-------|
| `PLATFORM_APP_DIR` | Platform.sh | App-Root-Pfad (`/app`) |
| `PLATFORM_ENVIRONMENT_TYPE` | Platform.sh | `production` oder `development` |
| `PLATFORM_ROUTES` | Platform.sh | JSON aller Routes (base64) |
| `PLATFORM_RELATIONSHIPS` | Platform.sh | JSON aller Services (base64) |
| `APP_CACHE_DIR` | `.environment` | Lokaler Cache-Pfad (`/app/localCache`) |
| `APP_LOG_DIR` | `applications.yaml` | Log-Pfad (`/app/localLog`) |
| `NODE_VERSION` | `applications.yaml` | Node.js-Version für Build |
| `SHOPWARE_CLI_VERSION` | `applications.yaml` | shopware-cli-Version für Build |
| `SHOPWARE_HTTP_CACHE_ENABLED` | `applications.yaml` | HTTP-Cache aktivieren (→ Cache-Control-Header) |
| `SHOPWARE_SKIP_WEBINSTALLER` | `applications.yaml` | Web-Installer deaktivieren |
| `SHOPWARE_ES_ENABLED` | `applications.yaml` | OpenSearch aktivieren |
| `SHOPWARE_SKIP_ASSET_INSTALL_CACHE_INVALIDATION` | Build-Hook | Asset-Install-Cache-Invalidierung überspringen |
| `SW_PAAS_DIR` | Lokal | sw-paas CLI Install-Pfad |
