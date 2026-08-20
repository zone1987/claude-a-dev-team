# Contao Logging (5.x)

## Contents

- [Overview](#overview)
- [System log integration](#system-log-integration)
- [ContaoContext actions](#contaocontext-actions)
- [Preconfigured logger services](#preconfigured-logger-services)
- [Available Contao channels](#available-contao-channels)
- [Extensibility](#extensibility)
- [Testing strategy](#testing-strategy)

## Overview

Contao uses **Monolog** and the **Symfony Monolog Bundle** as its logging infrastructure. The `contao` channel is reserved for framework-specific messages.

---

## System log integration

Messages with a `ContaoContext` are shown automatically in the Contao back end system log:

```php
use Contao\CoreBundle\Monolog\ContaoContext;

$logger->info(
    'This message appears in the Contao system log',
    ['contao' => new ContaoContext(__METHOD__, ContaoContext::GENERAL)]
);
```

---

## ContaoContext actions

| Constant | Purpose |
|-----------|-------|
| `ContaoContext::GENERAL` | General messages |
| `ContaoContext::CRON` | Cron job messages |
| `ContaoContext::ACCESS` | Access logs |
| `ContaoContext::FILES` | Filesystem operations |
| `ContaoContext::FORMS` | Form processing |
| `ContaoContext::ERROR` | Error messages |
| `ContaoContext::EMAIL` | E-mail dispatch |
| `ContaoContext::CONFIGURATION` | Configuration changes |

---

## Preconfigured logger services

### Via service tag

```yaml
# config/services.yaml
services:
    App\MyService:
        arguments:
            - '@?logger'
        tags:
            - { name: monolog.logger, channel: contao.cron }
```

Channels with the `contao.` prefix automatically receive matching `ContaoContext` assignments. The suffix determines the context action (e.g. `contao.cron` → `ContaoContext::CRON`).

### Autowiring

```php
use Psr\Log\LoggerInterface;

public function __construct(
    private readonly LoggerInterface $contaoCronLogger,
    private readonly LoggerInterface $contaoErrorLogger,
) {}
```

### Explicit service injection

```yaml
services:
    App\MyService:
        arguments:
            - '@monolog.logger.contao.cron'
            - '@monolog.logger.contao.error'
```

---

## Available Contao channels

| Channel | Usage |
|-------|-----------|
| `contao.access` | Access logs |
| `contao.configuration` | Configuration |
| `contao.cron` | Cron jobs |
| `contao.email` | E-mail dispatch |
| `contao.error` | Errors |
| `contao.files` | File operations |
| `contao.forms` | Forms |
| `contao.general` | General |

---

## Extensibility

Monolog supports handlers, formatters and processors. Reference implementations: `ContaoTableProcessor`, `ContaoTableHandler`.

---

## Testing strategy

- Configure the logger as an optional dependency (simplifies tests)
- `Psr\Log\NullLogger` for scenarios where logger calls are irrelevant
- Mock `Psr\Log\LoggerInterface` to verify logger interactions

---

*Source: https://docs.contao.org/5.x/dev/framework/logging/*
