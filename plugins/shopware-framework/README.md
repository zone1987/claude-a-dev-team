# shopware-framework

> Die Framework-Bausteine oberhalb der DAL: Async, Regeln, Flows, APIs, Mail, Media, Suche.

`shopware-framework` deckt die **Framework-Features oberhalb der reinen DAL** ab — also alles, womit ein Plugin
Geschäftslogik, Asynchronität, Erweiterungspunkte und Schnittstellen umsetzt.

Enthalten: **ScheduledTasks** (Cron-artige Aufgaben) und die **Message Queue** (Symfony Messenger: Messages,
Handler, Middleware) für asynchrone Verarbeitung; der **Rule Builder** (eigene Rules + Admin-Bedingungen) und der
**Flow Builder** (eigene Actions, Trigger, Transaktionsverhalten) für konfigurierbare Automatisierung; eigene
**Store-API-Routen** (kundenseitig) und **Admin-API-Controller** (Backend-Aktionen) samt **ACL**; **Webhooks** für
externe Empfänger; **App-Scripts** (Twig-basierte Server-Logik); **Mail** (Templates + Daten/Events, inkl. des
**vollständigen Variablen-Baums** aller 39 Standard-Mail-Templates); **Media & Thumbnails**; sowie die Such-/
Performance-Infrastruktur **Elasticsearch/OpenSearch** und **Redis** (Cache, Cart-Persister, Session, Locks).

Der Spezialist **`shopware-framework-dev`** und die Scaffolder **`/sw-scheduled-task`**, **`/sw-flow-action`**,
**`/sw-rule`**, **`/sw-store-api-route`** beschleunigen die Umsetzung. **Wann nutzen:** für wiederkehrende/
asynchrone Jobs, regel-/flow-basierte Logik, eigene API-Endpunkte, Mailversand, Medien oder Suche. Datenmodelle
dazu liefert `shopware-data`, das Plugin-Fundament `shopware-core`.

Teil des Marketplace **[claude-a-dev-team](../../README.md)**. Das Wissen ist aus den offiziellen Quellen destilliert und eingebettet; Skills laden ihre Tiefe progressiv aus `references/`.

## Installation

```
/plugin marketplace add https://github.com/zone1987/claude-a-dev-team
/plugin install shopware-framework@claude-a-dev-team
```

## Skills (25)

| Skill | Beschreibung |
|---|---|
| `sw-admin-api-controller` | Eigener Admin-API-Endpunkt (Aktion) in Shopware 6: Controller mit _routeScope api, /api/_action/..., Auth via Bearer, ACL-Absicherung |
| `sw-api-acl` | Zugriffsrechte (ACL) für Admin-API/Backend in Shopware 6: _acl-Route-Default, Privileges (entity:read/update/...), Privilegien für eigene Entities/Aktionen registrieren, Zusammenspiel mit Admin-ACL |
| `sw-app-script` | App Scripts in Shopware 6 (Twig-basierte Server-Logik für Apps): Script-Hooks, Resources/scripts/<hook>/, Services (data/store/cart), ohne eigenen App-Server |
| `sw-custom-rule` | Eigene Rule (Bedingung) für den Shopware-6 Rule Builder: Rule-Klasse (extends Rule), match(), constraints(), Admin-Komponente, Registrierung |
| `sw-elasticsearch` | Shopware Elasticsearch/OpenSearch Bundle |
| `sw-elasticsearch-extension` | Shopware Elasticsearch eigene Entities/Felder erweitern |
| `sw-events-reference` | Shopware 6 Webhook-Events Referenz — alle verfügbaren Events (checkout, order, state_enter/leave, newsletter, product, customer etc.), benötigte Permissions und Payload-Struktur |
| `sw-flow-action` | Eigene Flow-Builder-Action in Shopware 6: FlowAction (extends FlowAction / AppFlowAction), requirements/keys, handle(), Admin-Komponente, Registrierung |
| `sw-flow-reference` | Shopware 6 Flow-Action XML-Referenz für Apps — vollständige flow-action.xml-Struktur, Input-Felder, Parameter, Variablen je Event |
| `sw-flow-transaction` | Transaktionsverhalten von Flow-Builder-Actions in Shopware 6: transactional flow actions (Ausführung nach dem Business-Prozess), Fehler/Rollback, TransactionFailedException |
| `sw-flow-trigger` | Eigene Flow-Builder-Trigger (Business-Events) in Shopware 6 bereitstellen: FlowEventAware-Event, Aware-Interfaces, Event als Flow-Trigger registrieren, Storer |
| `sw-mail-data` | Daten/Variablen für Shopware-6 E-Mails bereitstellen: MailBeforeValidateEvent/MailBeforeSentEvent, eigene Template-Daten injizieren, MailSender, Anhänge |
| `sw-mail-template` | E-Mail-Templates in Shopware 6: MailTemplate/MailTemplateType per Migration/Repository anlegen, Twig-Inhalt (HTML+Plain), Variablen, Zuordnung zu Events/Flow |
| `sw-mail-variables` | Vollständiger Variablen-Baum für alle Shopware-6-Mail-Templates: welche Variablen im E-Mail-Template verfügbar sind, verschachtelter Variablenbaum per Template-Typ, Twig-Pfade (order.lineItems, order.orderCustomer.email usw.), auslösende Ev |
| `sw-media-handling` | Medien in Shopware 6 programmatisch verwalten: MediaService (Upload aus Datei/URL/Stream), media.repository, Ordner (media_folder), Media an Entities hängen, MediaType |
| `sw-media-thumbnail` | Thumbnails in Shopware 6: Thumbnail-Größen je Media-Folder, ThumbnailService generieren, media_thumbnail_size, Regenerierung (media:generate-thumbnails) |
| `sw-message-handler` | Message-Handler in Shopware 6 (Symfony Messenger): Handler mit #[AsMessageHandler], __invoke(Message), Registrierung, Idempotenz/Fehler |
| `sw-message-middleware` | Eigene Messenger-Middleware in Shopware 6: MiddlewareInterface, in den Message-Bus einklinken (z.B |
| `sw-message-queue` | Asynchrone Verarbeitung in Shopware 6 mit der Message Queue (Symfony Messenger): Message dispatchen (MessageBusInterface), async-Transport, Worker (messenger:consume), low_priority-Queue |
| `sw-redis` | Redis/Valkey in Shopware 6 nutzen: Cache, Cart-Persister, Session, Number-Range-Increment, Lock-Store, Messenger-Transport über Redis konfigurieren (config/packages, REDIS_URL, Adapter) |
| `sw-rule-condition` | Die Admin-Seite einer Shopware-6 Rule: Bedingungs-Komponente registrieren (sw-condition), Operatoren, Felder an die Rule-Constraints binden, Config-Component |
| `sw-scheduled-task` | Wiederkehrende Aufgaben in Shopware 6 via ScheduledTask: ScheduledTask + ScheduledTaskHandler, Intervall, Registrierung, Ausführung über scheduled-task:run / Cron |
| `sw-store-api-override` | Eine bestehende Shopware-6 Store-API-Route anpassen via Decoration (AbstractRoute dekorieren, getDecorated, inner-Route) |
| `sw-store-api-route` | Eigene Store-API-Route in Shopware 6: AbstractRoute + Route mit _routeScope store-api, Response-Struct, sw-access-key, Registrierung |
| `sw-webhook` | Webhooks in Shopware 6: Events an externe URLs senden (Webhook-Entity/Manifest), HMAC-Signatur, App-/Plugin-Kontext, Webhook-EventLog |

## Agents (1)

| Agent | Beschreibung |
|---|---|
| `shopware-framework-dev` | Spezialist für Shopware-6.7 Framework-Features: ScheduledTasks, Message Queue (Messenger), Rule Builder (eigene Rules), Flow Builder (Actions/Trigger/Transaktionen), Store-API-/Admin-API-Routen, ACL, Webhooks, App-Scripts, Mail-Templates/-D |

## Commands (4)

| Command | Beschreibung |
|---|---|
| `/sw-flow-action` | Scaffold einer Shopware-6 Flow-Builder-Action (PHP + Admin-Komponente) inkl |
| `/sw-rule` | Scaffold einer Shopware-6 Custom Rule (PHP Rule + Admin-Bedingungs-Komponente) für den Rule Builder, inkl |
| `/sw-scheduled-task` | Scaffold eines Shopware-6 ScheduledTask + Handler inkl. services.xml-Registrierung (Task-Tag + Message-Handler) |
| `/sw-store-api-route` | Scaffold einer Shopware-6 Store-API-Route (Abstract + Route + Response-Struct) mit _routeScope store-api und Registrierung |
