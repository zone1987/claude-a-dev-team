# Agentic Commerce – KI-Commerce-Agents & Produkt-Feeds

**Quelle**: https://docs.shopware.com/de/shopware-6-de/erweiterungen/agentic-commerce  
**Status**: Beta (limitierte Funktionalität, Erweiterung folgt)

## Überblick

**Agentic Commerce** integriert Shopware 6 mit KI-Commerce-Agenten und ermöglicht
automatisierten Handel über KI-Plattformen wie ChatGPT.

### Zwei Hauptkomponenten:

1. **Universal Commerce Protocol (UCP)** – Standardisierte Schnittstelle für KI-Agenten
2. **Product Feed Sales Channel** – Produktdaten-Export für externe Systeme und KI-Agenten

---

## Universal Commerce Protocol (UCP)

### Was es ist
Ein standardisiertes Protokoll, das KI-Commerce-Agenten ermöglicht:
- Deinen Shop **automatisch zu erkennen**
- Über eine **standardisierte Schnittstelle** zu interagieren
- Einkaufsprozesse **vollständig zu automatisieren**

### Konfiguration
**Einstellungen > Commerce > UCP**

Dort steuerbar, welche Verkaufskanäle für KI-Agenten zugänglich sind und
welche Fähigkeiten aktiviert werden:

| Fähigkeit | Beschreibung |
|---|---|
| **Katalogzugriff** | KI-Agent kann Produkte durchsuchen |
| **Warenkorb-Management** | KI-Agent kann Warenkorb befüllen |
| **Rabatt-Anwendung** | KI-Agent kann Gutscheine verwenden |
| **Checkout-Prozess** | KI-Agent kann Bestellung abschließen |
| **Bestellerstellung** | KI-Agent erstellt Bestellungen |
| **Zahlungs-Tokenisierung** | Sichere Zahlungsabwicklung durch KI-Agent |
| **Kunden-Identitätsverknüpfung** | KI-Agent kann Kundendaten zuordnen |

---

## Product Feed Sales Channel

### Unterstützte Plattformen

| Plattform | Feed-Format | Status |
|---|---|---|
| OpenAI / ChatGPT | JSONL | Verfügbar (US-only für ChatGPT-Marktplatz) |
| Google Shopping | XML | Verfügbar |
| Weitere | Geplant | Beta |

### Einrichtung

1. **Verkaufskanäle** → Neuen Kanal hinzufügen → "Agentic Commerce" wählen
2. Feed-Typ auswählen (JSONL für OpenAI / XML für Google)
3. Produktvarianten konfigurieren:

### Varianten-Mapping
Produktattribute auf KI-Plattform-Anforderungen mappen:

| Shopware-Attribut | KI-Plattform-Attribut |
|---|---|
| Eigenschaft "Farbe" | color |
| Eigenschaft "Größe" | size |
| Eigenschaft "Material" | material |
| Produktnummer | sku |

---

## Tracking & Analytics

Über den Agentic Commerce Kanal werden verfolgt:
- Bestellungen aus KI-Agent-Traffic
- Kundengewinnung über KI-Kanäle
- Umsatz aus AI-Commerce

---

## ChatGPT-Marktplatz: Verfügbarkeit

> **Aktuell**: ChatGPT-Marktplatz-Registrierung ist nur für **US-Händler** verfügbar.
> Europäische Verfügbarkeit ist geplant aber noch nicht angekündigt (Stand: 2024).

---

## Beta-Hinweis

- Funktion befindet sich in **aktiver Entwicklung**
- Funktionsumfang wird erweitert
- Vor produktivem Einsatz: Testumgebung verwenden
- Änderungen an API und Protokoll möglich

---

## Zukunftsvision

Shopware positioniert Agentic Commerce als strategische Investition in die Zukunft:
- Shopping ohne manuellen Eingriff des Kunden
- KI-Agenten als neue "Kunden-Touchpoints"
- Vollautomatisierter B2B-Einkauf über KI
