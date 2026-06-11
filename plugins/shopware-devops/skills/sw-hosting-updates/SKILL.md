---
name: sw-hosting-updates
description: >
  Shopware 6 Updates durchführen — Minor, Major, Staging, Rollback, Security-Plugin.
  Triggers: "update shopware", "shopware update", "major update", "minor update", "security plugin",
  "update durchführen", "maintenance mode", "system:update", "shopware aktualisieren",
  "staging instance", "staging mode", "blue-green deployment", "UPGRADE.md"
---

# Shopware Hosting — Updates & Staging

Refer to `references/deep/updates.md` for full CLI sequences and staging configuration.

## Update via CLI (recommended)

### Local
```bash
# Edit composer.json version constraint, then:
composer update --no-scripts
composer recipes:update
git add composer.json composer.lock && git commit -m "Update Shopware to X.Y.Z"
```

### Production (after deploy)
```bash
bin/console sales-channel:maintenance:enable --all
bin/console system:update:prepare
bin/console system:update:finish
bin/console sales-channel:maintenance:disable --all
```

## Security-only updates
Install [Security Plugin](https://store.shopware.com/en/swag136939272659f/shopware-6-security-plugin.html) to receive patches without upgrading the full version.

## Staging instance
1. Deploy code to staging server, duplicate DB: `shopware-cli project dump --clean --anonymize ...`
2. Adjust `.env` (`APP_URL`, separate DB/Redis/ES index prefix)
3. Activate staging mode: `./bin/console system:setup:staging`

Configure `config/packages/staging.yaml` for banner, mail-disable, URL-rewrite.

## Check extension compatibility before update
```bash
shopware-cli project upgrade-check
```

See also: `sw-cli` (upgrade-check, project dump), `sw-hosting-deployment` (deployment-helper).

Full reference: `references/deep/updates.md`
