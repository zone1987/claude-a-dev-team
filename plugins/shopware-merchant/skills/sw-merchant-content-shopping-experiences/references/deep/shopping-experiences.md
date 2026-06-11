# Shopware 6 – Erlebniswelten: Vollständige Dokumentation

**Quelle:** https://docs.shopware.com/de/shopware-6-de/Inhalte/Erlebniswelten  
**Version:** ab 6.7.9.0 (ältere Versionen ab 6.0.0 verfügbar)

---

## Screenshots

| Datei | Inhalt |
|---|---|
| `../../assets/uebersicht.png` | Erlebniswelten-Übersicht |
| `../../assets/layout-erstellen.png` | Dialog: Neues Layout anlegen |
| `../../assets/sektion-auswahl.png` | Sektions-Layout-Auswahl |
| `../../assets/layout-editor.png` | Layout-Editor Gesamtansicht |
| `../../assets/shopseite.png` | Shopseiten-Auswahl |
| `../../assets/ai-copilot.png` | AI Copilot Text-Vorschlag |
| `../../assets/bild-element.jpg` | Bild-Element Einstellungen |
| `../../assets/slider-einstellungen.png` | Slider-Block Einstellungen |
| `../../assets/galerie-einstellungen.png` | Galerie-Block Einstellungen |
| `../../assets/produkt-slider-einstellungen.png` | Produkt-Slider Einstellungen |
| `../../assets/block-einstellungen.png` | Block-Einstellungen Panel |
| `../../assets/sektions-einstellungen.png` | Sektions-Einstellungen Panel |
| `../../assets/sichtbarkeit.png` | Viewport-Sichtbarkeit |
| `../../assets/navigator.png` | Navigator-Ansicht |
| `../../assets/layout-zuweisung.png` | Layout-Zuweisungs-Dialog |
| `../../assets/kategorieseite.png` | Kategorieseite mit Listing |
| `../../assets/standardlayout.png` | Standardlayout festlegen |

---

## Übersicht und Navigation

Der Menüpunkt **Erlebniswelten** befindet sich unter **Inhalte** in der linken Admin-Navigation.

Auf der Übersichtsseite sind alle erstellten Layouts aufgelistet. Verfügbare Funktionen:
- **Suche** nach Layoutnamen
- **Sortierung** nach Erstell-/Änderungsdatum
- **Filtern** nach Layouttyp (Shopseiten, Landingpages, etc.)
- **Kontextmenü** (3 Punkte): Löschen, Duplizieren, Vorschau
- **Button**: „Neues Layout anlegen"

---

## Layout-Typen

### Shopseite
- **Verwendung**: Informationsseiten wie AGB, Impressum, Versandinfos, Kontaktformular
- **Zuweisung**: Einstellungen > Shops > Stammdaten > Bereich „Shopseiten"
- **Besonderheit**: Keine automatische URL-Generierung; Zuweisung über Shop-Konfiguration

### Landingpage
- **Verwendung**: Marketing-Kampagnen, Sonderaktionen, thematische Seiten
- **Zuweisung**: Über Kataloge > Kategorien (Kategorie als Landingpage markieren)
- **URL**: Aufruf über die URL der zugeordneten Kategorie
- **Hinweis**: Kein fest integriertes Produktlisting; Navigation kann ausgeblendet werden

### Kategorieseite
- **Verwendung**: Startseite von Kategorien mit Produktlisting
- **Besonderheit**: Enthält automatisch den Produktlisting-Block
- **Filter & Sortierung**: Konfigurierbar im Block-Bereich „Produktlisting"
- **Zuweisung**: Kataloge > Kategorien > Tab Layout

### Produktseite
- **Verwendung**: Individuelle Produktdetailseiten
- **Zuweisung**: Kataloge > Produkte > Produkt öffnen > Tab „Layout"
- **Individuelle Anpassung**: Einzelne Element-Werte können pro Produkt überschrieben werden
  (Produktname, Bilder, Beschreibung – ohne globale Layout-Änderung)

### Bundle-Seite
- **Verwendung**: Layouts für Produkt-Bundles
- **Besonderheit**: Automatische Datenbefüllung (Produktliste, Bundle-Name, Galerie, Beschreibung)
- **Voraussetzung**: Shopware Services / Bundles-Erweiterung

---

## Layout-Editor: Aufbau und Bedienung

### Linker Bereich: Vorschaufläche
- Zeigt das Layout in Echtzeit
- Klick auf Block öffnet Block-Einstellungen in rechter Sidebar
- Drag & Drop zwischen Sektionen möglich

### Rechte Sidebar: Werkzeuge

| Tab | Funktion |
|---|---|
| Einstellungen | Allgemeine Layout-Einstellungen |
| Blöcke | Block-Bibliothek nach Kategorien geordnet |
| Navigator | Hierarchische Blockübersicht |
| Layout-Zuweisung | Direktzuweisung an Kategorien |

---

## Sektionen (Sections)

### Neue Sektion hinzufügen
Unterer Bereich der Vorschaufläche → „Neue Sektion hinzufügen" → Layout wählen.

**Layoutoptionen:**
- Volle Breite (ohne Sidebar)
- Mit Sidebar links
- Mit Sidebar rechts

### Sektions-Einstellungen

Klick auf Sektionsrand → rechte Sidebar zeigt:

| Einstellung | Werte | Beschreibung |
|---|---|---|
| Sektionsname | Freitext | Identifikation im Navigator |
| CSS-Klassen | Freitext | Mehrere mit Leerzeichen trennen |
| Größenmodus | Volle Breite / Zentriert | Breite der Inhalte |
| Mobiles Sidebar-Verhalten | Angezeigt / Nicht angezeigt | Sidebar auf Mobilgeräten |
| Hintergrundfarbe | Farbauswahl + Hex | Farbe des Sektionshintergrunds |
| Hintergrundbild | Medienauswahl | Bild als Hintergrund |
| Bildmodus | Standard / Füllen / Strecken | Wie Hintergrundbild dargestellt wird |

---

## Blöcke

### Block aus Bibliothek einfügen
Rechte Sidebar → Tab „Blöcke" → Kategorie wählen → Block per Drag & Drop in Sektion ziehen.

### Block-Einstellungen

Klick auf Block → rechte Sidebar zeigt:

| Einstellung | Beschreibung |
|---|---|
| Name | Bezeichnung im Navigator |
| Hintergrundfarbe | Hex-Eingabe möglich |
| Hintergrundbild | Aus Medienbibliothek |
| Bildmodus | Standard / Füllen / Strecken |
| Layout/CSS-Klassen | Benutzerdefinierte CSS-Klassen |
| Abstände | Innen-/Außenabstände konfigurierbar |

---

## Elemente (Block-Inhalte)

### Text-Elemente

**Basis-Texteditor:**
- Formatierung: Bold, Italic, Underline, Listen, Einrückung
- Überschriften-Level (H1–H6)
- Textfarbe und Ausrichtung

**Erweiterte Funktionen auf Kategorieseiten:**
- **Datenzuordnung**: Dynamische Inhalte aus Kategoriedaten (Name, Beschreibung, etc.)
- **Variablen**: `{{ variablenname }}` für direkte Dateneinfügung

**Links einfügen:**
- URL (extern oder intern)
- Produkt (aus Katalog wählen)
- Kategorie (aus Kategoriebaum)
- E-Mail-Adresse
- Telefonnummer

**AI Copilot** (Shopware Commercial, kommerzieller Plan):
- Button „Text vorschlagen lassen"
- KI generiert Textvorschläge auf Basis des Kontexts
- Vorschlag kann übernommen oder verworfen werden

---

### Bild-Elemente

**Bildauswahl:**
- Aus Medienbereich wählen
- Direktupload möglich

**Datenzuordnung** (Produktseiten):
- Automatische Befüllung mit Produktbildern

**Anzeige-Einstellungen:**

| Einstellung | Optionen |
|---|---|
| Anzeigemodus | Standard / Füllen / Strecken |
| Vertikale Ausrichtung | Oben / Mitte / Unten |
| Horizontale Ausrichtung | Links / Mitte / Rechts |

**Verlinkung:**
- Kein Link
- URL
- Produkt
- Kategorie

**Größenempfehlungen:**
- Vollbreite (ganzseitig): 1280×528 px
- Maximale Darstellungsbreite: 1320 px bei Full-HD

---

### Slider

**Anzeigemodi:**
- Original (Originalgröße beibehalten)
- Feste Höhe (alle Bilder auf gleiche Höhe skalieren)
- Zugeschnitten (Seitenverhältnis anpassen)

**Navigation:**
- Pfeile links/rechts: de-/aktivierbar
- Punkte unten: de-/aktivierbar

**Automatischer Wechsel:**
- Aktivieren/Deaktivieren
- Verzögerung in Millisekunden
- ⚠️ Barrierefreiheitshinweis: Auto-Play kann problematisch für Nutzer mit
  vestibulären Störungen sein

**Bilder:**
- Einzelne Links pro Bild konfigurierbar
- „Dekoratives Bild"-Flag: Bild wird von Screenreadern ignoriert (für Gestaltungsbilder)

---

### Galerie

**Anzeigemodi:** Mehrere Modi wählbar (vertikal/horizontal/grid)

**Vorschau-Navigation:**
- Position: Links oder unten

**Zusatzfunktionen:**
- Zoom bei Klick auf Bild
- Vollbild-Modus aktivierbar
- Seitenverhältnis beibehalten (de-/aktivierbar)

---

### Commerce-Blöcke

#### Produktname & Hersteller-Logo
- Nur auf **Produktseiten** verfügbar
- Automatische Befüllung: Produktname, Hersteller-Logo aus Produktdaten
- Keine manuelle Konfiguration nötig

#### Drei Spalten Produkte-Boxen
- Bis zu 3 Produkte auswählbar (aus Katalog)
- **Layout-Typ:** Standard | Großes Bild | Minimaler Text
- Preis-Anzeige konfigurierbar

#### Produkt-Slider
- Mehrere Produkte in horizontalem Karussell
- **Einstellungen:**
  - Minimale Breite pro Element
  - Rahmen anzeigen (ja/nein)
  - Auto-Wechsel (ja/nein)
  - Animationsdauer in ms

#### Cross-Selling
- Tab „Inhalt": Referenz-Produkt auswählen
- Cross-Selling-Produkte werden automatisch aus Produktkonfiguration geladen
- Anzeige identisch zu Produkt-Slider

#### Bundle-Blöcke (Bundle-Seite)
- Automatische Befüllung mit Bundle-Daten:
  - Enthaltene Produkte
  - Bundle-Name
  - Bildergalerie
  - Bundle-Beschreibung
- Keine manuelle Produktauswahl nötig

---

### Video-Blöcke

#### Video (lokal hochgeladen)
| Option | Beschreibung |
|---|---|
| Videodatei | Upload aus Medienbereich |
| Automatisch abspielen | Video startet ohne Nutzeraktion |
| Stumm abspielen | Ton deaktiviert (Standard bei Auto-Play) |
| Auf Anfrage laden | Video erst bei Nutzerinteraktion laden |

**Wichtig:** Wenn „Automatisch abspielen" aktiviert, wird „Stumm abspielen" automatisch aktiviert.

#### YouTube
| Option | Beschreibung |
|---|---|
| YouTube-URL | Video-URL oder ID |
| Erweiterter Datenschutzmodus | Keine Cookies bis zur Wiedergabe |
| Startzeitpunkt | Sekunden ab denen Video beginnt |
| Endzeitpunkt | Sekunden bei denen Video endet |
| Steuerung anzeigen | YouTube-Controls einblenden |
| Automatisch abspielen | Video startet sofort |

#### Vimeo
| Option | Beschreibung |
|---|---|
| Vimeo-URL | Video-URL |
| Farbanpassung | Akzentfarbe des Players |
| Informationsleiste | Titel und Uploader-Info anzeigen |
| Automatisch abspielen | Video startet sofort |

---

### Weitere Blöcke

#### Sidebar
- Automatisch mit Navigations-/Filterelementen befüllt
- Nur in Layouts mit Sidebar-Sektion verfügbar

#### Formular
- **Typ**: Kontaktformular (Standard)
- **Empfänger-E-Mails**: Bis zu 5 Adressen konfigurierbar
- **E-Mail-Vorlagen**: Anpassbar unter Einstellungen > E-Mail-Vorlagen

#### HTML-Block
- Direktes HTML einbetten
- ⚠️ HTML Sanitizer ist aktiv: Nicht alle HTML-Tags erlaubt
- Einstellungen unter Einstellungen > System > HTML Sanitizer

#### 3D-Modelle (kommerziell, Plan „Rise")
- **Format**: Nur .glb (GL Binary)
- **Verwendung**: Realistische Produktpräsentation
- Interaktive Rotation im Storefront
- Benötigt Shopware Commercial Extension

---

### Produktlisting-Block (Kategorieseiten)

Automatisch in Kategorieseiten integriert; nicht entfernbar.

#### Sortierungen konfigurieren

1. Produktlisting-Block anklicken
2. Tab „Sortierungen"
3. **„Produktsortierung anzeigen"** aktivieren/deaktivieren
4. **Typ**: Eigene Sortierungen oder Standard-Sortierungen
5. Priorität: Doppelklick auf Eintrag → Zahl ändern
6. Standard-Sortierung: Aus Liste auswählen

#### Filter konfigurieren

1. Produktlisting-Block anklicken
2. Tab „Filter"
3. **Allgemeine Filter**: Hersteller, Preis aktivieren/deaktivieren
4. **Eigenschaftsbasierte Filter**: Produkteigenschaften (Farbe, Größe, etc.) einzeln aktivieren
5. **Hinweis**: Filter werden nur im Storefront angezeigt, wenn Produkte mit dieser
   Eigenschaft in der Kategorie vorhanden sind

---

## Viewport-Sichtbarkeit

Für jedes Element und jede Sektion steuerbar.

**Zugang**: Element/Sektion anklicken → Tab „Einstellungen" → Bereich „Sichtbarkeit"

| Viewport | Schwellenwert |
|---|---|
| Desktop | > 991 px Bildschirmbreite |
| Tablet | 767–991 px |
| Mobil | < 767 px |

**Optionen**: Anzeigen / Ausblenden pro Viewport-Typ

---

## Navigator

**Zugang**: Rechte Sidebar → Tab „Navigator"

Zeigt alle Blöcke als Hierarchie mit Sektions-Zuordnung.

| Funktion | Aktion |
|---|---|
| Reihenfolge ändern | Block per Drag & Drop verschieben |
| Block duplizieren | Plus-Symbol neben Block |
| Block löschen | Papierkorb-Symbol neben Block |
| Block umbenennen | Block-Einstellungen (Name-Feld) |

---

## Fehlerbehandlung im Editor

Beim Speichern prüft das System alle Pflichtfelder. Bei Fehlern:
- Fehlermeldung mit Beschreibung
- Betroffenes Element wird hervorgehoben
- Fehlerposition im Layout angezeigt

Typische Fehlerquellen:
- Pflichtbild fehlt in Bild-Block
- Ungültige URL in Link-Feld
- Fehlende Produkt-Zuweisung in Commerce-Block

---

## Layout-Zuweisung

### Methode 1: Aus dem Editor
Rechte Sidebar → Tab „Layout-Zuweisung" → Kategorien auswählen → Zuweisen

### Methode 2: Aus der Kategorie-Verwaltung
Kataloge > Kategorien > Kategorie öffnen > Tab „Layout" > Layout auswählen

### Methode 3: Aus der Produkt-Verwaltung
Kataloge > Produkte > Produkt öffnen > Tab „Layout" > Layout auswählen

### Standardlayouts
Editor-Sidebar → „Layout-Zuweisung" → „Standardlayouts" → „Als Standardlayout verwenden"
- Gilt für alle neu erstellten Kategorien/Produkte
- Spart Zeit bei gleichartigem Design

---

## Shopseiten-Zuweisung

Einstellungen > Shops > [Shop auswählen] > Stammdaten > Bereich „Shopseiten"

Verfügbare Seiten-Slots:
- Startseite
- AGB
- Widerrufsbelehrung
- Impressum
- Datenschutzerklärung
- Newsletter-Bestätigung
- Wartungsmodus-Seite
- 404-Fehlerseite

---

## Landingpage – besondere Konfiguration

1. Neues Layout vom Typ „Landingpage" erstellen
2. Layout gestalten (kein Produktlisting vorhanden)
3. Unter Kataloge > Kategorien: Neue oder bestehende Kategorie öffnen
4. Tab „Allgemein" → Aktiviere „Landingpage" oder weise Layout im Tab „Layout" zu
5. Optional: Kategorie aus Navigation ausblenden
6. URL: Automatisch die URL der Kategorie

---

## Produktseite – individuelle Element-Anpassung

Wenn ein Layout mehreren Produkten zugewiesen ist, können einzelne Elemente
produktspezifisch überschrieben werden:

1. Kataloge > Produkte > Produkt öffnen > Tab „Layout"
2. Zugewiesenes Layout wird angezeigt
3. Klick auf bearbeitbare Elemente → Produktspezifische Werte eingeben
4. Änderungen betreffen nur dieses Produkt, nicht das globale Layout

---

## Tipps und Best Practices

- **Benennung**: Layouts und Blöcke klar benennen (z.B. „Startseite Summer 2024")
- **Standardlayouts**: Frühzeitig definieren, spart bei Massenpflege Zeit
- **Bildgrößen**: 1280×528 px für Hero-Banner verwenden
- **Responsiveness**: Sichtbarkeit für jeden Viewport testen
- **Auto-Play**: Mit Bedacht einsetzen; Barrierefreiheitshinweise beachten
- **AI Copilot**: Nur auf kommerziellen Plänen verfügbar (Shopware Rise/Beyond)
- **3D-Modelle**: Nur .glb-Format; Dateigröße optimieren für Ladezeiten

---

## Verwandte Dokumentation

- Medien: `sw-merchant-content-media`
- Themes: `sw-merchant-content-themes`
- CMS-Erweiterungen: `sw-merchant-content-cms-extensions`
- Tutorial Shop gestalten: https://docs.shopware.com/de/shopware-6-de/tutorials-und-faq/wie-gestalte-ich-meinen-shop
- Interaktiver Lernpfad: https://hub.shopware.com/learn/unit/user-shopping-experiences
