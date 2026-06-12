# Shopware Nexus — Vollständige Referenz

> **Beta-Hinweis:** Shopware Nexus befindet sich in der Beta-Phase. Funktionen
> sind eingeschränkt und können sich in zukünftigen Updates erweitern.

## Was ist Shopware Nexus?

Nexus ist eine unified Platform für **event-getriebene Automatisierung und
Integration**. Händler können Systeme visuell per Low-Code orchestrieren und
skalierbare Workflows erstellen, die Shopware mit ERPs, CRMs und anderen
Business-Systemen verbinden.

## Key Capabilities

| Feature | Beschreibung |
|---------|-------------|
| Visual Workflow Builder | Drag-and-Drop-Interface |
| Shopware Event Triggers | Reagiert auf Entity-Events |
| Schedule Triggers | Cron-basierte Ausführung |
| Business Central Integration | CRUD für Items, Customers, Sales Orders |
| Shopware API Actions | Beliebige Shopware-Endpunkte aufrufen |
| API Requests | Generische HTTP-Calls |
| Slack Notifications | Slack-Nachrichten senden |
| Conditional Logic | If/else und Switch-Branching |
| S3 Storage | Daten in S3 speichern |
| Data Transformation | Daten mappen und filtern |
| Expression Placeholders | `{{payload.field}}` für Daten-Interpolation |
| Execution Monitoring | Runs und Metriken verfolgen |
| Delay Node | Verzögerungen zwischen Schritten |

## Nicht verfügbar in Beta

- SLA-Garantien
- 24/7 Support
- Multi-Region-Deployment (nur EU)
- On-Premise/Self-Hosted
- Workflow-Marketplace

## Geplant nach Beta

| Feature | Zeitrahmen |
|---------|-----------|
| AI-Assisted Authoring | GA |
| Advanced Analytics | GA |
| Per-Tenant Quotas | GA |
| Workflow Versioning UI | GA |
| SAP, Oracle Konnektoren | Post-GA |
| Custom Node Development | Post-GA |

---

## Getting Started

### Voraussetzungen

- Shopware 6.7 oder neuer
- Aktives Shopware-Abonnement
- Beta-Zugang durch Shopware gewährt
- Nexus-Service aktiviert
- Shopware Services aktiv (T&Cs akzeptiert, Shop in SBP registriert)

### Zugang

1. Login via Shopware SSO (Ory / OIDC)
2. Nach Authentifizierung: Nexus leitet zu einem Demo-Workflow weiter
3. Workflow wird funktional sobald der Shop verbunden ist

### Shop verbinden

Shops werden aus der Shopware Business Platform gezogen.

> **Beta-Limitation:** Nur das erste Unternehmen des User-Accounts wird
> verwendet. Nur Shops dieses Unternehmens sind in Nexus verfügbar.

### Workflow erstellen

Anleitung in der [User-Dokumentation](https://docs.shopware.com/en/shopware-6-en/shopware-services/shopware-nexus?category=shopware-6-en/insider-previews).

### Bekannte Beta-Limitierungen

| Limitation | Workaround |
|------------|------------|
| Kein Test-Modus | Staging-Shops verwenden |
| Begrenzte Fehlerdetails | Log-Nodes hinzufügen |
| Kein Undo/Redo | Häufig speichern |
| At-least-once delivery | Idempotente Workflows designen |

---

## Workflow Builder

### Workflow-Struktur

Ein Workflow besteht aus Nodes auf einem Canvas:

1. **Trigger** — startet den Workflow
2. **Actions** — tun etwas (API-Calls, ERP-Writes, Notifications)
3. **Transforms** — Daten formen/filtern
4. **Conditions** — Verzweigungslogik
5. **Outputs** — Ergebnisse speichern

### Workflow-Builder-Interface

| Element | Beschreibung |
|---------|-------------|
| Canvas | Visueller Arbeitsbereich |
| Node Palette | Verfügbare Nodes |
| Node Configuration | Parameter, Credentials, Notes, Debug |
| Toolbar | Save, Publish, Execute, Undeploy |
| Execution Tab | Run-Historie und Metriken |

### Workflow-Zustände

| Zustand | Beschreibung | Verfügbare Aktionen |
|---------|-------------|---------------------|
| Draft | Bearbeitung | Save, Publish |
| Published | Bereit | Execute |
| Deploying | Deployment wird erstellt | — |
| Active | Läuft | Undeploy |
| Inactive | Deployed aber gestoppt | Execute, Delete |
| Undeploying | Deployment wird entfernt | — |
| Failed | Deployment oder Ausführung fehlgeschlagen | Retry, Delete |

### Execution Metrics

- Status (Success / Failed / Running)
- Ausführungsdauer
- Verarbeitete Messages pro Node
- Fehler-Anzahl und Latenz

### Monitoring-Limitierungen (Beta)

- Keine per-Node Execution-Logs
- Begrenzte Payload-Inspektion
- Manuelles Refresh erforderlich

---

## Node-Typen

### Trigger-Nodes

| Node | Beschreibung | Konfiguration |
|------|-------------|--------------|
| Shopware Event Trigger | Reagiert auf Entity-Events | Shop, Event |
| Schedule Trigger | Zeitbasierte Ausführung | Cron, Timezone |

### Action-Nodes

| Node | Beschreibung | Konfiguration |
|------|-------------|--------------|
| Business Central | CRUD auf BC-Entities | Entity, Operation |
| Shopware API Call | Beliebiger Shopware-API-Aufruf | Method, Endpoint |
| Send Slack Message | Slack-Notification | Channel, Template |
| API Request | Generischer HTTP-Call | URL, Headers |
| Send Shopware Email | E-Mail via Shopware | Empfänger, Inhalt |

### Transform-Nodes

| Node | Beschreibung |
|------|-------------|
| Filter | Array-Items filtern |

### Condition-Nodes

| Node | Beschreibung |
|------|-------------|
| If | True/False Bedingung |
| Switch | Komplexe Verzweigungslogik |

### Control-Nodes

| Node | Beschreibung |
|------|-------------|
| Delay | Verzögerung vor Fortfahren |

### Output-Nodes

| Node | Beschreibung |
|------|-------------|
| S3 Storage | Payload in S3 speichern |

---

## Expression-Syntax

Expressions verwenden `{{ }}`-Syntax in Templates und Mappings.

### Beispiele

```text
{{payload.order.orderNumber}}
{{bc_customers_response.value[0].id}}
{{customer.firstName}} {{customer.lastName}}
```

### Häufige Verwendung

- **Slack-Templates:** Lesbare Notification-Messages erstellen
- **Daten-Mapping:** Werte aus Trigger-Payload an Action-Parameter übergeben
- **Branching:** `If`-Bedingungen auf Basis von Payload-Werten

---

## Business Central Integration

### Unterstützte Entities

- Customers
- Items
- Sales Orders

### Verfügbare Operationen (alle Entities)

| Operation | Beschreibung |
|-----------|-------------|
| `getAll` | Alle Records abrufen |
| `getOne` | Einzelnen Record per Identifier abrufen |
| `createOrUpdate` | Record erstellen oder aktualisieren |
| `delete` | Record entfernen |
| `action` | Spezifische Aktion auf Entity ausführen |

### OData Filter-Beispiele

Business Central unterstützt OData-Filtersyntax:

```text
email eq 'john@example.com'
inventory lt 10
status eq 'Open'
externalDocumentNumber eq 'SW-10001'
```

---

## Sicherheit & Datenschutz

| Aspekt | Detail |
|--------|--------|
| Authentifizierung | Shopware SSO |
| Verschlüsselung | AES-256-GCM via AWS KMS |
| Storage | Tenant-isoliert |
| Infrastruktur | EU-basiert (eu-central-1) |

---

## Troubleshooting

| Problem | Lösung |
|---------|--------|
| Workflow stuck deploying | Neu deployen (Redeploy) |
| Unauthorized errors | Neu authentifizieren |
| Fehlende Event-Daten | Payload mit Log-Node inspizieren |
| BC-Filter gibt leeres Ergebnis | OData-Syntax validieren |
| Slack-Nachricht wird nicht gesendet | Slack neu autorisieren |
