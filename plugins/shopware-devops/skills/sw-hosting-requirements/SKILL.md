---
name: sw-hosting-requirements
description: >
  Shopware 6 Server-Anforderungen, empfohlener Stack und Versionen.
  Triggers: "server requirements", "system requirements", "PHP version", "MariaDB version",
  "MySQL version", "Node version", "supported versions", "PHP extensions", "Servervoraussetzungen",
  "empfohlener Stack", "PHP-Anforderungen", "Systemvoraussetzungen"
---

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

Full reference: `references/deep/requirements.md`
