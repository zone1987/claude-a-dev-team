# Contao Async Messaging & Jobs (5.x)

---

## Part 1: Async messaging (Symfony Messenger, 5.1 and later)

### Default transport configuration

```yaml
framework:
    messenger:
        buses:
            messenger.bus.default:
                middleware:
                    - doctrine_ping_connection
                    - doctrine_close_connection
        failure_transport: contao_failure
        transports:
            sync: sync://
            contao_failure:    doctrine://default?table_name=tl_message_queue&queue_name=failure&auto_setup=false
            contao_prio_high:  doctrine://default?table_name=tl_message_queue&queue_name=prio_high&auto_setup=false
            contao_prio_normal: doctrine://default?table_name=tl_message_queue&queue_name=prio_normal&auto_setup=false
            contao_prio_low:   doctrine://default?table_name=tl_message_queue&queue_name=prio_low&auto_setup=false
```

Messages are stored in the `tl_message_queue` table – managed by the `DoctrineSchemaListener` via `contao:migrate`.

---

### WebWorker fallback

Processes messages during `kernel.terminate` when no dedicated worker is active:

- Smart detection via `WorkerStartedEvent` / `WorkerRunningEvent` (10-minute buffer)
- Time limit via `max_execution_time`
- Deferred processing after the response has been delivered (`fastcgi_finish_request()`)

```yaml
contao:
    messenger:
        web_worker:
            transports:
                - contao_prio_high
                - contao_prio_normal
                - contao_prio_low
            grace_period: 'PT5M'   # Adjust the detection window
```

**Disabling the WebWorker:**
```yaml
contao:
    messenger:
        web_worker:
            transports: []
```

---

### Built-in cron job process manager (shared hosting)

Automatically starts minute-long `messenger:consume` workers with autoscaling:

```yaml
contao:
    messenger:
        workers:
            -
                transports:
                    - contao_prio_high
                options:
                    - --time-limit=60
                    - --sleep=5
                autoscale:
                    desired_size: 5
                    max: 10
```

Prerequisite: a configured minutely cron job for `contao:cron`.

**Disabling the workers:**
```yaml
contao:
    messenger:
        workers: []
```

---

### Message routing

#### Contao >= 5.7 – the AsMessage attribute (recommended)

```php
use Symfony\Component\Messenger\Attribute\AsMessage;

#[AsMessage('contao_prio_high')]
class CreateAsyncZipFileMessage
{
    public function __construct(public array $fileIds) {}
}
```

#### Priority interfaces (all versions)

```php
use Contao\CoreBundle\Messenger\Message\HighPriorityMessageInterface;
use Contao\CoreBundle\Messenger\Message\NormalPriorityMessageInterface;
use Contao\CoreBundle\Messenger\Message\LowPriorityMessageInterface;

class MyMessage implements HighPriorityMessageInterface
{
    public function __construct(public array $fileIds) {}
}
```

```yaml
# Routing in framework.messenger.routing:
'Contao\CoreBundle\Messenger\Message\HighPriorityMessageInterface': contao_prio_high
'Contao\CoreBundle\Messenger\Message\NormalPriorityMessageInterface': contao_prio_normal
'Contao\CoreBundle\Messenger\Message\LowPriorityMessageInterface': contao_prio_low
```

---

### Complete implementation example

```php
// 1. Message class
namespace App\Messenger;

class CreateAsyncZipFileMessage
{
    public function __construct(public array $fileIds) {}
}

// 2. Message handler
use Symfony\Component\Messenger\Attribute\AsMessageHandler;

#[AsMessageHandler]
class CreateAsyncZipFileMessageHandler
{
    public function __invoke(CreateAsyncZipFileMessage $message): void
    {
        foreach ($message->fileIds as $fileId) {
            // Asynchronous processing logic
        }
    }
}
```

Reference implementation: `SearchIndexMessage`, `SearchIndexMessageHandler`, `SearchIndexListener` in the Contao core.

---

## Part 2: Jobs framework (Contao 5.7 and later, experimental)

> **Experimental** – not covered by the BC promise.

### Entry point

```php
use Contao\CoreBundle\Job\Jobs;

public function __construct(private Jobs $jobs) {}
```

---

### Creating jobs

```php
// Current user or system job
$job = $this->jobs->createJob('data_export');

// Public system job
$job = $this->jobs->createSystemJob('cache_clear', public: true);

// User-specific job
$job = $this->jobs->createUserJob('import_task', $userId);
```

---

### Job properties

```php
$job->getUuid();        // string
$job->getType();        // string
$job->getStatus();      // Status enum (new, pending, completed, …)
$job->getOwner();       // Owner object
$job->getCreatedAt();   // DateTimeImmutable
$job->isPublic();       // bool
```

> **Important:** Jobs are immutable – the methods return modified copies.

---

### Status transitions

```php
$job = $job->markPending();
$job = $job->markCompleted();
$job = $job->markFailed(['my_error']);
$job = $job->withWarnings(['my_warning']);
$job = $job->withErrors(['my_error']);
$job = $job->markFailedBecauseRequiresCLI();
```

---

### Managing progress

```php
// Manual percentage (0–100)
$job = $job->withProgress(42.5);

// Calculated from amounts
$job = $job->withProgressFromAmounts(50, 200);   // = 25%

// Unknown total (logarithmic, max. 95%)
$job = $job->withProgressFromAmounts(10, null);

// Finish (sets 100% automatically)
$job = $job->markCompleted();
```

---

### Retrieving and persisting jobs

```php
$jobs = $this->jobs->findMyNewOrPending();
$job  = $this->jobs->getByUuid($uuid);

$this->jobs->persist($job);
```

---

### Adding attachments

```php
// Text attachment
$this->jobs->addAttachment($job, 'report.txt', "Content\n");

// Stream attachment (for large files)
$stream = fopen('/path/to/file.zip', 'rb');
$this->jobs->addAttachment($job, 'export.zip', $stream);
fclose($stream);
```

---

### Complete handler example

```php
#[AsMessageHandler]
class MyMessageHandler
{
    public function __construct(
        private readonly Jobs $jobs,
        private readonly Connection $connection
    ) {}

    public function __invoke(MyMessage $message): void
    {
        $job = $this->jobs->getByUuid($message->getJobId());
        if (!$job || $job->isCompleted()) return;

        $job = $job->markPending();
        $this->jobs->persist($job);

        foreach ($this->connection->fetchAllAssociative('SELECT * FROM foo') as $i => $item) {
            // Expensive processing
            $job = $job->withProgressFromAmounts($i + 1);
            $this->jobs->persist($job);
        }

        $this->jobs->addAttachment($job, 'report.txt', "Export finished.\nRows: 123\n");
        $job = $job->markCompleted();
        $this->jobs->persist($job);
    }
}
```

---

*Sources:*
- *https://docs.contao.org/5.x/dev/framework/async-messaging/*
- *https://docs.contao.org/5.x/dev/framework/jobs/*
