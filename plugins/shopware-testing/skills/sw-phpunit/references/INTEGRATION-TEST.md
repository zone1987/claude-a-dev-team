# Shopware 6 — integration test

Tests against a real database and container: the DAL, service wiring, anything that only
behaves correctly when Shopware is actually running.

`IntegrationTestBehaviour` wraps every test method in a transaction and rolls it back, so
tests stay isolated and fast despite the database.

Configured by `sw-testing-standard` → `STANDARD-GATE.md`. Runs through `tests/TestBootstrap.php`, which boots the kernel:

```bash
composer test:integration    # ../../../vendor/bin/phpunit -c phpunit.xml.dist --testsuite=integration
```

```php
<?php declare(strict_types=1);

namespace YourPlugin\Tests\Integration\Service;

use PHPUnit\Framework\Attributes\CoversClass;
use PHPUnit\Framework\TestCase;
use Shopware\Core\Framework\Context;
use Shopware\Core\Framework\DataAbstractionLayer\Search\Criteria;
use Shopware\Core\Framework\Test\TestCaseBase\IntegrationTestBehaviour;
use Shopware\Core\Framework\Uuid\Uuid;
use YourPlugin\Service\SupplierWriter;

/**
 * @class SupplierWriterTest
 * @package YourPlugin.Tests
 */
#[CoversClass(SupplierWriter::class)]
final class SupplierWriterTest extends TestCase
{
    use IntegrationTestBehaviour;

    /**
     * @return void
     */
    public function testASupplierIsStoredWithTheNameItWasGiven(): void
    {
        $id = Uuid::randomHex();

        $this->writer()->write([['id' => $id, 'name' => 'Acme']], Context::createDefaultContext());

        $entity = $this->repository()
            ->search(new Criteria([$id]), Context::createDefaultContext())
            ->first();

        static::assertNotNull($entity);
        static::assertSame('Acme', $entity->getName());
    }

    /**
     * @return SupplierWriter
     */
    private function writer(): SupplierWriter
    {
        $writer = static::getContainer()->get(SupplierWriter::class);

        // PHPStan at level max needs the narrowing, and the assertion documents that a
        // missing service is a wiring defect rather than a test failure.
        static::assertInstanceOf(SupplierWriter::class, $writer);

        return $writer;
    }
}
```

## The rules this example encodes

**`extends TestCase` plus `use IntegrationTestBehaviour`**, not a Shopware base class.

**`static::getContainer()`**, not the instance form. In 6.7 it is a static method.

**Services are narrowed with `assertInstanceOf` before use.** PHPStan at level max requires
it, and it turns a missing service into a clear message instead of a null error three lines
later.

**Test data through private factory methods**, not fixture files. A method named
`orderWithOffer()` reads at the call site; a fixture file does not.

**`#[CoversClass]` and rule-shaped names**, exactly as in a unit test.

## What belongs here rather than in a unit test

- the DAL actually writing and reading what you think
- entity definitions matching the schema
- service wiring resolving
- a cart processor behaving against a real cart
- anything where mocking the dependency would mean mocking the thing under test

## What does not

Pure arithmetic, value objects, anything a mock can stand in for. Those are unit tests —
faster, and they fail with a clearer message.

## tests/Integration must exist even while empty

Three phpunit configs name it as a suite, and PHPUnit aborts with
`Test directory "…" not found` when it is missing. An empty directory does not survive a
clone, so keep a `.gitkeep` there explaining why.

## Builders and fixtures

For complex payloads: `TEST-BUILDER.md` and `TEST-FIXTURES.md`. Manage ids centrally in an
`IdsCollection` so a test reads as intent rather than as hex strings.
