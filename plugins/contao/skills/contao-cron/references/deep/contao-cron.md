# Contao Cron-Framework (5.x)

## Überblick

Contao führt periodische Aufgaben via Cron aus (z.B. abgelaufene Subscriptions, Token-Bereinigung). Alle Cron-Jobs sind Services mit dem Tag `contao.cronjob`.

---

## Cron-Ausführung konfigurieren

### Standard-Verhalten (Web-Listener)

Standardmäßig werden Cron-Jobs nach dem Response an den Besucher ausgeführt. Ab Contao 5.1 deaktiviert sich der Frontend-Cron automatisch wenn ein echtes Cron-System erkannt wird.

```yaml
# config/config.yaml
contao:
    cron:
        web_listener: false   # Standard: 'auto'
```

### CLI-Ausführung

```bash
vendor/bin/contao-console contao:cron

# Spezifischen Job erzwingen
vendor/bin/contao-console contao:cron "App\Cron\ExampleCron" --force
```

**Empfohlener Crontab-Eintrag:**
```
* * * * * /usr/bin/php /path/to/contao/vendor/bin/contao-console contao:cron
```

**Domain-Konfiguration für CLI:**
```yaml
# config/parameters.yaml
parameters:
    router.request_context.host: 'example.org'
    router.request_context.scheme: 'https'
```

### Via Web-URL

```bash
* * * * * wget -q -O /dev/null https://example.org/_contao/cron
```

> **Wichtig:** CLI-scoped Cron-Jobs werden nicht über die Web-Route ausgelöst.

---

## Cron-Jobs registrieren

### Methode 1: PHP-Attribute (empfohlen)

```php
namespace App\Cron;

use Contao\CoreBundle\DependencyInjection\Attribute\AsCronJob;

#[AsCronJob('hourly')]
class ExampleCron
{
    public function __invoke(): void
    {
        // Implementierung
    }
}
```

### Methode 2: Annotations

```php
use Contao\CoreBundle\ServiceAnnotation\CronJob;

/** @CronJob("hourly") */
class ExampleCron
{
    public function __invoke(): void {}
}
```

### Methode 3: YAML-Service-Tags

```yaml
services:
    App\Cron\ExampleCron:
        tags:
            - { name: contao.cronjob, interval: hourly }
```

### Intervalle

| Wert | Beschreibung |
|------|-------------|
| `minutely` | Jede Minute |
| `hourly` | Stündlich |
| `daily` | Täglich |
| `weekly` | Wöchentlich |
| `monthly` | Monatlich |
| `yearly` | Jährlich |
| `*/5 * * * *` | CRON-Ausdruck (beliebig) |

---

## Scope-aware Cron-Jobs

```php
use Contao\CoreBundle\Cron\Cron;
use Contao\CoreBundle\Exception\CronExecutionSkippedException;

#[AsCronJob('hourly')]
class HourlyCron
{
    public function __invoke(string $scope): void
    {
        if (Cron::SCOPE_WEB === $scope) {
            // Überspringen – verhindert Aktualisierung der letzten Ausführungszeit
            throw new CronExecutionSkippedException();
        }
        // Nur CLI-Ausführung
    }
}
```

---

## Asynchrone Cron-Jobs (ab Contao 5.1)

Gibt ein `PromiseInterface` zurück für nicht-blockierende Ausführung:

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
            // Asynchrone Logik
            $promise->resolve('Completed');
        });
    }
}
```

### ProcessUtil-Helper

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

        // Beliebiger Prozess
        $promise = $this->processUtil->createPromise(
            new Process(['command', 'args'])
        );

        // Symfony-Console-Kommando
        $promise = $this->processUtil->createPromise(
            $this->processUtil->createSymfonyConsoleProcess('app:command', '--option', 'argument')
        );

        return $promise;
    }
}
```

---

## Interna

Contao speichert die letzte Ausführung in der Tabelle `tl_cron_job`.

---

*Quelle: https://docs.contao.org/5.x/dev/framework/cron/*
