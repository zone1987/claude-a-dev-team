# Dashboard

**Quelle**: https://docs.shopware.com/de/shopware-6-de/erste-schritte/dashboard  
**Gilt ab**: Shopware 6.4.8.0 (für ältere Versionen separate Doku unter 6.0.0–6.4.7.0)

## Überblick

Das Dashboard ist die **Startseite nach dem Login** in die Shopware-6-Administration.
Es bietet einen ersten Überblick über aktuelle Shop-Themen und Kennzahlen.

---

## Bestandteile des Dashboards

### Statistik-Widgets

Das Dashboard zeigt standardmäßig **zwei Statistik-Panels**:

#### 1. Bestellungen (Anzahl-Trend)
- Zeigt die Anzahl eingegangener Bestellungen im gewählten Zeitraum
- Trend-Vergleich: aktueller Zeitraum vs. Vorperiode

#### 2. Umsatz (Entwicklung)
- Zeigt den Umsatz (Brutto) im gewählten Zeitraum
- Trend-Vergleich: aktueller Zeitraum vs. Vorperiode

### Zeitraum-Auswahl

Beide Widgets haben ein **Dropdown-Menü** zur Zeitraum-Auswahl:

| Option | Beschreibung |
|---|---|
| Seit gestern | Alle Bestellungen ab Mitternacht des Vortags |
| Letzte 7 Tage | Rollierendes 7-Tage-Fenster |
| Letzte 30 Tage | Rollierendes 30-Tage-Fenster |
| Diesen Monat | Aktueller Kalendermonat |
| Letzten Monat | Vormonat komplett |

> "Seit gestern" erfasst alle Bestellungen ab Mitternacht (00:00 Uhr) des Vortags.

---

### Hilfe & Feedback-Bereich

- **Hilfe-Links**: Direktzugang zur Shopware-Dokumentation
- **Feedback-Button**: Weiterleitung zum Issue-Tracker für direktes Feedback an Shopware

---

## Shopware Analytics vs. Standard-Dashboard

Das Standard-Dashboard zeigt einfache Kernzahlen. Für erweiterte Berichte:
- **Shopware Analytics Extension** installieren (ab Dashboard > Analytics)
- Liefert: Revenue, Conversion Rate, Seitenaufrufe, Kundensegmente, Zahlungsmethoden u.v.m.
- Verfügbar für alle Pläne (Rise, Evolve, Beyond)

→ Siehe `../../../sw-merchant-extensions/references/deep/shopware-analytics.md`

---

## Tipps

- Das Dashboard kann nicht individuell angepasst werden (kein Widget-Drag & Drop in der Standard-Version)
- Für tiefere Analysen: Shopware Analytics Extension oder externe BI-Tools via API
- Schnellzugriff auf das Dashboard: Immer über das Shopware-Logo oben links in der Navigation
