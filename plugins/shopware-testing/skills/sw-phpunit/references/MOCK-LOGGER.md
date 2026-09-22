---
title: Assert what was logged, not that logging happened
impact: MEDIUM
impactDescription: A recording logger makes the message and context assertable; a mock only proves a method was called
tags: mock, logging, monolog, unit-test
---

## A recording logger, not a mock

A service that logs is usually logging something a person will have to read. The test
should assert **what** was written, not merely that a method ran.

**Insufficient:**

```php
$logger = static::createMock(LoggerInterface::class);
$logger->expects($this->once())->method('warning');
```

This passes whatever the message says — including an empty string, or a message naming the
wrong entity.

**Sufficient:**

```php
$logger = new RecordingLogger();
$subject = new MyLoader($repository, $logger);

$subject->load($request, $context);

static::assertCount(1, $logger->records());
static::assertSame('warning', $logger->records()[0]['level']);
static::assertStringContainsString($categoryId, $logger->records()[0]['message']);
```

## The helper

`tests/Helper/RecordingLogger.php` — a `LoggerInterface` that keeps what it is given:

```php
<?php declare(strict_types=1);

namespace {PluginNamespace}\Tests\Helper;

use Psr\Log\AbstractLogger;

final class RecordingLogger extends AbstractLogger
{
    /** @var list<array{level: string, message: string, context: array<string, mixed>}> */
    private array $records = [];

    /**
     * @param mixed $level
     * @param string|\Stringable $message
     * @param array<string, mixed> $context
     */
    public function log($level, $message, array $context = []): void
    {
        $this->records[] = [
            'level'   => (string) $level,
            'message' => (string) $message,
            'context' => $context,
        ];
    }

    /** @return list<array{level: string, message: string, context: array<string, mixed>}> */
    public function records(): array
    {
        return $this->records;
    }
}
```

Extending `AbstractLogger` means the eight level methods (`warning()`, `error()`, …) all
route through `log()`, so only one method has to be written.

## Naming: never `run()` or `result()`

**A test helper must not be called `run()` or `result()`.** Both are `final` on PHPUnit's
`TestCase`, and the fatal takes the whole suite down — with an error that points at the
helper rather than at the collision.

## What is logged in the first place

The plugin's own log channel is set to `level: warning`, so only things worth somebody's
attention are written. A test asserting that normal operation logs nothing is as valuable
as one asserting that a failure logs something.

→ The logging setup itself: `sw-platform` → `LOGGING.md` in the `shopware-core` plugin.
