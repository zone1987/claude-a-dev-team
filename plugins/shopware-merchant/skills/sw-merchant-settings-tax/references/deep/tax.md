# Shopware 6 – Steuern (vollständige Referenz)

Quelle: https://docs.shopware.com/de/shopware-6-de/einstellungen/steuern

---

## Überblick

**Pfad:** Einstellungen > Regional > Steuern

Ein grüner Haken kennzeichnet den aktuellen Standard-Steuersatz.

---

## Steuersatz erstellen

| Feld | Beschreibung |
|---|---|
| Name | Bezeichnung des Steuersatzes |
| Prozentwert | Steuerprozentsatz (z.B. 19) |
| Als Standard verwenden | Vorgabe für neue Produkte |

---

## Steuersatz bearbeiten

> **Warnung:** Die Änderung eines bereits verwendeten Steuersatzes kann zu abweichenden Kalkulationen bei bestehenden Rechnungen und Artikeln führen.

---

## Länderspezifische Steuerregeln

Innerhalb eines Steuersatzes können differenzierte Regeln für folgende Einheiten eingerichtet werden:
- Einzelne Postleitzahlen
- Postleitzahlenbereiche
- Bundesländer
- Gesamte Länder

### Feld „Aktiv ab"
Wenn ein Datum hinterlegt wird, gilt der Steuersatz erst ab diesem Termin in der Storefront.
> **Hinweis:** Preise im Produkt werden bei einem geänderten Steuersatz **nicht** automatisch neu berechnet.

---

## EU-OSS (One-Stop-Shop)

Ab 1. Juli 2021 gilt ein Schwellenwert von **10.000 €** für innergemeinschaftliche B2C-Verkäufe.
- Überschreiter müssen sich im Online-OSS-Portal registrieren
- Shopware unterstützt die notwendigen Steuerregeln pro Land

---

## Steueranbieter (externe Dienste)

Für komplexe Steuersysteme (z.B. USA) können externe Steuerdienstleister integriert werden:
- Dienst aktivieren
- Priorität anpassen
- Verfügbarkeitsbedingungen konfigurieren

---

## Integration mit Kundengruppen

In den Kundengruppen-Einstellungen kann für jede Gruppe einzeln konfiguriert werden, ob Preise **brutto** oder **netto** angezeigt und berechnet werden.
