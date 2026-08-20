# Shopware PaaS — Complete configuration reference

Source: `shopware/recipes` — the `shopware/paas-meta/6.7/` recipe (Platform.sh based).

---

## Contents

- [`.platform/applications.yaml` (complete, 6.7)](#platformapplicationsyaml-complete-67)
- [`.platform/services.yaml` (complete, 6.7)](#platformservicesyaml-complete-67)
- [`.platform/routes.yaml` (complete, 6.7)](#platformroutesyaml-complete-67)
- [`config/packages/paas.yaml` (complete, 6.7)](#configpackagespaasyaml-complete-67)
- [`.environment` (project root)](#environment-project-root)
- [`.shopware-project.yaml` (project root)](#shopware-projectyaml-project-root)
- [Platform.sh environment variables](#platformsh-environment-variables)
- [Mounts overview](#mounts-overview)

## `.platform/applications.yaml` (complete, 6.7)

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
            # Preserve files from mounts (the build phase has no access to mounts)
            mv $APP_CACHE_DIR ./RO-localCache
            mv ./var ./RO-var
        deploy: |
            set -e
            # Sync build artifacts into the mounts
            rsync -av --delete "${PLATFORM_APP_DIR}/RO-localCache/" "${APP_CACHE_DIR}/"
            rsync -av "${PLATFORM_APP_DIR}/RO-var/" "${PLATFORM_APP_DIR}/var/"
            # Create the Dompdf directories
            mkdir -p "${PLATFORM_APP_DIR}/var/dompdf/tempDir"
            mkdir -p "${PLATFORM_APP_DIR}/var/dompdf/fontCache"
            rsync -av "${PLATFORM_APP_DIR}/vendor/dompdf/dompdf/lib/fonts" \
              "${PLATFORM_APP_DIR}/var/dompdf/fontDir"
            # Run the deployment helper
            php vendor/bin/shopware-deployment-helper run \
              --skip-asset-install --skip-theme-compile
            # Non-production environments: update the sales channel domain
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

## `.platform/services.yaml` (complete, 6.7)

```yaml
db:
    type: mariadb:11.4
    disk: 2048

cacheredis:
    type: redis:7.2
    configuration:
        maxmemory_policy: volatile-lfu     # Cache: LFU for volatile keys

sessionredis:
    type: redis-persistent:7.2
    disk: 1024
    configuration:
        maxmemory_policy: allkeys-lru      # Sessions: LRU across all keys

rabbitmq:
    type: rabbitmq:3.13
    disk: 1024

# Optional (commented out):
# opensearch:
#     type: opensearch:2
#     disk: 256

fileshare:
    type: network-storage:2.0
    disk: 4096                             # Shared mounts for media, themes, etc.
```

**Service types:**
- `redis` — in-memory (no persistence, cache only)
- `redis-persistent` — persistent Redis (for sessions)
- `network-storage` — NFS mount, shared between app and worker

---

## `.platform/routes.yaml` (complete, 6.7)

```yaml
"https://{default}/":
    type: upstream
    id: shopware
    upstream: "app:http"
    cache:
        enabled: true
        cookies: ["/^ss?ess/"]     # Session cookies: sses, ssess
```

**`id: shopware`** — used in the deploy hook to determine the frontend URL:
```bash
FRONTEND_URL=$(echo $PLATFORM_ROUTES | base64 --decode | jq -r 'to_entries[] | select(.value.id=="shopware") | .key')
```

---

## `config/packages/paas.yaml` (complete, 6.7)

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
        enable_admin_worker: false        # Admin worker disabled (dedicated worker container)
        enable_queue_stats_worker: false
    deployment:
        cluster_setup: true               # Cluster mode for multi-container
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
            path: php://stderr            # Logs to stderr (Platform.sh collects stderr)
            level: debug
            formatter: monolog.formatter.json
        console:
            type: console
            process_psr_3_messages: false
            channels: ["!event", "!doctrine"]

elasticsearch:
    index_settings:
        number_of_replicas: null          # Platform.sh manages replication
        number_of_shards: null
```

---

## `.environment` (project root)

```bash
export APP_CACHE_DIR=$PLATFORM_APP_DIR/localCache
```

Sourced on every request and worker start. Points the cache path at the local (not shared) mount for better performance.

---

## `.shopware-project.yaml` (project root)

```yaml
deployment:
    cache:
        always_clear: true
```

Configures `shopware-cli project ci` so the cache is always cleared (required for cluster deployments).

---

## Platform.sh environment variables

| Variable | Description |
|----------|--------------|
| `PLATFORM_APP_DIR` | Absolute path to the app root (`/app`) |
| `PLATFORM_ENVIRONMENT_TYPE` | `production` or `development` |
| `PLATFORM_ROUTES` | JSON of all routes, base64 encoded |
| `PLATFORM_RELATIONSHIPS` | JSON of all service connections, base64 encoded |

**Relationship URLs are extracted via:** `PLATFORM_RELATIONSHIPS | base64 --decode | jq`.
Shopware understands `DATABASE_URL`, `CACHE_URL`, `SESSION_REDIS_URL` — these are filled automatically from `PLATFORM_RELATIONSHIPS` by Platform.sh magic.

---

## Mounts overview

| Mount | Type | Description |
|-------|-----|--------------|
| `/files` | network-storage (fileshare) | Documents, theme config |
| `/public/media` | network-storage (fileshare) | Product images |
| `/public/thumbnail` | network-storage (fileshare) | Generated thumbnails |
| `/public/theme` | network-storage (fileshare) | Compiled theme assets |
| `/public/sitemap` | network-storage (fileshare) | Sitemap XML files |
| `/var` | network-storage (fileshare) | Symfony var/ (shared, for clusters) |
| `/localCache` | local | Opcache/PHP cache (per container, fast) |
| `/localLog` | local | Local logs (not shared) |

**Critical:** the build phase has no access to mounts! Therefore:
```bash
# At the end of the build hook: move artifacts to RO-*
mv $APP_CACHE_DIR ./RO-localCache
mv ./var ./RO-var

# At the start of the deploy hook: copy them into the mounts with rsync
rsync -av --delete "${PLATFORM_APP_DIR}/RO-localCache/" "${APP_CACHE_DIR}/"
rsync -av "${PLATFORM_APP_DIR}/RO-var/" "${PLATFORM_APP_DIR}/var/"
```
