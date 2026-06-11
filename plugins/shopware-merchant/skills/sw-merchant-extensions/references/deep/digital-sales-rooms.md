# Digital Sales Rooms – Live-Shopping-Events

**Quelle**: https://docs.shopware.com/de/shopware-6-de/erweiterungen/digital-sales-rooms  
**Plan**: Shopware Beyond (exklusiv)  
**Technologie**: Separate Frontend-Applikation + daily.co API + Mercure Service

## Überblick

**Digital Sales Rooms** ermöglicht interaktive Live-Shopping-Events mit ausgewählten Kunden:
- Video-basierte Produktpräsentationen
- Geführte oder selbstständige Navigation
- Direkter Kaufabschluss während des Events

---

## Technische Voraussetzungen

| Komponente | Beschreibung |
|---|---|
| **daily.co API-Account** | Video-Konferenz-Dienst (Pflicht) |
| **Mercure-Service** | Real-Time-Kommunikation zwischen Guide und Teilnehmern |
| Separate Frontend-App | Eigenständige Anwendung (nicht ein Admin-Plugin) |

> **Hinweis**: Die Einrichtung erfordert Entwickler/Administrator-Unterstützung.
> daily.co und Mercure werden vom Team konfiguriert.

---

## Betriebsmodi

### 1. Ungeleiteter Modus (Unguided)
- Kunden navigieren die Präsentation **selbstständig**
- Keine Live-Interaktion mit einem Guide
- Asynchrone Präsentation (Kunden öffnen den Link zu ihrem Zeitpunkt)

### 2. Geleiteter Modus (Guided)
- Ein **Guide** führt Teilnehmer in Echtzeit durch die Präsentation
- Guide-Ansicht: Sonderwerkzeuge für Live-Steuerung
- Video-Verbindung zwischen Guide und Teilnehmern aktiv

---

## Hauptkomponenten

### Präsentationen
- CMS-ähnliche Layouts (ähnlich Erlebniswelten)
- Individuell gestaltbare Shopping-Erlebnisse
- Produkte, Texte, Bilder, Videos einbindbar

### Termine (Appointments)
- Geplante Events mit spezifischen Kunden
- Einladungs-E-Mails mit Zugangslinks
- Datum, Uhrzeit, Teilnehmer konfigurierbar

### Guide-Ansicht (Guide View)
Während Live-Events stehen zur Verfügung:
| Tool | Funktion |
|---|---|
| Produkt-Schnelllist | Bestimmte Produkte sofort anzeigen |
| Teilnehmer-Management | Teilnehmer stumm schalten, entfernen |
| Echtzeit-Rabatte | Spontane Rabatte während des Events vergeben |
| Chat | Schriftliche Kommunikation |

---

## Teilnehmer-Funktionen (Kunden)

| Funktion | Beschreibung |
|---|---|
| Produkte durchsuchen | Präsentierte Produkte ansehen |
| Zuletzt angesehene Produkte | Quick-Access-Liste |
| Wunschlisten | Produkte zur Wunschliste hinzufügen |
| Warenkorb verwalten | Direkt im Event kaufen |
| Angebote anfragen | (Mit B2B-Components aktiviert) |
| Shared Shopping Lists | Gemeinsame Einkaufslisten mit anderen Teilnehmern |
| Folgetermin buchen | Neuen Termin direkt buchen |

---

## Einrichtungsworkflow (vereinfacht)

```
1. daily.co API-Account erstellen
2. Mercure-Service konfigurieren (Entwickler)
3. Frontend-App deployen (Entwickler)
4. Im Admin: Digital Sales Rooms konfigurieren
5. Erste Präsentation erstellen
6. Ersten Termin anlegen
7. Kunden einladen (automatische E-Mail mit Link)
```

---

## Anwendungsfälle

- **Fashion**: Virtuelle Kollektionspräsentation für B2B-Einkäufer
- **Luxusgüter**: Exklusive Produktvorstellungen für VIP-Kunden
- **B2B-Vertrieb**: Produktdemonstrationen für Geschäftskunden
- **Beauty/Kosmetik**: Live-Beratung mit Produkt-Empfehlungen
