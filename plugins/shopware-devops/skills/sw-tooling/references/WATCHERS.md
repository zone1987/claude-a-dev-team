# Shopware 6 — Watchers & hot module replacement

## Building JS/CSS (without a watcher)

| Command | Purpose |
|---|---|
| `composer run build:js:admin` | Admin (source code) |
| `shopware-cli project admin-build` | Admin (production template) |
| `composer run build:js:storefront` | Storefront (source code) |
| `shopware-cli project storefront-build` | Storefront (production template) |

## Starting the watchers (HMR)

| Command | Purpose |
|---|---|
| `composer run watch:admin` | Admin watcher (source code) |
| `composer run storefront:dev-server` | Storefront watcher ≥ 6.7.11.0 |
| `composer run watch:storefront` | Storefront watcher < 6.7.11.0 |
| `shopware-cli project admin-watch` | Admin watcher (production template) |
| `shopware-cli project storefront-watch` | Storefront watcher (production template) |

Watchers **do not replace** the final build step!

## Environment variables

```bash
# Production mode (no Symfony toolbar in the storefront):
APP_ENV=prod composer run watch:storefront

# Fix IPv6 problems with NodeJS >= 17:
IPV4FIRST=1 composer run watch:storefront
```

- `APP_ENV=dev` → development mode: Symfony toolbar in the storefront, better error messages
- `APP_ENV=prod` → production mode: no debugging toolbar
- `IPV4FIRST=1` → NodeJS v17+ prefers IPv6; this flag forces IPv4
