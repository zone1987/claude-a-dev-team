# Shopware 6 — Logging

Plugins sollten in einen **eigenen Monolog-Channel** loggen (eigene Datei unter `var/log/`), nicht in den
Core-Channel. A-Dev-Team-Muster: `PluginLoggerTrait` registriert in `build()` einen plugin-spezifischen Logger.

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
