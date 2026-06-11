---
name: sw-logging
description: >
  Logging in Shopware-6-Plugins: eigener Monolog-Channel, plugin-eigene Log-Datei, PluginLoggerTrait,
  Log-Levels. Trigger: "Plugin logging", "Monolog channel", "eigene Logdatei", "logger injizieren",
  "PluginLoggerTrait", "logger.factory", "shopware log". Shopware 6.7.
---

# Shopware 6 — Logging

Plugins sollten in einen **eigenen Monolog-Channel** loggen (eigene Datei unter `var/log/`), nicht in den
Core-Channel. forty-four-Muster: `PluginLoggerTrait` registriert in `build()` einen plugin-spezifischen Logger.

```php
// in der Plugin-Klasse
use PluginLoggerTrait;
public function build(ContainerBuilder $container): void
{
    parent::build($container);
    $this->registerPluginLogger($container, $this->getPath());
}
```

Alternativ deklarativ via `monolog.yaml` (Channel + Handler). Logger dann als `Psr\Log\LoggerInterface` mit
passendem Channel-Binding injizieren. Log-Levels gemäß ADR „exception log levels" (kein Debug-Spam in Prod).

→ Trait: [examples/PluginLoggerTrait.php](examples/PluginLoggerTrait.php)
→ Channel-Konfig: [examples/monolog.yaml](examples/monolog.yaml)
