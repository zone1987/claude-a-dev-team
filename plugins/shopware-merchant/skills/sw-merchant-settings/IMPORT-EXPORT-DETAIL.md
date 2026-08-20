# Shopware 6 – Import / Export (vollständige Referenz)

Quelle: https://docs.shopware.com/de/shopware6-de/einstellungen/importexport

---

## Überblick

**Pfad:** Einstellungen > Automatisierung > Import/Export

Ermöglicht das Verwalten von Shop-Inhalten über CSV-Dateien.

---

## CSV-Anforderungen

| Anforderung | Wert |
|---|---|
| Zeichenkodierung | UTF-8 |
| Feldtrennzeichen | Semikolon (`;`) |
| Textbegrenzer | Anführungszeichen (`"`) |
| Dezimaltrennzeichen Preise | Punkt (5.00, nicht 5,00) |

---

## Import

- CSV-Datei hochladen → Datensätze hinzufügen oder aktualisieren
- Validierung bei fehlerhaften Einträgen → Fehlerbericht (Download-Option)
- **Testmodus:** Validierung ohne Commit (keine Änderungen an der Datenbank)
- Fehler-CSV enthält nur fehlerhafte Datensätze mit Fehlerbeschreibungen

---

## Export

- Bestehendes Datenmaterial als CSV exportieren
- Exporthistorie: Letzte 30 Tage
- Für externe Verwendung oder Drittanbieter-Integrationen

### AI Copilot Export (ab Plan Rise)
- Natürlichsprachliche Abfragen für spezifische Datensätze
- Beispiel: „Exportiere alle Produkte ohne Beschreibung"

---

## Unterstützte Objekttypen & Pflichtfelder

| Objekttyp | Pflichtfelder |
|---|---|
| Produkte | id, taxId, productNumber, stock, name |
| Kunden | id, defaultBillingAddressId, defaultShippingAddressId, customerNumber, firstName, lastName, email |
| Kategorien | id, type, name |
| Bestellungen | id, salesChannelId, orderDateTime, stateId |
| Medien | — |
| Newsletter-Empfänger | — |
| Eigenschaften | — |
| Erweiterte Preise | — |
| Variantenkonfigurationen | — |
| Cross-Selling | — |

---

## Erweiterter Identifier

**Zweite eindeutige Kennung:** Ermöglicht Zuordnung über alternative Bezeichner anstelle von UUIDs.

Beispiel: Produkt über `productNumber` statt UUID identifizieren.

---

## Benutzerdefinierte Profile

Eigene Import-/Export-Konfigurationen erstellen:
- Datenbankfelder auf CSV-Spalten mappen
- Optionale Standardwerte definieren
- Positionsreihenfolge festlegen

---

## Import-Workflows (Schritt-für-Schritt)

### Produkte importieren
1. Profil auswählen (Standard: „Produkte")
2. CSV-Datei auswählen
3. Optional: Testmodus aktivieren
4. Import starten
5. Fehlerbericht prüfen (falls vorhanden)

### Varianten importieren
Setzt vorhandene Elternartikel voraus; Produktnummer-Muster für Varianten definieren.

### Weitere Workflows
- Newsletter-Empfänger importieren
- Eigenschaften importieren
- Erweiterte Preise importieren
- Kategorien und Medien importieren
