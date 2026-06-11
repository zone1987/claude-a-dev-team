# Shopware 6 – Produkte: Vollständige Referenz

> Quelle: https://docs.shopware.com/de/shopware-6-de/kataloge/produkte  
> Gilt ab: Shopware 6.7.9.0+

---

## 1. Produktübersicht (Listansicht)

Pfad: **Kataloge > Produkte**

### Spalten der Übersicht

| Spalte | Beschreibung |
|---|---|
| Aktiv | Verfügbarkeitsstatus im Shop (grüner/roter Punkt) |
| Name | Produktbezeichnung, erscheint auf der Artikeldetailseite |
| Produktnummer | Eindeutige Kennzeichnung des Produkts |
| Preis | Preis für die Standardkundengruppe |
| Lagerbestand | Aktueller Bestand (Farbcodierung: Rot=0, Gelb=1–25, Grün>25) |
| Hersteller | Name des zugeordneten Herstellers |

Spalten sind durch Klick auf den Spaltenkopf auf- und absteigend sortierbar.
Nicht benötigte Spalten können über **Listeneinstellungen** ausgeblendet werden.
Über Listeneinstellungen ist auch der **Kompaktmodus** aktivierbar.

### Kontextmenü pro Produkt

- **Bearbeiten**: Öffnet die Produktdetailmaske
- **Duplizieren**: Erstellt eine Kopie des Produkts
- **Löschen**: Löscht das Produkt dauerhaft

> **Hinweis**: Gelöschte Produkte bleiben in bestehenden Bestellungen als Position sichtbar. Empfehlung: Inaktiv schalten statt löschen.

Bei Variantenprodukten erscheint ein Symbol vor dem Produktnamen. Klick darauf öffnet ein Modal mit Variantendetails.

---

## 2. Neues Produkt anlegen – Pflichtfelder

1. Klick auf **„Produkt hinzufügen"**
2. Mindestangaben vor dem ersten Speichern:
   - **Titel** – Produktname
   - **Produktnummer** – manuell oder auto-generiert
   - **Steuersatz** – aus Dropdown wählen
   - **Bruttopreis** und **Nettopreis**
   - **Lagerbestand** – Zahl ≥ 0
3. Auf **„Speichern"** klicken → Tabs werden freigeschaltet

---

## 3. Bereich: Allgemein

### 3.1 Informationen

| Feld | Beschreibung |
|---|---|
| Titel | Produktname für Listing und Detailseite |
| Hersteller | Auswahl aus bestehenden Herstellern oder Neuanlage direkt im Feld |
| Produktnummer | Individuelle Zuweisung, muss eindeutig sein |
| Beschreibung | WYSIWYG-Editor; Formatierungseinfügen ohne Formatierung: `Strg+Shift+V` (Mac: `Cmd+Shift+V`) |
| Produkt hervorheben | Aktiviert ein Badge im Listing (z. B. „Neu", „Empfohlen") |
| AI-Beschreibungsassistent | Verfügbar ab Rise-Plan; generiert Beschreibungen aus Produktdaten |

### 3.2 Preise

| Feld | Beschreibung |
|---|---|
| Steuersatz | Standard ist vorausgewählt, muss korrekt gesetzt sein |
| Bruttopreis | Verkaufspreis inkl. MwSt. |
| Nettopreis | Verkaufspreis exkl. MwSt.; beide Felder sind verknüpft (Kettensymbol) |
| Einkaufspreis | Interner Kalkulationswert, nicht öffentlich |
| Streichpreis | UVP / Originalpreis (wird durchgestrichen angezeigt) |
| Günstigster Preis (30 Tage) | EU-Preisangabenrichtlinie: niedrigster Preis der letzten 30 Tage |
| Währungspreise | Für jeden konfigurierten Währungskanal eigene Preise festlegbar |
| Kettensymbol | Verknüpft Brutto und Netto – Änderung eines Feldes berechnet das andere automatisch |

### 3.3 Lieferbarkeit

| Feld | Beschreibung |
|---|---|
| Lagerbestand | Aktueller Bestand; kann jederzeit geändert werden |
| Abverkauf | Wenn aktiviert: Verkauf nur bis Bestand = 0; danach nicht mehr kaufbar |
| Lieferzeit | Überschreibt die Lieferzeit der zugeordneten Versandart |
| Wiederauffüllzeit | Angabe in Tagen, wann der Artikel wieder verfügbar sein wird |
| Versandkostenfrei | Ja/Nein – Produkt ist von Versandkosten befreit |
| Mindestabnahme | Mindeststückzahl pro Bestellung |
| Staffelung | In welchen Mengenvielfachen bestellt werden kann |
| Maximalabnahme | Maximale Stückzahl pro Bestellung |

### 3.4 Lagerhäuser und Lagerhausgruppen (ab 6.4.19.0, Beyond Plan)

- Dropdown zur Auswahl der Lagerhausgruppe
- Nach Auswahl erscheint: „Verfügbarkeit und Lieferzeit nach Lagern anzeigen"
- Detailmaske zeigt Bestand pro einzelnem Lager
- Priorität pro Lager einstellbar
- Lieferzeit-Reiter mit vordefinierten Optionen: Sofort, 1–3 Tage, 2–5 Tage, 1–2 Wochen, 3–4 Wochen

---

## 4. Bereich: Zuweisung

### 4.1 Sichtbarkeit und Kategorien

| Feld | Beschreibung |
|---|---|
| Verkaufskanal | Dem Produkt zugeordnete Verkaufskanäle |
| Aktiv | Steuert ob das Produkt in der Storefront erscheint |
| Kategorien | Mehrfach-Zuweisung möglich; erscheint in der Kategorienavigation |
| Erweiterte Sichtbarkeit | Optionen: Sichtbar (Listing + Suche) / In Produktlisten ausblenden / In Produktlisten und Suche ausblenden |
| Tags | Schlagworte für Regel-Targeting und interne Sortierung |
| Such-Schlagwörter | Erweitern den Suchindex um zusätzliche Begriffe |

### 4.2 Medien

- Produktfotos, Videos, 3D-Modelle hochladen
- **Empfohlene Bildgröße**: Quadratisch, 600×600 px (optimal)
- **Zoom-Qualität**: Bis 1920×1920 px möglich
- **Video-Formate**: webm, mkv, flv, ogv, ogg, avi, mov, wmv, mp4 (Empfehlung: MP4)
- **3D-Modelle**: Nur GLB-Format, wird mit ThreeJS-Bibliothek gerendert
- **AR-Aktivierung**: Möglich für iOS 12+ und Android 8.0+ mit ARCore 1.9

### 4.3 Auszeichnung

| Feld | Beschreibung |
|---|---|
| Erscheinungsdatum | Informatives Datum für Kunden (kein Kaufstopp!) |
| EAN | European Article Number / Barcode |
| Herstellernummer | Interne Referenz, nicht öffentlich sichtbar |

---

## 5. Tab: Spezifikationen

### 5.1 Maße & Verpackung

**Produktmaße** (für Versandkostenberechnung nutzbar):

| Feld | Einheit |
|---|---|
| Breite | mm oder cm |
| Höhe | mm oder cm |
| Länge | mm oder cm |
| Gewicht | kg oder g |

**Verkaufs- & Verpackungsinformationen** (für Grundpreisberechnung):

| Feld | Beschreibung |
|---|---|
| Verkaufseinheit | Inhalt des Produkts (z. B. 0,25 oder 700) |
| Produkteinheit | Einheit des Inhalts (z. B. Liter, Flasche, Stück) |
| Grundeinheit | Referenzeinheit für Grundpreis (z. B. 1 kg, 1 L) – **verpflichtend** |
| Verpackungseinheit | Anzahl der Einheiten in der Verpackung |
| Verpackungseinheit-Mehrzahl | Mehrzahl der Verpackungseinheit |

**Grundpreisberechnung** setzt voraus: Verkaufseinheit + Produkteinheit + Grundeinheit.  
Beispiel: Flasche mit 0,25 L → Verkaufseinheit: 0,25, Produkteinheit: Liter, Grundeinheit: 1 Liter

### 5.2 Eigenschaften

- Filterbare Produktinformationen (z. B. Größe, Farbe, Material)
- Auswahl aus vordefinierten Eigenschaften (Kataloge > Eigenschaften)
- Mehrfach-Zuweisungen möglich
- Suchfunktion im Auswahlfeld verfügbar
- **AI Copilot**: Automatische Konfiguration aus Beschreibungstext (erfordert kommerziellen Plan)

### 5.3 Wesentliche Merkmale

- Vorlagen-basierte Auswahl
- Zeigt die wichtigsten Produktmerkmale im Warenkorb und Checkout an
- Kann enthalten: Eigenschaften, Zusatzfelder, Produktinfos, Grundpreisangaben

### 5.4 Zusatzfelder

- Zeigt zugewiesene Zusatzfeld-Sets (Custom Fields)
- Mögliche Feldtypen: Checkbox, Bilder, Farbauswahl, Text, Zahl, Datum
- Können in Templates via Variablen eingebunden werden

---

## 6. Tab: Erweiterte Preise

Preisregeln basieren auf dem **Rule Builder**:

- Mengenabhängige Staffelpreise
- Kunden- oder Kundengruppen-spezifische Preise
- Zeitlich begrenzte Preisaktionen
- Pro Regel: Brutto, Netto, Streichpreis, günstigster Preis (30 Tage) einstellbar

---

## 7. Tab: Varianten

### 7.1 Varianten generieren

1. Link **„Eigenschaften zuweisen"** klicken
2. Eigenschaftsgruppe auswählen (muss unter Kataloge > Eigenschaften angelegt sein)
3. Optionen aktivieren (Checkboxen je Ausprägung)
4. Preis-Auf- und Abschläge je Option definieren (optional)
5. Variantenausschlüsse konfigurieren (mehrere Bedingungen mit UND-Verknüpfung)
6. **„Varianten generieren"** klicken

### 7.2 Sortieroptionen in der Variantenliste

- Name, Preis, Lagerbestand, Produktnummer, Aktiv

### 7.3 Storefront-Darstellung

**Anzeigereihenfolge der Eigenschaften und Optionen** in der Storefront konfigurierbar.  
**Bildzuweisung** je Variante möglich.

**Produktlisten-Anzeigemodus:**

| Modus | Verhalten |
|---|---|
| Einzelne Hauptvariante → Main product | Keine vorausgewählte Variante im Listing |
| Einzelne Hauptvariante → Single Variant | Vordefinierte Variante vorausgewählt (Dropdown-Auswahl) |
| Auffächern der Eigenschaften | Mehrere Varianten als separate Produkte im Listing |

### 7.4 Einzelne Variante bearbeiten

- Kettensymbol zeigt, ob ein Feld vom Hauptprodukt **geerbt** wird (lila Symbol)
- Vererbung aufheben = Feld direkt bearbeitbar
- Alle Bereiche der Hauptmaske sind varianten-individuell konfigurierbar

### 7.5 Schnelle Änderungen (Inline-Editing)

- **Doppelklick** auf eine Zeile aktiviert Schnellbearbeitung
- Lila Kettensymbol = Vererbung aufhebbar
- Felder: Preis, Lagerbestand, Produktnummer, Medien, Aktiv-Status

### 7.6 Mehrfachänderung bei Varianten

- Bis zu **1000 Varianten** gleichzeitig auswählbar (auch seitenübergreifend)
- Verfügbare Operationen: Überschreiben, Leeren, Hinzufügen, Entfernen
- Fortschritt wird per Benachrichtigung angezeigt

---

## 8. Tab: Layout

- Erlebniswelt-Layout dem Produkt zuordnen
- Bestehendes Layout zuweisen **oder** neues Layout erstellen
- Blöcke können direkt im Produktkontext bearbeitet werden, ohne Erlebniswelten zu wechseln

---

## 9. Tab: SEO

### 9.1 SEO-Einstellungen

| Feld | Empfehlung |
|---|---|
| Meta-Titel | Maximal ~70 Zeichen (Suchmaschinen kürzen ab) |
| Meta-Beschreibung | Ideal 130–160 Zeichen |
| Schlüsselwörter | Kein direkter Ranking-Einfluss, aber für interne Suche nutzbar |
| Canonical-URL für alle Varianten | Definiert, welche Variante die kanonische URL hat |

### 9.2 SEO URLs

- Pro Verkaufskanal eigene URL definierbar
- SEO-Pfad wird automatisch aus dem Produktnamen generiert
- Bei Produkten in mehreren Kategorien: **Hauptkategorie** für die URL auswählen

---

## 10. Tab: Cross Selling

### Typ: Dynamische Produktgruppe

| Feld | Beschreibung |
|---|---|
| Titel | Bezeichnung des Cross-Selling-Blocks |
| Aktiv | Ein-/Ausschalten |
| Position | Reihenfolge (1, 2, 3, …) |
| Produktgruppe | Auswahl der dynamischen Produktgruppe |
| Sortierung | Name, Preis, Erscheinungsdatum |
| Maximale Produktanzahl | Anzahl der angezeigten Produkte |
| Vorschau | Zeigt aktuell zutreffende Produkte |

### Typ: Manuelle Zuweisung

Identische Felder wie oben, zusätzlich:
- Manuelle Auswahl der zugeordneten Produkte (Ein- oder Mehrfachauswahl)

---

## 11. Tab: Bundles (Shopware Services Feature)

### Bundles hinzufügen

1. **„Produkt zu Bundles hinzufügen"** klicken
2. Suche nach vorhandenen Bundles
3. Mehrfachauswahl möglich
4. Bestätigen

### Bundles bearbeiten

- Übersicht: Produktanzahl, Verfügbarkeit, Aktivstatus
- Kontextmenü:
  - Bundle-Details öffnen
  - Auf Produktdetailseite anzeigen / nicht anzeigen
  - Bundle entfernen

Synchronisierung ist **bidirektional** zwischen Produkt und Bundle-Verwaltung.

---

## 12. Tab: Bewertungen

- Übersicht aller Kundenbewertungen für dieses Produkt
- **Sichtbar-Markierung** erforderlich damit Bewertung in der Storefront erscheint
- Bearbeitung per Kontextmenü
- Link auf die Bewertungs-Detailseite (Kataloge > Bewertungen)

---

## 13. Digitale Produkte

Digitale Produkte haben dieselbe Maske, zusätzlich:

| Merkmal | Detail |
|---|---|
| Datei-Upload | Im Medien-Bereich; alle gängigen digitalen Formate |
| Backend-Erkennung | Badge zeigt an, dass es sich um ein digitales Produkt handelt |
| Varianten | Auch bei digitalen Produkten möglich (z. B. physisch + digital) |
| Bestellprozess | Checkbox für Rechtshinweis bei Bestellung |
| Lieferung | E-Mail mit Datei-Anhang nach Zahlungseingang |
| Kundenkonto | Kunden laden Datei unter „Mein Konto > Bestellungen" herunter |

---

## 14. Erweiterter Bearbeitungsmodus

- Toggle oben rechts in der Produktmaske
- Wenn deaktiviert: Checkboxen zum Ein-/Ausblenden von Abschnitten
- Betrifft die Bereiche „Allgemein" und „Spezifikationen"
- Ermöglicht vereinfachte Ansicht für Einsteiger

---

## 15. Mehrfachänderung in der Produktübersicht

1. Produkte in der Liste auswählen (max. 1000)
2. **„Mehrfachänderung"** klicken
3. Checkboxen der zu ändernden Felder setzen
4. Werte eingeben
5. Dropdown-Operationen:
   - **Überschreiben**: Bestehende Werte ersetzen
   - **Leeren**: Alle Einstellungen des Blocks entfernen
   - **Hinzufügen**: Ergänzen ohne Bestehendes zu löschen
   - **Entfernen**: Bestimmte Einstellungen gezielt löschen
6. Speichern → Fortschrittsanzeige

---

## 16. Produktübersicht-Linksammlung

| Bereich | Admin-Pfad |
|---|---|
| Produktübersicht | Kataloge > Produkte |
| Eigenschaften | Kataloge > Eigenschaften |
| Kategorien | Kataloge > Kategorien |
| Dynamische Produktgruppen | Kataloge > Dynamische Produktgruppen |
| Steuern | Einstellungen > Handel > Steuern |
| Versandarten | Einstellungen > Versand > Versandarten |
| Lagerhäuser | Einstellungen > Lagerhäuser |
| Erlebniswelten | Inhalte > Erlebniswelten |

---

*Quelle: https://docs.shopware.com/de/shopware-6-de/kataloge/produkte*
