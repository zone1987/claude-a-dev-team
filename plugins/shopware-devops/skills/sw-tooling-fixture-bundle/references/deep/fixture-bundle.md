# Shopware Fixture Bundle (vollständige Referenz)

Quelle: `guides/development/tooling/fixture-bundle.md`

## Installation

```bash
composer require shopware/fixture-bundle:*
```

## Konzept

Das Fixture Bundle bietet einen flexiblen und organisierten Weg, Test- und Demo-Daten in Shopware 6 zu laden. Unterstützt:
- Dependency-Management zwischen Fixtures
- Priority-basierte Ausführungsreihenfolge
- Group-Filtering für selektives Laden

## Basis-Fixture anlegen

Klasse implementiert `FixtureInterface` und trägt das `#[Fixture]`-Attribut:

```php
<?php declare(strict_types=1);

namespace Swag\BasicExample\Test\Fixture;

use Shopware\Core\Framework\DataAbstractionLayer\EntityRepository;
use Shopware\Core\Framework\Test\TestCaseBase\Fixture;
use Shopware\Core\Framework\Test\TestCaseBase\FixtureInterface;
use Shopware\Core\Framework\Uuid\Uuid;
use Symfony\Component\DependencyInjection\Attribute\Autowire;

#[Fixture(name: 'category')]
class CategoryFixture implements FixtureInterface
{
    public function __construct(
        #[Autowire(service: 'category.repository')]
        private readonly EntityRepository $categoryRepository,
    ) {}

    public function load(): void
    {
        $categories = [
            ['id' => Uuid::randomHex(), 'name' => 'Electronics', 'active' => true],
            ['id' => Uuid::randomHex(), 'name' => 'Clothing', 'active' => true],
        ];

        $this->categoryRepository->create($categories, Context::createDefaultContext());
    }
}
```

## `#[Fixture]`-Attribut — Parameter

```php
#[Fixture(
    name: 'product',          // string: Name der Fixture
    priority: 50,             // int, default 0: Höher = früher ausgeführt
    dependsOn: [              // array: Klassen die zuerst laufen müssen
        CategoryFixture::class,
        ManufacturerFixture::class,
    ],
    groups: ['catalog', 'test-data']  // array, default ['default']: Gruppen
)]
```

## Commands

### Fixtures laden

```bash
# Alle Fixtures:
bin/console fixture:load

# Spezifische Gruppe:
bin/console fixture:load --group=test-data
bin/console fixture:load --group=demo-data
```

### Fixtures auflisten

```bash
bin/console fixture:list
```

Beispielausgabe:
```
Available Fixtures
==================

+-------+---------------------+----------+-----------------+---------------------+
| Order | Class               | Priority | Groups          | Depends On          |
+-------+---------------------+----------+-----------------+---------------------+
| 1     | CategoryFixture     | 100      | catalog, test-  | -                   |
| 2     | ManufacturerFixture | 90       | catalog         | -                   |
| 3     | ProductFixture      | 50       | catalog, test-  | CategoryFixture,    |
|       |                     |          | data            | ManufacturerFixture |
| 4     | CustomerFixture     | 0        | customers       | -                   |
+-------+---------------------+----------+-----------------+---------------------+

[OK] Found 4 fixture(s).
```

## Ausführungsreihenfolge

1. **Dependencies**: Wenn `dependsOn` deklariert → immer nach den Dependencies
2. **Priority**: Unter unabhängigen Fixtures höherer Wert = früher
3. **Kreisabhängigkeiten**: System wirft Exception bei Erkennung

## Spezialisierte Loader

### ThemeFixtureLoader

Für Theme-Einstellungen (Farben, Logo, Fonts). Automatisches Theme-Discovery und Recompilation. Änderungen nur bei Bedarf.

```php
#[Fixture(name: 'theme', groups: ['theme-config', 'branding'])]
class ThemeFixture implements FixtureInterface
{
    public function __construct(
        private readonly ThemeFixtureLoader $themeFixtureLoader
    ) {}

    public function load(): void
    {
        // Logo hochladen (einmalig, wird via File-Content dedupliziert)
        $logo = $this->mediaHelper->upload(
            __DIR__ . '/shop.png',
            $this->mediaHelper->getDefaultFolder(ThemeDefinition::ENTITY_NAME)->getId()
        );

        $this->themeFixtureLoader->apply(
            (new ThemeFixtureDefinition('Shopware default theme'))
                ->config('sw-color-brand-primary', '#ff6900')
                ->config('sw-border-radius-default', '8px')
                ->config('sw-font-family-base', '"Inter", sans-serif')
                ->config('sw-logo-desktop', $logo)
        );
    }
}
```

### CustomFieldSetFixtureLoader

Custom Field Sets und ihre Custom Fields für Entities erstellen und verwalten:

```php
#[Fixture(name: 'custom-field')]
class CustomFieldFixture implements FixtureInterface
{
    public function __construct(
        private readonly CustomFieldSetFixtureLoader $customFieldSetFixtureLoader
    ) {}

    public function load(): void
    {
        $this->customFieldSetFixtureLoader->apply(
            (new CustomFieldSetFixtureDefinition('Product Specifications', 'product_specs'))
                ->relation('product')
                ->field(
                    (new CustomFieldFixtureDefinition('weight', CustomFieldTypes::FLOAT))
                        ->label('en-GB', 'Weight (kg)')
                        ->label('de-DE', 'Gewicht (kg)')
                )
                ->field(
                    (new CustomFieldFixtureDefinition('warranty_period', CustomFieldTypes::INT))
                        ->label('en-GB', 'Warranty Period (months)')
                )
        );
    }
}
```

### CustomerFixtureLoader

Kunden mit Adressen, Custom Fields und anderen Eigenschaften erstellen.
Email-Adresse als eindeutiger Identifier — bestehende Kunden werden aktualisiert (Upsert).

```php
#[Fixture(name: 'customer', groups: ['customers', 'addresses'])]
class CustomerFixture implements FixtureInterface
{
    public function __construct(
        private readonly CustomerFixtureLoader $customerFixtureLoader
    ) {}

    public function load(): void
    {
        $this->customerFixtureLoader->apply(
            (new CustomerFixtureDefinition('max.mustermann@example.com'))
                ->firstName('Max')
                ->lastName('Mustermann')
                ->salutation('mr')
                ->password('password')
                ->defaultBillingAddress([
                    'firstName' => 'Max',
                    'lastName' => 'Mustermann',
                    'street' => 'Musterstraße 123',
                    'zipcode' => '12345',
                    'city' => 'Musterstadt',
                    'country' => 'DEU',
                ])
                ->addAddress('work', [
                    'firstName' => 'Max',
                    'street' => 'Office Street 789',
                    'zipcode' => '11111',
                    'city' => 'Business City',
                    'country' => 'DEU',
                ])
        );
    }
}
```

## Best Practices

- **Meaningful Names**: Klare, beschreibende Klassennamen
- **Gruppen nutzen**: `test-data`, `demo-data`, `performance-test`
- **Dependencies deklarieren**: Vorhersagbare Ausführungsreihenfolge
- **Single Responsibility**: Jede Fixture hat eine klare Verantwortung
- **Idempotentes Design**: Mehrfach ausführbar ohne Fehler oder Duplikate
- **Dependency Injection**: Services per Constructor injizieren (nicht aus Container fetchen)
