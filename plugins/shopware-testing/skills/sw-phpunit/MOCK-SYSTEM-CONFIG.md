# Shopware 6 — SystemConfig mocken

Config-abhängige Logik im Unit-Test ohne DB testen mit `StaticSystemConfigService`.

```php
$config = new StaticSystemConfigService([
    'FfExample.config.active' => true,
    'FfExample.config.apiKey' => 'test',
]);
$sut = new FfService($config);
```

Sales-Channel-spezifische Werte als verschachteltes Array je Channel-ID. Vermeidet Mock-Stubs auf `get()`.
Für Integration mit echter Config → `sw-integration-test`. Config-Nutzung im Code: `shopware-core` (`sw-system-config`).

→ [../shopware-phpunit/`MOCK-SYSTEM-CONFIG-MOCK-STATIC-SYSTEM-CONFIG-SERVICE.md`](../shopware-phpunit/`MOCK-SYSTEM-CONFIG-MOCK-STATIC-SYSTEM-CONFIG-SERVICE.md`)
