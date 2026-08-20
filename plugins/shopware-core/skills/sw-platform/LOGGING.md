# Shopware 6 — Logging

Plugins should log into their **own Monolog channel** (a dedicated file under `var/log/`), not into the
core channel. A common pattern: a `PluginLoggerTrait` registering a plugin-specific logger in `build()`.

```php
// in the plugin class
use PluginLoggerTrait;
public function build(ContainerBuilder $container): void
{
    parent::build($container);
    $this->registerPluginLogger($container, $this->getPath());
}
```

Alternatively declare it in `monolog.yaml` (channel + handler). Then inject the logger as `Psr\Log\LoggerInterface` with
the matching channel binding. Log levels follow the ADR "exception log levels" (no debug spam in production).

→ Trait: [examples/PluginLoggerTrait.php](examples/PluginLoggerTrait.php)
→ Channel config: [examples/monolog.yaml](examples/monolog.yaml)
