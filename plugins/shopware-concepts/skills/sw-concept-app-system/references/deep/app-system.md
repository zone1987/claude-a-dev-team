# Shopware App-System — Vollständige Konzept-Doku

Quellen: `concepts/extensions/apps-concept.md`, `concepts/framework/in-app-purchases.md`

---

## App-System (apps-concept.md)

Das App-System ermöglicht Erweiterung und Anpassung von Shopware-Funktionalität und -Erscheinungsbild.
Nutzt wohldefinierte Extension Points.

### Architektur-Prinzip

**Entkopplung** von Shopware:
- Nur HTTP-Schnittstelle muss verstanden werden (kein Shopware-Internals-Wissen nötig)
- Freie Technologiewahl für App-Backend-Server
- Deployment von Shopware und App unabhängig
- Admin API + Webhooks als Kommunikationsmedium (statt Sprachkonstrukte)

**Folge**: App ist automatisch Multi-Tenant-Cloud-kompatibel (Shopware SaaS).

### Manifest (`manifest.xml`)

Zentrales Bindeglied zwischen Shopware und App:
- Definiert verfügbare Features
- Beschreibt Endpoints für Shopware-Anfragen
- Deklariert Permissions
- Registriert Webhooks, Actions, CMS-Blöcke, etc.

Mehr Details: App Base Guide in der Shopware-Dokumentation.

### Kommunikation Shopware ↔ App

**Shopware → App** (Events/Webhooks):
- HTTP-POST an in manifest.xml definierte Endpoints
- App abonniert Events, die sie interessieren

**App → Shopware** (Daten):
- Admin REST API für Lesen und Schreiben von Shopware-Daten

**Sicherheit**: Registration Handshake bei Installation:
- Shopware verifiziert App-Backend-Server
- App erhält Credentials für API-Authentifizierung

**Optional**: Falls App und Shopware nicht kommunizieren müssen (z.B. reine Theme-App)
ist die Registrierung optional.

### App-Capabilities

#### 1. Storefront-Erscheinungsbild anpassen

Assets (Twig-Templates, JS-Quellen, SCSS, Snippets) mit `manifest.xml` mitliefern.
Shopware rebuildet Storefront automatisch bei App-Installation.
Keine Bereitstellung der Assets über externen Server nötig.

#### 2. Payment-Provider integrieren (ab 6.4.1.0)

**Synchrone Payments**: Keine Benutzerinteraktion; Genehmigung via Hintergrundanfrage.
**Asynchrone Payments**: Benutzer-Redirect; App liefert Redirect-URL;
nach Rückkehr: Shopware verifiziert Zahlungsstatus bei App.

#### 3. App Scripts (ab 6.4.8.0)

Business-Logik **im Shopware Execution Stack** (nicht auf externem Server):
- Use Case 1: Zusätzliche Daten laden, die im Storefront gerendert werden sollen
- Use Case 2: Cart manipulieren
- Implementierung: Twig-basiert (sicherer als direktes PHP)
- Läuft innerhalb Shopware, nicht auf App-Server → kein Webhook benötigt

#### 4. Custom Rule Builder Conditions (ab 6.4.12.0)

Eigene Bedingungen für den Rule Builder hinzufügen.
Deklaration in `manifest.xml`.

---

## In-App Purchases / IAP (in-app-purchases.md)

Ab Shopware 6.6.9.0 verfügbar.

### Konzept

Features hinter Paywall **innerhalb derselben Extension** — Free Tier mit limitierten Features,
Paid Version mit mehr Features.

### IAP erstellen

Erstellung im Shopware Account.
Dokumentation: Extension Partner-Bereich in Shopware Account.

### Token-Mechanismus (JWT)

- Jeder In-App Purchase repräsentiert durch **signiertes JWT** (issued per Extension)
- JWT stellt sicher: Kauf-Daten können nicht manipuliert oder gefälscht werden
- **Alle gekauften IAPs** sind Teil der JWT Claims

**Verifikation**:
- JWKS: `https://api.shopware.com/inappfeatures/jwks`
- Shopware verifiziert Signatur automatisch für Core und Admin

**Token-Aktualisierung**:
- Automatisch bei neuen Käufen und bei periodischen Updates
- Manuell: `bin/console scheduled-task:run-single in-app-purchase.update`
- Oder: `POST /api/_action/in-app-purchases/refresh`

### IAP für Apps (empfohlen)

Optimiert für App-Server-Use-Case:
- IAP JWT wird bei **jedem** Request von Shopware an App-Server mitgesendet
- App-Server validiert aktive Käufe und schaltet entsprechende Features frei
- Apps sind inherent sicherer für IAP (kein direkter Code-Zugriff)

### IAP für Plugins (weniger empfohlen)

Plugins sind weniger sicher wegen offener Natur (anfälliger für Spoofing/Tampering).

### Checkout-Prozess

Shopware übernimmt den **gesamten Checkout-Prozess** (Payment + Subscription Management).
Extension muss nur IAP-Identifier bereitstellen → Modal-Window für Kauf wird automatisch geöffnet.
