# Shopware 6 — Admin API Test

Tests admin API endpoints with an authenticated client (`AdminApiTestBehaviour`/`getBrowser`).

```php
use IntegrationTestBehaviour, AdminApiTestBehaviour;

public function testAction(): void
{
    $this->getBrowser()->request('POST', '/api/_action/ff/import/' . $id);
    static::assertSame(200, $this->getBrowser()->getResponse()->getStatusCode());
}
```

The browser holds a valid bearer token. Test ACL/permission cases explicitly (a dedicated integration user with
restricted rights). Custom endpoints/ACL: `shopware-framework` (`sw-admin-api-controller`/`sw-api-acl`).
