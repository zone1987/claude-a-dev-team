# Shopware 6 — Mocking SystemConfig

Test config-dependent logic in unit tests without a DB using `StaticSystemConfigService`.

```php
$config = new StaticSystemConfigService([
    'FfExample.config.active' => true,
    'FfExample.config.apiKey' => 'test',
]);
$sut = new FfService($config);
```

Provide sales-channel-specific values as a nested array per channel ID. This avoids mock stubs on `get()`.
For integration with the real config → `sw-integration-test`. Using config in code: `shopware-core` (`sw-system-config`).

→ [../shopware-phpunit/`MOCK-SYSTEM-CONFIG-MOCK-STATIC-SYSTEM-CONFIG-SERVICE.md`](../shopware-phpunit/`MOCK-SYSTEM-CONFIG-MOCK-STATIC-SYSTEM-CONFIG-SERVICE.md`)
