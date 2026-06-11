# Shopware 6 – Lagerhäuser (vollständige Referenz)

Quelle: https://docs.shopware.com/de/shopware6-de/einstellungen/lagerhaeuser

---

## Überblick

**Pfad:** Einstellungen > Handel > Lagerhäuser  
**Verfügbar ab:** 6.4.19.0  
**Plan:** Commercial — Shopware Beyond

Ermöglicht das Anlegen von Lagerhäusern und deren Zusammenfassung in Lagerhausgruppen.

---

## Lagerhäuser

### Anlage

| Feld | Beschreibung |
|---|---|
| Lagerhaus-Name | Eindeutige Bezeichnung |
| Interne Beschreibung | Zusatzinformationen (Adresse, Produktart) |
| Lagerhausgruppen-Zuweisung | Dropdown zur Gruppen-Zuordnung |

### Bearbeitung & Löschung
- `...`-Menü → „Bearbeiten" oder „Löschen"
- Alternativ: In Bearbeitungsmaske „Lagerhaus löschen"

### Produktzuweisung
Im Produkt unter „Lagerbestand & Lieferbarkeit" → Lagerhausgruppe auswählen → detaillierte Lager-Einstellungen erscheinen.

---

## Lagerhausgruppen

### Anlage

| Feld | Beschreibung |
|---|---|
| Name | Pflichtfeld |
| Priorität | Numerische Priorisierung (bestimmt Leerungs-Reihenfolge) |
| Interne Beschreibung | Zusatzinformationen |
| Zugewiesene Regel | Rule-basierte Aktivierung für Bestellungen |

### Lagerhäuser hinzufügen
1. „Lagerhäuser hinzufügen" klicken
2. Lagerhäuser per Checkbox auswählen
3. Bestätigen

### Priorisierung
Doppelklick auf Prioritätsspalte → Wert anpassen → Haken-Button speichern.

### Zuweisung aufheben
- Via `...`-Button in der Gruppe → „Löschen"
- Oder: X im Gruppeneintrag des Lagerhauses klicken

---

## Anwendungsfälle

- **Internationale Lieferoptimierung:** Regionale Lagergruppen für lokale Lieferung
- **Regelgestützte Verfügbarkeit:** Rule Builder für Lageraktivierung
- **Priorisierte Lagerung:** Lagerhaus-Reihenfolge steuert Bestandsentnahme
