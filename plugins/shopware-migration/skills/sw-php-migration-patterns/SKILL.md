---
name: sw-php-migration-patterns
description: >
  PHP-Migrationsmuster für Shopware-Plugins (6.6→6.7): geänderte Signaturen/Interfaces (z.B. neuer Payment-Handler),
  Constructor Property Promotion, Enums, entfernte/deprecierte APIs, composer conflict. Trigger: "PHP migration shopware",
  "Signatur geändert", "AbstractPaymentHandler migration", "deprecated API ersetzen", "php-migration shopware 6.7". Shopware 6.7.
---

# Shopware 6 — PHP-Migrationsmuster

Typische PHP-Anpassungen beim Major-Upgrade:

- **Geänderte Interfaces/Signaturen**: z.B. Payment vom alten Sync/Async-Interface zum `AbstractPaymentHandler` (6.7);
  geänderte Methodensignaturen in Core-Klassen (gegen `UPGRADE-6.7.md` prüfen).
- **Entfernte/deprecierte APIs** ersetzen (Deprecation-Notices, `sw-deprecation-handling`).
- **Moderne PHP-Features**: Constructor Property Promotion, `readonly`, Enums (ADR „php enums"), strikte Typen.
- **composer.json**: `conflict`-Range auf Zielversion (6.7 → `<6.7 || >=6.8`), Abhängigkeiten/Packages auditieren.

Vorgehen: `vendor/bin/rector process` (Shopware-Set) für automatisierbare Änderungen, Rest manuell; danach PHPStan/ECS.
Details/Audit in den References des Skills `shopware-6.7-migration`.

→ [../shopware-6.7-migration/references/php-migration.md](../shopware-6.7-migration/references/php-migration.md), [../shopware-6.7-migration/references/composer-packages-audit.md](../shopware-6.7-migration/references/composer-packages-audit.md)
