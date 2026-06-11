# Shopware Messaging — Vollständige Konzept-Doku

Quelle: `concepts/framework/messaging.md`

---

## Messaging-Konzept

Shopware integriert **Symfony Messenger** + Enqueue für asynchrone Nachrichten-Verarbeitung.

### Komponenten

#### Message Bus

- Service-Tag: `messenger.default_bus`
- **Pflicht** für Shopware-interne Nachrichten
- Verarbeitet Nachrichten durch konfigurierte Middleware
- Für externe Systeme: eigener custom Message Bus konfigurierbar

#### Middleware

Wird beim Dispatch durch den Message Bus aufgerufen.
Definiert was beim Dispatch passiert.

Wichtige Standard-Middleware:
- `send_message` — sendet Nachricht an konfigurierten Transport
- `handle_message` — ruft Handler für Nachricht auf

**Eigene Middleware**: `MiddlewareInterface` implementieren + in Message Bus-Konfiguration registrieren.

#### Handler

Wird aufgerufen, wenn `handle_messages` Middleware eine Nachricht verarbeitet.

```php
#[AsMessageHandler]
class MyMessageHandler
{
    public function __invoke(MyMessage $message): void
    {
        // Handler-Logik
    }
}
```

PHP-Callable; empfohlener Weg: Klasse mit `#[AsMessageHandler]` Attribut und `__invoke()` Methode
mit typisierten Message-Parameter.

#### Message

Einfaches PHP-Objekt:
- Muss serialisierbar sein
- Enthält alle für den Handler notwendigen Informationen

#### Envelope

Message Bus wrapp Message in **Envelope** vor dem Dispatch.

#### Stamps

Middleware fügt **Stamps** zum Envelope hinzu — enthalten Metadaten über die Nachricht.

**Eigene Stamps**: Message in Envelope wrappen + Stamps vor Dispatch hinzufügen,
oder eigene custom Middleware erstellen.

#### Transport

Verbindung zum 3rd-Party-Message-Broker.
Mehrere Transports konfigurierbar; Messages auf verschiedene Transports routbar.

**Unterstützte Transports**:
- Alle [Symfony-Transports](https://symfony.com/doc/current/messenger.html#transports) (AMQP, Redis, Doctrine, etc.)
- Alle [Enqueue-Transports](https://github.com/php-enqueue/enqueue-dev/tree/master/docs/transport) (SQS, Kafka, etc.)

**Kein Transport konfiguriert**: synchrone Verarbeitung (wie Symfony Event System).

### Nachrichten senden

```php
// Injection des default message bus via DI
public function __construct(private MessageBusInterface $bus) {}

// Dispatch
$this->bus->dispatch(new MyMessage($data));
```

Optionaler Bus für sensitive/verschlüsselte Daten verfügbar.

### Nachrichten konsumieren

**Via CLI (Worker)**:
```bash
bin/console messenger:consume
```
Startet persistenten Worker der eingehende Nachrichten vom Transport empfängt und dispatcht.

**Via API**:
- HTTP POST-Endpoint
- Verarbeitet Nachrichten für 2 Sekunden
- Response: Anzahl verarbeiteter Nachrichten
