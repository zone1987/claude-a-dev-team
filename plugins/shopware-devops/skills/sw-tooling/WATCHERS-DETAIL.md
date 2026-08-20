# Shopware 6 — Watchers & hot module replacement (complete reference)

Source: `guides/development/tooling/using-watchers.md`

## Overview

When developing with Shopware, JavaScript changes normally require build commands for the administration or the storefront. HMR (hot module replacement) makes it possible to load and preview changes automatically.

**Important**: HMR watchers do not replace the final build process once development is finished.

## Building JS/CSS (regular build)

### Source code (composer run)

```bash
# Administration:
composer run build:js:admin

# Storefront:
composer run build:js:storefront
```

### Production template (shopware-cli)

```bash
# Administration:
shopware-cli project admin-build

# Storefront:
shopware-cli project storefront-build
```

## Enabling hot module replacement

### Source code (Shopware source code repository)

```bash
# Administration:
composer run watch:admin

# Storefront (from Shopware 6.7.11.0):
composer run storefront:dev-server

# Storefront (before Shopware 6.7.11.0):
composer run watch:storefront
```

### Production template (shopware-cli)

```bash
# Administration:
shopware-cli project admin-watch

# Storefront:
shopware-cli project storefront-watch
```

## Environment variables

Environment variables influence Shopware and therefore the watchers too. The Unix prefix syntax sets the variable for that command only.

### APP_ENV

```bash
# Production mode (no Symfony toolbar, no debug features):
APP_ENV=prod composer run watch:storefront

# Development mode (default):
# composer run watch:storefront  (APP_ENV=dev is the default)
```

- `APP_ENV=dev`: development mode — Symfony toolbar in the storefront, better error messages, query logging
- `APP_ENV=prod`: production mode — no debug tools, caching active

### IPV4FIRST

From NodeJS v17.0.0 on, IPv6 is preferred over IPv4. In some setups IPv6 can cause problems with watchers.

```bash
# Force IPv4 (NodeJS v17+):
IPV4FIRST=1 composer run watch:storefront
IPV4FIRST=1 composer run watch:admin
```

## Notes

1. Watchers suit **active development** — faster feedback
2. A **final build** is still required before deployment or plugin packaging
3. With `APP_ENV=dev` more resources are consumed
4. Watcher processes run in the foreground — for background execution: `&` or separate terminals
