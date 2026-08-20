# Shopware 6 — Store-API-Test

Testet Store-API-Routen end-to-end über einen SalesChannel-Browser.

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

Browser setzt `sw-access-key` automatisch. Für Admin-API → `sw-admin-api-test`. Eigene Routen: `shopware-framework`
(`sw-store-api-route`).

→ [../shopware-phpunit/`STORE-API-TEST-API-STORE-API-TESTING.md`](../shopware-phpunit/`STORE-API-TEST-API-STORE-API-TESTING.md`)
