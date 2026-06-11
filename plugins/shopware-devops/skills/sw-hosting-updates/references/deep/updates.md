# Shopware 6 — Updates & Staging (Deep Reference)

Sources: `guides/hosting/installation-updates/performing-updates.md`, `guides/hosting/installation-updates/creating-a-staging-instance.md`, `guides/hosting/installation-updates/cluster-setup.md`

## Update types

| Type | Frequency | Attention needed |
|---|---|---|
| Minor/Patch | Monthly | Low — no breaking changes per Backwards Compatibility Promise |
| Major | Annually | High — breaking changes, review UPGRADE.md |

## Pre-update checklist

```bash
# 1. Check extension compatibility
shopware-cli project upgrade-check

# 2. Backup database and files

# 3. Enable maintenance mode
bin/console sales-channel:maintenance:enable --all
```

For major updates additionally:
- Update PHP version first (overlapping PHP support guaranteed)
- Review [UPGRADE.md](https://github.com/search?q=repo%3Ashopware%2Fshopware+UPGRADE-6)
- Update all extensions to latest before AND after Shopware update

## Update via CLI

### Local development

```bash
# 1. Update composer.json version constraint
# "shopware/core": "6.7.0.0"

# 2. Update dependencies
composer update --no-scripts

# 3. Update Symfony Flex recipes
composer recipes:update

# 4. Commit
git add composer.json composer.lock
git commit -m "Update Shopware to 6.7.0"
```

### Production server (after deploy)

```bash
bin/console sales-channel:maintenance:enable --all
bin/console system:update:prepare
bin/console system:update:finish
bin/console sales-channel:maintenance:disable --all
```

**Warning:** Only run on production after updated code is deployed. Migrations must match deployed code.

## Web updater

Available in Administration > Settings > System > Shopware Update.
Only for small instances — not recommended for production (timeouts, memory).

## Extension developer tools

- [Rector for Shopware](https://github.com/FriendsOfShopware/shopware-rector) — PHP code upgrades
- [Codemods](https://github.com/shopware/shopware/blob/trunk/src/Administration/Resources/app/administration/code-mods.js) — JS upgrades
- PHPStorm Twig Block Versioning plugin

## Security patches without upgrading

Install [Security Plugin](https://store.shopware.com/en/swag136939272659f/shopware-6-security-plugin.html) for patches without version upgrades.

For dependency-level vulnerabilities:
```bash
composer audit
composer update <dependency-name>
```

## Disable auto-update (cluster/production)

```yaml
shopware:
    auto_update:
        enabled: false
```

## Staging instance

### Setup phases

**Phase 1 — Create environment:**
1. Deploy code to staging server
2. Duplicate DB: `shopware-cli project dump --clean --anonymize --host ... --output shop.sql shopware`
3. Configure `.env` for staging:
   - Change `APP_URL` to staging domain
   - Use separate DB connection
   - Set `SHOPWARE_ES_INDEX_PREFIX` to unique prefix
   - Use separate Redis, do not share with live

**Phase 2 — Activate staging mode:**
```bash
./bin/console system:setup:staging --no-interaction --force
```

### staging.yaml configuration

```yaml
# config/packages/staging.yaml
shopware:
    staging:
        mailing:
            disable_delivery: true   # default: true
        storefront:
            show_banner: true
        administration:
            show_banner: true
        elasticsearch:
            check_for_existence: true
        sales_channel:
            domain_rewrite:
                - type: equal
                  match: https://my-live-store.com
                  replace: https://my-staging-store.com
                - type: prefix
                  match: https://my-live-store.com
                  replace: https://my-staging-store.com
                - type: regex
                  match: '/https?:\/\/(\w+)\.(\w+)$/m'
                  replace: 'http://$1-$2.local'
```

### What staging mode does

| What it does | What it does NOT do |
|---|---|
| Deletes apps with external connections | Does not duplicate installation |
| Resets instance ID | Does not copy DB or files |
| Disables email delivery | Does not modify live environment |
| Rewrites URLs to staging domain | |
| Checks ES indices don't exist | |
| Shows staging banner | |

### Protect staging environment

Apache:
```apache
SetEnvIf Request_URI /api noauth=1
<RequireAny>
Require env noauth
Require env REDIRECT_noauth
Require valid-user
</RequireAny>
```

Alternatives: Cloudflare Access, Azure Application Gateway, oauth2-proxy.

### Staging in Deployment Helper

```yaml
# .shopware-project.yml
deployment:
    staging:
        enabled: true
```

Or via env: `SHOPWARE_DEPLOYMENT_STAGING=1`

**Warning:** Never enable on production — it deletes apps and disables email.

## Cluster setup

```yaml
shopware:
    deployment:
        cluster_setup: true   # available since 6.5.6.0
```

This prevents local-only operations that can diverge node state.

### Shared directories in cluster

- S3 for media, themes, sitemap, assets, private files
- `var/services/` must be shared (installed service source files)

### Redis for cluster (5 recommended instances)

1. Session + Cart
2. cache.object
3. Lock + Increment storage
4. Number Ranges
5. Message Queue

Set `redis.clusters.cache_slots=1` in php.ini when using Redis cluster.

### Strong CPU recommendation

Prioritize CPU speed over core count for all servers (app, SQL, ES, Redis).
