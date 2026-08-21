# Shopware 6 — Core Code Guidelines: Complete Reference

Sources: `resources/guidelines/code/core/` (all .md files)

---

## Contents

- [1. PHP Language Features (PHP 8.1+ / Shopware 6.5+)](#1-php-language-features-php-81--shopware-65)
- [2. Extendability Guidelines](#2-extendability-guidelines)
- [3. Decorator Pattern — Rules](#3-decorator-pattern--rules)
- [4. Domain Exceptions](#4-domain-exceptions)
- [5. Feature Flags](#5-feature-flags)
- [6. @final and @internal Annotation](#6-final-and-internal-annotation)
- [7. Database Migrations](#7-database-migrations)
- [8. Unit Tests](#8-unit-tests)
- [9. Writing Code for Static Analysis](#9-writing-code-for-static-analysis)
- [10. ADR Format](#10-adr-format)
- [References](#references)

## 1. PHP Language Features (PHP 8.1+ / Shopware 6.5+)

### Promoted Properties

```php
// Instead of:
class Point {
    private int $x;
    public function __construct(int $x) { $this->x = $x; }
}
// Better:
class Point {
    public function __construct(private int $x) {}
}
```

### Readonly Properties (DTOs)

```php
class ProductReindexCommand
{
    public function __construct(
        public readonly int $productId,
        public readonly bool $includeStock
    ) {}
}
```

### match instead of switch

```php
$message = match ($statusCode) {
    200, 300 => null,
    400 => 'not found',
    500 => 'server error',
    default => 'unknown status code',
};
```

Advantages: strict comparison, no fall-through, exhaustive, expression (returns a value).

### Enums

```php
enum IndexMethod { case PARTIAL; case FULL; }

class Indexer {
    public function product(int $id, IndexMethod $method): void {
        match ($method) {
            IndexMethod::PARTIAL => $this->partial($id),
            IndexMethod::FULL => $this->full($id)
        };
    }
}
```

Use enums instead of constant arrays; they are typable, have singleton semantics, and offer `from()`/`tryFrom()` for serialization.

### Native Types

- Union types: `int|string`
- Intersection types: `MyService&MockObject`
- `mixed` when the value really can be anything
- `never` for methods that never return (throw/exit)
- `@var/@param/@return` only for generics, array shapes, class strings, integer ranges, etc.

### First-Class Callable Syntax

```php
$longest = max(array_map(strlen(...), $strings)); // instead of 'strlen'
$callable = $object->doCoolStuff(...);
```

### Attributes instead of Annotations

```php
// Instead of a docblock annotation:
#[Route('/blog', name: 'blog_list')]
public function list(): Response { /* ... */ }

// Symfony DI without XML:
public function __construct(
    #[Autowire(service: 'email_adapter')]
    private Adapter $adapter,
    #[Autowire('%kernel.debug_mode%')]
    private bool $debugMode,
) {}
```

### Named Arguments

Only for PHP's own APIs (for example `htmlspecialchars`), NOT for Shopware APIs (parameter names are NOT a BC promise).

### Nullsafe Operator

```php
$addressLine2 = $user?->address?->addressLine2;
```

### list<T> instead of array<T>

```php
/** @return list<string> */
public function getChoices(): array { return ['a', 'b']; }
```

Use `list<T>` for sequential value collections without semantic keys. Normalize with `array_values()` after `array_merge()`/`array_unique()`.

### New String Functions

- `str_contains`, `str_starts_with`, `str_ends_with` instead of `strpos`/`substr`

---

## 2. Extendability Guidelines

Fully documented in `sw-extendability`. Short version:

- **Events (mediator)** — first choice; pass only primary keys
- **Decorator** — AbstractClass + `getDecorated()` + `DecorationPatternException`
- **Factory/Registry** — for new user input types via tagged services
- **Visitor** — for object processing
- **Adapter** — for swapping technology

---

## 3. Decorator Pattern — Rules

```php
abstract class AbstractRuleLoader
{
    abstract public function getDecorated(): AbstractRuleLoader;
    abstract public function load(Context $context): RuleCollection;
}

class CoreRuleLoader extends AbstractRuleLoader
{
    public function getDecorated(): AbstractRuleLoader
    {
        throw new DecorationPatternException(self::class);
    }
    public function load(Context $context): RuleCollection { /* ... */ }
}

class PluginDecorator extends AbstractRuleLoader
{
    public function __construct(private AbstractRuleLoader $inner) {}
    public function getDecorated(): AbstractRuleLoader { return $this->inner; }
    public function load(Context $context): RuleCollection
    {
        $rules = $this->inner->load($context);
        // extension
        return $rules;
    }
}
```

**Rules:**
1. The AbstractClass implements `getDecorated(): self`
2. The core throws `DecorationPatternException` in `getDecorated()`
3. The AbstractClass is NOT `@internal` or `@final`
4. Implementations: NO additional public methods
5. Implementations: NO `EventSubscriberInterface`
6. The PHPStan rule `DecorationPatternRule` enforces this

Add new methods in a BC-safe way: as non-abstract methods in the AbstractClass that delegate:
```php
public function create(Context $context): RuleCollection
{
    return $this->getDecorated()->create($context);
}
```

---

## 4. Domain Exceptions

One exception factory class per domain, extending `HttpException`.

```php
#[Package('customer-order')]
class CustomerException extends HttpException
{
    public const CUSTOMER_GROUP_NOT_FOUND = 'CHECKOUT__CUSTOMER_GROUP_NOT_FOUND';

    public static function customerGroupNotFound(string $id): self
    {
        return new self(
            Response::HTTP_BAD_REQUEST,
            self::CUSTOMER_GROUP_NOT_FOUND,
            'Customer group with id "{{ id }}" not found',
            ['id' => $id]
        );
    }
}
```

**Rules:**
- `__construct` is `private` — only factory methods create instances
- Error codes: unique within the domain; stable (no changes after a release)
- Location: directly in the top-level domain directory (`Checkout\Cart`, `Content\Product`, etc.)
- Catchable exceptions: a dedicated exception class inheriting from the DomainException, in an `Exception/` subfolder

```php
class CustomerNotFoundException extends CustomerException {}
```

- HTTP status codes: always use the appropriate official code
- ADR: https://github.com/shopware/shopware/blob/71ef1dffc97a131069cd4649f71ba35d04771e24/adr/2022-02-24-domain-exceptions.md

---

## 5. Feature Flags

Feature flags let you merge unfinished changes into `trunk` without activating them.

### .env configuration
```
V6_5_0_0=1
```

### PHP
```php
use Shopware\Core\Framework\Feature;

// Conditional execution:
if (!Feature::isActive('v6.5.0.0')) {
    // old behavior
    return;
}
// new behavior

// Callback:
Feature::ifActive('v6.5.0.0', function() { /* ... */ });

// Deprecation:
/** @deprecated tag:v6.5.0 - Class is deprecated, use ... instead */
class OldClass {
    public function foo(): void {
        Feature::triggerDeprecationOrThrow('v6.5.0.0', 'Class is deprecated, use ... instead');
    }
}

// Tests:
Feature::skipTestIfActive('v6.5.0.0', $this);
```

### JavaScript (Admin)
```javascript
// Hide a module:
Module.register('sw-awesome', { flag: 'v6.5.0.0', ... });

// Inject the feature service:
inject: ['feature'],
featureIsActive(flag) { return this.feature.isActive(flag); }
```

### Twig (Storefront)
```twig
{% if feature('v6.5.0.0') %}
    <span>Feature is active</span>
{% endif %}
```

### Major Feature Flags

Major flags (`v6.5.0.0`, `v6.6.0.0`) signal breaking changes before the release. They remain after the release, so you can use them as a version switch instead of `version_compare`.

### Plugin-Owned Flags

For internal use; the behavior can change at any time:
```php
private const FEATURE_FLAGS = ['paypal:v1.0.0.0'];

public function boot(): void
{
    Feature::setRegisteredFeatures(
        array_merge(array_keys(Feature::getAll()), self::FEATURE_FLAGS),
        $this->container->getParameter('kernel.cache_dir') . '/shopware_features.php'
    );
}
```

---

## 6. @final and @internal Annotation

→ Fully documented in `sw-extendability`.

Short version:
- `@final`: public API, not extendable
- `@internal`: private API, no guarantees, do not use in plugins

---

## 7. Database Migrations

### Structure

```php
// One namespace per major version:
namespace Shopware\Core\Migration\V6_7;

class Migration1234567890MyFeature extends MigrationStep
{
    public function update(Connection $connection): void
    {
        // Non-destructive, backward-compatible
        $connection->executeStatement('
            ALTER TABLE product ADD COLUMN new_field VARCHAR(255) NULL
        ');
    }

    public function updateDestructive(Connection $connection): void
    {
        // Irreversible (for example dropping a column) — only in a separate step
        $connection->executeStatement('
            ALTER TABLE product DROP COLUMN old_field
        ');
    }
}
```

### Mandatory Rules

1. **NEVER change an already released migration** — write a new migration instead of editing it
2. **Idempotent** — a migration must be executable multiple times; use `IF [NOT] EXISTS`
3. **Never trust identifiers** — always determine identifiers via a query, never hard-code them
4. **Never overwrite customer data** — check `updated_at IS NULL` before updates
5. **Performance** — max. 10 seconds on a local system; test with production data volumes
6. **Never assume a default language** — use `ImportTranslationsTrait`
7. **Table naming** — snake_case, no `swag_` prefix, descriptive names

### Expand-and-Contract Pattern

```
1. Expand:    Add the new column (non-destructive, update())
2. Migrate:   Copy data from the old column into the new one (update())
3. Contract:  Drop the old column (updateDestructive())
```

### Migration Modes for Destructive Changes

| Mode | Runs destructive up to |
|------|--------------------------|
| `mode=all` | Current major version |
| `mode=blue-green` | Previous major version |
| `mode=safe` (default) | Two majors before the current one |

### Creating a Migration

```bash
bin/console database:create-migration
# Execute:
bin/console database:migrate --all core.V6_7
```

### Migration Tests

- Tests live in `tests/Migration/V6_*/`
- NO `IntegrationTestBehaviour` / `KernelTestBehaviour` — get the connection via `KernelLifecycleManager::getConnection()`
- Run `update()` twice to verify idempotency
- DDL commands (CREATE/ALTER/DROP TABLE) run outside transactions (implicit commit)
- DDL tests must revert DDL changes manually (no rollback via `MigrationTestTrait`)
- Use `MigrationTestTrait` for pure DML migrations
- Use `MultiInsertQueryQueue` for bulk fixture data

---

## 8. Unit Tests

### Principles

- **100% coverage** means: all use cases are tested, not just a high line count
- **Performance**: keep tests fast; mock database access
- **Behavior over implementation**: what the code does, not how
- **Modularity**: tests must not depend on artifacts left by other tests
- **Cleanup**: remove event listeners in `teardown()`; roll back the database
- **Failure cases**: not only the happy path; test error cases too
- **Expected exceptions**: `expectExceptionObject()` instead of try/catch

### Mock Strategy

Use mocks sparingly:
1. Use the real implementation when possible (no database access, no side effects)
2. Hand-crafted stub/dummy (for example `StaticEntityRepository`, `StaticSystemConfigService`)
3. The PHPUnit mock framework as a last resort

**Mocks are problematic because they:**
- Refactor badly (IDEs do not recognize mock references)
- Test implementation details instead of behavior
- Can go stale when the implementation changes

### Good Test Examples

- `CriteriaTest` — simple DTO tests
- `CashRoundingTest` — test matrix for a single service
- `AddCustomerTagActionTest` — mocks for repositories
- `ProductCartTest` — integration test with helper functions
- `CachedProductListingRouteTest` — complex test matrix

### ParaTest Compatibility

Tests must be compatible with the parallel test setup.

---

## 9. Writing Code for Static Analysis

PHPStan is used heavily — code must be statically analyzable.

### Type Safety Priorities

1. **Runtime checks** (preferred):
```php
$foo = $bar->getFoo(); // Foo|null
if ($foo === null) {
    throw new \InvalidArgumentException('Foo must not be null');
}
// PHPStan now knows: $foo is Foo
```

2. **assert()** (development/test only):
```php
assert($foo !== null);         // For development/test
assert(is_string($foo));
assert($foo instanceof Foo);
```

3. **@var annotations** (last resort):
```php
/** @var Foo $foo */
$foo = $bar->getFoo();
```

### Avoid Type Casts

Casts (`(string)`, `(int)`) hide type errors; PHPStan does not detect unexpected cast effects.

### Use @var/@param/@return only for:

- Generics: `@return Collection<int, Product>`
- Array shapes: `@param array{id: string, name: string} $data`
- Special PHPStan types: `class-string`, `positive-int`

### list<T> vs array<T>

```php
/** @return list<string> */
public function getTags(): array
{
    return array_values(array_unique($tags)); // array_values() normalizes to a list
}
```

---

## 10. ADR Format

Expectations for Architecture Decision Records:

- A complete description of the requirements
- List all affected technical domains
- List all affected areas of logic
- Pseudo code for visualization
- Define all public APIs to be created or changed
- Describe extendability and business cases
- Rationale for the decision
- All consequences for third-party developers

### Recommended Procedure

1. Create a list of the domains you will touch
2. For each domain: why it is affected (two sentences)
3. Per domain: "Problems" (what has to change — not yet how)
4. Per domain: "Solution" (how the problems are solved)
5. Section "Extendability": how developers can extend the new system
6. Pseudo code at the end

---

## References

- `resources/guidelines/code/core/6.5-new-php-language-features.md`
- `resources/guidelines/code/core/extendability.md`
- `resources/guidelines/code/core/decorator-pattern.md`
- `resources/guidelines/code/core/domain-exceptions.md`
- `resources/guidelines/code/core/feature-flags.md`
- `resources/guidelines/code/core/final-and-internal.md`
- `resources/guidelines/code/core/internal.md`
- `resources/guidelines/code/core/database-migations.md`
- `resources/guidelines/code/core/unit-tests.md`
- `resources/guidelines/code/core/writing-code-for-static-analysis.md`
- `resources/guidelines/code/core/adr.md`
