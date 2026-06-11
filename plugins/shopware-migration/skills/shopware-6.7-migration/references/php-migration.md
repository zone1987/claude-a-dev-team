# PHP Migration Reference

PHP code changes required when migrating Shopware plugins from 6.6 to 6.7.

---

## 1. Constructor Property Promotion

PHP 8.1+ constructor property promotion eliminates boilerplate property declarations and assignments. Shopware 6.7 requires PHP >= 8.2 and strongly recommends this pattern.

### Basic Pattern

```php
// BEFORE (6.6)

/**
 * @class ProductImportService
 * @package FfProductImport
 */
#[Package('custom-plugins')]
class ProductImportService
{
    /**
     * @var EntityRepository
     */
    private EntityRepository $productRepository;

    /**
     * @var SystemConfigService
     */
    private SystemConfigService $configService;

    /**
     * @var LoggerInterface
     */
    private LoggerInterface $logger;

    /**
     * @param EntityRepository $productRepository
     * @param SystemConfigService $configService
     * @param LoggerInterface $logger
     */
    public function __construct(
        EntityRepository $productRepository,
        SystemConfigService $configService,
        LoggerInterface $logger,
    ) {
        $this->productRepository = $productRepository;
        $this->configService = $configService;
        $this->logger = $logger;
    }
}

// AFTER (6.7)

/**
 * @class ProductImportService
 * @package FfProductImport
 */
#[Package('custom-plugins')]
class ProductImportService
{
    /**
     * @param EntityRepository $productRepository
     * @param SystemConfigService $configService
     * @param LoggerInterface $logger
     */
    public function __construct(
        private readonly EntityRepository $productRepository,
        private readonly SystemConfigService $configService,
        private readonly LoggerInterface $logger,
    ) {}
}
```

### Rules

1. **Always use `readonly`** unless the property needs to be mutable
2. **Always use `private`** unless the property needs wider visibility (use `protected` for inheritance)
3. **Empty body** uses `{}` on the same line as the closing parenthesis
4. **Keep the DocBlock** with `@param` tags even with promoted properties
5. **Trailing comma** after the last parameter

### Mixed Promoted and Non-Promoted

When some constructor logic is needed beyond simple assignment:

```php
/**
 * @param EntityRepository $productRepository
 * @param string $defaultLocale
 */
public function __construct(
    private readonly EntityRepository $productRepository,
    string $defaultLocale,
) {
    $this->locale = strtolower($defaultLocale);
}
```

### Subscriber Example

```php
// BEFORE
/**
 * @class ProductSubscriber
 * @package FfProductImport
 */
#[Package('custom-plugins')]
class ProductSubscriber implements EventSubscriberInterface
{
    /**
     * @var SystemConfigService
     */
    private SystemConfigService $configService;

    /**
     * @param SystemConfigService $configService
     */
    public function __construct(SystemConfigService $configService)
    {
        $this->configService = $configService;
    }

    /**
     * @return array<string, string>
     */
    public static function getSubscribedEvents(): array
    {
        return [
            ProductEvents::PRODUCT_WRITTEN_EVENT => 'onProductWritten',
        ];
    }
}

// AFTER
/**
 * @class ProductSubscriber
 * @package FfProductImport
 */
#[Package('custom-plugins')]
class ProductSubscriber implements EventSubscriberInterface
{
    /**
     * @param SystemConfigService $configService
     */
    public function __construct(
        private readonly SystemConfigService $configService,
    ) {}

    /**
     * @return array<string, string>
     */
    public static function getSubscribedEvents(): array
    {
        return [
            ProductEvents::PRODUCT_WRITTEN_EVENT => 'onProductWritten',
        ];
    }
}
```

---

## 2. Coding Style Requirements

Shopware 6.7 enforces stricter coding standards. These align with the conventions in the `shopware-plugins` skill's `examples/coding-style.md`.

### Opening Braces (Allman Style)

Classes and methods: opening brace on a **new line**.

```php
// CORRECT
class MyService
{
    public function doSomething(): void
    {
        // ...
    }
}

// WRONG
class MyService {
    public function doSomething(): void {
        // ...
    }
}
```

### Class DocBlocks

Every class must have a multi-line DocBlock with `@class` and `@package`. The DocBlock goes **BEFORE** any PHP attributes.

**Annotation order within the DocBlock:**

1. Description (optional, if the class needs explanation)
2. `@method` annotations (for collections, magic methods, etc.)
3. **Blank line** (separator)
4. `@class {ClassName}`
5. `@package {Namespace}`

```php
// Standard class (no description, no @method)
/**
 * @class ProductImportCommand
 * @package FfProductImport\Command
 */
#[AsCommand(
    name: 'ff:product-import:run',
    description: 'Run product import from external API'
)]
#[Package('custom-plugins')]
class ProductImportCommand extends Command
{
```

```php
// Collection class with @method annotations
/**
 * @method void                           add(TimelineTranslationEntity $entity)
 * @method void                           set(string $key, TimelineTranslationEntity $entity)
 * @method TimelineTranslationEntity[]    getIterator()
 * @method TimelineTranslationEntity[]    getElements()
 * @method TimelineTranslationEntity|null get(string $key)
 * @method TimelineTranslationEntity|null first()
 * @method TimelineTranslationEntity|null last()
 *
 * @class TimelineTranslationCollection
 * @package FfTimeline\Core\Content\Timeline\Aggregate
 */
#[Package('custom-plugins')]
class TimelineTranslationCollection extends EntityCollection
{
```

```php
// Class with description and @method annotations
/**
 * Handles importing products from external API with retry logic.
 *
 * @method ProductEntity|null findByExternalId(string $externalId)
 *
 * @class ProductImportService
 * @package FfProductImport\Core\Service
 */
#[Package('custom-plugins')]
class ProductImportService
{
```

**Key rules:**
- `@class` and `@package` are always LAST in the DocBlock, separated by a blank line from everything above
- `@method` annotations use aligned spacing for readability
- The DocBlock always goes BEFORE any PHP attributes (`#[Package(...)]`, `#[AsCommand(...)]`, etc.)

### Method DocBlocks

Every method must have a multi-line DocBlock:

```php
/**
 * @param string $productId
 * @param Context $context
 * @return ProductEntity|null
 * @throws ProductNotFoundException
 */
public function findProduct(string $productId, Context $context): ?ProductEntity
{
```

### Type Declarations

- Every parameter must have a type declaration
- Every method must have a return type declaration
- Use nullable types with `?` prefix: `?string`, `?int`
- Use union types where appropriate: `string|int`

```php
// CORRECT
public function process(?string $id, array $data): ProductEntity|null
{

// WRONG (missing types)
public function process($id, $data)
{
```

### Constants and Properties

Always with DocBlock:

```php
/**
 * @var string
 */
private const API_ENDPOINT = 'https://api.example.com/v2';

/**
 * @var int
 */
private int $retryCount = 3;
```

### Empty Constructor Bodies

```php
// CORRECT
public function __construct(
    private readonly MyService $service,
) {}

// WRONG
public function __construct(
    private readonly MyService $service,
) {
}
```

---

## 3. Domain Exceptions

Follow the factory pattern established in ADR `2022-02-24-domain-exceptions`. Each domain gets one exception class that acts as a factory.

### Pattern

```php
<?php

declare(strict_types=1);

namespace FfProductImport\Core\Exception;

use Shopware\Core\Framework\HttpException;
use Symfony\Component\HttpFoundation\Response;

/**
 * @class ProductImportException
 * @package FfProductImport\Core\Exception
 */
#[Package('custom-plugins')]
class ProductImportException extends HttpException
{
    /**
     * @var string
     */
    public const PRODUCT_NOT_FOUND = 'FF_PRODUCT_IMPORT__PRODUCT_NOT_FOUND';

    /**
     * @var string
     */
    public const IMPORT_FAILED = 'FF_PRODUCT_IMPORT__IMPORT_FAILED';

    /**
     * @var string
     */
    public const INVALID_API_RESPONSE = 'FF_PRODUCT_IMPORT__INVALID_API_RESPONSE';

    /**
     * @param string $productId
     * @return self
     */
    public static function productNotFound(string $productId): self
    {
        return new self(
            Response::HTTP_NOT_FOUND,
            self::PRODUCT_NOT_FOUND,
            'Product with id "{{ productId }}" not found.',
            ['productId' => $productId]
        );
    }

    /**
     * @param string $reason
     * @param \Throwable|null $previous
     * @return self
     */
    public static function importFailed(string $reason, ?\Throwable $previous = null): self
    {
        return new self(
            Response::HTTP_INTERNAL_SERVER_ERROR,
            self::IMPORT_FAILED,
            'Product import failed: {{ reason }}',
            ['reason' => $reason],
            $previous
        );
    }

    /**
     * @param int $statusCode
     * @return self
     */
    public static function invalidApiResponse(int $statusCode): self
    {
        return new self(
            Response::HTTP_BAD_GATEWAY,
            self::INVALID_API_RESPONSE,
            'External API returned unexpected status code {{ statusCode }}.',
            ['statusCode' => (string) $statusCode]
        );
    }
}
```

### Usage

```php
// Throw domain exceptions
throw ProductImportException::productNotFound($productId);
throw ProductImportException::importFailed('API timeout', $previousException);
throw ProductImportException::invalidApiResponse(503);

// DO NOT use generic exceptions
// WRONG: throw new \RuntimeException('Product not found');
// WRONG: throw new \InvalidArgumentException('Invalid response');
```

### Error Code Convention

Format: `{VENDOR}_{PLUGIN}_{ERROR_NAME}`

Examples:
- `FF_PRODUCT_IMPORT__PRODUCT_NOT_FOUND`
- `ADT_ORDER_EXPORT__EXPORT_FAILED`
- `AG_NEWSLETTER__SUBSCRIBER_EXISTS`

---

## 4. PHP Enums for Constants

Replace string/integer constant groups with backed enums when the value set is fixed and known.

### Basic Migration

```php
// BEFORE (constants)
class ImportStatus
{
    public const PENDING = 'pending';
    public const RUNNING = 'running';
    public const COMPLETED = 'completed';
    public const FAILED = 'failed';
}

// Usage
if ($status === ImportStatus::PENDING) { ... }

// AFTER (backed enum)
enum ImportStatus: string
{
    case Pending = 'pending';
    case Running = 'running';
    case Completed = 'completed';
    case Failed = 'failed';
}

// Usage
if ($status === ImportStatus::Pending) { ... }

// With methods
enum ImportStatus: string
{
    case Pending = 'pending';
    case Running = 'running';
    case Completed = 'completed';
    case Failed = 'failed';

    /**
     * @return bool
     */
    public function isFinished(): bool
    {
        return match ($this) {
            self::Completed, self::Failed => true,
            default => false,
        };
    }

    /**
     * @return string
     */
    public function label(): string
    {
        return match ($this) {
            self::Pending => 'Pending',
            self::Running => 'In Progress',
            self::Completed => 'Done',
            self::Failed => 'Failed',
        };
    }
}
```

### Expand and Contract Pattern

For gradual migration (backward compatibility during transition):

**Step 1: Expand** - Add enum alongside constants:

```php
// Keep old constants for backward compatibility
class ImportStatus
{
    /** @deprecated Use ImportStatus enum instead */
    public const PENDING = 'pending';
    /** @deprecated Use ImportStatus enum instead */
    public const RUNNING = 'running';
}

// New enum
enum ImportStatusEnum: string
{
    case Pending = 'pending';
    case Running = 'running';
}
```

**Step 2: Migrate** - Update all usages to use the enum.

**Step 3: Contract** - Remove the old constants class.

### When NOT to Use Enums

- Dynamic value sets (values stored in database)
- Configuration values that plugins may extend
- Values that need to be serialized to JSON frequently (use `->value` accessor)

---

## 5. Rector Configuration

Use Rector with Shopware-specific sets for 6.7 migration. The `rector.php` must use `ShopwareSetList::SHOPWARE_6_7_0` and `ShopwareSetList::SHOPWARE_6_8_0` to apply all Shopware-specific code transformations.

```php
// rector.php
<?php

declare(strict_types=1);

use Frosh\Rector\Set\ShopwareSetList;
use Rector\Config\RectorConfig;

return RectorConfig::configure()
    ->withPaths([
        __DIR__ . '/src',
    ])
    ->withSets([
        ShopwareSetList::SHOPWARE_6_7_0,
        ShopwareSetList::SHOPWARE_6_8_0,
    ]);
```

### Why Both Sets?

- `ShopwareSetList::SHOPWARE_6_7_0` — applies transformations for Shopware 6.7 compatibility (deprecated API replacements, constructor promotion, etc.)
- `ShopwareSetList::SHOPWARE_6_8_0` — prepares code for 6.8 by addressing features that will be removed in 6.8 (proactive cleanup)

### Running Rector

```bash
# Preview changes (dry run)
vendor/bin/rector process --dry-run --clear-cache

# Apply changes
vendor/bin/rector process --clear-cache
```

### Important

- Do NOT use generic `LevelSetList::UP_TO_PHP_84` — the Shopware sets already include the necessary PHP-level transformations
- Always review Rector output manually before committing
- Run Rector before other migration steps (codemod, manual fixes) as it automates many PHP-level changes
