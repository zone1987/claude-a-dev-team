---
name: sw-system-config
description: >
  Konfigurationswerte in Shopware 6 lesen/schreiben mit SystemConfigService: Scopes (global vs. Sales-Channel),
  Defaults, Typen, Plugin-Config-Keys. Trigger: "SystemConfigService", "Konfiguration lesen", "config get/set",
  "sales channel config", "system_config", "Einstellung auslesen", "config scope". Shopware 6.7.
---

# Shopware 6 — SystemConfigService

Zentraler Zugriff auf Konfiguration (Plugin-Config aus `config.xml`, Core-Settings, eigene Keys).

```php
$value   = $this->systemConfigService->get('FfContentPlus.config.apiKey', $salesChannelId);
$bool    = $this->systemConfigService->getBool('FfContentPlus.config.active', $salesChannelId);
$this->systemConfigService->set('FfContentPlus.config.apiKey', $newKey, $salesChannelId);
```

Scopes: ohne `$salesChannelId` = globaler Default; mit ID = Sales-Channel-Override (fällt auf global zurück).
Typisierte Getter (`getBool/getInt/getFloat/getString`) bevorzugen. Auf Config-Änderungen reagieren via
`SystemConfigChangedEvent` (`sw-events-subscriber`). Maske/Feldtypen definieren: `sw-plugin-config`.
