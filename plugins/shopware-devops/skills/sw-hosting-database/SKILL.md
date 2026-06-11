---
name: sw-hosting-database
description: >
  Shopware 6 Datenbank-Setup — MySQL/MariaDB Cluster, Read Replicas, ProxySQL, Reconnect, Redis-Konfiguration.
  Triggers: "database cluster", "read replica", "MySQL cluster", "ProxySQL", "database setup",
  "Datenbankcluster", "read-only replica", "DATABASE_REPLICA", "MySQL gone away",
  "FrankenPHP worker mode reconnect", "facile doctrine mysql come back", "Redis setup",
  "Redis Konfiguration", "Redis cluster", "Redis connections", "Valkey"
---

# Shopware Hosting — Database & Redis

Refer to `references/deep/database.md` for full MySQL and Redis configuration details.

## MySQL cluster

```dotenv
DATABASE_URL=mysql://user:pass@primary:3306/shopware
DATABASE_REPLICA_0_URL=mysql://user:pass@replica1:3306/shopware
DATABASE_REPLICA_1_URL=mysql://user:pass@replica2:3306/shopware
```

Set on MySQL server:
- `group_concat_max_len ≥ 320000`
- `sql_mode` must NOT contain `ONLY_FULL_GROUP_BY`
- Then set `SQL_SET_DEFAULT_SESSION_VARIABLES=0` in `.env`

ProxySQL is recommended as DB proxy instead of direct multi-host config.

## Reconnect for long-running workers (FrankenPHP)

```bash
composer require facile-it/doctrine-mysql-come-back
```

```dotenv
DATABASE_URL="mysql://user:pass@localhost:3306/db?wrapperClass=Facile\DoctrineMySQLComeBack\Doctrine\DBAL\Connection&driverOptions[x_reconnect_attempts]=3"
```

## Redis named connections (since 6.6.8.0)

```yaml
# config/packages/shopware.yaml
shopware:
    redis:
        connections:
            ephemeral:
                dsn: 'redis://host1:port/1'
            persistent:
                dsn: 'redis://host2:port/2?persistent=1'
```

### Redis data categories
| Data type | Eviction policy | Persistence |
|---|---|---|
| Cache (HTTP + object) | `volatile-lru` | none |
| Sessions | `allkeys-lru` | RDB + AOF |
| Cart, number-ranges, locks, increment | `volatile-lru` | RDB + AOF |

### Recommended 5-Redis setup (cluster)
1. Session + Cart
2. cache.object
3. Lock + Increment storage
4. Number Ranges
5. Message Queue

See also: `sw-hosting-performance`, `sw-hosting-caching-http`.

Full reference: `references/deep/database.md`
