# Shopware 6 — Store API Test

Tests Store API routes end-to-end through a sales channel browser.

```php
use IntegrationTestBehaviour, SalesChannelApiTestBehaviour;

public function testRoute(): void
{
    $browser = $this->createCustomSalesChannelBrowser(['id' => $salesChannelId]);
    $browser->request('GET', '/store-api/ff/example');
    $response = json_decode($browser->getResponse()->getContent(), true);
    static::assertSame(200, $browser->getResponse()->getStatusCode());
}
```

The browser sets `sw-access-key` automatically. For the Admin API → `sw-admin-api-test`. Custom routes: `shopware-framework`
(`sw-store-api-route`).

→ [../shopware-phpunit/`STORE-API-TEST-API-STORE-API-TESTING.md`](../shopware-phpunit/`STORE-API-TEST-API-STORE-API-TESTING.md`)
