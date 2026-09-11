# Shopware 6 — PHPUnit setup

**The complete setup is in `sw-testing-standard` → `STANDARD-GATE.md`**: five phpunit
configurations, two bootstraps, the composer scripts, and the pcov requirement in
`.ddev/config.yaml`. Build from there; this file is the short orientation.

## The two things people get wrong

**PHPUnit belongs to the project, never to the plugin.** `phpunit/phpunit` is not in the
plugin's `require-dev`, and scripts call `../../../vendor/bin/phpunit`:

```bash
composer test:unit          # ../../../vendor/bin/phpunit -c phpunit.unit.xml.dist
composer test:integration   # ../../../vendor/bin/phpunit -c phpunit.xml.dist --testsuite=integration
```

A plugin that pins its own version pins one that goes stale, and the two can disagree about
what a test means.

**There are two bootstraps, not one.** Unit tests must not boot a kernel:

| File | What it loads | Used by |
|---|---|---|
| `tests/UnitBootstrap.php` | autoloaders only | `phpunit.unit.xml.dist` |
| `tests/TestBootstrap.php` | Shopware's `TestBootstrapper` | `phpunit.xml.dist` and the coverage variants |

Pointing the unit suite at `TestBootstrap.php` works and makes every unit test boot a
kernel it does not need — the suite slows to a crawl for no benefit.

## Test directories

```
tests/
├── UnitBootstrap.php
├── TestBootstrap.php
├── Unit/            no kernel, no database
├── Integration/     IntegrationTestBehaviour, real DAL
├── Architecture/    phpat rules, run by PHPStan
└── Acceptance/      Playwright, its own package.json
```

All four exist in every plugin. `tests/Integration/` keeps a `.gitkeep` while empty,
because three configs name it and PHPUnit aborts when it is missing.

## A test, in the shape the standard requires

```php
<?php declare(strict_types=1);

namespace YourPlugin\Tests\Integration\Service;

use PHPUnit\Framework\Attributes\CoversClass;
use PHPUnit\Framework\TestCase;
use Shopware\Core\Framework\Test\TestCaseBase\IntegrationTestBehaviour;
use YourPlugin\Service\ExampleService;

/**
 * @class ExampleServiceTest
 * @package YourPlugin.Tests
 */
#[CoversClass(ExampleService::class)]
final class ExampleServiceTest extends TestCase
{
    use IntegrationTestBehaviour;

    /**
     * @return void
     */
    public function testAnExampleIsStoredUnderTheNameItWasGiven(): void
    {
        $repository = static::getContainer()->get('your_entity.repository');

        static::assertInstanceOf(EntityRepository::class, $repository);
        // …
    }
}
```

`#[CoversClass]`, `final`, `static::getContainer()`, and a name that states the rule. All
four are required — see [UNIT-TEST.md](UNIT-TEST.md) and
[INTEGRATION-TEST.md](INTEGRATION-TEST.md).

## The pyramid, with a correction

Many unit tests, fewer integration tests — that part holds.

**The old advice to use end-to-end tests "sparingly" does not.** Whatever the plugin ships
gets a Playwright test: every administration page, every storefront output. It is the only
level that reaches Twig, and the only one that answers what the user sees.
→ `STANDARD-PLAYWRIGHT.md`
