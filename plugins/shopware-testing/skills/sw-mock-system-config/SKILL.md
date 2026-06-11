---
name: sw-mock-system-config
description: >
  SystemConfigService in Shopware-6-Unit-Tests mocken: StaticSystemConfigService, Plugin-Config-Werte ohne DB setzen.
  Trigger: "SystemConfigService mock", "StaticSystemConfigService", "Config mocken test", "plugin config test", "config wert test shopware".
  Shopware 6.7.
---

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

→ [../shopware-phpunit/references/mock-static-system-config-service.md](../shopware-phpunit/references/mock-static-system-config-service.md)
