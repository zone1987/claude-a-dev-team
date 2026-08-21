# Shopware 6 — PHPUnit Setup

Plugin tests run against the Shopware kernel. Put `phpunit.xml.dist` in the plugin, bootstrap through Shopware's
`TestBootstrapper`; integration tests use `IntegrationTestBehaviour` (a transaction per test + DB reset).

```php
class FooTest extends TestCase
{
    use IntegrationTestBehaviour;
    private EntityRepository $repo;
    protected function setUp(): void { $this->repo = $this->getContainer()->get('ff_example.repository'); }
}
```

Run with `vendor/bin/phpunit` or `composer test` (the DB env `DATABASE_URL` points at the test DB). Test pyramid (ADR
"follow test pyramid"): many unit tests (`sw-unit-test`), fewer integration tests (`sw-integration-test`), few E2E tests.

→ Bootstrap & base class: [../shopware-phpunit/`SETUP-KERNEL-BOOTSTRAP.md`](../shopware-phpunit/`SETUP-KERNEL-BOOTSTRAP.md`), [../shopware-phpunit/`SETUP-BASE-TEST-CLASS.md`](../shopware-phpunit/`SETUP-BASE-TEST-CLASS.md`)
