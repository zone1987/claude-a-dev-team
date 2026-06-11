# Shopware 6 – Dynamische Produktgruppen: Vollständige Referenz

> Quelle: https://docs.shopware.com/de/shopware-6-de/Kataloge/DynamischeProduktgruppen  
> Gilt ab: Shopware 6.4.12.0+

---

## 1. Was sind Dynamische Produktgruppen?

Dynamische Produktgruppen (auch: Produktstreams) sind regelbasierte Produktmengen. Shopware sammelt automatisch alle Produkte, die die definierten Bedingungen erfüllen. Die Gruppe aktualisiert sich dynamisch – neue Produkte, die die Regeln erfüllen, werden automatisch hinzugefügt; Produkte, die nicht mehr passen, fallen automatisch heraus.

Verwaltung unter: **Kataloge > Dynamische Produktgruppen**

---

## 2. Produktgruppenübersicht

### Spalten der Übersicht

| Spalte | Beschreibung |
|---|---|
| Name | Bezeichnung der Produktgruppe |
| Beschreibung | Optionale Beschreibung |
| Änderungsdatum | Datum der letzten Bearbeitung |
| Status | Zeigt ob alle Regeln gültig und vollständig konfiguriert sind |

### Kontextmenü

| Option | Beschreibung |
|---|---|
| Bearbeiten | Öffnet Bearbeitungsmaske der Produktgruppe |
| Duplizieren | Erstellt Kopie inkl. aller Bedingungen |
| Löschen | Löscht die Produktgruppe (Zuweisung in Kategorien etc. wird ebenfalls entfernt) |

---

## 3. Neue Produktgruppe anlegen

1. Klick auf **„Produktgruppe anlegen"**
2. **Name** eingeben (Pflichtfeld)
3. **Beschreibung** eingeben (optional)
4. **Speichern** oder **„Speichern und duplizieren"**
5. Bedingungen im Regelwerk definieren

---

## 4. Bedingungen / Regelwerk

### 4.1 Aufbau des Regelwerks

Das Regelwerk ist ein visueller Editor mit folgenden Elementen:

| Element | Beschreibung |
|---|---|
| Eigenschaftsauswahl (1) | Art der Bedingung (Kategorie, Preis, Tag, etc.) |
| Bedingungstyp (2) | Vergleichsoperator (gleich, größer als, etc.) |
| UND-Verknüpfung (3) | Alle Bedingungen dieser Ebene müssen zutreffen |
| ODER-Verknüpfung (4) | Mindestens eine Bedingung muss zutreffen |
| Unterbedingungen (5) | Verschachtelte Bedingungsgruppen |
| Kontextmenü (6) | Einfügen vor/nach bestehenden Bedingungen |
| Vorschau-Button (7) | Zeigt Produkte die aktuell den Regeln entsprechen |

### 4.2 Verfügbare Operatoren

| Operator | Bedeutung |
|---|---|
| Gleich | Exakt dieser Wert |
| Ungleich | Nicht dieser Wert |
| Eins von | Einer der angegebenen Werte |
| Keins von | Keiner der angegebenen Werte |
| Alle von | Alle angegebenen Werte müssen zutreffen |
| Alle außer | Alle außer den angegebenen Werten |
| Größer als | Numerischer Vergleich (z. B. Preis) |
| Kleiner als | Numerischer Vergleich |
| Größer gleich | Numerischer Vergleich inkl. Gleichheit |
| Kleiner gleich | Numerischer Vergleich inkl. Gleichheit |
| Enthält | Textteilstring-Suche |
| Enthält nicht | Textteilstring-Ausschluss |

### 4.3 Verfügbare Bedingungstypen

**Produkt-Bedingungen:**
- Produkt (explizite Produktauswahl per ID/Name)
- Produktnummer
- Produktname

**Kategorie-Bedingungen:**
- Kategorie (mit Kategoriepfad-Auswahl)
- Kategoriebaumebene

**Eigenschaften und Ausprägungen:**
- Eigenschaftsgruppe
- Eigenschafts-Ausprägung (spezifischer Wert)

**Tags:**
- Tag (Schlagwort-Zuweisung)

**Preis-Bedingungen:**
- Preis (brutto/netto, je Währung separat filterbar)
- Streichpreis
- Einkaufspreis

**Bestand & Lieferbarkeit:**
- Lagerbestand (Zahl-Vergleich)
- Abverkauf (Ja/Nein)
- Versandkostenfrei (Ja/Nein)

**Lieferzeiten:**
- Lieferzeit (ID oder Name der Lieferzeit)

**Hersteller:**
- Hersteller (Auswahl des Herstellers)

**Medien:**
- Hat Medien / Hat keine Medien

**Aktiv-Status:**
- Produkt aktiv (Ja/Nein)

**Benutzerdefinierte Felder:**
- Zusatzfelder (Custom Fields) – feldspezifische Bedingungen

### 4.4 Verknüpfungslogik

```
Bedingungsgruppe (UND)
├── Kategorie = "Bekleidung"           ← muss zutreffen
└── ODER-Gruppe
    ├── Farbe = "Rot"                  ← mindestens eine dieser
    └── Farbe = "Blau"                 ← Bedingungen muss zutreffen

+ Preis < 50 EUR                       ← muss ebenfalls zutreffen
```

Unterbedingungen ermöglichen komplexe Verschachtelungen für präzise Produktauswahl.

---

## 5. Vorschau

Der **Vorschau-Button** zeigt in Echtzeit, welche Produkte aktuell den definierten Regeln entsprechen.

- Zeigt Produktname, Preis, Lagerbestand
- Hilft beim Testen und Validieren der Regeln vor der Aktivierung
- Aktualisiert sich nach Regeländerungen sofort

---

## 6. Einsatzbereiche

### 6.1 Kategorien dynamisch befüllen

Statt manuelle Produktzuweisung in Kategorien:

1. Kategorie öffnen (Kataloge > Kategorien)
2. Tab **Produkte**
3. Typ: **Dynamische Produktgruppe** wählen
4. Produktgruppe auswählen

> **Hinweis**: Wechsel zu dynamischer Zuordnung deaktiviert alle manuellen Zuweisungen in dieser Kategorie!

### 6.2 Produktfeeds / Produktvergleiche

- Produktgruppen können für externe Feeds (z. B. Google Shopping) genutzt werden
- Ermöglicht automatische Feed-Aktualisierung ohne manuelle Pflege

### 6.3 Erlebniswelten (Produkt-Slider)

In Erlebniswelten (Inhalte > Erlebniswelten):
- **Commerce-Block „Produkt-Slider"** kann eine dynamische Produktgruppe als Quelle nutzen
- Produkte aktualisieren sich automatisch je nach Regelerfüllung

### 6.4 Cross-Selling auf Produktdetailseite

In der Produktmaske unter **Tab Cross Selling**:
- Typ: **Dynamische Produktgruppe** wählen
- Produktgruppe auswählen
- Sortierung (Name, Preis, Erscheinungsdatum) und maximale Anzahl festlegen

---

## 7. Status und Validierung

Der **Status** in der Übersicht zeigt:
- Grün/Aktiv: Alle Regeln sind gültig und vollständig konfiguriert
- Rot/Inaktiv: Regeln haben Fehler oder sind unvollständig (z. B. fehlende Werte)

---

## 8. Beispiele

### Beispiel 1: Alle Produkte unter 20 EUR in der Kategorie „Sale"

Bedingungen:
```
UND
├── Kategorie = "Sale"
└── Preis <= 20.00 EUR
```

### Beispiel 2: Produkte eines Herstellers in einer bestimmten Farbe

Bedingungen:
```
UND
├── Hersteller = "Nike"
└── Eigenschaft Farbe = EINS VON ["Rot", "Blau", "Schwarz"]
```

### Beispiel 3: Neue Produkte der letzten 30 Tage mit Lagerbestand

Bedingungen:
```
UND
├── Lagerbestand > 0
├── Abverkauf = Nein
└── Erscheinungsdatum >= [Datum vor 30 Tagen]
```

### Beispiel 4: Bestseller nach Tag markieren

Bedingungen:
```
UND
└── Tag = "Bestseller"
```
(Produkte manuell mit dem Tag „Bestseller" versehen)

---

## 9. Tipps und Best Practices

- Dynamische Produktgruppen sollten **sprechende Namen** haben, die den Inhalt klar beschreiben
- Die **Vorschau** vor dem Speichern nutzen um unerwartete Produktmengen zu vermeiden
- Komplexe Verschachtelungen machen Regeln schwer wartbar → auf Einfachheit achten
- Für saisonale Aktionen eignen sich datumsbezogene Bedingungen
- Zu viele ODER-Verknüpfungen können sehr große Produktmengen ergeben → Produktanzahl in der Vorschau prüfen
- Beim **Duplizieren** einer Produktgruppe werden alle Bedingungen übernommen – ideal für ähnliche Gruppen

---

*Quelle: https://docs.shopware.com/de/shopware-6-de/Kataloge/DynamischeProduktgruppen*
