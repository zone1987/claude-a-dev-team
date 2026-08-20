# Shopware APIs — Vollständige Konzept-Doku

Quellen: `concepts/api/index.md`, `admin-api.md`, `store-api.md`

---

## API-Überblick (concepts/api/index.md)

Shopware stellt HTTP-basierte APIs bereit, über die externe Systeme und custom Applikationen
mit der Plattform interagieren können.

**Zwei funktionale APIs:**

- **Store API** — kundenseitige Interaktionen
- **Admin API** — administrative und systemseitige Operationen

Beide nutzen HTTP mit JSON-Payloads. Gemeinsame Design-Prinzipien:

- **Search Criteria Abstraktion** — Filter, Sorting, Pagination einheitlich
- **Strukturierte JSON Request/Response Bodies**
- **Header-basiertes kontextuelles Verhalten**

---

## Admin API (concepts/api/admin-api.md)

### Zweck

Administrative und Integrations-Oberfläche von Shopware. Ermöglicht strukturierten Zugriff auf:
- Produkte, Bestellungen, Kunden, Medien, Konfigurationen
- CRUD-Operationen für **alle Entitäten** in Shopware

### Einsatzgebiete

- Backend-Integrationen
- Automatisierung
- Datensynchronisation (Import/Export)
- System-zu-System-Kommunikation
- Benachrichtigungen

### Eigenschaften

- **Authentifizierung**: OAuth 2.0 (mandatory)
- **Prioritäten**: Konsistenz, Fehlerbehandlung, Validierung, transaktionale Integrität
- **Performance-Fokus**: hohe Datenlasten (nicht primär Response-Zeit)

### Referenz

https://shopware.stoplight.io/docs/admin-api/8d53c59b2e6bc-shopware-admin-api

---

## Store API (concepts/api/store-api.md)

### Zweck

Kundenseitige Oberfläche von Shopware. Designed für Storefront-/Frontend-Interaktionen:
- Produkte browsen
- Warenkorb verwalten
- Checkout durchführen
- Kundenkonto verwalten

Exponiert nur **kundensichere Daten** (kein Admin-Zugriff möglich).

### Architekturrolle

Normalisierter Interface-Layer zwischen Kundenfrontend und Shopware-Core:
- Headless Frontends (SPAs, native Apps) nutzen JSON over HTTP
- Core Business-Logik wird über HTTP-Routen exponiert
- **Storefront UND API-Konsumenten nutzen dieselben Store-API-Services** (keine Logik-Duplikation)

### Authentifizierung

- Öffentlich erreichbar (anonyme Nutzung für Browsing)
- Context-Token-Header (`sw-context-token`) für kundenbezogene Endpunkte
- Kein OAuth erforderlich

### Einsatz mit Composable Frontends

Shopware bietet "Composable Frontends" als headless Frontend-Implementierung auf Basis der Store API.

### Referenz

https://shopware.stoplight.io/docs/store-api/7b972a75a8d8d-shopware-store-api
