---
name: sw-hosting-env-config
description: >
  Shopware 6 Environment-Konfiguration — .env, APP_SECRET, DATABASE_URL, Feature-Flags, Static System Config, shopware.yaml.
  Triggers: "environment variables", "env configuration", ".env shopware", "APP_SECRET",
  "DATABASE_URL", "APP_URL", "feature flags", "static system config", "shopware.yaml",
  "Umgebungsvariablen", "Konfiguration", "system_config", "BLUE_GREEN_DEPLOYMENT",
  "COMPOSER_PLUGIN_LOADER", "static system configuration", "config/packages"
---

# Shopware Hosting — Environment & Configuration

Refer to `references/deep/env-config.md` for the complete environment variables table.

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

Full reference: `references/deep/env-config.md`
