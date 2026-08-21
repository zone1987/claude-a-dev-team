# Shopware messaging — concept

Complete concept documentation: `MESSAGING-DATA-STORES.md`

## Brief overview

Shopware integrates **Symfony Messenger** + Enqueue for asynchronous message processing.

### Core components

| Component | Description |
|---|---|
| **Message bus** | `messenger.default_bus` — the central dispatch point; mandatory for Shopware-internal messages |
| **Message** | Serialisable PHP object with all data the handler needs |
| **Handler** | Callable with `#[AsMessageHandler]`; `__invoke()` with a typed message parameter |
| **Middleware** | Processes the message on dispatch (e.g. `send_message`, `handle_message`) |
| **Envelope** | Wrapper around the message with stamps (metadata) |
| **Transport** | Connection to a message broker (AMQP, SQS, Redis, Doctrine, etc.) |

### Synchronous vs. asynchronous

- Without a configured transport: **synchronous processing** (like Symfony events)
- With a transport: **asynchronous processing** via a background worker

### Consumption

- CLI: `bin/console messenger:consume` — persistent worker
- API: POST endpoint — processes for 2 seconds, returns the count

### Sensitive bus

An additional message bus for encrypted/sensitive data is available.

Technical implementation: `shopware-framework` (dev plugin)
