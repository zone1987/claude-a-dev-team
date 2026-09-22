# Shopware 6 — unit test

Isolated logic — services, value objects, calculations — **without** kernel or database.
The fastest level, and where most of the 100 % comes from.

Configured by `sw-testing-standard` → `STANDARD-GATE.md`. Runs through `tests/UnitBootstrap.php`, which loads autoloaders and nothing else:

```bash
composer test:unit    # ../../../vendor/bin/phpunit -c phpunit.unit.xml.dist
```

```php
<?php declare(strict_types=1);

namespace YourPlugin\Tests\Unit\Service;

use PHPUnit\Framework\Attributes\CoversClass;
use PHPUnit\Framework\TestCase;
use YourPlugin\Service\PriceCalculator;

/**
 * @class PriceCalculatorTest
 * @package YourPlugin.Tests
 */
#[CoversClass(PriceCalculator::class)]
final class PriceCalculatorTest extends TestCase
{
    /**
     * @return void
     */
    public function testAnAmountIsRoundedToTheCentRatherThanTruncated(): void
    {
        // 19.994 held as a float is below 19.995; truncating would report 19.99 for a
        // price the shopper was charged 20.00 for.
        static::assertSame(19.99, (new PriceCalculator())->normalize(19.994));
    }

    /**
     * @return void
     */
    public function testAnEmptyBasketIsWorthNothingRatherThanFailing(): void
    {
        static::assertSame(0, (new PriceCalculator())->total([]));
    }
}
```

## The rules this example encodes

**`#[CoversClass]` on the class.** Without it the coverage report calls tested code
untested, and the figure depends on the order the tests happened to run in. **Never
`#[CoversNothing]`** — a test that covers nothing is deleted, not written.

**The name states the rule**, not the method:
`testAnAmountIsRoundedToTheCentRatherThanTruncated`, never `testRounds`. The name is the
documentation that survives a refactoring, and a suite of rule-shaped names reads as the
specification of the class.

**`static::assertSame`**, not `$this->assertEquals`. Strict equality, and the static form
is what the core writes 22562 times against 48 instance calls.

**A comment only where the case is not obvious**, and it says *why the case exists* — which
float lands where — not what the line does.

## Mocks and stubs are not the same thing

```php
// No call is asserted on it: a stub.
$context = static::createStub(SalesChannelContext::class);
$context->method('getCurrencyId')->willReturn(Defaults::CURRENCY);

// A call is asserted: a mock.
$logger = static::createMock(LoggerInterface::class);
$logger->expects($this->once())->method('warning');
```

PHPUnit 12 reports a mock without expectations as a notice, and `failOnRisky` turns that
into a failure. Use `createStub` when you mean a stub.

For repositories and configuration: `StaticEntityRepository` and
`StaticSystemConfigService` — see `MOCK-REPOSITORY.md` and `MOCK-SYSTEM-CONFIG.md`.

## Exceptions

```php
$this->expectExceptionObject(new CurrencyMismatchException('EUR', 'CHF'));
```

`expectExceptionObject` asserts the message too, which `expectException` does not.

## A tautological assertion is not a test

```php
// Useless: the type is statically known, so this can never fail. PHPStan rejects it.
static::assertInstanceOf(Plugin::class, new MyPlugin(true, __DIR__));

// Useful: this can fail, and would if someone removed the parent.
static::assertTrue((new \ReflectionClass(MyPlugin::class))->isSubclassOf(Plugin::class));
```

The first form reaches the line and proves nothing — exactly how a coverage figure gets
inflated without the code getting safer.

## Where the boundary is

DAL behaviour, container wiring and anything needing a database belong in an integration
test → [INTEGRATION-TEST.md](INTEGRATION-TEST.md). If a unit test needs a kernel, it is not
a unit test.
