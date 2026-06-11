---
name: sw-concept-messaging
description: >
  Shopware Messaging (Symfony Messenger): Message Bus, Handler, Transport, asynchrone Verarbeitung.
  Trigger: "Messaging Shopware", "Message Queue", "Symfony Messenger Shopware",
  "asynchrone Verarbeitung", "Message Handler", "wie funktioniert die Message Queue",
  "shopware async", "MessageBus", "Transport konfigurieren", "Nachrichten konsumieren",
  "Worker Shopware", "shopware queue", "message dispatch", "Shopware Messenger Middleware".
---

# Shopware Messaging — Konzept

Vollständige Konzept-Doku: `references/deep/data-stores.md`

## Kurzüberblick

Shopware integriert **Symfony Messenger** + Enqueue für asynchrone Nachrichten-Verarbeitung.

### Kernkomponenten

| Komponente | Beschreibung |
|---|---|
| **Message Bus** | `messenger.default_bus` — zentraler Dispatch-Punkt; pflichtgemäß für Shopware-interne Nachrichten |
| **Message** | Serialisierbares PHP-Objekt mit allen Handler-notwendigen Daten |
| **Handler** | Callable mit `#[AsMessageHandler]`; `__invoke()` mit typisierten Message-Parameter |
| **Middleware** | Verarbeitet Nachricht beim Dispatch (z.B. `send_message`, `handle_message`) |
| **Envelope** | Hülle um Message mit Stamps (Metadaten) |
| **Transport** | Verbindung zu Message-Broker (AMQP, SQS, Redis, Doctrine, etc.) |

### Synchron vs. Asynchron

- Ohne konfigurierten Transport: **synchrone Verarbeitung** (wie Symfony Events)
- Mit Transport: **asynchrone Verarbeitung** via Background-Worker

### Konsum

- CLI: `bin/console messenger:consume` — persistenter Worker
- API: POST-Endpoint — verarbeitet 2 Sekunden lang, gibt Anzahl zurück

### Sensitiver Bus

Zusätzlicher Message Bus für verschlüsselte/sensitive Daten verfügbar.

Technische Umsetzung: `shopware-framework` (Dev-Plugin)
