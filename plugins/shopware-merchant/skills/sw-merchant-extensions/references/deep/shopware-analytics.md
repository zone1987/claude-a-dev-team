# Shopware Analytics – Erweitertes Reporting

**Quelle**: https://docs.shopware.com/de/shopware-6-de/erweiterungen/shopware-analytics  
**Pfad im Admin**: Dashboard > Analytics  
**Verfügbar für**: Alle Pläne (Rise, Evolve, Beyond)

## Überblick

**Shopware Analytics** erweitert die Standard-Dashboard-Statistiken um detailliertes Reporting.
Datenverarbeitung erfolgt auf dem eigenen System – kein Drittanbieter-Tracking.

---

## Versionen

| Shopware Version | Analytics Version |
|---|---|
| Shopware 6.5 | App Version 1.4.x |
| Shopware 6.6+ | App Version 2.4.x |

---

## Installation & Aktivierung

1. **Erweiterungen > Meine Erweiterungen** oder **Erweiterungen > Store**
2. "Shopware Analytics" suchen → Installieren + Aktivieren
3. Zugang: **Dashboard > Analytics**

---

## Konfigurationsoptionen

### Zeitraum-Filter
- Vordefinierte Zeiträume: Heute, Gestern, Letzte 7/30 Tage, Diesen/Letzten Monat, Dieses/Letztes Jahr
- **Benutzerdefinierter Zeitraum**: Start- und Enddatum frei wählen

### Filter-Dimensionen
| Filter | Mögliche Werte |
|---|---|
| Verkaufskanal | Alle Kanäle oder spezifischer Kanal |
| Land | Kundenland der Bestellung |
| Kundengruppe | z. B. B2C, B2B |
| Bestellstatus | Offen, In Bearbeitung, Abgeschlossen, Storniert |
| Zahlungsstatus | Offen, Bezahlt, Teilweise bezahlt |

---

## Backend-Metriken

### Umsatz & Bestellungen
| Kennzahl | Beschreibung |
|---|---|
| Gesamtumsatz | Bruttoumsatz im gewählten Zeitraum |
| Anzahl Bestellungen | Gesamtzahl der Bestellungen |
| Durchschnittlicher Bestellwert | Umsatz / Anzahl Bestellungen |

### Zahlungsmethoden
- Welche Zahlungsmethoden werden wie häufig genutzt?
- Umsatzanteil pro Zahlungsmethode

### Kundengewinnung
- Neu- vs. Bestandskunden
- Kundenentwicklung über Zeit

### Rabatte & Gutscheine
- Gesamtrabattvolumen
- Häufig genutzte Gutscheincodes

### Umsatz nach Dimension
- Nach Hersteller
- Nach Land / Region
- Nach Produkt (Top-Seller)
- Nach Versandmethode

---

## Storefront-Metriken (erfordert Event Tracking)

> **Voraussetzung**: Tracking muss aktiv sein und Kunden müssen zustimmen (DSGVO-konform)

| Kennzahl | Beschreibung |
|---|---|
| Seitenaufrufe | Gesamte Page Views |
| Unique Visitors | Eindeutige Besucher |
| Conversion Rate | Besucher → Käufer (%) |
| Customer Journey | Pfad vom ersten Besuch zur Bestellung |

---

## Datenschutz & Performance-Hinweis

- Datenverarbeitung: **Auf dem eigenen Server** (keine Drittanbieter)
- Nutzer müssen der Datenverarbeitung zustimmen
- **Wichtig**: "Große Datenvolumen können die Systemperformance beeinflussen" – bei großen Shops
  Analyse außerhalb der Peak-Zeiten durchführen

---

## Troubleshooting

| Problem | Lösung |
|---|---|
| Keine Daten nach URL-Wechsel | `bin/console app:url-change:resolve` ausführen |
| Tracking-Aktivierung schlägt fehl | Prüfen ob externe Kommunikation (Firewall) geblockt wird |
| Daten veraltet | Message-Queue prüfen (`php bin/console messenger:consume`) |
| Berichte laden langsam | Zeitraum einschränken oder Off-Peak-Analyse durchführen |
