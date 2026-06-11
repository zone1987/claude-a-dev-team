---
name: sw-phpstan-shopware
description: >
  PHPStan-Extension für Shopware-Plugins. Aktiviere wenn: phpstan-shopware, PHPStan-Regeln für Shopware,
  statische Analyse Shopware Plugin, shopwarelabs/phpstan-shopware, rules.neon einbinden,
  Shopware spezifische PHPStan Fehler verstehen oder beheben.
---

# sw-phpstan-shopware

Shopware-spezifische PHPStan-Erweiterung (`shopwarelabs/phpstan-shopware`).
Enthält ~27 Regeln für Sicherheit, DAL-Korrektheit, interne API-Schutz und Best Practices.

## Installation

```bash
composer require --dev shopwarelabs/phpstan-shopware
```

Die Regeln werden via `phpstan/extension-installer` **automatisch** eingebunden (kein manueller Include nötig, wenn `extra.phpstan.includes` in composer.json greift).

Ohne Extension-Installer manuell in `phpstan.neon` einbinden:

```yaml
includes:
    - vendor/shopwarelabs/phpstan-shopware/rules.neon
```

## Empfohlenes Level

Level **6–8** für Plugin-Entwicklung. Die Shopware-Regeln sind level-unabhängig und greifen auf allen Levels.

```yaml
parameters:
    level: 8
    paths:
        - src
```

## Was ist enthalten?

- 27 Regeln in `rules.neon` (automatisch geladen)
- 1 Type-Extension: `CollectionHasSpecifyingExtension` (verbessert Typinferenz bei `Collection::has()`)
- 2 Collectors: `DALDefinitionCollector`, `DALEntityCollector` (für DAL-Definition vs. Entity-Abgleich)

Vollständige Regelliste mit Beschreibung und Beispielen: `references/deep/rules.md`
