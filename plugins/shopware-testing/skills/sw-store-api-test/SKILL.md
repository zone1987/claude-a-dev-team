---
name: sw-store-api-test
description: >
  Store-API-Tests in Shopware 6: SalesChannelApiTestBehaviour, getSalesChannelBrowser, Requests gegen /store-api,
  Response prüfen. Trigger: "Store API Test", "SalesChannelApiTestBehaviour", "getSalesChannelBrowser", "store-api request test",
  "API test storefront". Shopware 6.7.
---

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

→ [../shopware-phpunit/references/api-store-api-testing.md](../shopware-phpunit/references/api-store-api-testing.md)
