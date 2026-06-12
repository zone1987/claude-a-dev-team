# Contao Logging (5.x)

## Überblick

Contao nutzt **Monolog** und das **Symfony Monolog Bundle** als Logging-Infrastruktur. Der `contao`-Kanal ist für Framework-spezifische Nachrichten reserviert.

---

## System-Log-Integration

Nachrichten mit `ContaoContext` werden automatisch im Contao-Backend-System-Log angezeigt:

```php
use Contao\CoreBundle\Monolog\ContaoContext;

$logger->info(
    'Diese Nachricht erscheint im Contao System-Log',
    ['contao' => new ContaoContext(__METHOD__, ContaoContext::GENERAL)]
);
```

---

## ContaoContext-Aktionen

| Konstante | Zweck |
|-----------|-------|
| `ContaoContext::GENERAL` | Allgemeine Meldungen |
| `ContaoContext::CRON` | Cron-Job-Meldungen |
| `ContaoContext::ACCESS` | Zugriffsprotokolle |
| `ContaoContext::FILES` | Dateisystem-Operationen |
| `ContaoContext::FORMS` | Formular-Verarbeitung |
| `ContaoContext::ERROR` | Fehlermeldungen |
| `ContaoContext::EMAIL` | E-Mail-Versand |
| `ContaoContext::CONFIGURATION` | Konfigurationsänderungen |

---

## Vorkonfigurierte Logger-Services

### Via Service-Tag

```yaml
# config/services.yaml
services:
    App\MyService:
        arguments:
            - '@?logger'
        tags:
            - { name: monolog.logger, channel: contao.cron }
```

Kanäle mit `contao.`-Präfix erhalten automatisch passende `ContaoContext`-Zuweisungen. Das Suffix bestimmt die Kontextaktion (z.B. `contao.cron` → `ContaoContext::CRON`).

### Autowiring

```php
use Psr\Log\LoggerInterface;

public function __construct(
    private readonly LoggerInterface $contaoCronLogger,
    private readonly LoggerInterface $contaoErrorLogger,
) {}
```

### Explizite Service-Injektion

```yaml
services:
    App\MyService:
        arguments:
            - '@monolog.logger.contao.cron'
            - '@monolog.logger.contao.error'
```

---

## Verfügbare Contao-Kanäle

| Kanal | Verwendung |
|-------|-----------|
| `contao.access` | Zugriffsprotokolle |
| `contao.configuration` | Konfiguration |
| `contao.cron` | Cron-Jobs |
| `contao.email` | E-Mail-Versand |
| `contao.error` | Fehler |
| `contao.files` | Datei-Operationen |
| `contao.forms` | Formulare |
| `contao.general` | Allgemein |

---

## Erweiterbarkeit

Monolog unterstützt Handler, Formatter und Processors. Referenz-Implementierungen: `ContaoTableProcessor`, `ContaoTableHandler`.

---

## Testing-Strategie

- Logger als optionale Abhängigkeit konfigurieren (vereinfacht Tests)
- `Psr\Log\NullLogger` für Szenarien wo Logger-Aufrufe irrelevant sind
- `Psr\Log\LoggerInterface` mocken zum Verifizieren von Logger-Interaktionen

---

*Quelle: https://docs.contao.org/5.x/dev/framework/logging/*
