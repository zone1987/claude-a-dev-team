---
title: Mock Services via Container Instead of Constructor Injection
impact: MEDIUM
impactDescription: Avoids brittle mocks and tests that break on refactoring
tags: mock, service, container, dependency-injection
---

## Mock Services via Container Instead of Constructor Injection

In integration tests, replace services in the DI container rather than manually constructing classes with mocked dependencies. This ensures decorators, event listeners, and other wiring still work correctly.

**Incorrect (manually constructing the service with mocks):**

```php
public function testTheServiceUsesTheConfiguredValue(): void
{
    $repositoryMock = static::createMock(EntityRepository::class);
    $repositoryMock->method('search')->willReturn(new EntitySearchResult(
        'product', 0, new EntityCollection(), null, new Criteria(), Context::createDefaultContext()
    ));

    // Breaks if MyService constructor changes or has additional dependencies
    $service = new MyService($repositoryMock, static::createMock(EventDispatcherInterface::class));
    $result = $service->doSomething();

    static::assertTrue($result);
}
```

**Correct (replacing the service in the container):**

```php
use PHPUnit\Framework\Attributes\CoversClass;
use Shopware\Core\Framework\Test\TestCaseBase\IntegrationTestBehaviour;

/**
 * @class MyServiceTest
 * @package YourPlugin.Tests
 */
#[CoversClass(MyService::class)]
final class MyServiceTest extends TestCase
{
    use IntegrationTestBehaviour;

    /**
     * @return void
     */
    public function testTheServiceAcceptsWhatTheProviderReturns(): void
    {
        // createStub, not createMock: no call is asserted on it, only a return value is
        // supplied. PHPUnit 12 reports a mock without expectations as a notice, and
        // failOnRisky="true" turns that into a failure.
        $provider = static::createStub(SomeExternalDependency::class);
        $provider->method('call')->willReturn('a-value');

        static::getContainer()->set(SomeExternalDependency::class, $provider);

        $service = static::getContainer()->get(MyService::class);
        static::assertInstanceOf(MyService::class, $service);

        static::assertTrue($service->doSomething());
    }

    /**
     * @return void
     */
    public function testTheProviderIsAskedExactlyOnce(): void
    {
        // createMock here, because the call itself is the assertion.
        $provider = static::createMock(SomeExternalDependency::class);
        $provider->expects(static::once())->method('call')->willReturn('a-value');

        static::getContainer()->set(SomeExternalDependency::class, $provider);

        $service = static::getContainer()->get(MyService::class);
        static::assertInstanceOf(MyService::class, $service);

        $service->doSomething();
    }
}
```

**The difference between the two is not stylistic.** A stub supplies answers; a mock
asserts that a call happened. Using `createMock` where you meant a stub makes the suite
fail under the standard's `failOnRisky="true"`.

Only mock external boundaries (HTTP clients, third-party APIs). For Shopware services and repositories, prefer using the real implementations in integration tests.
