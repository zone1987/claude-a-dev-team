# Shopware 6 — Logging

**Every plugin logs into its own Monolog channel**, never into the core one.

**Why:** the shop's log is full. Somebody looking for one plugin's warning searches it
among thousands of lines other code wrote. A dedicated channel writes a dedicated file
that holds only what this plugin has to say.

## The configuration

`src/Resources/config/packages/monolog.yaml`:

```yaml
monolog:
    channels:
        - '{log-channel}'

    handlers:
        {pluginNameCamel}:
            type: rotating_file
            path: "%kernel.logs_dir%/{log-channel}/%kernel.environment%.log"
            level: warning
            max_files: 14
            channels: ['{log-channel}']
```

`{log-channel}` is snake_case and carries the vendor prefix, e.g. `acme_product_badge`.

| Setting | Value | Why |
|---|---|---|
| `type` | `rotating_file` | one file per day. A single file grows until nobody can open it |
| `path` | `…/{log-channel}/<env>.log` | its own directory, split by environment |
| `level` | `warning` | see *What is logged* below |
| `max_files` | `14` | long enough to investigate something reported on a Friday |
| `channels` | only its own | **without this line the handler catches everything**, including other code's messages |

→ Full file: [examples/logging-monolog.yaml](../examples/logging-monolog.yaml)

## The plugin class must override `build()` — this is the trap

**Shopware does not load `Resources/config/packages/` by itself.**
`Bundle::registerContainerFile()` loads `Resources/config/services.*` and nothing else.

Without the following code the `monolog.yaml` exists but has no effect — and the failure
is silent. Nothing is logged, and the cause looks like a problem in the logging call.

```php
/**
 * @throws LoaderLoadException when no loader can read the packages glob
 */
#[\Override]
public function build(ContainerBuilder $container): void
{
    parent::build($container);

    // Bundle::registerContainerFile() loads Resources/config/services.*; packages/ is not.
    $locator = new FileLocator('Resources/config');
    $resolver = new LoaderResolver([
        new YamlFileLoader($container, $locator),
        new GlobFileLoader($container, $locator),
        new DirectoryLoader($container, $locator),
    ]);

    $configLoader = new DelegatingLoader($resolver);
    $configLoader->load(rtrim($this->getPath(), '/') . '/Resources/config/{packages}/*.yaml', 'glob');
}
```

`rtrim($this->getPath(), '/')` is needed because `getPath()` ends with a slash or without
it depending on how the plugin was installed.

→ As a reusable trait: [examples/logging-PluginLoggerTrait.php](../examples/logging-PluginLoggerTrait.php)

## The service alias

Monolog derives a service `monolog.logger.<channel>` from the channel name. Give it a
readable alias in the plugin's own service definitions:

```php
$services->alias('{log-channel}.logger', 'monolog.logger.{log-channel}')
    ->public();
```

## What is logged

**Only things worth somebody's attention.** `level: warning` is the floor — `info` and
`debug` are never written.

Examples of what belongs in the log:

- a record whose category cannot be resolved
- a position outside the listing
- a lookup that returned nothing where something was expected

**What never goes in:**

| What | Why not |
|---|---|
| normal operation | a log that writes on every page view is a log nobody reads |
| personal data | GDPR. A customer id is personal as soon as it is tied to an account |
| full request payloads | same reason, plus disk |
| credentials, tokens, keys | never, under any circumstance |

## In a test

Inject the logger as `Psr\Log\LoggerInterface` and replace it with a **recording logger**
in the test — never with a mock.

```php
$logger = new RecordingLogger();
$subject = new SomeService($repository, $logger);

$subject->doTheThing($request, $context);

static::assertCount(1, $logger->records());
static::assertSame('warning', $logger->records()[0]['level']);
```

**Why not a mock:** `expects($this->once())->method('warning')` proves the method was
called. It does not prove **what** was logged — and the message is the whole point of the
log line.

→ The recording logger and the rest of the test setup: the `sw-testing-standard` skill in
the `shopware-testing` plugin.
