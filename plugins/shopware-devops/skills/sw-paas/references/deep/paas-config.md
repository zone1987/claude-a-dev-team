# Shopware PaaS — Vollständige Konfigurations-Referenz

Quelle: `shopware/recipes` — `shopware/paas-meta/6.7/`-Recipe (Platform.sh-basiert).

---

## `.platform/applications.yaml` (vollständig, 6.7)

```yaml
-   name: app
    type: php:8.4
    build:
        flavor: none
    variables:
        env:
            APP_ENV: prod
            SHOPWARE_HTTP_CACHE_ENABLED: 1
            NODE_VERSION: v22.17.0
            SHOPWARE_CLI_VERSION: 0.6.17
            SHOPWARE_ES_ENABLED: 0
            SHOPWARE_ES_INDEXING_ENABLED: 0
            SHOPWARE_ES_INDEX_PREFIX: "sw6"
            SHOPWARE_SKIP_WEBINSTALLER: 1
            COMPOSER_ROOT_VERSION: 1.0.0
            APP_LOG_DIR: /app/localLog
        php:
            upload_max_filesize: 32M
            post_max_size: 32M
            memory_limit: 512M
            "zend.assertions": -1
            "opcache.enable_file_override": 1
            "opcache.interned_strings_buffer": 20
            "opcache.validate_timestamps": 0
            "zend.detect_unicode": 0
            realpath_cache_ttl: 3600
            "opcache.memory_consumption": 128M
            "opcache.max_accelerated_files": 20000
    runtime:
        extensions:
            - ctype
            - dom
            - iconv
            - mbstring
            - fileinfo
            - intl
            - redis
            - sodium
            - amqp
    hooks:
        build: |
            set -e
            echo "Installing Node ${NODE_VERSION} and shopware-cli ${SHOPWARE_CLI_VERSION}"
            mkdir -p /tmp/tools
            curl -qL -s -o node.tar.xz "https://nodejs.org/dist/${NODE_VERSION}/node-${NODE_VERSION}-linux-x64.tar.xz"
            tar xf node.tar.xz -C /tmp/tools --strip-components=1
            curl -qL -s -o shopware-cli.tar.gz \
              https://github.com/shopware/shopware-cli/releases/download/${SHOPWARE_CLI_VERSION}/shopware-cli_Linux_x86_64.tar.gz
            tar xf shopware-cli.tar.gz -C /tmp/tools shopware-cli
            mv /tmp/tools/shopware-cli /tmp/tools/bin
            rm node.tar.xz shopware-cli.tar.gz
            export PATH="/tmp/tools/bin:$PATH"
            export APP_CACHE_DIR=$PLATFORM_APP_DIR/localCache
            export SHOPWARE_SKIP_ASSET_INSTALL_CACHE_INVALIDATION=1
            shopware-cli project ci .
            # Files aus Mounts sichern (Build-Phase hat keinen Zugriff auf Mounts)
            mv $APP_CACHE_DIR ./RO-localCache
            mv ./var ./RO-var
        deploy: |
            set -e
            # Build-Artefakte in Mounts synchronisieren
            rsync -av --delete "${PLATFORM_APP_DIR}/RO-localCache/" "${APP_CACHE_DIR}/"
            rsync -av "${PLATFORM_APP_DIR}/RO-var/" "${PLATFORM_APP_DIR}/var/"
            # Dompdf-Verzeichnisse anlegen
            mkdir -p "${PLATFORM_APP_DIR}/var/dompdf/tempDir"
            mkdir -p "${PLATFORM_APP_DIR}/var/dompdf/fontCache"
            rsync -av "${PLATFORM_APP_DIR}/vendor/dompdf/dompdf/lib/fonts" \
              "${PLATFORM_APP_DIR}/var/dompdf/fontDir"
            # Deployment-Helper ausführen
            php vendor/bin/shopware-deployment-helper run \
              --skip-asset-install --skip-theme-compile
            # Nicht-Produktions-Umgebungen: Sales-Channel-Domain aktualisieren
            if [ "$PLATFORM_ENVIRONMENT_TYPE" != production ]; then
                export FRONTEND_URL=$(echo $PLATFORM_ROUTES | base64 --decode | \
                  jq -r 'to_entries[] | select(.value.id=="shopware") | .key')
                export FRONTEND_DOMAIN=$(php -r 'echo parse_url($_SERVER["FRONTEND_URL"], PHP_URL_HOST);')
                bin/console sales-channel:update:domain "$FRONTEND_DOMAIN"
            fi
        post_deploy: |
            set -e
            php bin/console theme:compile --sync
    relationships:
        database: "db:mysql"
        rediscache: "cacheredis:redis"
        redissession: "sessionredis:redis"
        rabbitmqqueue: "rabbitmq:rabbitmq"
        # opensearch: "opensearch:opensearch"    # optional
    disk: 2048
    mounts:
        "/files":
            source: service
            service: fileshare
            source_path: "files"
        "/public/media":
            source: service
            service: fileshare
            source_path: "public/media"
        "/public/thumbnail":
            source: service
            service: fileshare
            source_path: "public/thumbnail"
        "/public/theme":
            source: service
            service: fileshare
            source_path: "public/theme"
        "/public/sitemap":
            source: service
            service: fileshare
            source_path: "public/sitemap"
        "/var":
            source: service
            service: fileshare
            source_path: "var"
        "/localCache":
            source: local
            source_path: "localCache"
        "/localLog":
            source: local
            source_path: "localLog"
    web:
        locations:
            "/":
                root: "public"
                passthru: "/index.php"
                expires: 24h
                rules:
                    \.(css|js|gif|jpe?g|png|ttf|eot|woff2?|otf|cast|mp4|json|yaml|ico|svg?)$:
                        expires: 4w
    workers:
        queue:
            disk: 128
            commands:
                pre_start: |
                    export APP_CACHE_DIR=$PLATFORM_APP_DIR/localCache
                    rm -rf $APP_CACHE_DIR/var
                    php $PLATFORM_APP_DIR/bin/console
                start: >
                    APP_CACHE_DIR=$PLATFORM_APP_DIR/localCache
                    bin/console messenger:consume async low_priority failed
                    --memory-limit=$(cat /run/config.json | jq .info.limits.memory)M
                    --time-limit=295
    crons:
        scheduler:
            spec: '*/5 * * * *'
            cmd: 'APP_CACHE_DIR=/app/localCache php bin/console scheduled-task:run --no-wait'
```

---

## `.platform/services.yaml` (vollständig, 6.7)

```yaml
db:
    type: mariadb:11.4
    disk: 2048

cacheredis:
    type: redis:7.2
    configuration:
        maxmemory_policy: volatile-lfu     # Cache: LFU für volatile keys

sessionredis:
    type: redis-persistent:7.2
    disk: 1024
    configuration:
        maxmemory_policy: allkeys-lru      # Sessions: LRU über alle keys

rabbitmq:
    type: rabbitmq:3.13
    disk: 1024

# Optional (auskommentiert):
# opensearch:
#     type: opensearch:2
#     disk: 256

fileshare:
    type: network-storage:2.0
    disk: 4096                             # Shared Mounts für Media, Themes, etc.
```

**Service-Typen:**
- `redis` — In-Memory (kein Persist, nur Cache)
- `redis-persistent` — Persistenter Redis (für Sessions)
- `network-storage` — NFS-Mount, shared zwischen App und Worker

---

## `.platform/routes.yaml` (vollständig, 6.7)

```yaml
"https://{default}/":
    type: upstream
    id: shopware
    upstream: "app:http"
    cache:
        enabled: true
        cookies: ["/^ss?ess/"]     # Session-Cookies: sses, ssess
```

**`id: shopware`** — wird im Deploy-Hook genutzt um die Frontend-URL zu ermitteln:
```bash
FRONTEND_URL=$(echo $PLATFORM_ROUTES | base64 --decode | jq -r 'to_entries[] | select(.value.id=="shopware") | .key')
```

---

## `config/packages/paas.yaml` (vollständig, 6.7)

```yaml
framework:
    session:
        handler_id: "%env(SESSION_REDIS_URL)%/0?persistent=1"
    cache:
        app: cache.adapter.redis
        system: cache.adapter.redis
        default_redis_provider: "%env(CACHE_URL)%/0?persistent=1"

shopware:
    admin_worker:
        enable_admin_worker: false        # Admin Worker deaktiviert (eigener Worker-Container)
        enable_queue_stats_worker: false
    deployment:
        cluster_setup: true               # Cluster-Modus für Multi-Container
    dompdf:
        options:
            tempDir: "%kernel.project_dir%/var/dompdf/tempDir"
            fontDir: "%kernel.project_dir%/var/dompdf/fontDir"
            fontCache: "%kernel.project_dir%/var/dompdf/fontCache"

monolog:
    handlers:
        main:
            type: fingers_crossed
            action_level: error
            handler: nested
            excluded_http_codes: [404, 405]
            buffer_size: 50
        nested:
            type: stream
            path: php://stderr            # Logs nach stderr (Platform.sh sammelt stderr)
            level: debug
            formatter: monolog.formatter.json
        console:
            type: console
            process_psr_3_messages: false
            channels: ["!event", "!doctrine"]

elasticsearch:
    index_settings:
        number_of_replicas: null          # Platform.sh verwaltet Replikation
        number_of_shards: null
```

---

## `.environment` (Projekt-Root)

```bash
export APP_CACHE_DIR=$PLATFORM_APP_DIR/localCache
```

Wird bei jedem Request und Worker-Start sourced. Setzt den Cache-Pfad auf lokalen (nicht geteilten) Mount für bessere Performance.

---

## `.shopware-project.yaml` (Projekt-Root)

```yaml
deployment:
    cache:
        always_clear: true
```

Konfiguriert `shopware-cli project ci` so dass der Cache immer geleert wird (nötig für Cluster-Deployments).

---

## Platform.sh Umgebungsvariablen

| Variable | Beschreibung |
|----------|--------------|
| `PLATFORM_APP_DIR` | Absoluter Pfad zum App-Root (`/app`) |
| `PLATFORM_ENVIRONMENT_TYPE` | `production` oder `development` |
| `PLATFORM_ROUTES` | JSON aller Routes, base64-encoded |
| `PLATFORM_RELATIONSHIPS` | JSON aller Service-Connections, base64-encoded |

**Relationship-URLs werden via:** `PLATFORM_RELATIONSHIPS | base64 --decode | jq` extrahiert.
Shopware versteht `DATABASE_URL`, `CACHE_URL`, `SESSION_REDIS_URL` — diese werden automatisch aus `PLATFORM_RELATIONSHIPS` befüllt via Platform.sh-Magic.

---

## Mounts-Übersicht

| Mount | Typ | Beschreibung |
|-------|-----|--------------|
| `/files` | network-storage (fileshare) | Dokumente, Theme-Config |
| `/public/media` | network-storage (fileshare) | Produkt-Bilder |
| `/public/thumbnail` | network-storage (fileshare) | Generierte Thumbnails |
| `/public/theme` | network-storage (fileshare) | Kompilierte Theme-Assets |
| `/public/sitemap` | network-storage (fileshare) | Sitemap-XML-Dateien |
| `/var` | network-storage (fileshare) | Symfony var/ (shared, für Cluster) |
| `/localCache` | local | Opcache/PHP-Cache (pro Container, schnell) |
| `/localLog` | local | Lokale Logs (nicht shared) |

**Kritisch:** Build-Phase hat keinen Zugriff auf Mounts! Deshalb:
```bash
# Am Ende des Build-Hooks: Artefakte nach RO-* verschieben
mv $APP_CACHE_DIR ./RO-localCache
mv ./var ./RO-var

# Am Anfang des Deploy-Hooks: Mit rsync in Mounts kopieren
rsync -av --delete "${PLATFORM_APP_DIR}/RO-localCache/" "${APP_CACHE_DIR}/"
rsync -av "${PLATFORM_APP_DIR}/RO-var/" "${PLATFORM_APP_DIR}/var/"
```
