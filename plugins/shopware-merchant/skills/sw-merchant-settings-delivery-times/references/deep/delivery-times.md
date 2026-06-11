# Shopware 6 – Lieferzeiten (vollständige Referenz)

Quelle: https://docs.shopware.com/de/shopware-6-de/einstellungen/lieferzeiten

---

## Überblick

**Pfad:** Einstellungen > Handel > Lieferzeiten

Ermöglicht die Anzeige voraussichtlicher Lieferzeiten auf Produktdetailseiten.

---

## Lieferzeit anlegen

| Feld | Typ | Beschreibung |
|---|---|---|
| Name | Text | Kundenfreundliche Bezeichnung (erscheint auf Produktdetailseite) |
| Einheit | Dropdown | Tag, Woche, Monat, Jahr |
| Minimum | Ganzzahl | Mindestdauer |
| Maximum | Ganzzahl | Maximaldauer |

---

## Lieferzeit zuweisen

### Bei Versandarten
- In den Basisinformationen der Versandart → Lieferzeit auswählen
- Diese gilt als Standard für Produkte ohne eigene Lieferzeit-Zuweisung
- Nützlich für länderspezifische oder versandartspezifische Unterschiede

### Bei Produkten
- Im Bereich „Lieferbarkeit" der Produktinformationen
- Produktspezifische Lieferzeit **überschreibt** die Versandart-Lieferzeit

---

## Warenkorb-Anzeige

**Aktivierung:** Einstellungen > Allgemein > Warenkorb > „Lieferzeit im Warenkorb anzeigen"

- Pro Verkaufskanal konfigurierbar
- Berechnung ab aktuellem Datum
- Berücksichtigt Lagerbestand und Wiederauffüllzeiten

---

## Berechnungslogik

Dynamische Anzeige kombiniert:
1. Lieferzeit des Produkts
2. Verfügbarer Lagerbestand
3. Wiederauffüllzeit (bei Lagerbestandsmangel)

**Beispiel:**
- Aktuelles Datum: 01.01.2020
- Lieferzeit: 1–3 Tage
- Lagerbestand: vorhanden
- Ergebnis: „voraussichtlich 02.01.2020–04.01.2020"

---

## Storefront-Darstellung

- Neben Verfügbarkeitsstatus auf Produktdetailseiten
- Dynamischer Datumsbereich im Warenkorb und Checkout (wenn aktiviert)
- Individuell für jeden Artikel im Warenkorb
