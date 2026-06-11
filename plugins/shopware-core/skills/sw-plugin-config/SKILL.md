---
name: sw-plugin-config
description: >
  Plugin-Konfiguration in Shopware 6: config.xml (Cards, Input-Felder, Typen, Defaults) und das Auslesen
  via SystemConfigService. Trigger: "config.xml", "Plugin-Konfiguration", "Plugin-Einstellungen",
  "plugin settings", "Konfigurationsfeld", "SystemConfigService lesen", "Plugin config admin". Shopware 6.7.
  Scaffolder: /sw-config-create.
---

# Shopware 6 — Plugin-Konfiguration

`src/Resources/config/config.xml` definiert die Einstellungsmaske (Admin → Erweiterungen → Konfiguration).
Aufbau: `<card>` → `<input-field type="...">` mit `<name>`, `<label>`, `<defaultValue>`.
Feldtypen u.a.: `text`, `bool`, `int`, `float`, `single-select`, `multi-select`, `password`, `colorpicker`, `datetime`.

Auslesen im Code über `SystemConfigService` (Key = `{PluginName}.config.{feldName}`):

```php
$value = $this->systemConfigService->get('FfContentPlus.config.apiKey', $salesChannelId);
```

`$salesChannelId` ist optional (Sales-Channel-spezifischer Override). Details zum SystemConfigService und Scopes: `sw-system-config`.

→ Vollständige Feldtypen, Optionen, Bundles: [references/configuration.md](references/configuration.md)
→ Beispiel: [examples/config.xml](examples/config.xml)
