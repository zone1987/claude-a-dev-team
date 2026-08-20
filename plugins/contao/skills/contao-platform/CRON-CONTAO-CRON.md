# Contao Cron framework (5.x)

## Contents

- [Overview](#overview)
- [Configuring cron execution](#configuring-cron-execution)
- [Registering cron jobs](#registering-cron-jobs)
- [Scope-aware cron jobs](#scope-aware-cron-jobs)
- [Asynchronous cron jobs (Contao 5.1 and later)](#asynchronous-cron-jobs-contao-51-and-later)
- [Internals](#internals)

## Overview

Contao runs periodic tasks via cron (e.g. expired subscriptions, token cleanup). All cron jobs are services carrying the `contao.cronjob` tag.

---

## Configuring cron execution

### Default behavior (web listener)

By default, cron jobs run after the response has been sent to the visitor. From Contao 5.1 onwards, the front end cron disables itself automatically when a real cron system is detected.

```yaml
# config/config.yaml
contao:
    cron:
        web_listener: false   # Default: 'auto'
```

### CLI execution

```bash
vendor/bin/contao-console contao:cron

# Force a specific job
vendor/bin/contao-console contao:cron "App\Cron\ExampleCron" --force
```

**Recommended crontab entry:**
```
* * * * * /usr/bin/php /path/to/contao/vendor/bin/contao-console contao:cron
```

**Domain configuration for the CLI:**
```yaml
# config/parameters.yaml
parameters:
    router.request_context.host: 'example.org'
    router.request_context.scheme: 'https'
```

### Via web URL

```bash
* * * * * wget -q -O /dev/null https://example.org/_contao/cron
```

> **Important:** CLI-scoped cron jobs are not triggered through the web route.

---

## Registering cron jobs

### Method 1: PHP attributes (recommended)

```php
namespace App\Cron;

use Contao\CoreBundle\DependencyInjection\Attribute\AsCronJob;

#[AsCronJob('hourly')]
class ExampleCron
{
    public function __invoke(): void
    {
        // Implementation
    }
}
```

### Method 2: Annotations

```php
use Contao\CoreBundle\ServiceAnnotation\CronJob;

/** @CronJob("hourly") */
class ExampleCron
{
    public function __invoke(): void {}
}
```

### Method 3: YAML service tags

```yaml
services:
    App\Cron\ExampleCron:
        tags:
            - { name: contao.cronjob, interval: hourly }
```

### Intervals

| Value | Description |
|------|-------------|
| `minutely` | Every minute |
| `hourly` | Hourly |
| `daily` | Daily |
| `weekly` | Weekly |
| `monthly` | Monthly |
| `yearly` | Yearly |
| `*/5 * * * *` | CRON expression (arbitrary) |

---

## Scope-aware cron jobs

```php
use Contao\CoreBundle\Cron\Cron;
use Contao\CoreBundle\Exception\CronExecutionSkippedException;

#[AsCronJob('hourly')]
class HourlyCron
{
    public function __invoke(string $scope): void
    {
        if (Cron::SCOPE_WEB === $scope) {
            // Skip – prevents updating the last execution time
            throw new CronExecutionSkippedException();
        }
        // CLI execution only
    }
}
```

---

## Asynchronous cron jobs (Contao 5.1 and later)

Return a `PromiseInterface` for non-blocking execution:

```php
use GuzzleHttp\Promise\Promise;
use GuzzleHttp\Promise\PromiseInterface;

#[AsCronJob('hourly')]
class HourlyCron
{
    public function __invoke(string $scope): PromiseInterface
    {
        if (Cron::SCOPE_WEB === $scope) {
            throw new CronExecutionSkippedException();
        }

        return new Promise(static function () use (&$promise): void {
            // Asynchronous logic
            $promise->resolve('Completed');
        });
    }
}
```

### ProcessUtil helper

```php
use Contao\CoreBundle\Util\ProcessUtil;
use Symfony\Component\Process\Process;

class HourlyCron
{
    public function __construct(private ProcessUtil $processUtil) {}

    public function __invoke(string $scope): PromiseInterface
    {
        if (Cron::SCOPE_WEB === $scope) {
            throw new CronExecutionSkippedException();
        }

        // Any process
        $promise = $this->processUtil->createPromise(
            new Process(['command', 'args'])
        );

        // Symfony console command
        $promise = $this->processUtil->createPromise(
            $this->processUtil->createSymfonyConsoleProcess('app:command', '--option', 'argument')
        );

        return $promise;
    }
}
```

---

## Internals

Contao stores the last execution in the `tl_cron_job` table.

---

*Source: https://docs.contao.org/5.x/dev/framework/cron/*
