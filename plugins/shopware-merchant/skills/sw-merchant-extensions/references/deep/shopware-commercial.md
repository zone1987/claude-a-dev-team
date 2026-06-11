# Shopware Commercial – Plan-Features freischalten

**Quelle**: https://docs.shopware.com/de/shopware-6-de/erweiterungen/shopware-commercial

## Überblick

Die **Shopware Commercial Extension** schaltet alle Features des gebuchten Plans
(Rise, Evolve oder Beyond) frei. Sie synct automatisch den aktiven Plan und stellt
alle verfügbaren Funktionen bereit – ohne separate Updates pro Feature.

---

## Installation

### Cloud-Nutzer
- Vorinstalliert und automatisch aktiv – kein Handlungsbedarf.

### Self-Hosted
1. **Erweiterungen > Store** öffnen
2. Nach "Shopware Commercial" suchen
3. **Hinzufügen** klicken
4. Danach: **Erweiterungen > Meine Erweiterungen > Aktivieren**

---

## Features nach Plan

### Shopware Rise (Basis)

| Kategorie | Feature | Beschreibung |
|---|---|---|
| **AI Copilot** | Inhaltserstellung | KI-generierte Produktbeschreibungen |
| **AI Copilot** | Klassifizierung | Automatische Produktkategorisierung |
| **AI Copilot** | Übersetzungen | KI-gestützte Übersetzungen |
| **Workflow** | Rule Builder | Regelbasierte Automatisierungen |
| **Workflow** | Flow Builder | Ereignis-basierte Workflows |
| **Content** | Custom Products | Konfigurierbare Produkte mit Optionen |
| **Content** | Social Shopping | Facebook, Instagram, Google Shopping |
| **Content** | Immersive Elements | 3D-/VR-Produktpräsentationen |

### Shopware Evolve (+ gegenüber Rise)

| Kategorie | Feature | Beschreibung |
|---|---|---|
| **Suche** | Advanced Search 2.0 | OpenSearch-basierte Hochleistungssuche |
| **Content** | CMS-Erweiterungen | Quick View, Scroll-Nav, Block-Visibility |
| **Zugang** | Dynamic Access | Regelbasierte Sichtbarkeit für Produkte/Kategorien |
| **B2B** | Quick Order | Schnellbestellung für Geschäftskunden |
| **B2B** | Freigabeprozesse | Bestellgenehmigungen |
| **B2B** | Angebote | Angebotserstellung und -verwaltung |
| **Publishing** | Shopware Publisher | Draft-Verwaltung für Erlebniswelten |
| **Sales** | Sales Agent | Außendienst-Frontend-App |

### Shopware Beyond (+ gegenüber Evolve)

| Kategorie | Feature | Beschreibung |
|---|---|---|
| **Inventar** | Multi-Inventory | Mehrere Lager, Bestands-Routing |
| **Abo** | Subscriptions | Wiederkehrende Bestellungen |
| **Preise** | Kundenspez. Preise | Individuelle Preise pro Kunde (API-basiert) |
| **Sales** | Digital Sales Rooms | Live-Shopping-Events mit Video |

---

## AI Copilot – Details (alle Pläne)

Der AI Copilot ist in der Administration integriert und unterstützt:

- **Produktbeschreibungen generieren**: Im Produkt-Formular → "Beschreibung generieren"
- **SEO-Texte**: Meta-Descriptions, SEO-Titel vorschlagen
- **Übersetzungen**: Bestehende Texte in andere Sprachen übersetzen
- **Klassifizierung**: Produkte automatisch Kategorien zuweisen

---

## CLI-Befehle (Self-Hosted)

Die Commercial Extension fügt zusätzliche Konsolen-Befehle hinzu:

```bash
# Lizenzstatus prüfen
php bin/console commercial:license:status

# Features neu laden
php bin/console commercial:feature:refresh

# Index für Advanced Search neu aufbauen
php bin/console es:admin:index
```

---

## Häufige Fragen

**F: Was passiert, wenn ich meinen Plan downgrade?**
A: Features des höheren Plans werden sofort deaktiviert. Daten bleiben erhalten, sind aber
nicht mehr zugänglich bis zu einem Plan-Upgrade.

**F: Muss ich Commercial nach einem Shopware-Update neu installieren?**
A: Nein. Die Extension aktualisiert sich automatisch zusammen mit Shopware-Updates.

**F: Wo sehe ich, welchen Plan ich aktiv habe?**
A: Shopware Account (account.shopware.com) > Shop-Details > Aktiver Plan
