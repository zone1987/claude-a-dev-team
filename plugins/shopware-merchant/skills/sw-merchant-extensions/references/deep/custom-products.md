# Custom Products – Konfigurierbare Produkte

**Quelle**: https://docs.shopware.com/de/shopware-6-de/erweiterungen/customproducts  
**Plan**: Shopware Rise (oder höher)  
**Pfad im Admin**: Katalog > Custom Products

## Überblick

**Custom Products** ermöglicht es, Produkte mit individuell konfigurierbaren Optionen anzubieten.
Kunden können Produkte auf der Produktdetailseite personalisieren (z. B. Gravuren, Drucke,
Farben, Maßangaben).

---

## Konzept

```
Custom Products Template
└── Produkt-Template (Vorlage)
    ├── Optionsgruppe 1 (z. B. "Beschriftung")
    │   ├── Option: Textfeld (Eingabe)
    │   └── Option: Schriftart (Dropdown)
    └── Optionsgruppe 2 (z. B. "Material")
        ├── Option: Holz (+5,00 €)
        └── Option: Metall (+15,00 €)
```

Templates werden erstellt und dann mit **beliebig vielen Produkten** verknüpft.

---

## Template erstellen

1. **Katalog > Custom Products** öffnen
2. **Neues Template** anlegen
3. Template-Namen vergeben (intern)
4. Optionsgruppen und Optionen hinzufügen

---

## Optionstypen (12 verfügbar)

| Typ | Beschreibung |
|---|---|
| **Textfeld** | Einzeilige Texteingabe ("Mit dem Textfeld bietest Du dem Kunden die Möglichkeit, dem Artikel einen einzeiligen Text hinzuzufügen.") |
| **Textarea** | Mehrzeilige Texteingabe |
| **Datum** | Datumsauswahl |
| **Zeit** | Zeitauswahl |
| **Farbwähler** | Farbpalette zur Auswahl |
| **Bildauswahl** | Kunden laden eigene Bilder hoch |
| **Checkbox** | Ja/Nein-Option |
| **Mehrfachauswahl** | Mehrere Optionen gleichzeitig wählbar |
| **Einzelauswahl (Radio)** | Genau eine Option wählbar |
| **Dropdown** | Auswahl aus Liste |
| **Dateiupload** | Kunden laden Dateien hoch |
| **HTML-Editor** | Rich-Text-Eingabe |

---

## Preiskonfiguration

### Aufpreise pro Option
- **Absolut**: Fester Betrag (z. B. +5,00 €)
- **Relativ (%)**: Prozentaufschlag auf Basispreis
- **Währungsspezifisch**: Verschiedene Preise pro Währung
- **Regelbasiert (Advanced)**: Rule-Builder-Aufpreise

### Preisanzeige
Der Endpreis = Basispreis + Summe aller gewählten Aufpreise.
Die Konfiguration wird im Warenkorb und in der Bestellübersicht angezeigt.

---

## Anzeigemodi im Storefront

### Normal-Modus
- Alle Optionen gleichzeitig sichtbar
- Angezeigt **über** dem "In den Warenkorb"-Button

### Schritt-für-Schritt-Modus (Step-by-Step)
- Kunden werden durch Optionen geführt
- Jeweils eine Gruppe auf einmal sichtbar
- Weiter-Button zwischen Gruppen

---

## Erweiterte Funktionen

| Funktion | Beschreibung |
|---|---|
| **Inkompatible Optionen ausschließen** | Bestimmte Kombinationen verhindern |
| **Konfiguration bestätigen** | Kunden müssen Konfiguration explizit bestätigen |
| **Konfigurationslink teilen** | Kunden können ihre Konfiguration als Link teilen |
| **Dateizugriff in Bestelldetails** | Hochgeladene Dateien im Admin abrufbar |

---

## Template mit Produkt verknüpfen

1. Produkt in **Katalog > Produkte** öffnen
2. Tab **Custom Products** auswählen
3. Vorhandenes Template auswählen oder neues erstellen

Ein Template kann mit beliebig vielen Produkten verknüpft werden.

---

## Häufige Anwendungsfälle

- Druckereien: Text-/Bildaufdrucke auf T-Shirts, Tassen
- Schmuck: Gravuren, Materialwahl
- Tischlereien: Maßangaben, Holzart, Farbe
- Backwaren: Beschriftungen, Dekoration
- Fotodienstleistungen: Bildupload für Fotodrucke
