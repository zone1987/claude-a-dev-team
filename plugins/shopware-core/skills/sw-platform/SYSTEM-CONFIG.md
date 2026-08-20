# Shopware 6 — SystemConfigService

Central access to configuration (plugin config from `config.xml`, core settings, your own keys).

```php
$value   = $this->systemConfigService->get('FfContentPlus.config.apiKey', $salesChannelId);
$bool    = $this->systemConfigService->getBool('FfContentPlus.config.active', $salesChannelId);
$this->systemConfigService->set('FfContentPlus.config.apiKey', $newKey, $salesChannelId);
```

Scopes: without `$salesChannelId` = global default; with an ID = sales channel override (falls back to global).
Prefer the typed getters (`getBool/getInt/getFloat/getString`). React to config changes via
`SystemConfigChangedEvent` (`sw-events-subscriber`). Defining the form/field types: `sw-plugin-config`.
