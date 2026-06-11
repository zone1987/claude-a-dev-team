# Marketing – Übersicht

**Pfad:** Admin > Marketing

## Beschreibung

Der Bereich Marketing in der Shopware 6 Administration bietet alle Werkzeuge zur Durchführung von Rabattaktionen und zur Verwaltung von Newsletter-Abonnenten.

> **Hinweis:** Der Marketing-Bereich ist Teil der Shopware-Administration und ab Version 6.0.0 verfügbar.

## Enthaltene Bereiche

### 1. Rabatte & Aktionen

Pfad: Admin > Marketing > Rabatte & Aktionen

Ermöglicht das Anlegen von Rabattaktionen (Promotions) für Verkaufskanäle. Unterstützt:

- Aktionscodes (keine, festgelegte oder individuelle Codes)
- Bedingungen über den Rule Builder
- Verschiedene Rabattarten (absolut, prozentual, Festpreis)
- Zeitliche Begrenzungen
- Nutzungslimits (gesamt und je Kunde)

**Details:** Siehe `sw-merchant-marketing-promotions` und `sw-merchant-marketing-codes`

### 2. Newsletter Empfänger

Pfad: Admin > Marketing > Newsletter Empfänger

Verwaltung aller Kunden, die sich für den Newsletter eingetragen haben. Unterstützt:

- Statusverwaltung (Warten auf Aktivierung, Sofort Aktiv, Aktiv, Warten auf Löschung)
- Filterung nach Status, Sprache und Verkaufskanal
- Bearbeitung von Empfängerdaten (Adresse, Sprache, E-Mail, Tags)

**Details:** Siehe `sw-merchant-marketing-newsletter`

## Verwandte Bereiche

| Bereich | Pfad | Relevanz |
|---------|------|----------|
| Rule Builder | Einstellungen > Automatisierung > Rule Builder | Bedingungen für Promotions |
| Verkaufskanäle | Verkaufskanäle | Promotions kanalbezogen zuweisen |
| Flow Builder | Einstellungen > Automatisierung > Flow Builder | Automatisierung auf Basis von Promotions |

## Sub-Skills

| Skill | Thema |
|-------|-------|
| `sw-merchant-marketing-promotions` | Rabatte & Aktionen anlegen, konfigurieren |
| `sw-merchant-marketing-codes` | Aktionscodes: festgelegt, individuell, Beispiele |
| `sw-merchant-marketing-newsletter` | Newsletter-Empfänger verwalten |
| `sw-merchant-marketing-rule-builder` | Rule Builder für Bedingungen |
