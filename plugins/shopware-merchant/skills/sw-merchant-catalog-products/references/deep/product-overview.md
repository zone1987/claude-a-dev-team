# Shopware 6 – Produktübersicht (Listansicht): Vollständige Referenz

> Quelle: https://docs.shopware.com/de/shopware-6-de/produkte/uebersicht  
> Gilt ab: Shopware 6.0.0+

---

## 1. Überblick

Die Produktübersicht unter **Kataloge > Produkte** ist die zentrale Liste aller angelegten Produkte. Sie bietet eine schnelle Orientierung und ermöglicht Massenoperationen.

---

## 2. Spalten und Darstellung

### Standard-Spalten

| Spalte | Beschreibung | Sortierbar |
|---|---|---|
| Aktiv | Verfügbarkeitsstatus (grün = aktiv, rot = inaktiv) | Ja |
| Name | Produktbezeichnung | Ja |
| Produktnummer | Eindeutige Kennzeichnung | Ja |
| Preis | Preis für die Standardkundengruppe | Ja |
| Lagerbestand | Aktueller Bestand (farbkodiert) | Ja |
| Hersteller | Zugeordneter Herstellername | Ja |

### Lagerbestand-Farbkodierung

| Farbe | Bestand |
|---|---|
| Rot | 0 (nicht auf Lager) |
| Gelb | 1–25 (niedriger Bestand) |
| Grün | > 25 (ausreichend) |

### Spalten anpassen

Über **Listeneinstellungen** (Zahnrad-Symbol):
- Spalten ein- und ausblenden
- Spaltenreihenfolge per Drag & Drop anpassen
- **Kompaktmodus** aktivieren (weniger Zeilenhöhe, mehr Produkte sichtbar)

---

## 3. Kontextmenü pro Produkt

Klick auf **„..."** (Drei-Punkte-Button) rechts neben einem Produkt:

| Option | Beschreibung |
|---|---|
| Bearbeiten | Öffnet die vollständige Produktdetailmaske |
| Duplizieren | Erstellt eine Kopie des Produkts mit allen Einstellungen |
| Löschen | Löscht das Produkt dauerhaft |

### Variantenprodukte

- Symbol vor dem Produktnamen zeigt, dass es sich um ein Variantenprodukt handelt
- Klick auf das Symbol öffnet ein **Modal** mit Übersicht aller Varianten und deren Kerninfos

---

## 4. Mehrfachänderung

### Was ist Mehrfachänderung?

Die Mehrfachänderung ermöglicht die gleichzeitige Bearbeitung mehrerer Produkte ohne jedes einzeln öffnen zu müssen. Besonders nützlich für Massenaktualisierungen von Preisen, Kategorien oder Status.

### Voraussetzungen

- Maximal **1000 Produkte** pro Vorgang
- Auswahl kann seitenübergreifend erfolgen

### Schritt-für-Schritt

1. Produkte auswählen (Checkbox links neben dem Produkt)
   - Einzelne Produkte: Checkboxen anklicken
   - Alle auf der Seite: Checkbox im Tabellenkopf
   - Alle Seiten: Erweiterte Auswahl nutzen
2. Button **„Mehrfachänderung"** klickt
3. Gewünschte Felder per **Checkbox** aktivieren
4. Werte eingeben oder Operationen auswählen
5. Speichern → Fortschrittsbalken erscheint

### Dropdown-Operationen

| Operation | Verhalten |
|---|---|
| **Überschreiben** | Ersetzt alle bisherigen Werte durch den neuen Wert |
| **Leeren** | Entfernt alle Einstellungen dieses Blocks (löscht Werte) |
| **Hinzufügen** | Ergänzt den neuen Wert ohne bestehende Werte zu löschen |
| **Entfernen** | Löscht spezifisch den angegebenen Wert aus der Zuordnung |

### Änderbare Felder

**Allgemein:**
- Aktiv-Status (Ein/Aus für alle ausgewählten Produkte)
- Hersteller
- Tags (hinzufügen/entfernen)
- Sichtbarkeit / Erweiterte Sichtbarkeit
- Kategorien
- Such-Schlagwörter
- Versandkostenfrei

**Lieferbarkeit:**
- Lagerbestand
- Abverkauf
- Lieferzeit
- Wiederauffüllzeit
- Mindest-/Staffel-/Maximalabnahme

**Preise (Basis-Preisfelder):**
- Steuersatz
- Bruttopreis / Nettopreis
- Streichpreis
- Einkaufspreis
- Günstigster Preis (30 Tage)

**Erweiterte Preise:**
- Staffelpreise und regelbasierte Preise über ein Modal-Interface
- Optionen: Duplizieren, Löschen, Hinzufügen von Preisregeln

---

## 5. Suche und Filter

### Volltextsuche

- Suchfeld oben in der Produktliste
- Sucht in: Name, Produktnummer, EAN, Herstellernummer

### Listenfilter

Filter-Optionen (je nach Konfiguration verfügbar):
- Aktiv / Inaktiv
- Hersteller
- Kategorien
- Lagerbestand-Bereiche
- Verkaufskanal-Zuordnung

---

## 6. Wichtige Hinweise

### Produkte löschen vs. deaktivieren

> **Empfehlung**: Produkte **nicht löschen** wenn sie in bestehenden Bestellungen vorkommen!
> 
> Gelöschte Produkte bleiben zwar als Positionen in Bestellungen sichtbar, aber alle weiteren Verwaltungsoptionen (Retouren, Nachbestellungen etc.) können eingeschränkt sein.
>
> **Besser**: Produkt **inaktiv** schalten (Aktiv-Status deaktivieren)

### Variantenprodukte in der Liste

- Das Variantensymbol erscheint nur beim Hauptprodukt
- Varianten selbst erscheinen nicht als separate Zeilen in der Liste
- Über das Modal (Klick auf Variantensymbol) Varianten-Schnellübersicht abrufen

---

*Quelle: https://docs.shopware.com/de/shopware-6-de/produkte/uebersicht*
