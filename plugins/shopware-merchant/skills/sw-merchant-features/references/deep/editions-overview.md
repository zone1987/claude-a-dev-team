# Shopware 6 – Editionen & Feature-Überblick (vollständig)

## Editionen-Hierarchie

Shopware 6 ist in vier kumulativen Editionen verfügbar:

```
Community Edition (CE/Core)
  └── Rise (enthält alles aus CE)
        └── Evolve (enthält alles aus Rise)
              └── Beyond (enthält alles aus Evolve)
```

Die **Shopware Commercial** Erweiterung schaltet planabhängige Zusatzfunktionen frei. Bei Cloud-Installationen ist sie vorinstalliert; bei Self-Hosted muss sie über **Erweiterungen > Store** manuell installiert werden.

---

## Community Edition (CE) – Kernfunktionen

### Content Management & Design
- **Erlebniswelten (Shopping Experiences)**: Drag-&-Drop-Editor für Shopseiten, Landingpages, Kategorie- und Produktseiten
  - 5 Layout-Typen: Shop-Seiten, Landingpages, Kategorieseiten, Produktseiten, Bundle-Seiten
  - Blöcke: Text, Bilder, Slider, Galerien, Commerce, Video, Formulare, HTML
  - Viewport-Vorschau für responsives Design
  - Datenmapping für dynamische Inhalte auf Kategorie-/Produktseiten
- Geräteoptimieertes Design mit anpassbaren Templates

### Workflow & Automatisierung
- **Rollen & Rechte**: Benutzerverwaltung mit individuellen Berechtigungsstufen
  - Berechtigungshierarchie: Anzeigen → Bearbeiten → Erstellen → Löschen → Alle
  - Spezielle Berechtigungen: Grundeinstellungen, Updates, Erweiterungen, Ereignisprotokoll, Cache, Import/Export
  - API-Zugriffsschlüssel für Integrationen
- **Rule Builder**: Bedingungsbasierte Regeln für Versandkosten und andere Funktionen (Basis)
- **Flow Builder**: Event-basierte Automatisierung von Geschäftsprozessen ohne Code (Basis)
  - 100+ Trigger (Bestellungen, Kunden, Zahlungen, Benachrichtigungen)
  - Aktionen: E-Mail-Versand, Dokumentenerstellung, Statusvergabe, Kundengruppenänderung, Tag-Management

### Customer Experience & Marketing
- Kundengruppen
- Aktionen & Promotions
- SEO-Optimierung
- Produktsuche
- Cross-Selling
- Produktbewertungen
- Tag-Management

### Inventar & Bestellverwaltung
- Physische und digitale Produkte
- Dynamische Produktgruppen
- Zahlungsgateway-Integration
- Versandanbieter-Integration
- Kategorieverwaltung

### B2B (Basis)
- Brutto-/Netto-Preisanzeige nach Kundengruppe mit konfigurierbaren Steuersätzen

### Internationalisierung
- Unbegrenzte Verkaufskanäle (Storefronts, Vergleichsportale, Social Shopping)
- Multi-Währung und Steuerverwaltung
- Multi-Sprach-Unterstützung

### Weitere Features
- Import/Export-Tools
- Migration von anderen eCommerce-Plattformen
- Erweiterbarkeit über den Shopware Store

---

## Rise Plan – Zusatzfeatures

Enthält alle CE-Features plus:

| Feature | Beschreibung |
|---|---|
| **Flow Builder – Flows teilen** | Export/Import von Flows zwischen Instanzen (ab 6.4.19.0) |
| **Custom Products** | Konfigurierbare/personalisierbare Produkte mit individuellen Optionen |
| **Premium Themes** | Professionelle Design-Templates für Storefronts |
| **Retouren-Management** | Retourenabwicklung direkt im Admin-Panel |
| **Rule Builder – Vorschau** | Echtzeit-Test von Regeln gegen echte Bestellungen (TRUE/FALSE) |
| **Social Commerce** | Integration mit Social-Media-Verkaufskanälen |
| **Shopware AI Copilot** | KI-Assistent für Inhalte, Produktbeschreibungen, Suche |
| **3D-Viewer Block für Erlebniswelten** | 3D-Produktvisualisierung in Shopping Experiences |
| **Immersive Elements** | 5 verschiedene 3D-Elemente für Erlebniswelten (ab 16.05.2024) |
| **Scene Editor (Beta)** | Visuelle 3D-Szenen erstellen und Produktbilder generieren |
| **Rule Builder – Regeln teilen** | Download/Import von Regeln als JSON (ab 6.7.1.0) |

---

## Evolve Plan – Zusatzfeatures

Enthält alle Rise-Features plus:

| Feature | Beschreibung |
|---|---|
| **Advanced Search 2.0** | OpenSearch-basierte erweiterte Suche mit Boostings, Actions, Synonymen |
| **B2B Components** | B2B-Funktionalitäten: Angebote, Mitarbeiter, Genehmigungen, Budgets |
| **CMS Erweiterungen** | Erweiterte CMS-Funktionen |
| **CMS Regeln** | Regelbasierte Sichtbarkeit von CMS-Inhalten |
| **Dynamic Access** | Zugriffssteuerung und Berechtigungsverwaltung |
| **Publisher** | Content-Publishing-Tools |
| **Flow Builder – Webhook-Aktionen** | Externe URLs via GET/POST/PUT/PATCH/DELETE aufrufen |
| **Sales Agent** | Außendienstmitarbeiter-App für B2B-Kundenverwaltung |

---

## Beyond Plan – Zusatzfeatures

Enthält alle Evolve-Features plus:

| Feature | Beschreibung |
|---|---|
| **Digital Sales Rooms** | Interaktive Live-Video-Shopping-Events |
| **Kundenspezifische Preise** | Individuelle Preise pro Kunde via API (ERP-Integration) |
| **Multi-Inventory** | Lagerverwaltung über mehrere Standorte |
| **Abonnements** | Wiederkehrende Bestellungen mit konfigurierbaren Intervallen |
| **Flow Builder – zeitverzögerte Aktionen** | Geplante Ausführung von Flow-Aktionen (Stunden/Tage/Wochen) |

---

## Support-Vergleich

| Leistung | Rise | Evolve | Beyond |
|---|---|---|---|
| **Verfügbarkeit** | 09:00–17:00 Uhr* | 07:00–19:00 Uhr* | 24/7 |
| **Reaktionszeit** | 8 Stunden | 4 Stunden | 1 Stunde |
| **Schriftlicher Support** | ✓ | ✓ | ✓ |
| **Telefonischer Support (Rückruf)** | — | ✓ | ✓ |
| **Hotline** | — | ✓ | ✓ |
| **Entwickler-Support** | — | — | ✓ |
| **Persönliches Onboarding** | — | — | ✓ |
| **Account Manager** | — | — | ✓ |
| **Community-Forum** | ✓ | ✓ | ✓ |
| **Kostenfreie Erstinstallation** | ✓ | ✓ | ✓ |
| **Updates & Patches** | ✓ | ✓ | ✓ |

*Ausnahmen: Feiertage NRW, 24.12. ab 12:00, 31.12. ab 12:00, 3 interne Events/Jahr (2026: 15.01., 14.04., 08.10.)

---

## Shopware Commercial Extension – Installation

- **Cloud**: Automatisch vorinstalliert
- **Self-Hosted**: Erweiterungen > Store → „Shopware Commercial" suchen und installieren

Die Extension aktiviert Features je nach gebuchtem Plan automatisch.

---

## Weiterführende Skills

- `sw-merchant-commercial` – Überblick aller Commercial Features
- `sw-merchant-commercial-ai-copilot` – AI Copilot Funktionen
- `sw-merchant-commercial-subscriptions` – Abonnements
- `sw-merchant-commercial-advanced-search` – Advanced Search 2.0
- `sw-merchant-commercial-b2b` – B2B Components
- `sw-merchant-commercial-returns` – Retouren-Management
- `sw-merchant-commercial-flow-builder` – Flow Builder (Commercial)
- `sw-merchant-commercial-rule-builder` – Rule Builder (Commercial)
- `sw-merchant-commercial-multi-inventory` – Multi-Inventory
- `sw-merchant-commercial-sales-agent` – Sales Agent
- `sw-merchant-commercial-digital-sales-rooms` – Digital Sales Rooms
- `sw-merchant-commercial-custom-pricing` – Kundenspezifische Preise
- `sw-merchant-commercial-spatial` – Spatial Commerce

---

*Quelle: https://docs.shopware.com/de/shopware-6-de/features (Stand: 2026-06)*
