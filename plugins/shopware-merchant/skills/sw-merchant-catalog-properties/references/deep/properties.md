# Shopware 6 – Eigenschaften: Vollständige Referenz

> Quelle: https://docs.shopware.com/de/shopware-6-de/produkte/eigenschaften  
> Gilt ab: Shopware 6.4.0.0+

---

## 1. Was sind Eigenschaften?

Eigenschaften (Properties) sind filterbare Produktinformationen in Shopware 6. Sie dienen zwei Hauptzwecken:

1. **Produktfilter**: Kunden können im Listing nach Eigenschaften filtern (z. B. Größe: M, Farbe: Rot)
2. **Variantengenerierung**: Eigenschaften sind die Basis für Produktvarianten

Verwaltung unter: **Kataloge > Eigenschaften**

---

## 2. Eigenschaftsübersicht

### Spalten der Liste

| Spalte | Beschreibung |
|---|---|
| Eigenschaftsname | Name der Eigenschaftsgruppe (z. B. „Größe", „Farbe") |
| Ausprägungen | Zugeordnete Werte (z. B. „XS, S, M, L, XL, XXL") |
| Beschreibung | Optionale Beschreibung der Eigenschaft |
| Produktfilter-Sichtbarkeit | Zeigt ob die Eigenschaft im Filter erscheint |
| Aktionsmenü („...") | Bearbeiten oder Löschen |

> **WARNUNG**: Das Löschen einer Eigenschaft entfernt diese **von allen zugewiesenen Produkten** inkl. aller Ausprägungen!

---

## 3. Neue Eigenschaft anlegen

1. Klick auf **„Eigenschaft hinzufügen"**
2. Grundinformationen ausfüllen (siehe Felder unten)
3. Ausprägungen (Werte) hinzufügen
4. Speichern

### 3.1 Grundinformationsfelder

| Feld | Beschreibung | Pflicht |
|---|---|---|
| Name | Eigenschaftsname; erscheint auf Produktdetailseite und in Filtern | Ja |
| Beschreibung | Optionale Erklärung der Eigenschaft | Nein |
| Produktfilter-Sichtbarkeit | Toggle; bestimmt ob diese Eigenschaft im Listing-Filter erscheint | Nein |
| Anzeigetyp | Art der Darstellung im Filter | Nein |
| Sortierung | Sortierart für Ausprägungen | Nein |
| Position | Reihenfolge auf der Produktdetailseite | Nein |

### 3.2 Anzeigetypen

| Typ | Darstellung im Filter | Darstellung im Produkt |
|---|---|---|
| **Text** | Textuell (Standard) | Textuell |
| **Farbe** | Farbige Kreise/Kacheln (HEX-Wert) | Farbige Optionsfelder |
| **Bild** | Benutzerdefinierte Bilder | Bilder als Auswahl |
| **Dropdown** | Textbasiiert im Filter | Dropdown-Menü auf Detailseite |

### 3.3 Sortieroptionen

| Option | Verhalten |
|---|---|
| **Alphanumerisch** | Automatische Sortierung a–z, dann 1–10 |
| **Benutzerdefiniert** | Manuell über das Positionsfeld der Ausprägungen steuerbar |

---

## 4. Ausprägungen (Werte) anlegen

Ausprägungen sind die konkreten Werte einer Eigenschaft.  
Beispiel: Eigenschaft „Größe" → Ausprägungen: XS, S, M, L, XL, XXL

### 4.1 Felder je Ausprägung

| Feld | Beschreibung | Verfügbar bei Typ |
|---|---|---|
| Name | Bezeichnung der Ausprägung (z. B. „Rot", „XL") | Alle |
| Position | Numerische Position für benutzerdefinierte Sortierung | Alle |
| Farb-HEX | Hexadezimaler Farbwert (z. B. `#FF0000`) | Nur Typ: Farbe |
| Bild | Bild-Upload oder URL | Nur Typ: Bild |

### 4.2 Bild-Upload für Ausprägungen (Typ: Bild)

Zwei Methoden:
1. **Aus Medienverwaltung wählen**: Bestehende Medien aus Inhalte > Medien auswählen
2. **Lokale Datei hochladen**: Datei vom Computer direkt hochladen
3. **URL-Import**: Öffentlich erreichbare Bild-URL eingeben

---

## 5. Eigenschaften Produkten zuweisen

In der Produktmaske unter **Tab Spezifikationen > Eigenschaften**:

1. Produktmaske öffnen (Kataloge > Produkte > Produkt)
2. Tab **Spezifikationen** wählen
3. Bereich **Eigenschaften** → **Eigenschaft hinzufügen** klicken
4. Eigenschaftsgruppe aus Dropdown wählen
5. Ausprägungen (Werte) auswählen
6. Mehrfachzuweisungen von verschiedenen Eigenschaftsgruppen möglich

### AI Copilot (kommerzieller Plan)

Der **AI Copilot** kann Eigenschaften automatisch aus der Produktbeschreibung konfigurieren:
- Beschreibung muss ausreichend detailliert sein
- AI erkennt relevante Eigenschaften und schlägt Ausprägungen vor
- Vorschläge können manuell angepasst werden

---

## 6. Eigenschaften als Varianten-Basis

Eigenschaften bilden die Grundlage für Produktvarianten:

1. Produkt anlegen (Hauptprodukt)
2. Tab **Varianten** öffnen
3. Auf **„Eigenschaften zuweisen"** klicken
4. Eigenschaftsgruppen mit gewünschten Ausprägungen auswählen
5. Variantenausschlüsse konfigurieren (optional)
6. **„Varianten generieren"** klicken

Shopware erstellt dann automatisch alle Kombinationen der ausgewählten Ausprägungen.

**Beispiel:**
- Eigenschaft „Größe": S, M, L
- Eigenschaft „Farbe": Rot, Blau
- Ergibt: 6 Varianten (S/Rot, S/Blau, M/Rot, M/Blau, L/Rot, L/Blau)

---

## 7. Eigenschaften im Produktfilter

Damit eine Eigenschaft im Listing-Filter erscheint:

1. Eigenschaft bearbeiten
2. **„Produktfilter-Sichtbarkeit"** aktivieren
3. Speichern

Die Eigenschaft erscheint dann automatisch in den Filtermöglichkeiten der zugehörigen Kategorieseiten.

---

## 8. Unterschied: Eigenschaften vs. Zusatzfelder vs. Wesentliche Merkmale

| Funktion | Eigenschaften | Zusatzfelder | Wesentliche Merkmale |
|---|---|---|---|
| Filterbar | Ja | Nein | Nein |
| Variantenbasis | Ja | Nein | Nein |
| Storefront-Filter | Ja | Nein | Nein |
| Warenkorb/Checkout | Nein | Möglich | Ja |
| Freitext | Nein | Ja | Nein |
| Template-Variable | Nein | Ja | Nein |

---

## 9. Tipps

- Eigenschaftsnamen sollten **konsistent** und **eindeutig** gewählt werden (z. B. immer „Größe" statt mal „Größe" mal „Size")
- Ausprägungen können **nachträglich** ergänzt werden ohne bestehende Varianten zu beeinflussen
- Bei Typ **Farbe**: Den HEX-Wert korrekt eingeben (#RRGGBB Format)
- **Sortierung**: Bei alphanumerisch werden Zahlen korrekt sortiert (1, 2, 10 statt 1, 10, 2)
- Eigenschaften aus einem Produkt entfernen löscht die Eigenschaft **nicht** systemweit

---

*Quelle: https://docs.shopware.com/de/shopware-6-de/produkte/eigenschaften*
