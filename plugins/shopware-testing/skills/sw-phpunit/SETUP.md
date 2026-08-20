# Shopware 6 — PHPUnit-Setup

Plugin-Tests laufen gegen den Shopware-Kernel. `phpunit.xml.dist` im Plugin, Bootstrap über Shopwares
`TestBootstrapper`; Integrationstests nutzen `IntegrationTestBehaviour` (Transaktion je Test + DB-Reset).

```php
class FooTest extends TestCase
{
    use IntegrationTestBehaviour;
    private EntityRepository $repo;
    protected function setUp(): void { $this->repo = $this->getContainer()->get('ff_example.repository'); }
}
```

Ausführen: `vendor/bin/phpunit` bzw. `composer test` (DB-Env `DATABASE_URL` der Test-DB). Test-Pyramide (ADR
„follow test pyramid"): viele Unit- (`sw-unit-test`), weniger Integration- (`sw-integration-test`), wenige E2E-Tests.

→ Bootstrap & Base-Class: [../shopware-phpunit/`SETUP-KERNEL-BOOTSTRAP.md`](../shopware-phpunit/`SETUP-KERNEL-BOOTSTRAP.md`), [../shopware-phpunit/`SETUP-BASE-TEST-CLASS.md`](../shopware-phpunit/`SETUP-BASE-TEST-CLASS.md`)
