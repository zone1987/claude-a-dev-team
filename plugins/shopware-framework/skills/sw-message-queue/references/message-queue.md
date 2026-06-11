# Message Queue

## Overview

Shopware uses Symfony Messenger for async message processing. Plugins can dispatch messages to be handled asynchronously by background workers.

## Message Class

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

## Message Handler

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

## Dispatching Messages

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

## Service Registration

With autoconfigure, handlers are auto-tagged:

```xml
<service id="FfContentPlus\MessageQueue\ImportProductHandler"/>
```

## Running the Worker

```bash
# Process messages
ddev exec bin/console messenger:consume async

# With time limit
ddev exec bin/console messenger:consume async --time-limit=60

# With memory limit
ddev exec bin/console messenger:consume async --memory-limit=128M

# Specific transport
ddev exec bin/console messenger:consume async low_priority
```

## Middleware

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

## Best Practices

1. **Messages must be serializable** — use only scalar types and arrays
2. **Keep messages small** — pass IDs, not full entities
3. **Handle failures gracefully** — messages may be retried
4. **Use `AsyncMessageInterface`** — marks messages for async processing
5. **Batch operations** — dispatch many small messages rather than one large one
