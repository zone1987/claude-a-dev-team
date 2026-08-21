# Shopware Fixture Bundle

```bash
composer require shopware/fixture-bundle:*
```

## Basic fixture

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

## `#[Fixture]` attribute

| Parameter | Default | Description |
|---|---|---|
| `priority` | `0` | Higher value = earlier execution |
| `dependsOn` | `[]` | Array of fixture classes that must run first |
| `groups` | `['default']` | Group membership |

## Commands

```bash
bin/console fixture:load                  # load all fixtures
bin/console fixture:load --group=test-data  # only a specific group
bin/console fixture:list                  # overview (order, priority, dependencies)
```

## Specialized loaders

**ThemeFixtureLoader**: theme settings (colors, logo, fonts) — automatic theme discovery and recompilation.
**CustomFieldSetFixtureLoader**: custom field sets + custom fields for entities.
**CustomerFixtureLoader**: customers with addresses, custom fields (email = unique identifier, upsert).

## Execution order

1. Dependencies (dependsOn) → always first
2. Priority (higher = earlier)
3. Circular dependencies → exception

## Best practices

- Design them to be idempotent (repeatable without errors/duplicates)
- One responsibility per fixture class
- Dependency injection instead of a container fetch
- Use groups: `test-data`, `demo-data`, `performance-test`

Complete loader examples: `FIXTURE-BUNDLE-DETAIL.md`.
