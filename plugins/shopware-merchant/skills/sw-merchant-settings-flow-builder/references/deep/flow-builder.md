# Shopware 6 – Flow Builder (vollständige Referenz)

Quelle: https://docs.shopware.com/de/shopware-6-de/einstellungen/Flow-Builder

---

## Überblick

**Pfad:** Einstellungen > Automatisierung > Flow Builder

Ermöglicht die ereignisbasierte Automatisierung von Geschäftsprozessen ohne Programmierkenntnisse.

---

## Konfigurationsbereich „Allgemein"

| Feld | Funktion |
|---|---|
| Name | Identifikation in der Übersicht |
| Beschreibung | Aussagekräftige Erläuterung |
| Priorität | Ausführungsreihenfolge bei gleichen Triggern (höher = früher) |
| Aktiv | Temporäres Aktivieren/Deaktivieren |

---

## Hauptkomponenten

### 1. Trigger (Auslöser)

Über 80 verfügbare Ereignisse, kategorisiert:

**Kunden-Events:**
| Event | Zeitpunkt |
|---|---|
| `checkout.customer.before.login` | Vor dem Login |
| `checkout.customer.login` | Bei Login |
| `checkout.customer.register` | Neue Registrierung |
| `checkout.customer.deleted` | Kundenlöschung |

**Bestellungs-Events:**
| Event | Zeitpunkt |
|---|---|
| `checkout.order.placed` | Bestellung aufgegeben |
| `state_enter.order.state.*` | Statusänderungen (offen, in Bearbeitung, abgeschlossen, storniert) |

**Zahlungs-Events:**
| Event | Zeitpunkt |
|---|---|
| `state_enter.order_transaction.state.paid` | Zahlung erfolgt |
| `state_enter.order_transaction.state.refunded` | Erstattung |
| `checkout.order.payment_method.changed` | Zahlungsmethode geändert → setzt Status auto. auf „Offen" |

**Lieferungs-Events:**
| Event | Zeitpunkt |
|---|---|
| `state_enter.order_delivery.state.shipped` | Versandt |
| `state_enter.order_delivery.state.returned` | Retourniert |

**Marketing-Events:**
| Event | Zeitpunkt |
|---|---|
| `newsletter.register` | Newsletter-Anmeldung |
| `newsletter.confirm` | Newsletter-Bestätigung |
| `review_form.send` | Produktbewertung eingereicht |

**Mail-Events:**
| Event | Zeitpunkt |
|---|---|
| `mail.before.send` | Vor E-Mail-Versand |
| `mail.sent` | E-Mail versendet |

**Sonstige:**
| Event | Zeitpunkt |
|---|---|
| `contact_form.send` | Kontaktformular abgesendet |
| `customer.recovery.request` | Passwort-Wiederherstellung angefordert |

---

### 2. Bedingungen

- Basieren auf dem Rule Builder
- Zwei Ausgänge: **Wahr** oder **Falsch**
- Mehrere Bedingungen sequenziell kombinierbar
- Bestimmen, welche Aktion ausgeführt wird

---

### 3. Verzögerung (ab Plan Shopware Beyond)

**Verfügbare Zeiteinheiten:**
- Stunde, Tag, Woche, Monat
- Benutzerdefiniert: Format `SS.TT.WW.MM`

**Geplante Aktionen:**
Übersicht aller verzögerten Aktionen mit:
- Bestellnummer, Kundeninfo
- Verbleibende Zeit, geplanter Ausführungszeitpunkt

---

### 4. Aktionen

#### E-Mail verschicken
| Feld | Optionen |
|---|---|
| Empfänger | Administrator (alle Admin-Nutzer!), Kunde, spezifische E-Mail |
| Absender | Konfigurierbar |
| Template | Auswahl aus E-Mail-Templates |
| Anhänge | Dokumente optional hinzufügbar |

> **Achtung:** „Administrator" sendet an **ALLE** Admin-Benutzer inkl. externe (Agenturen, Dienstleister).

#### Status zuweisen
- Zahlungsstatus, Versandstatus, Bestellstatus ändern
- **Abhängigkeiten beachten:** Einige Status erfordern vorherige Status (z.B. „Erstattet" nur nach „Bezahlt")

#### Dokumente erzeugen
- Dokumenttyp im Dropdown auswählen
- Neues Dokument wird der Bestellung hinzugefügt

#### Tag hinzufügen / entfernen
- Nur für Tag-fähige Entitäten
- Flexible Tagging-Verwaltung

#### Kundengruppe zuweisen
- Kundengruppe über Dropdown ändern

#### Kontostatus zuweisen
- Kunde aktiv oder inaktiv setzen

#### Zusatzfeld zuweisen
| Feld | Beschreibung |
|---|---|
| Entität | Kunde oder Bestellung |
| Zusatzfeld-Set | Set auswählen |
| Spezifisches Feld | Feld konfigurieren |

#### Affiliate- und Kampagnen-Code zuweisen
- Entität (Kunde/Bestellung) + Code + Überschreib-Option

#### Download-Recht setzen
- Für digitale Produkte: Downloadlink freischalten oder sperren

#### Flow anhalten
- Stoppt den kompletten Flow
- Verhindert nachfolgende Aktionen
- Nützlich nach „Falsch"-Bedingungen

#### Call URL / Webhook (ab Plan Evolve)
**HTTP-Methoden:** GET, POST, PUT, PATCH, DELETE

| Feld | Beschreibung |
|---|---|
| URL | Ziel-Adresse |
| Parameter | Key-Value-Paare aus Shop-System |
| URL-Vorschau | Zeigt finale URL mit Parametern |
| Header-Parameter | Spezielle Server-Header |
| Body | JSON/Code-Format (Shopware-Variablen verfügbar) |
| Basic Auth | Authentifizierungsdaten |

---

## Custom Trigger (ab v6.5.3.0)

Drei Flow-Typen möglich:
1. Interne Shopware-Flows
2. Shopware-Events → Webhooks in Drittsystemen
3. Drittsystem-Events → Shopware-Flows

---

## Flows teilen & verwalten

### Herunterladen
Kontextmenü → **Herunterladen** → JSON-Export

> **Hinweis:** Kategorie-, Produkt-, Eigenschafts-Verweise müssen beim Upload neu zugeordnet werden.

### Hochladen
Einstellungen > Flow Builder → **Flow hochladen** → Datei wählen

### Flow-Templates
Von Shopware bereitgestellte Vorlagen für Standard-Flows.

---

## Verfügbarkeit nach Plan

| Feature | Plan |
|---|---|
| Basis-Aktionen | Standard |
| Flow-Teilen | Shopware Rise (ab v6.4.19.0) |
| Zeitverzögerte Aktionen | Shopware Beyond |
| Webhook-Aktionen (Call URL) | Shopware Evolve |

---

## Wichtige Hinweise

- `checkout.order.payment_method.changed` setzt Zahlungsstatus automatisch auf „Offen" — manuelles Setzen nicht nötig
- Manche Aktionen (Tags) funktionieren nur mit kompatiblen Entitäten

---

## Lernressourcen

- Lernpfad: https://hub.shopware.com/learn/unit/user-flow-builder
