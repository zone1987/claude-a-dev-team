# Contao Async Messaging & Jobs (5.x)

---

## Teil 1: Async Messaging (Symfony Messenger ab 5.1)

### Standard-Transport-Konfiguration

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

Nachrichten werden in der Tabelle `tl_message_queue` gespeichert – verwaltet von `DoctrineSchemaListener` via `contao:migrate`.

---

### WebWorker-Fallback

Verarbeitet Nachrichten während `kernel.terminate` wenn kein dedizierter Worker aktiv ist:

- Smart Detection via `WorkerStartedEvent` / `WorkerRunningEvent` (10-Minuten-Puffer)
- Zeitlimit via `max_execution_time`
- Deferred Processing nach Response-Auslieferung (`fastcgi_finish_request()`)

```yaml
contao:
    messenger:
        web_worker:
            transports:
                - contao_prio_high
                - contao_prio_normal
                - contao_prio_low
            grace_period: 'PT5M'   # Erkennungsfenster anpassen
```

**WebWorker deaktivieren:**
```yaml
contao:
    messenger:
        web_worker:
            transports: []
```

---

### Eingebauter Cron-Job-Prozessmanager (Shared Hosting)

Startet minutenlange `messenger:consume`-Worker automatisch mit Autoscaling:

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

Voraussetzung: Konfigurierter Minuten-Cronjob für `contao:cron`.

**Worker deaktivieren:**
```yaml
contao:
    messenger:
        workers: []
```

---

### Message-Routing

#### Contao >= 5.7 – AsMessage-Attribut (empfohlen)

```php
use Symfony\Component\Messenger\Attribute\AsMessage;

#[AsMessage('contao_prio_high')]
class CreateAsyncZipFileMessage
{
    public function __construct(public array $fileIds) {}
}
```

#### Prioritäts-Interfaces (alle Versionen)

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

### Vollständiges Implementierungsbeispiel

```php
// 1. Message-Klasse
namespace App\Messenger;

class CreateAsyncZipFileMessage
{
    public function __construct(public array $fileIds) {}
}

// 2. Message-Handler
use Symfony\Component\Messenger\Attribute\AsMessageHandler;

#[AsMessageHandler]
class CreateAsyncZipFileMessageHandler
{
    public function __invoke(CreateAsyncZipFileMessage $message): void
    {
        foreach ($message->fileIds as $fileId) {
            // Asynchrone Verarbeitungslogik
        }
    }
}
```

Referenz-Implementierung: `SearchIndexMessage`, `SearchIndexMessageHandler`, `SearchIndexListener` im Contao Core.

---

## Teil 2: Jobs-Framework (ab Contao 5.7, experimentell)

> **Experimentell** – nicht durch BC-Promise abgedeckt.

### Einstiegspunkt

```php
use Contao\CoreBundle\Job\Jobs;

public function __construct(private Jobs $jobs) {}
```

---

### Jobs erstellen

```php
// Aktueller Nutzer oder System-Job
$job = $this->jobs->createJob('data_export');

// Öffentlicher System-Job
$job = $this->jobs->createSystemJob('cache_clear', public: true);

// Nutzerspezifischer Job
$job = $this->jobs->createUserJob('import_task', $userId);
```

---

### Job-Eigenschaften

```php
$job->getUuid();        // string
$job->getType();        // string
$job->getStatus();      // Status-Enum (new, pending, completed, …)
$job->getOwner();       // Owner-Objekt
$job->getCreatedAt();   // DateTimeImmutable
$job->isPublic();       // bool
```

> **Wichtig:** Jobs sind immutable – Methoden geben modifizierte Kopien zurück.

---

### Status-Übergänge

```php
$job = $job->markPending();
$job = $job->markCompleted();
$job = $job->markFailed(['my_error']);
$job = $job->withWarnings(['my_warning']);
$job = $job->withErrors(['my_error']);
$job = $job->markFailedBecauseRequiresCLI();
```

---

### Fortschritt verwalten

```php
// Manueller Prozentsatz (0–100)
$job = $job->withProgress(42.5);

// Aus Mengen berechnen
$job = $job->withProgressFromAmounts(50, 200);   // = 25%

// Unbekannte Gesamtzahl (logarithmisch, max. 95%)
$job = $job->withProgressFromAmounts(10, null);

// Abschließen (setzt 100% automatisch)
$job = $job->markCompleted();
```

---

### Jobs abrufen und speichern

```php
$jobs = $this->jobs->findMyNewOrPending();
$job  = $this->jobs->getByUuid($uuid);

$this->jobs->persist($job);
```

---

### Anhänge hinzufügen

```php
// Text-Anhang
$this->jobs->addAttachment($job, 'report.txt', "Content\n");

// Stream-Anhang (für große Dateien)
$stream = fopen('/path/to/file.zip', 'rb');
$this->jobs->addAttachment($job, 'export.zip', $stream);
fclose($stream);
```

---

### Vollständiges Handler-Beispiel

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
            // Aufwändige Verarbeitung
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

*Quellen:*
- *https://docs.contao.org/5.x/dev/framework/async-messaging/*
- *https://docs.contao.org/5.x/dev/framework/jobs/*
