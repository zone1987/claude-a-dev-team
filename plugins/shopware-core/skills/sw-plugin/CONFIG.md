# Shopware 6 — Plugin-Konfiguration

`src/Resources/config/config.xml` definiert die Einstellungsmaske (Admin → Erweiterungen → Konfiguration).
Aufbau: `<card>` → `<input-field type="...">` mit `<name>`, `<label>`, `<defaultValue>`.
Feldtypen u.a.: `text`, `bool`, `int`, `float`, `single-select`, `multi-select`, `password`, `colorpicker`, `datetime`.

Auslesen im Code über `SystemConfigService` (Key = `{PluginName}.config.{feldName}`):

```php
$value = $this->systemConfigService->get('FfContentPlus.config.apiKey', $salesChannelId);
```

`$salesChannelId` ist optional (Sales-Channel-spezifischer Override). Details zum SystemConfigService und Scopes: `sw-system-config`.

→ Vollständige Feldtypen, Optionen, Bundles: [CONFIG-CONFIGURATION.md](CONFIG-CONFIGURATION.md)
→ Beispiel: [examples/config.xml](examples/config.xml)
