# Shopware Kundenspezifische Preise – Vollständige Dokumentation

## Überblick

Das Feature „Kundenspezifische Preise" ermöglicht Shopbetreibern, jedem Kunden individuell kalkulierte Preise anzubieten – Listenpreise, Staffelpreise und währungsabhängige Preise.

**Verfügbarkeit:** Beyond-Plan
**Mindestversion:** 1.0.0.0 (Commercial Extension)
**Voraussetzung:** Shopware Commercial Extension
**Verwaltung:** Ausschließlich über API (kein UI-Modul im Admin)

---

## Kernfunktionen

### Unterstützte Preistypen

| Typ | Beschreibung |
|---|---|
| Listenpreise | Individueller Basispreis je Kunde |
| Staffelpreise | Preis abhängig von der Bestellmenge |
| Währungspreise | Kundenspezifische Preise je Währung |

### Kundenzuordnung

Preise werden direkt einer Kunden-ID zugeordnet. Die Zuordnung erfolgt über die API mit der spezifischen Kunden-UUID.

---

## API-Integration

### Konzept

Das System ist für die **schnelle Synchronisierung großer Datenmengen** optimiert, ideal für:
- ERP-Systemintegration
- PIM-Systemsynchronisation
- Großhandels-Preislisten

**Wichtig:** Es gibt kein UI-Modul in der Shopware-Administration. Alle Operationen werden über die API durchgeführt.

### Technische API-Dokumentation

Vollständige API-Referenz: Shopware Stoplight-Dokumentation (offiziell)

### Varianten-Hinweis

Vererbungen bei Produktvarianten werden **nicht** berücksichtigt. Für jede Variante wird die spezifische Varianten-ID benötigt:

```
Produkt mit Varianten:
  - Hauptprodukt-ID: abc-123 (kein Preis, keine Vererbung)
  - Variante Rot-S: ID xyz-001 → eigener Preis erforderlich
  - Variante Blau-M: ID xyz-002 → eigener Preis erforderlich
```

---

## Storefront-Verhalten

### Angemeldeter Kunde
Sobald sich ein Kunde einloggt, der kundenspezifische Preise hinterlegt hat:
- Individualisierte Preise werden automatisch auf Produktdetailseiten angezeigt
- Kategorieseiten und Suche zeigen ebenfalls kundenspezifische Preise
- Warenkorb-Berechnungen nutzen die individuellen Preise

### Nicht angemeldeter Kunde (oder Logout)
- Reguläre Listenpreise werden angezeigt
- Wechsel zum Standard-Preis erfolgt sofort nach Logout

---

## Abgrenzung zu B2B Custom Pricing

| Feature | B2B Custom Pricing (Evolve) | Kundenspezifische Preise (Beyond) |
|---|---|---|
| Ziel | Organisationseinheiten / Tags | Einzelkunden (Kunden-ID) |
| Konfiguration | Admin-UI (Rabatt-Regeln) | Nur API |
| Typ | Prozentualer/Fixer Rabatt | Exakte Preise |
| Volumen | Kleine bis mittlere Datenmengen | Große Datenmengen (ERP) |
| Staffelpreise | Begrenzt | Vollständig unterstützt |

---

## Typische Anwendungsfälle

### 1. Großhandel mit ERP-Integration
- ERP verwaltet individuelle Kundenpreise
- Täglicher/stündlicher Sync via API
- Kunden sehen ihre verhandelten Preise direkt im Shop

### 2. Rahmenvertragspreise
- Langfristige Verträge mit Fixpreisen
- Preise werden einmalig per API gesetzt
- Gültig bis Vertragsende (manuell oder automatisch über API aktualisiert)

### 3. Internationale B2B-Preislisten
- Verschiedene Preise je Währung für internationale Großkunden
- Vollautomatische Synchronisation via API

---

*Quelle: https://docs.shopware.com/de/shopware-6-de/erweiterungen/kundenspezifische-preise (Stand: 2026-06)*
