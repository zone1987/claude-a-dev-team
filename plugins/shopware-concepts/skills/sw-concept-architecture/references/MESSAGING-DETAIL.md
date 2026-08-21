# Shopware messaging — complete concept documentation

Source: `concepts/framework/messaging.md`

---

## Messaging concept

Shopware integrates **Symfony Messenger** + Enqueue for asynchronous message processing.

### Components

#### Message bus

- Service tag: `messenger.default_bus`
- **Mandatory** for Shopware-internal messages
- Processes messages through the configured middleware
- For external systems: a custom message bus of your own can be configured

#### Middleware

Called by the message bus on dispatch.
Defines what happens on dispatch.

Important standard middleware:
- `send_message` — sends the message to the configured transport
- `handle_message` — calls the handler for the message

**Custom middleware**: implement `MiddlewareInterface` + register it in the message bus configuration.

#### Handler

Called when the `handle_messages` middleware processes a message.

```php
#[AsMessageHandler]
class MyMessageHandler
{
    public function __invoke(MyMessage $message): void
    {
        // handler logic
    }
}
```

A PHP callable; the recommended way: a class with the `#[AsMessageHandler]` attribute and an `__invoke()` method
with a typed message parameter.

#### Message

A plain PHP object:
- Must be serialisable
- Contains all the information the handler needs

#### Envelope

The message bus wraps the message in an **envelope** before dispatch.

#### Stamps

Middleware adds **stamps** to the envelope — they contain metadata about the message.

**Custom stamps**: wrap the message in an envelope + add stamps before dispatch,
or create custom middleware of your own.

#### Transport

The connection to the 3rd-party message broker.
Several transports can be configured; messages can be routed onto different transports.

**Supported transports**:
- All [Symfony transports](https://symfony.com/doc/current/messenger.html#transports) (AMQP, Redis, Doctrine, etc.)
- All [Enqueue transports](https://github.com/php-enqueue/enqueue-dev/tree/master/docs/transport) (SQS, Kafka, etc.)

**No transport configured**: synchronous processing (like the Symfony event system).

### Sending messages

```php
// Injection of the default message bus via DI
public function __construct(private MessageBusInterface $bus) {}

// Dispatch
$this->bus->dispatch(new MyMessage($data));
```

An optional bus for sensitive/encrypted data is available.

### Consuming messages

**Via CLI (worker)**:
```bash
bin/console messenger:consume
```
Starts a persistent worker that receives incoming messages from the transport and dispatches them.

**Via API**:
- HTTP POST endpoint
- Processes messages for 2 seconds
- Response: the number of processed messages
