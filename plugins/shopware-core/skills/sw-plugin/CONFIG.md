# Shopware 6 — Plugin Configuration

`src/Resources/config/config.xml` defines the settings form (Admin → Extensions → Configuration).
Structure: `<card>` → `<input-field type="...">` with `<name>`, `<label>`, `<defaultValue>`.
Field types include `text`, `bool`, `int`, `float`, `single-select`, `multi-select`, `password`, `colorpicker`, `datetime`.

Read values in code through the `SystemConfigService` (key = `{PluginName}.config.{fieldName}`):

```php
$value = $this->systemConfigService->get('FfContentPlus.config.apiKey', $salesChannelId);
```

`$salesChannelId` is optional (sales-channel-specific override). Details on the SystemConfigService and scopes: `sw-system-config`.

→ All field types, options, bundles: [CONFIG-CONFIGURATION.md](CONFIG-CONFIGURATION.md)
→ Example: [examples/config.xml](examples/config.xml)
