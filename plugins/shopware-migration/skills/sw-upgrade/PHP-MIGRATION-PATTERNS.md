# Shopware 6 — PHP migration patterns

Typical PHP adjustments for a major upgrade:

- **Changed interfaces/signatures**: e.g. payment from the old sync/async interface to `AbstractPaymentHandler` (6.7);
  changed method signatures in core classes (check against `UPGRADE-6.7.md`).
- Replace **removed/deprecated APIs** (deprecation notices, `sw-deprecation-handling`).
- **Modern PHP features**: constructor property promotion, `readonly`, enums (ADR "php enums"), strict types.
- **composer.json**: `conflict` range to the target version (6.7 → `<6.7 || >=6.8`), audit dependencies/packages.

Approach: `vendor/bin/rector process` (Shopware set) for automatable changes, the rest manually; then PHPStan/ECS.
Details/audit in the references of the `shopware-6.7-migration` skill.

→ [../shopware-6.7-migration/`PHP-MIGRATION.md`](../shopware-6.7-migration/`PHP-MIGRATION.md`), [../shopware-6.7-migration/`PHP-MIGRATION-PATTERNS-COMPOSER-PACKAGES-AUDIT.md`](../shopware-6.7-migration/`PHP-MIGRATION-PATTERNS-COMPOSER-PACKAGES-AUDIT.md`)
