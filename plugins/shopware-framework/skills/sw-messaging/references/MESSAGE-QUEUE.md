# Shopware 6 — Message Queue

Shopware uses Symfony Messenger for asynchronous tasks. A message is a simple DTO; a handler processes it
(see `sw-message-handler`). Dispatch through the bus:

```php
$this->bus->dispatch(new FfImportMessage($id));
```

Transports: `async` (default) and `low_priority` (e.g. indexing). The worker consumes:
`ddev exec bin/console messenger:consume async low_priority`. In production run it as a daemon (Supervisor);
failed messages end up in the `failed` transport (`messenger:failed:*`).

Suitable for long/expensive operations (import, mail sending, indexing). Recurring on a schedule → `sw-scheduled-task`.
Own middleware: `sw-message-middleware`.

## Message Queue

### Contents

- [Overview](#overview)
- [Message Class](#message-class)
- [Message Handler](#message-handler)
- [Dispatching Messages](#dispatching-messages)
- [Service Registration](#service-registration)
- [Running the Worker](#running-the-worker)
- [Middleware](#middleware)
- [Best Practices](#best-practices)

### Overview

Shopware uses Symfony Messenger for async message processing. Plugins can dispatch messages to be handled asynchronously by background workers.

### Message Class

```php
<?php declare(strict_types=1);

namespace FfContentPlus\MessageQueue;

use Shopware\Core\Framework\Log\Package;
use Shopware\Core\Framework\MessageQueue\AsyncMessageInterface;

/**
 * @class ImportProductMessage
 * @package FfContentPlus\MessageQueue
 */
#[Package('custom-plugins')]
class ImportProductMessage implements AsyncMessageInterface
{
    /**
     * @param string $productId
     * @param string $externalId
     */
    public function __construct(
        private readonly string $productId,
        private readonly string $externalId,
    ) {}

    /**
     * @return string
     */
    public function getProductId(): string
    {
        return $this->productId;
    }

    /**
     * @return string
     */
    public function getExternalId(): string
    {
        return $this->externalId;
    }
}
```

### Message Handler

```php
<?php declare(strict_types=1);

namespace FfContentPlus\MessageQueue;

use Shopware\Core\Framework\Log\Package;
use Symfony\Component\Messenger\Attribute\AsMessageHandler;

/**
 * @class ImportProductHandler
 * @package FfContentPlus\MessageQueue
 */
#[AsMessageHandler]
#[Package('custom-plugins')]
class ImportProductHandler
{
    /**
     * @param MyImportService $importService
     */
    public function __construct(
        private readonly MyImportService $importService,
    ) {}

    /**
     * @param ImportProductMessage $message
     * @return void
     */
    public function __invoke(ImportProductMessage $message): void
    {
        $this->importService->importProduct(
            $message->getProductId(),
            $message->getExternalId()
        );
    }
}
```

### Dispatching Messages

```php
use Symfony\Component\Messenger\MessageBusInterface;

class MyService
{
    public function __construct(
        private readonly MessageBusInterface $messageBus,
    ) {}

    public function scheduleImport(string $productId, string $externalId): void
    {
        $this->messageBus->dispatch(
            new ImportProductMessage($productId, $externalId)
        );
    }
}
```

### Service Registration

```php
<?php declare(strict_types=1);

namespace FfContentPlus\Resources\config\services;

use FfContentPlus\MessageQueue\ImportProductHandler;
use Symfony\Component\DependencyInjection\Loader\Configurator\ContainerConfigurator;

use function Symfony\Component\DependencyInjection\Loader\Configurator\service;

return static function (ContainerConfigurator $containerConfigurator): void {
    $services = $containerConfigurator->services();

    $services->set(ImportProductHandler::class)
        ->args([service('product.repository')])
        // Without autoconfigure this tag is not inferred from #[AsMessageHandler].
        ->tag('messenger.message_handler');
};
```

`#[AsMessageHandler]` alone registers nothing here: the attribute is read through
`registerForAutoconfiguration`, which this setup does not use. The class exists, the
service is registered, and the message is never handled — the queue simply grows.

### Running the Worker

```bash
## Process messages
ddev exec bin/console messenger:consume async

## With time limit
ddev exec bin/console messenger:consume async --time-limit=60

## With memory limit
ddev exec bin/console messenger:consume async --memory-limit=128M

## Specific transport
ddev exec bin/console messenger:consume async low_priority
```

### Middleware

Add middleware to process messages before/after handling:

```php
use Symfony\Component\Messenger\Envelope;
use Symfony\Component\Messenger\Middleware\MiddlewareInterface;
use Symfony\Component\Messenger\Middleware\StackInterface;

class LoggingMiddleware implements MiddlewareInterface
{
    public function handle(Envelope $envelope, StackInterface $stack): Envelope
    {
        // Before handling
        $this->logger->info('Processing message', [
            'class' => get_class($envelope->getMessage()),
        ]);

        $envelope = $stack->next()->handle($envelope, $stack);

        // After handling
        return $envelope;
    }
}
```

### Best Practices

1. **Messages must be serializable** — use only scalar types and arrays
2. **Keep messages small** — pass IDs, not full entities
3. **Handle failures gracefully** — messages may be retried
4. **Use `AsyncMessageInterface`** — marks messages for async processing
5. **Batch operations** — dispatch many small messages rather than one large one
