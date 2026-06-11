# Shopware Multi-Inventory – Vollständige Dokumentation

## Überblick

Die Multi-Inventory-Funktionalität ermöglicht Händlern, mehrere Lagerhäuser und Lagerstandorte zu verwalten. Produkte können unabhängig vom Lagerstandort gekauft werden, solange sie in mindestens einem Lager verfügbar sind.

**Verfügbarkeit:** Beyond-Plan
**Mindestversion:** Shopware 15.09.22
**Voraussetzung:** Shopware Commercial Extension

---

## Kernprinzip

```
Produkt A vorhanden in:
  - Lager Hamburg (5 Stück)
  - Lager München (0 Stück)
  - Lager Berlin (3 Stück)

Ergebnis: Produkt A ist verfügbar (8 Stück gesamt)
```

Kunden sehen die Gesamtverfügbarkeit. Die Lagerauswahl für die Lieferung erfolgt automatisch nach konfigurierten Regeln.

---

## Lagerhäuser anlegen

**Pfad im Admin:** Einstellungen → Lagerhäuser (oder Einstellungen → Lagerhausverwaltung)

### Lagerhaus-Konfiguration
| Feld | Beschreibung |
|---|---|
| Name | Interner Name des Lagers |
| Adresse | Lagerstandort |
| Priorität | Bevorzugtes Lager bei mehreren verfügbaren |
| Aktiv/Inaktiv | Lager aus der Verfügbarkeitsberechnung ausschließen |

---

## Lagergruppen (Warehouse Groups)

Lagerhäuser können zu Gruppen zusammengefasst werden:

- **Gruppe**: Eine Sammlung von Lagerhäusern
- **Priorität innerhalb der Gruppe**: Welches Lager wird bevorzugt?
- **Gruppen-Zuweisung**: Über den Rule Builder (z.B. nach Verkaufskanal oder Lieferregion)

### Anwendungsfall
- Region Nord: Lager Hamburg, Lager Kiel
- Region Süd: Lager München, Lager Stuttgart
- Kunden aus PLZ 2xxxxx → Gruppe Nord
- Kunden aus PLZ 8xxxxx → Gruppe Süd

---

## Rule Builder Integration

Die Lagerauswahl kann über den Rule Builder gesteuert werden:

**Mögliche Regeln:**
- Verkaufskanal → bestimmte Lagergruppe
- Lieferadresse (Land, PLZ) → regionales Lager
- Produkt-Kategorie → spezielles Lager

**Pfad:** Einstellungen → Rule Builder → Neue Regel → Bedingung: Lagerbestand

---

## Bestandsverwaltung je Lager

Für jedes Produkt kann der Bestand je Lagerhaus gepflegt werden:

**Pfad:** Kataloge → Produkte → Produkt öffnen → Tab: Lagerbestände

| Lager | Bestand | Reserviert | Verfügbar |
|---|---|---|---|
| Hamburg | 10 | 2 | 8 |
| München | 5 | 0 | 5 |
| Berlin | 0 | 0 | 0 |

---

## Verfügbarkeitslogik

### Standard-Verhalten
- Gesamtverfügbarkeit = Summe aller aktiven Lager
- Bestellung wird dem Lager mit höchster Priorität zugeordnet
- Bei Nicht-Verfügbarkeit im Prioritätslager: Nächstes Lager wird genommen

### Konfigurierbare Optionen
- **Mindestbestand pro Lager**: Artikel erst ab X Einheiten als verfügbar anzeigen
- **Splitlieferungen**: Erlauben oder verbieten (Bestellung aus mehreren Lagern)
- **Lager-Exklusion**: Bestimmte Lager von der Online-Verfügbarkeit ausschließen

---

## Verwandte Features

- **Retouren-Management**: Zurückgegebene Artikel werden einem Lager zugeordnet
- **Abonnements**: Wiederkehrende Bestellungen berücksichtigen Lagerverfügbarkeit
- **Rule Builder**: Steuert Lager-Priorisierung und -Auswahl

---

*Quelle: https://docs.shopware.com/de/shopware-6-de/features/multi-inventory (Stand: 2026-06)*
