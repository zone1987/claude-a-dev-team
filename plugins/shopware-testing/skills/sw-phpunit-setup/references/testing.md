# Testing

## Overview

Shopware plugins use PHPUnit for backend tests. The `shopware-phpunit` skill provides comprehensive guidance — this reference covers the essentials.

## Test Directory Structure

```
tests/
├── TestBootstrap.php
├── Unit/
│   └── Service/
│       └── MyServiceTest.php
└── Integration/
    └── Service/
        └── MyServiceIntegrationTest.php
```

## PHPUnit Configuration

```xml
<!-- phpunit.xml.dist -->
<?xml version="1.0" encoding="UTF-8"?>
<phpunit xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:noNamespaceSchemaLocation="https://schema.phpunit.de/10.5/phpunit.xsd"
         bootstrap="tests/TestBootstrap.php"
         cacheDirectory=".phpunit.cache"
         executionOrder="depends,defects">
    <testsuites>
        <testsuite name="unit">
            <directory>tests/Unit</directory>
        </testsuite>
        <testsuite name="integration">
            <directory>tests/Integration</directory>
        </testsuite>
    </testsuites>
</phpunit>
```

## Unit Test Example

```php
<?php declare(strict_types=1);

namespace FfContentPlus\Tests\Unit\Service;

use FfContentPlus\Service\MyService;
use PHPUnit\Framework\Attributes\CoversClass;
use PHPUnit\Framework\TestCase;
use Shopware\Core\Framework\Log\Package;

#[Package('custom-plugins')]
#[CoversClass(MyService::class)]
class MyServiceTest extends TestCase
{
    public function testCalculateDiscount(): void
    {
        $service = new MyService();
        $result = $service->calculateDiscount(100.0, 10);

        static::assertSame(90.0, $result);
    }
}
```

## Integration Test Example

```php
<?php declare(strict_types=1);

namespace FfContentPlus\Tests\Integration\Service;

use FfContentPlus\Service\MyService;
use PHPUnit\Framework\Attributes\CoversClass;
use Shopware\Core\Framework\Test\TestCaseBase\IntegrationTestBehaviour;
use PHPUnit\Framework\TestCase;

#[CoversClass(MyService::class)]
class MyServiceIntegrationTest extends TestCase
{
    use IntegrationTestBehaviour;

    public function testServiceIsRegistered(): void
    {
        $service = $this->getContainer()->get(MyService::class);
        static::assertInstanceOf(MyService::class, $service);
    }
}
```

## Running Tests

```bash
# All tests
ddev exec bin/phpunit --configuration custom/static-plugins/FfContentPlus/phpunit.xml.dist

# Only unit tests
ddev exec bin/phpunit --configuration custom/static-plugins/FfContentPlus/phpunit.xml.dist --testsuite=unit

# Specific test
ddev exec bin/phpunit --configuration custom/static-plugins/FfContentPlus/phpunit.xml.dist --filter=testCalculateDiscount
```

## Key Test Traits

| Trait | Purpose |
|-------|---------|
| `IntegrationTestBehaviour` | Provides DI container, database, kernel |
| `SalesChannelApiTestBehaviour` | Test Store API endpoints |
| `AdminApiTestBehaviour` | Test Admin API endpoints |

## Cross-Reference

For comprehensive PHPUnit testing guidance (mocking repositories, testing subscribers, DAL operations), use the `shopware-phpunit` skill.
