# Shopware 6 — Installation & Docker (Deep Reference)

Sources: `guides/hosting/installation-updates/docker.md`, `guides/hosting/installation-updates/extension-management.md`

## Create new project

```bash
composer create-project shopware/production:6.6.7.0 <folder>
cd <folder>
composer require shopware/docker
```

## Dockerfile (multi-stage with FrankenPHP)

```dockerfile
#syntax=docker/dockerfile:1.4

ARG PHP_VERSION=8.3
FROM ghcr.io/shopware/docker-base:$PHP_VERSION-frankenphp AS base-image
FROM ghcr.io/shopware/shopware-cli:latest-php-$PHP_VERSION AS shopware-cli

FROM shopware-cli AS build

ADD . /src
WORKDIR /src

RUN --mount=type=secret,id=packages_token,env=SHOPWARE_PACKAGES_TOKEN \
    --mount=type=secret,id=composer_auth,dst=/src/auth.json \
    --mount=type=cache,target=/root/.composer \
    --mount=type=cache,target=/root/.npm \
    /usr/local/bin/entrypoint.sh shopware-cli project ci /src

FROM base-image AS final

COPY --from=build --chown=82 --link /src /var/www/html
```

**Recommended:** Pin to a sha256 digest. Set up Dependabot/Renovate for updates.

## Available Docker tags

- `ghcr.io/shopware/docker-base:8.3-frankenphp` — PHP 8.3 with FrankenPHP
- `ghcr.io/shopware/docker-base:8.3-frankenphp-otel` — with OpenTelemetry
- `ghcr.io/shopware/docker-base:8.3.12-frankenphp` — pinned patch version

FrankenPHP is preferred over Caddy/Nginx in containers (auto resource allocation, single process).

## Default PHP extensions in Docker image

`bcmath`, `gd`, `intl`, `mysqli`, `pdo_mysql`, `pcntl`, `sockets`, `bz2`, `gmp`, `soap`, `zip`, `ftp`, `ffi`, `opcache`, `redis`, `apcu`, `amqp`, `zstd`

## Docker environment variables

| Variable | Default | Description |
|---|---|---|
| `PHP_SESSION_HANDLER` | files | Set to `redis` for Redis sessions |
| `PHP_SESSION_SAVE_PATH` | (empty) | Set to `tcp://redis:6379` |
| `PHP_MAX_UPLOAD_SIZE` | 128m | PHP upload size limit |
| `PHP_MAX_EXECUTION_TIME` | 300 | Max execution time |
| `PHP_MEMORY_LIMIT` | 512m | Memory limit |
| `PHP_OPCACHE_VALIDATE_TIMESTAMPS` | 1 | Disable in production |
| `PHP_OPCACHE_MEMORY_CONSUMPTION` | 128 | OPcache memory |
| `PHP_OPCACHE_MAX_ACCELERATED_FILES` | 10000 | Increase to 20000+ |
| `FPM_PM` | dynamic | FPM process manager |
| `FPM_PM_MAX_CHILDREN` | 5 | Max FPM children |

## Docker volumes (local storage)

| Path | Content |
|---|---|
| `/var/www/html/files` | Invoices, private files |
| `/var/www/html/public/theme` | Theme files |
| `/var/www/html/public/media` | Images |
| `/var/www/html/public/thumbnail` | Thumbnails |
| `/var/www/html/public/sitemap` | Sitemap |

**Best practice:** Use S3 for all files — no volumes needed.

## Docker Compose example

```yaml
x-environment: &shopware
    build:
        context: .
    environment:
        DATABASE_URL: 'mysql://shopware:shopware@database/shopware'
        APP_URL: 'http://localhost:8000'
    volumes:
        - files:/var/www/html/files
        - theme:/var/www/html/public/theme
        - media:/var/www/html/public/media
        - thumbnail:/var/www/html/public/thumbnail
        - sitemap:/var/www/html/public/sitemap

services:
    database:
        image: mariadb:11.4

    init-perm:
        <<: *shopware
        user: "root"
        entrypoint: chown 82:82 /var/www/html/files /var/www/html/public/theme ...

    init:
        <<: *shopware
        entrypoint: ["php", "vendor/bin/shopware-deployment-helper", "run"]
        depends_on:
            database:
                condition: service_started

    web:
        <<: *shopware
        depends_on:
            init:
                condition: service_completed_successfully
        ports:
            - 8000:8000

    worker:
        <<: *shopware
        entrypoint: ["php", "bin/console", "messenger:consume", "async", "low_priority", "--time-limit=300", "--memory-limit=512M"]
        deploy:
            replicas: 3

    scheduler:
        <<: *shopware
        entrypoint: ["php", "bin/console", "scheduled-task:run"]
```

## Custom PHP extensions

```dockerfile
USER root
RUN install-php-extensions tideways
USER www-data
```

## Custom Nginx config in container

- `.conf` → added to `http` block
- `.inc` → added to `server` block

Place at `/etc/nginx/conf.d/`.

## Extension management via Composer

```bash
# Authenticate with Shopware registry
composer config repositories.shopware-packages '{"type": "composer", "url": "https://packages.shopware.com"}'
composer config bearer.packages.shopware.com <your-token>

# Install and activate extension
composer require store.shopware.com/{extension-name}
bin/console plugin:install --activate <extension-name>

# Migrate existing extension to Composer
composer require store.shopware.com/{extension-name}
rm -rf custom/plugins/{extension-name}
bin/console plugin:refresh
```

## Enable authoritative class map (all plugins via Composer)

```json
{
    "config": {
        "optimize-autoloader": true,
        "classmap-authoritative": true
    }
}
```

```bash
composer dump-autoload
```

## Disable runtime extension management (cluster)

```yaml
# config/packages/z-shopware.yaml
shopware:
    deployment:
        runtime_extension_management: false
```

## Composer plugin loader

```dotenv
COMPOSER_PLUGIN_LOADER=1
```

Use with `bin/console plugin:install --activate <name>` during deployment.

## Health Check

```
GET /api/_info/health-check  → 200 OK when healthy
```

Docker HEALTHCHECK:
```dockerfile
HEALTHCHECK CMD curl --fail http://localhost/api/_info/health-check || exit 1
```

## Nginx client_max_body_size adjustment

```dockerfile
USER root
RUN sed -i "s/client_max_body_size 128M/client_max_body_size 256M/" /etc/nginx/nginx.conf
USER www-data
```
