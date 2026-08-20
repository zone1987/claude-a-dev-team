# Shopware Fixture Bundle (complete reference)

Source: `guides/development/tooling/fixture-bundle.md`

## Contents

- [Installation](#installation)
- [Concept](#concept)
- [Creating a basic fixture](#creating-a-basic-fixture)
- [`#[Fixture]` attribute — parameters](#fixture-attribute--parameters)
- [Commands](#commands)
- [Execution order](#execution-order)
- [Specialized loaders](#specialized-loaders)
- [Best practices](#best-practices)

## Installation

```bash
composer require shopware/fixture-bundle:*
```

## Concept

The Fixture Bundle offers a flexible and organized way to load test and demo data into Shopware 6. It supports:
- Dependency management between fixtures
- Priority-based execution order
- Group filtering for selective loading

## Creating a basic fixture

The class implements `FixtureInterface` and carries the `#[Fixture]` attribute:

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

## `#[Fixture]` attribute — parameters

```php
#[Fixture(
    name: 'product',          // string: name of the fixture
    priority: 50,             // int, default 0: higher = executed earlier
    dependsOn: [              // array: classes that must run first
        CategoryFixture::class,
        ManufacturerFixture::class,
    ],
    groups: ['catalog', 'test-data']  // array, default ['default']: groups
)]
```

## Commands

### Loading fixtures

```bash
# All fixtures:
bin/console fixture:load

# A specific group:
bin/console fixture:load --group=test-data
bin/console fixture:load --group=demo-data
```

### Listing fixtures

```bash
bin/console fixture:list
```

Example output:
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

## Execution order

1. **Dependencies**: when `dependsOn` is declared → always after the dependencies
2. **Priority**: among independent fixtures, a higher value runs earlier
3. **Circular dependencies**: the system throws an exception when it detects one

## Specialized loaders

### ThemeFixtureLoader

For theme settings (colors, logo, fonts). Automatic theme discovery and recompilation. Changes only when needed.

```php
#[Fixture(name: 'theme', groups: ['theme-config', 'branding'])]
class ThemeFixture implements FixtureInterface
{
    public function __construct(
        private readonly ThemeFixtureLoader $themeFixtureLoader
    ) {}

    public function load(): void
    {
        // Upload the logo (once, deduplicated via the file content)
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

Create and manage custom field sets and their custom fields for entities:

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

Create customers with addresses, custom fields and other properties.
The email address is the unique identifier — existing customers are updated (upsert).

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

## Best practices

- **Meaningful names**: clear, descriptive class names
- **Use groups**: `test-data`, `demo-data`, `performance-test`
- **Declare dependencies**: predictable execution order
- **Single responsibility**: each fixture has one clear responsibility
- **Idempotent design**: repeatable without errors or duplicates
- **Dependency injection**: inject services via the constructor (do not fetch them from the container)
