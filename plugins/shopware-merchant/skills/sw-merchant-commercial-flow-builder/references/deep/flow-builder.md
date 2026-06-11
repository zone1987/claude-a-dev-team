# Shopware Flow Builder (Commercial Features) – Vollständige Dokumentation

## Überblick

Der Flow Builder ist Shopwares No-Code-Automatisierungstool für event-basierte Geschäftsprozesse.

**Pfad im Admin:** Einstellungen → Automatisierung → Flow Builder

**Verfügbarkeit nach Plan:**

| Feature | Plan |
|---|---|
| Flow Builder (Basis) | Community Edition |
| Flows teilen | Rise (ab 6.4.19.0) |
| Webhook-Aktionen | Evolve+ |
| Zeitverzögerte Aktionen | Beyond |

---

## Grundstruktur eines Flows

### 1. Trigger (Auslöser)

Jeder Flow beginnt mit einem Ereignis. Shopware bietet 100+ Trigger:

**Kundenbasiert:**
- Kunde registriert
- Kunde angemeldet
- Kundendaten geändert

**Bestellbasiert:**
- Bestellung aufgegeben
- Zahlungsstatus geändert
- Lieferstatus geändert
- Bestellung storniert

**Zahlungsbasiert:**
- Zahlung erfolgreich
- Zahlung fehlgeschlagen

**Benachrichtigungsbasiert:**
- Manuell ausgelöst (für Tests)

### 2. Bedingungen (Conditions)

Regeln aus dem Rule Builder können auf Flows angewendet werden:
- Jede Bedingung evaluiert als TRUE oder FALSE
- Verzweigung: Unterschiedliche Aktionen je nach Ergebnis
- Mehrere Bedingungen können verkettet werden

### 3. Aktionen (Actions)

**Kommunikation:**
- E-Mail versenden (mit optionalen Dokumentenanhängen)
- Benachrichtigung an Admin

**Dokumente:**
- Rechnung generieren
- Lieferschein generieren
- Gutschrift generieren

**Status-Management:**
- Bestellstatus setzen
- Zahlungsstatus setzen
- Lieferstatus setzen

**Kundenverwaltung:**
- Kundengruppe ändern
- Tag hinzufügen/entfernen
- Konto aktivieren/deaktivieren

**Digitale Produkte:**
- Download-Rechte vergeben

**Marketing:**
- Affiliate-Code zuweisen
- Kampagnencode zuweisen

**Benutzerdefiniert:**
- Custom Fields befüllen

---

## Commercial Feature: Flows teilen (Rise+, ab 6.4.19.0)

Flows können zwischen Shopware-Instanzen geteilt werden:

### Export
1. Flow in der Liste öffnen
2. „Flow exportieren" → JSON-Datei wird heruntergeladen

### Import
1. Neuer Flow → „Flow importieren"
2. JSON-Datei hochladen
3. System erstellt automatisch fehlende Referenzen (Kundengruppen, Tags etc.)

**Anwendungsfall:** Entwicklungs- und Produktionssystem synchron halten

---

## Commercial Feature: Webhook-Aktionen (Evolve+)

Flows können externe Systeme via HTTP-Anfragen ansprechen.

### Konfiguration
| Feld | Optionen |
|---|---|
| Methode | GET, POST, PUT, PATCH, DELETE |
| URL | Ziel-Endpoint |
| Parameter | Key-Value-Paare (URL-Parameter) |
| Header | Benutzerdefinierte HTTP-Header |
| Body | JSON oder Form-Data |
| Authentifizierung | Basic Auth (Benutzername + Passwort) |

### Anwendungsfälle
- CRM bei neuer Bestellung benachrichtigen
- ERP-System bei Statusänderungen updaten
- Slack-Nachricht bei kritischen Ereignissen senden
- Externe Lagerssysteme ansprechen

---

## Commercial Feature: Zeitverzögerte Aktionen (Beyond)

Flows können Aktionen zeitgesteuert ausführen.

### Delay-Optionen
| Einheit | Beschreibung |
|---|---|
| Stunden | X Stunden nach Trigger |
| Tage | X Tage nach Trigger |
| Wochen | X Wochen nach Trigger |
| Monate | X Monate nach Trigger |
| Benutzerdefiniert | Frei konfigurierbares Format |

### Anwendungsfälle
- 7 Tage nach Kauf: Bewertungsanfrage-E-Mail senden
- 3 Tage vor Abo-Verlängerung: Erinnerung senden
- 30 Tage nach letztem Kauf: Reaktivierungs-E-Mail
- 1 Tag nach Bestellabbruch: Erinnerung (mit Rule Builder Bedingung)

---

## Konfigurationstabs

### Tab: Allgemein
| Feld | Beschreibung |
|---|---|
| Name | Interne Bezeichnung des Flows |
| Beschreibung | Erläuterung des Zwecks |
| Priorität | Ausführungsreihenfolge bei mehreren Flows mit gleichem Trigger (höher = früher) |
| Aktiv | Flow aktivieren/deaktivieren |

### Tab: Flow
Visueller Editor mit:
- Trigger-Auswahl
- Bedingungsblöcke (TRUE/FALSE-Verzweigung)
- Aktionsblöcke (parallel oder sequenziell)
- Flow-Vorlagen für häufige Anwendungsfälle

---

## Custom Triggers (ab 6.5.3.0)

Drittanbieter-Integrationen können externe System-Ereignisse als Flow-Trigger registrieren. Dadurch können externe Systeme Shopware-Flows auslösen.

---

## Praxisbeispiele

### Beispiel 1: Bestellbestätigung mit Rechnung
- **Trigger:** Bestellung aufgegeben
- **Aktion 1:** Rechnung generieren
- **Aktion 2:** E-Mail mit Rechnungsanhang senden

### Beispiel 2: VIP-Kunde nach Umsatz (Evolve)
- **Trigger:** Bestellung bezahlt
- **Bedingung:** Gesamtumsatz Kunde > 1.000 €
- **TRUE:** Kundengruppe → „VIP"
- **FALSE:** Keine Aktion

### Beispiel 3: Nachfass-E-Mail mit Delay (Beyond)
- **Trigger:** Bestellung abgeschlossen
- **Delay:** 7 Tage
- **Aktion:** Bewertungsanfrage-E-Mail senden

---

*Quelle: https://docs.shopware.com/de/shopware-6-de/einstellungen/Flow-Builder (Stand: 2026-06)*
