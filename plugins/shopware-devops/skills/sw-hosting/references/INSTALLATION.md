# Shopware Hosting — Installation & Docker

Refer to `INSTALLATION-DETAIL.md` for full Docker Compose examples, Dockerfile, and extension management details.

## New project

```bash
composer create-project shopware/production <folder>
cd <folder>
composer require shopware/docker
```

## Docker image

```dockerfile
ARG PHP_VERSION=8.3
FROM ghcr.io/shopware/docker-base:$PHP_VERSION-frankenphp AS base-image
FROM ghcr.io/shopware/shopware-cli:latest-php-$PHP_VERSION AS shopware-cli

FROM shopware-cli AS build
ADD . /src
WORKDIR /src
RUN --mount=type=secret,id=packages_token,env=SHOPWARE_PACKAGES_TOKEN \
    --mount=type=cache,target=/root/.composer \
    --mount=type=cache,target=/root/.npm \
    /usr/local/bin/entrypoint.sh shopware-cli project ci /src

FROM base-image AS final
COPY --from=build --chown=82 --link /src /var/www/html
```

Recommended tag: `ghcr.io/shopware/docker-base:8.3-frankenphp` (FrankenPHP preferred over Nginx/Caddy for containers).

## Extension management via Composer

```bash
composer config repositories.shopware-packages '{"type": "composer", "url": "https://packages.shopware.com"}'
composer config bearer.packages.shopware.com <your-token>
composer require store.shopware.com/{extension-name}
bin/console plugin:install --activate <extension-name>
```

Enable read-only admin Extension Manager:
```yaml
# config/packages/z-shopware.yaml
shopware:
    deployment:
        runtime_extension_management: false
```

Enable Composer plugin loader (cluster setups):
```dotenv
COMPOSER_PLUGIN_LOADER=1
```

See also: `sw-hosting-deployment` (deployment-helper), `sw-cli` (shopware-cli CI command).

Full reference: `INSTALLATION-DETAIL.md`
