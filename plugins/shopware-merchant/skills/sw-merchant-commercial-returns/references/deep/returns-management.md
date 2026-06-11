# Shopware Retouren-Management – Vollständige Dokumentation

## Überblick

Das Retouren-Management ermöglicht Händlern, Rücksendungen direkt im Admin-Panel auf Basis bestehender Bestellungen abzuwickeln.

**Verfügbarkeit:** Rise-Plan und höher
**Voraussetzung:** Shopware Commercial Extension
**Einschränkung (aktuelle Version):** Nur eine Retoure pro Bestellung möglich; Bestandsberechnungen müssen manuell durchgeführt werden

---

## Retoure anlegen

### Schritt-für-Schritt

1. Im Admin navigieren zu: **Bestellungen → Bestellungen**
2. Bestellung öffnen
3. Tab **Allgemein** öffnen
4. Artikel auswählen, die zurückgegeben wurden
5. Button **„Artikel zurückgeben"** klicken

### Dialog: Rückgabe erfassen

Im erscheinenden Dialog:
- **Retourenmenge**: Anzahl zurückgegebener Artikel pro Position
- **Kommentar** (optional): Interne Notiz zur Retoure (z.B. Retourengrund)

### Einschränkungen
- Nur Artikel aus der jeweiligen Bestellung können retourniert werden
- Digitale Produkte können je nach Konfiguration ausgeschlossen sein
- Maximal eine Retoure pro Bestellung in der aktuellen Version

---

## Retoure bearbeiten

Nach dem Anlegen erscheint die Retoure im Tab **Retouren** der Bestellung.

### Tab: Allgemein
| Feld | Beschreibung |
|---|---|
| Retourenstatus | Aktueller Status (z.B. offen, in Bearbeitung, abgeschlossen) |
| Kommentar | Interne oder kundenseitige Notiz |

### Tab: Positionen

Für jede retournierte Position:
- Retourenmenge nachträglich anpassen
- Individuellen Positionsstatus setzen (z.B. „Angenommen", „Abgelehnt")
- Versandkosten anpassen (per Doppelklick editierbar)

### Teilgutschriften

Händler können für einzelne Positionen oder Teilmengen Gutschriften erstellen:
- Betrag manuell festlegen
- Dokument automatisch generieren

---

## Kundensicht im Storefront

Kunden können ihre erstellten Retouren im persönlichen Account einsehen:
- Retourenstatus (vom Händler zugewiesen)
- Retournierte Artikel und Mengen
- Kommentare des Händlers

**Wichtig:** Der Status muss manuell vom Händler im Admin aktualisiert werden.

---

## Retourenstatus-Workflow

Ein typischer Workflow:

```
Retoure angelegt
       ↓
  In Prüfung
       ↓
  Angenommen / Abgelehnt (je Position möglich)
       ↓
  Gutschrift erstellt
       ↓
  Abgeschlossen
```

---

## Lernressourcen

Auf dem Shopware Community Hub ist ein interaktiver Lernpfad für das Retouren-Management verfügbar, der Schritt-für-Schritt durch alle Funktionen führt.

---

*Quelle: https://docs.shopware.com/de/shopware-6-de/bestellungen/retouren-management (Stand: 2026-06)*
