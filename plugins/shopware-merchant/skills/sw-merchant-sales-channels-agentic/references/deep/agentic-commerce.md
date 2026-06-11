# Shopware 6 – Agentic Commerce Product Feed: Vollständige Dokumentation

> Quelle: https://docs.shopware.com/de/shopware-6-de/einstellungen/agentic-commerce-product-feed
> Version: 6.7.10.0+

---

## 1. Überblick

Der **Agentic Commerce Product Feed** ist ein neuer Verkaufskanal-Typ in Shopware ab Version 6.7.10.0. Er fungiert als zentrale Plattform für KI-gestützte Produktverteilung und ermöglicht die Bereitstellung von Produktdaten für KI-Agenten und KI-Plattformen wie ChatGPT.

**Wichtige Einschränkung:** Die Registrierung für den ChatGPT-Marktplatz ist **aktuell nur in den USA verfügbar**.

---

## 2. Funktionsumfang

| Funktion | Beschreibung |
|---|---|
| **JSONL-Feed** | Standardkonformes Format für KI-Plattformen |
| **OpenAI-Template** | Vorkonfiguriertes Template für OpenAI/ChatGPT |
| **Affiliate-Code** | Kanalzuordnung für Tracking |
| **Kampagnen-Code** | Detaillierte Analyse der KI-generierten Conversions |
| **Statistiken** | Bestellungen, Kunden, Umsatz aus diesem Kanal |
| **Dynamische Produktgruppen** | Flexibler Produktexport-Umfang |
| **Scheduler** | Automatische Feed-Generierung |

---

## 3. Kanal anlegen

### Schritt-für-Schritt

1. Hauptmenü > Verkaufskanäle > **+** Symbol
2. Typ **"Agentic Commerce Product Feed"** wählen
3. Konfigurationsbereich öffnet sich

---

## 4. Konfiguration

### 4.1 Grundeinstellungen

| Feld | Beschreibung |
|---|---|
| **Template** | OpenAI-Template auswählen |
| **Name** | Eindeutige Kanalbezeichnung (intern) |
| **Als Favorit markieren** | In Admin-Sidebar anzeigen |

### 4.2 OpenAI-Konfiguration

| Feld | Beschreibung |
|---|---|
| **Rückgaberichtlinien-URL** | URL zur Rückgabe-/Erstattungsrichtlinien-Seite des Shops |
| **Variantenattribut: Farbe** | Eigenschaft aus Shopware für Farbe-Mapping |
| **Variantenattribut: Größe** | Eigenschaft aus Shopware für Größe-Mapping |
| **Variantenattribut: Geschlecht** | Eigenschaft für Geschlecht-Mapping |
| **Variantenattribut: Material** | Eigenschaft für Material-Mapping |
| **Custom-Varianten-Zuweisungen** | Optionale eigene Varianten-Attribute |

### 4.3 Tracking

| Feld | Beschreibung |
|---|---|
| **Affiliate-Code** | Für Kanalzuordnung in Berichten |
| **Kampagnen-Code** | Für detaillierte Kampagnen-Analyse |

### 4.4 Feed-Management

| Feld | Beschreibung |
|---|---|
| **Dynamische Produktgruppe** | Welche Produkte in den Feed aufgenommen werden |
| **Generierungsintervall** | Zeitabstand für Feed-Aktualisierung (inkl. Live-Modus für Echtzeit) |
| **Scheduler aktivieren** | Automatische Generierung via Shopware-Scheduler |

---

## 5. Reiter: Integration

Im Integration-Reiter:
- **Feed-URL** für die KI-Plattform
- Informationen zur Einbindung in OpenAI/ChatGPT

---

## 6. Reiter: Template

Das JSONL-Template steuert den Aufbau der Exportdatei. Analog zum Produktvergleich-Kanal kann das Template bei Bedarf angepasst werden.

---

## 7. Reiter: Statistiken

Metriken für den Kanal:
- **Bestellungen** – Aus diesem Kanal generierte Bestellungen
- **Kunden** – Neuakquisitionen via KI-Plattform
- **Umsatz** – Umsatz aus diesem Kanal

Voraussetzung: Korrekte Konfiguration von Affiliate- und Kampagnen-Code.

---

## 8. Verfügbarkeit und Einschränkungen

| Aspekt | Detail |
|---|---|
| **Mindestversion** | Shopware 6.7.10.0 |
| **ChatGPT Marketplace** | Registrierung aktuell nur in den USA |
| **Feed-Format** | JSONL (JSON Lines) |
| **Voraussetzung** | Passendes Shopware-Abonnement |

---

## Quelle

https://docs.shopware.com/de/shopware-6-de/einstellungen/agentic-commerce-product-feed
