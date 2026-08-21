# Shopware Hosting — Server Requirements

Refer to the deep reference for the full recommended stack table and version details.

## Key facts

- **PHP**: min 8.2, recommended 8.4 — requires `memory_limit ≥ 512M`, `max_execution_time ≥ 30s`
- **MySQL/MariaDB**: MariaDB ≥ 10.11.6 or MySQL ≥ 8.0.22; recommended MariaDB 11.4 / MySQL 8.4
- **Node.js**: min 20, recommended Node 24 / npm 10
- **Web server**: Caddy (recommended), Nginx, Apache — or Symfony CLI for local dev
- **Search** (optional): OpenSearch ≥ 1.0 / Elasticsearch ≥ 7.8; recommended OpenSearch 2.17.1
- **Cache/KV** (optional): Redis v7+ / Valkey 8.0; `maxmemory-policy: volatile-lfu`
- **Queue** (optional): RabbitMQ or AWS SQS (default: SQL DB)

## Verification commands

```bash
php -v && php -m && php -i | grep memory_limit
composer -V && node -v && npm -v
```

See also: `sw-hosting-performance` (PHP config tweaks), `sw-paas` (managed environments).

## Shopware 6 — Server Requirements (Deep Reference)

Source: `guides/hosting/index.md`

### Recommended Stack

| Component | Minimum Version | Recommended | Notes |
|---|---|---|---|
| **PHP** | 8.2+ | 8.4 | `memory_limit ≥ 512M`, `max_execution_time ≥ 30s`. Required: `ctype`, `curl`, `dom`, `fileinfo`, `gd`, `iconv`, `intl`, `mbstring`, `openssl`, `pcre`, `pdo_mysql`, `phar`, `simplexml`, `xml`, `xmlreader`, `zip`, `zlib`. Optional: `amqp`. Composer 2.2+ recommended. |
| **SQL** | MariaDB ≥ 10.11.6 or MySQL ≥ 8.0.22 | MariaDB 11.4 / MySQL 8.4 | `max_allowed_packet ≥ 32M`. Innovation releases NOT supported. |
| **Node.js / npm** | Node 20.0.0+ | Node 24 / npm 10 | Required. |
| **Search** | OpenSearch 1.0+ or Elasticsearch 7.8+ | OpenSearch 2.17.1 | Optional. Admin search preview requires OpenSearch 2.12+ or ES 8.8+. OpenSearch 3.1 support added in 6.7.3.1 |
| **Cache/KV** | Redis v7+ | Valkey 8.0 | Optional. `maxmemory-policy: volatile-lfu` |
| **Web server** | Any | Caddy | Required. For local dev: Symfony CLI works out of the box. |
| **Queue** | Any Symfony Messenger transport | RabbitMQ | Optional. Default: SQL DB. |

### macOS note
If PHP installed via Homebrew, `intl` extension may not be included:
```bash
brew install php-intl
php -m | grep intl
```

### Verification commands
```bash
php -v                         # CLI PHP version
php -m                         # List PHP modules
php -i | grep memory_limit     # Check memory_limit
composer -V                    # Composer version
node -v                        # Node version
npm -v                         # npm version
```

### Multiple PHP versions note
On many systems, CLI and FPM may have different `php.ini` files. Always verify which binary is in use:
```bash
which php
php-fpm -v
```
