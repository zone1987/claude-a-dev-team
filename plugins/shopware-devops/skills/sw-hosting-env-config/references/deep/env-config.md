# Shopware 6 — Environment & Configuration (Deep Reference)

Sources: `guides/hosting/configurations/shopware/environment-variables.md`, `guides/hosting/configurations/shopware/static-system-config.md`, `guides/hosting/configurations/index.md`, `guides/hosting/configurations/framework/`, `guides/hosting/infrastructure/rate-limiter.md`

## All environment variables

| Variable | Default | Description |
|---|---|---|
| `ADMIN_OPENSEARCH_URL` | (empty) | OpenSearch URL for administration |
| `APP_BUILD_DIR` | `{projectRoot}/var/cache` | Temp directory for cache folder creation (since 6.6.8.0) |
| `APP_CACHE_DIR` | `{projectRoot}/var/cache` | Cache storage directory (since 6.6.8.0) |
| `APP_ENV` | `prod` | Environment (prod/dev) |
| `APP_LOG_DIR` | `{projectRoot}/var/log` | Log directory (since 6.6.8.0) |
| `APP_SECRET` | (empty) | App secret: `openssl rand -hex 32` |
| `APP_URL` | (empty) | Public shop URL |
| `APP_URL_CHECK_DISABLED` | `false` | Disable self-URL validation check |
| `BLUE_GREEN_DEPLOYMENT` | `0` | Enable blue-green (requires SUPER privilege for DB triggers) |
| `COMPOSER_HOME` | `/tmp/composer` | Composer cache for Plugin Manager |
| `COMPOSER_PLUGIN_LOADER` | (empty) | When set (e.g. `1`): use Composer plugin loader instead of DB |
| `DATABASE_SSL_CA` | (empty) | Path to SSL CA file |
| `DATABASE_SSL_CERT` | (empty) | Path to SSL Cert file |
| `DATABASE_SSL_DONT_VERIFY_SERVER_CERT` | (empty) | Disable server cert verification |
| `DATABASE_SSL_KEY` | (empty) | Path to SSL Key file |
| `DATABASE_URL` | (empty) | MySQL DSN |
| `DATABASE_REPLICA_x_URL` | (empty) | Replica DSNs (0, 1, 2...) |
| `ENABLE_OPENSEARCH_FOR_ADMIN_API` | (empty) | Apply OpenSearch globally for Admin API (experimental, since 6.7.9.0) |
| `ENABLE_SERVICES` | `auto` | `auto`/`true`/`false` — enable Shopware Services |
| `FASTLY_API_KEY` | (empty) | Fastly CDN API key (keep secure!) |
| `INSTANCE_ID` | (empty) | Shop instance ID: `openssl rand -hex 32` |
| `LOCK_DSN` | `flock` | Symfony lock DSN |
| `MAILER_DSN` | `null://localhost` | Mailer DSN (Admin config overwrites) |
| `MESSENGER_TRANSPORT_DSN` | (empty) | Default async queue DSN |
| `MESSENGER_TRANSPORT_FAILURE_DSN` | (empty) | Failed messages queue DSN |
| `MESSENGER_TRANSPORT_LOW_PRIORITY_DSN` | (empty) | Low priority queue DSN |
| `OPENSEARCH_URL` | (empty) | OpenSearch/ES hosts (comma-separated) |
| `REDIS_PREFIX` | (empty) | Prefix for Redis keys |
| `REDIS_URL` | (empty) | Redis URL for caching and sessions |
| `SHOPWARE_ADMIN_ES_ENABLED` | (empty) | Enable ES for administration |
| `SHOPWARE_ADMIN_ES_INDEX_PREFIX` | `sw-admin` | Admin ES index prefix |
| `SHOPWARE_ADMIN_ES_INDEXING_BATCH_SIZE` | `1000` | Admin ES batch size (since 6.7.9.0) |
| `SHOPWARE_ADMIN_ES_REFRESH_INDICES` | (empty) | Refresh admin indices after indexing |
| `SHOPWARE_ADMIN_ES_THROW_EXCEPTION` | `1` | Throw on admin ES errors (`1`=yes, `0`=no) |
| `SHOPWARE_ADMINISTRATION_PATH_NAME` | `admin` | Custom admin path |
| `SHOPWARE_DBAL_TIMEZONE_SUPPORT_ENABLED` | `0` | Enable timezone support in DBAL |
| `SHOPWARE_DISABLE_UPDATE_CHECK` | (empty) | Disable auto update checks |
| `SHOPWARE_ES_ENABLED` | `0` | Enable ES for storefront |
| `SHOPWARE_ES_EXCLUDE_SOURCE` | `0` | Exclude source from ES |
| `SHOPWARE_ES_INDEX_PREFIX` | (empty) | ES index prefix |
| `SHOPWARE_ES_INDEXING_BATCH_SIZE` | `100` | ES indexing batch size |
| `SHOPWARE_ES_INDEXING_ENABLED` | `0` | Enable ES indexing |
| `SHOPWARE_ES_NGRAM_MAX_GRAM` | `5` | Max n-gram size |
| `SHOPWARE_ES_NGRAM_MIN_GRAM` | `4` | Min n-gram size |
| `SHOPWARE_ES_THROW_EXCEPTION` | `1` | Throw on ES errors |
| `SHOPWARE_ES_USE_LANGUAGE_ANALYZER` | `1` | Use language-specific analyzers |
| `SHOPWARE_HTTP_CACHE_ENABLED` | `1` | HTTP cache enabled |
| `SHOPWARE_HTTP_DEFAULT_TTL` | `7200` | HTTP cache default TTL (deprecated in 6.8) |
| `SQL_SET_DEFAULT_SESSION_VARIABLES` | (not set) | Skip MySQL session variable setup (set `0` after manual MySQL config) |
| `SHOPWARE_DEPLOYMENT_TIMEOUT` | `300` | Setup command timeout |
| `SHOPWARE_USAGE_DATA_CONSENT` | (empty) | `accepted` or `revoked` |

## Config file structure

```
<project-root>/
└── config/
    └── packages/
        ├── shopware.yaml           ← global Shopware config
        ├── cache.yaml              ← Symfony cache pools
        ├── lock.yaml               ← Symfony lock
        ├── redis.yml               ← session handler
        ├── storefront.yaml         ← storefront/theme settings
        ├── elasticsearch.yaml      ← ES index settings
        ├── prod/
        │   ├── shopware.yaml       ← production-specific overrides
        │   ├── monolog.yaml        ← production log levels
        │   └── framework.yaml      ← production framework settings
        ├── dev/
        │   └── ...
        └── staging.yaml            ← staging mode settings
```

## Minimal production .env

```dotenv
APP_ENV=prod
APP_SECRET=<openssl rand -hex 32>
INSTANCE_ID=<openssl rand -hex 32>
APP_URL=https://myshop.com
DATABASE_URL=mysql://user:pass@host:3306/shopware
SHOPWARE_HTTP_CACHE_ENABLED=1
MAILER_DSN=smtp://user:pass@smtp.example.com:587
```

## Static System Configuration (since 6.6.4.0)

Overwrite database-stored system config with YAML files. Config in `config/packages/` takes precedence. Overwridden keys are non-editable in Admin.

```yaml
# config/packages/z-shopware.yaml
shopware:
    system_config:
        default:
            core.listing.allowBuyInListing: true
            core.basicInformation.shopName: 'My Shop'
        # Sales channel specific:
        0188da12724970b9b4a708298259b171:
            core.listing.allowBuyInListing: false
```

With environment variable:
```yaml
shopware:
    system_config:
        default:
            core.listing.allowBuyInListing: '%env(bool:ALLOW_BUY_IN_LISTING)%'
```

Use cases:
- Fix config that should never be changed by users
- Different configs per environment without DB access
- Version-controlled system configuration

## Cluster configuration

```yaml
# config/packages/shopware.yaml
shopware:
    deployment:
        cluster_setup: true           # prevents local-only operations
    auto_update:
        enabled: false                # disable web updater
        runtime_extension_management: false  # disable admin extension manager
```

## Rate Limiter configuration

```yaml
shopware:
    api:
        rate_limiter:
            login:
                enabled: true
                policy: 'time_backoff'
                reset: '24 hours'
                limits:
                    - limit: 3
                      interval: '10 seconds'
                    - limit: 5
                      interval: '60 seconds'
            oauth:
                enabled: true
                policy: 'time_backoff'
                reset: '24 hours'
                limits:
                    - limit: 3
                      interval: '10 seconds'
```

Available limiters:
- `login` — Storefront customer auth
- `guest_login` — Guest after-order auth
- `oauth` — API/Admin auth
- `reset_password` — Customer password reset
- `user_recovery` — Admin user password recovery
- `contact_form` — Contact form

Per-identity limiters (since 6.7.10.0):
- `login_user` — per email
- `login_client` — per IP
- `oauth_user` — per username
- `oauth_client` — per IP

## Framework configurations

Configuration originates in [Symfony FrameworkBundle](https://symfony.com/doc/current/reference/configuration/framework.html).
See Symfony docs for full reference.

## SameSite protection

See `config/packages/framework/samesite-protection.md` for CSRF/SameSite cookie configuration.
