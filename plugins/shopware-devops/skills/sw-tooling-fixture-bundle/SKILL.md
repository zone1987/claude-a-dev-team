---
name: sw-tooling-fixture-bundle
description: >
  Shopware Fixture Bundle — Testdaten und Demo-Daten in Shopware 6 laden.
  `#[Fixture]`-Attribut, `FixtureInterface`, priority/dependsOn/groups, Commands
  `fixture:load` / `fixture:list`, spezielle Loader (Theme, CustomField, Customer).
  Trigger: "fixture bundle shopware", "testdaten laden", "demodaten shopware",
  "fixture:load", "fixture:list", "FixtureInterface", "Fixture Attribut", "ThemeFixtureLoader",
  "CustomerFixtureLoader", "CustomFieldSetFixtureLoader", "shopware/fixture-bundle". Shopware 6.7.
---

# Shopware Fixture Bundle

```bash
composer require shopware/fixture-bundle:*
```

## Basis-Fixture

```php
#[Fixture(name: 'category', priority: 100, groups: ['catalog', 'test-data'])]
class CategoryFixture implements FixtureInterface
{
    public function __construct(
        #[Autowire(service: 'category.repository')]
        private readonly EntityRepository $categoryRepository,
    ) {}

    public function load(): void
    {
        $this->categoryRepository->create([
            ['id' => Uuid::randomHex(), 'name' => 'Electronics', 'active' => true],
        ], Context::createDefaultContext());
    }
}
```

## `#[Fixture]`-Attribut

| Parameter | Default | Beschreibung |
|---|---|---|
| `priority` | `0` | Höherer Wert = frühere Ausführung |
| `dependsOn` | `[]` | Array von Fixture-Klassen, die zuerst laufen müssen |
| `groups` | `['default']` | Gruppenzugehörigkeit |

## Commands

```bash
bin/console fixture:load                  # alle Fixtures laden
bin/console fixture:load --group=test-data  # nur bestimmte Gruppe
bin/console fixture:list                  # Übersicht (Reihenfolge, Priority, Dependencies)
```

## Spezialisierte Loader

**ThemeFixtureLoader**: Theme-Einstellungen (Farben, Logo, Fonts) — automatisches Theme-Discovery und Recompilation.
**CustomFieldSetFixtureLoader**: Custom Field Sets + Custom Fields für Entities.
**CustomerFixtureLoader**: Kunden mit Adressen, Custom Fields (Email = unique identifier, upsert).

## Ausführungsreihenfolge

1. Dependencies (dependsOn) → immer zuerst
2. Priority (höher = früher)
3. Kreisabhängigkeiten → Exception

## Best Practices

- Idempotent gestalten (mehrfach ausführbar ohne Fehler/Duplikate)
- Eine Verantwortung pro Fixture-Klasse
- Dependency Injection statt Container-Fetch
- Gruppen nutzen: `test-data`, `demo-data`, `performance-test`

Vollständige Loader-Beispiele: `references/deep/fixture-bundle.md`.
