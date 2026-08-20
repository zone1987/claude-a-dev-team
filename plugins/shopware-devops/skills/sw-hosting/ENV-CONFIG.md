# Shopware Hosting — Environment & Configuration

Refer to `ENV-CONFIG-DETAIL.md` for the complete environment variables table.

## Key environment variables

```dotenv
APP_ENV=prod
APP_SECRET=<openssl rand -hex 32>
INSTANCE_ID=<openssl rand -hex 32>
APP_URL=https://myshop.com
DATABASE_URL=mysql://user:pass@host:3306/shopware
MAILER_DSN=smtp://user:pass@smtp.example.com:587

# Optional
BLUE_GREEN_DEPLOYMENT=0
COMPOSER_PLUGIN_LOADER=1
SQL_SET_DEFAULT_SESSION_VARIABLES=0
APP_URL_CHECK_DISABLED=1
```

## Config structure

```text
config/
└── packages/
    ├── shopware.yaml          # global Shopware config
    ├── prod/
    │   ├── shopware.yaml      # production overrides
    │   └── monolog.yaml
    └── dev/
        └── ...
```

## Static System Config (since 6.6.4.0)

Lock system config values and make them non-editable in Admin:

```yaml
# config/packages/z-shopware.yaml
shopware:
    system_config:
        default:
            core.listing.allowBuyInListing: true
        0188da12724970b9b4a708298259b171:
            core.listing.allowBuyInListing: false
```

With env variable:
```yaml
shopware:
    system_config:
        default:
            core.listing.allowBuyInListing: '%env(bool:ALLOW_BUY_IN_LISTING)%'
```

## Cluster setup flag

```yaml
# config/packages/shopware.yaml
shopware:
    deployment:
        cluster_setup: true
    auto_update:
        enabled: false
```

## Rate Limiter

```yaml
shopware:
    api:
        rate_limiter:
            login:
                enabled: false
            oauth:
                enabled: true
                policy: 'time_backoff'
                reset: '24 hours'
                limits:
                    - limit: 3
                      interval: '10 seconds'
                    - limit: 5
                      interval: '60 seconds'
```

See also: `sw-hosting-performance` (env.local.php), `sw-hosting-observability` (logging/OpenTelemetry).

Full reference: `ENV-CONFIG-DETAIL.md`
