---
name: sw-rector
description: >
  Automatisierte Code-Modernisierung/Migration für Shopware-6-Plugins mit Rector: rector.php, Shopware-Rule-Set,
  PHP-Level-Upgrades, Deprecation-Fixes. Trigger: "Rector shopware", "rector.php", "Codemod shopware", "automatische Migration code",
  "rector process", "shopware-rector rules". Shopware 6.7.
---

# Shopware 6 — Rector

Rector transformiert Code automatisch (PHP-Versions-Upgrades, Shopware-Deprecation-Fixes, Codemods).

```php
// rector.php
return RectorConfig::configure()
    ->withPaths([__DIR__ . '/src'])
    ->withPhpSets()                 // PHP-Level-Modernisierung
    ->withSets([/* Shopware-Rector-Set (shopware/rector) */]);
```

```bash
vendor/bin/rector process --dry-run   # Vorschau
vendor/bin/rector process             # anwenden
```

Besonders nützlich bei **Major-Upgrades** (6.6→6.7→6.8): Shopware liefert Rector-Regeln für deprecierte APIs
(Plugin `shopware-migration` → `sw-deprecation-handling`). Ergebnis danach mit ECS/PHPStan prüfen.
