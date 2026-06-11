# Shopware Extensions — Vollständige Konzept-Doku

Quellen: `concepts/extensions/index.md`, `apps-concept.md`, `plugins-concept.md`

---

## Extensions Überblick (index.md)

Shopware Core ist so designed, dass Erweiterbarkeit ohne Beeinträchtigung von Wartbarkeit
oder struktureller Integrität möglich ist.

**Zwei Extensionstypen:**

| | Apps | Plugins |
|---|---|---|
| Ausführung | Außerhalb Shopware-Prozess | Innerhalb Shopware-Prozess |
| Kommunikation | HTTP-Webhooks + Admin API | Direkter Code-Zugriff |
| Cloud-kompatibel | Ja (SaaS + Self-hosted) | **Nein** (nur Self-hosted) |
| Technologie | Beliebig | PHP (Symfony Bundle) |

---

## Apps (apps-concept.md)

### Design-Ziel: Entkopplung

Das App-System ist von Shopware selbst entkoppelt — zwei Vorteile:

1. **Technologie-Freiheit** — Nur die HTTP-Schnittstelle muss verstanden werden; keine Shopware-Internals nötig. Beliebige Sprache/Framework für den App-Backend-Server.
2. **Cloud-kompatibel** — Funktioniert mit Multi-Tenant-Cloud-Systemen (Shopware SaaS).

### Zentrales Interface: Manifest (`manifest.xml`)

- Verbindet Shopware und die App
- Definiert Features der App und wie Shopware sich verbindet
- Muss mit jeder App ausgeliefert werden

### Kommunikation

**Shopware → App**: HTTP-POST an definierte Endpoints (Webhooks); App reagiert auf Events
**App → Shopware**: Admin REST API für Datenzugriff und -modifikation

Beim Installieren: **Registration Handshake** — Shopware verifiziert App-Server, App erhält API-Credentials.

### App-Capabilities

#### Storefront-Erscheinungsbild anpassen

- Twig-Templates, JavaScript, SCSS, Snippets mitliefern
- Shopware rebuildet Storefront bei App-Installation automatisch
- Keine Bereitstellung über externen Server nötig

#### Payment-Provider integrieren (ab 6.4.1.0)

- **Synchrone Payments** — keine Nutzer-Interaktion; Hintergrundanfrage für Genehmigung
- **Asynchrone Payments** — Nutzer-Redirect; App liefert Redirect-URL; nach Rückkehr: Shopware verifiziert Status bei App

#### App Scripts (ab 6.4.8.0)

- Custom Business-Logik **im Shopware Execution Stack** ausführen
- Use Cases: zusätzliche Daten für Storefront laden, Cart manipulieren
- Twig-basiert (sicher, keine direkten PHP-Aufrufe)

#### Rule Builder Conditions (ab 6.4.12.0)

- Custom Bedingungen für den Rule Builder hinzufügen
- Über `manifest.xml` deklarieren

---

## Plugins (plugins-concept.md)

### Konzept

Plugins sind **Symfony Bundle Extensions** — basieren auf Symfony Bundles und erweitern diese.

Bundles/Plugins können bereitstellen:
- Assets (Templates, CSS, JS)
- Controllers
- Services (DI-Container)
- Tests

### Basisklasse

Abstrakte Base Class (`PluginBaseClass`) mit Helper-Methoden:
- Plugin-Name und Root-Path im DI-Container initialisieren
- Helper für Lifecycle (install, update, uninstall, activate, deactivate)

Jedes Plugin = Composer-Package (kann Abhängigkeiten definieren).

### Tiefer Zugriff

Plugins können fast alles:
- Custom User Provider
- Custom Search Engine
- Beliebige Symfony-Services überschreiben oder dekorieren

### Cloud-Inkompatibilität

**Wichtig**: Plugins sind wegen direktem Prozess- und Datenbankzugriff **nicht** mit Shopware Cloud
kompatibel. Für Cloud: App-System verwenden.
