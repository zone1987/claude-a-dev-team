# Shopware 6 — PHP migration patterns

Typical PHP adjustments for a major upgrade:

- **Changed interfaces/signatures**: e.g. payment from the old sync/async interface to `AbstractPaymentHandler` (6.7);
  changed method signatures in core classes (check against `UPGRADE-6.7.md`).
- Replace **removed/deprecated APIs** (deprecation notices, `sw-deprecation-handling`).
- **Modern PHP features**: constructor property promotion, `readonly`, enums (ADR "php enums"), strict types.
- **composer.json**: `conflict` range to the target version (6.7 → `<6.7 || >=6.8`), audit dependencies/packages.

Approach: `composer rector` (dry run) and `composer rector:fix` with the Shopware set of the version the plugin is
released for — never the next major's set — for automatable changes, the rest manually. Then `composer gate`: it is
the one command, running the fixers and every check (PHPStan, php-cs-fixer, Rector dry run, Stylelint, unit tests).
Every command runs in the container: `ddev exec bash -c "cd /var/www/html/shopware/custom/static-plugins/<PLUGIN-NAME> && composer gate"`.
Details/audit in the references of the `shopware-6.7-migration` skill.

→ [../shopware-6.7-migration/`PHP-MIGRATION.md`](../shopware-6.7-migration/`PHP-MIGRATION.md`), [../shopware-6.7-migration/`PHP-MIGRATION-PATTERNS-COMPOSER-PACKAGES-AUDIT.md`](../shopware-6.7-migration/`PHP-MIGRATION-PATTERNS-COMPOSER-PACKAGES-AUDIT.md`)
