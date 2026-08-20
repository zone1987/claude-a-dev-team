---
name: sw-messaging
description: Shopware messaging: the message queue, handlers, middleware, Redis configuration. Use when the request names a Shopware message queue, message handler or Redis.
---

# Shopware message queue

Asynchronous work through Symfony Messenger, with Shopware's own middleware and transports.

## Reference map

- **[MESSAGE-HANDLER.md](MESSAGE-HANDLER.md)**: A handler processes a message asynchronously.
- **[MESSAGE-MIDDLEWARE.md](MESSAGE-MIDDLEWARE.md)**: Middleware wraps every message on the bus.
- **[MESSAGE-QUEUE.md](MESSAGE-QUEUE.md)**: Shopware uses Symfony Messenger for asynchronous tasks. [MESSAGE-QUEUE-DETAIL](MESSAGE-QUEUE-DETAIL.md).
- **[REDIS.md](REDIS.md)**: Redis is used in Shopware optionally as fast storage for several subsystems — through configuration. [REDIS-DETAIL](REDIS-DETAIL.md).

## Source

Distilled from [developer.shopware.com](https://developer.shopware.com) (framework guides and reference) plus the Shopware 6.7 source, retrieved 2026-08-20.
