# Shopware 6 – Inhalte: Vollständige Übersicht

**Quelle:** https://docs.shopware.com/de/shopware-6-de/inhalte  
**Version:** ab 6.7.0.0

---

## Bereich im Admin

Pfad: **Inhalte** (Hauptnavigation links)

Der Inhalte-Bereich enthält die vier Hauptmodule:

1. **Erlebniswelten** – visueller Seiten-Builder (CMS)
2. **Medien** – zentrale Medienbibliothek
3. **Themes** – Design-Konfiguration des Storefronts
4. **CMS-Erweiterungen** – Zusatzfunktionen (Shopware Evolve+)

---

## Erlebniswelten (Shopping Experiences)

Pfad: Inhalte > Erlebniswelten

Shopwares eigenes Drag-and-Drop-CMS. Ermöglicht das Erstellen und Zuweisen
von Layouts für verschiedene Seitentypen ohne Code-Kenntnisse.

### Architektur

```
Layout
└── Sektion (Section)
    └── Block
        └── Element (Text, Bild, Video, ...)
```

### Layouttypen

| Typ | Verwendung | Besonderheit |
|---|---|---|
| Shopseite | AGB, Impressum, Kontakt | Zuweisung unter Einstellungen > Shops |
| Landingpage | Marketing-Seiten | Eigene URL über Kategorie-Zuweisung |
| Kategorieseite | Kategorie-Startseiten | Enthält Produktlisting automatisch |
| Produktseite | Produktdetailseiten | Individuelle Anpassung pro Produkt möglich |
| Bundle-Seite | Produkt-Bundles | Automatische Bundle-Datenbefüllung |

### Block-Kategorien und Elemente

#### Text-Blöcke
- Vollwertiger WYSIWYG-Editor mit Formatierung (Bold, Italic, Listen, Links)
- **Datenzuordnung**: Dynamische Inhalte aus Kategorie/Produkt-Daten
- **Variablen**: `{{ variable }}` Syntax für direkte Dateneingabe
- **AI Copilot** (kommerziell): KI-generierte Textvorschläge
- **Link-Typen**: URL, Produkt, Kategorie, E-Mail, Telefon

#### Bild-Blöcke
- Bildauswahl aus Medienbereich oder Direktupload
- Datenzuordnung für automatische Bildbefüllung
- **Anzeigemodi**: Standard | Füllen | Strecken
- **Ausrichtung**: Vertikal und horizontal konfigurierbar
- **Link**: Bild als Verlinkung verwendbar
- **Größenempfehlung**: 1280×528 px für vollbreite Bilder; max. 1320 px bei Full-HD

#### Slider
- **Anzeigemodi**: Original | Feste Höhe | Zugeschnitten
- Mindeststhöhe konfigurierbar
- Pfeil- und Punkt-Navigation (de-/aktivierbar)
- Auto-Play mit Verzögerung (ms) – Barrierefreiheitshinweis beachten
- Bilder einzeln verlinkbar
- Dekoratives Bild-Flag für Screenreader-Zugänglichkeit

#### Galerie
- Mehrere Anzeigemodi wählbar
- Vorschau-Navigation (links oder unten)
- Zoom-Funktion
- Vollbild-Modus
- Seitenverhältnis-Beibehaltung

#### Commerce-Blöcke

**Produktname & Hersteller-Logo**
- Auf Produktseiten: automatische Befüllung mit Produktname und Hersteller-Logo

**Drei Spalten Produkte-Boxen**
- Bis zu 3 Produkte anzeigen
- Layout-Typ: Standard | Großes Bild | Minimaler Text

**Produkt-Slider**
- Horizontaler Slider für mehrere Produkte
- Minimale Breite einstellbar
- Rahmen de-/aktivierbar
- Auto-Wechsel mit Animationsdauer (ms)

**Cross-Selling**
- Produkt für Cross-Selling-Basis im Tab „Inhalt" angeben
- Verknüpfte Produkte werden automatisch geladen

**Bundles**
- Automatische Befüllung: Produktliste, Bundle-Name, Galerie, Beschreibung
- Speziell für Bundle-Seitentyp

#### Video-Blöcke

| Typ | Besonderheiten |
|---|---|
| Video (lokal) | Auto-Play, Stummschalten, Auf Anfrage laden |
| YouTube | Erweiterter Datenschutzmodus, Start-/Endzeit |
| Vimeo | Farbanpassung, Informations-Overlay konfigurierbar |

**Achtung**: Auto-Play deaktiviert automatisch Ton-Option (Barrierefreiheit).

#### Weitere Blöcke

- **Sidebar**: Automatisch befüllt (Filter, Navigation)
- **Formular**: Kontaktformular mit konfigurierbaren Empfänger-E-Mails
- **HTML**: Direktes HTML einbetten (HTML Sanitizer-Einstellungen beachten)
- **3D-Modelle** (kommerziell, Plan „Rise"): .glb-Format, realistische Produktvisualisierung

#### Produktlisting-Block (Kategorieseiten)

Automatisch in Kategorieseiten integriert. Konfigurierbar:

**Sortierungen:**
- „Produktsortierung anzeigen" aktivieren/deaktivieren
- Eigene oder Standard-Sortierungen
- Priorität durch Doppelklick ändern
- Standard-Sortierung auswählen

**Filter:**
- Allgemeine Filter: Hersteller, Preis
- Eigenschaftsbasierte Filter konfigurierbar
- Filter werden nur angezeigt, wenn Produkte mit dieser Eigenschaft existieren

---

### Einstellungen im Layout-Editor

#### Block-Einstellungen (Klick auf Block → rechte Sidebar)

| Einstellung | Beschreibung |
|---|---|
| Name | Bezeichnung für Navigator |
| Hintergrundfarbe | Farbauswahl inkl. Hex-Eingabe |
| Hintergrundbild | Bild aus Medienbibliothek |
| Bildmodus | Standard/Füllen/Strecken |
| Layout/CSS-Klassen | Custom-CSS-Klassen und Abstände |

#### Sektions-Einstellungen

| Einstellung | Beschreibung |
|---|---|
| Sektionsname | Zur Identifikation im Navigator |
| CSS-Klassen | Mehrere mit Leerzeichen trennen |
| Größenmodus | Volle Breite oder zentriert |
| Mobiles Sidebar-Verhalten | „Nicht angezeigt" für mobiles Ausblenden |
| Hintergrundfarbe/-bild | Identisch zu Block-Einstellungen |

#### Sichtbarkeit (Viewport-Steuerung)

Jedes Element und jede Sektion kann geräteabhängig ein-/ausgeblendet werden.
Einstellung pro Viewport: Desktop | Tablet | Mobil.

#### Navigator

Rechte Sidebar-Tab. Zeigt alle Blöcke als Hierarchie:
- **Drag & Drop**: Reihenfolge per Ziehen ändern
- **Plus-Icon**: Block duplizieren
- **Papierkorb-Icon**: Block löschen

#### Fehlerbehandlung

Beim Speichern zeigt das System:
- Genaue Fehlermeldung
- Betroffenes Element
- Fehlerposition im Layout

---

### Layout-Zuweisung

#### Shopseiten
Einstellungen > Shops > Stammdaten > Bereich „Shopseiten"

#### Kategorieseiten
Kataloge > Kategorien > Kategorie öffnen > Tab „Layout" > Layout zuweisen

#### Landingpages
1. Landingpage-Layout erstellen
2. Unter Kataloge > Kategorien einer Kategorie zuweisen
3. Aufruf über URL der Kategorie

#### Produktseiten
Kataloge > Produkte > Produkt öffnen > Tab „Layout" > Layout auswählen
→ Individuelle Elementwerte pro Produkt überschreibbar

#### Standardlayouts festlegen
Layout-Editor > Sidebar > Layout-Zuweisung > Standardlayouts > „Als Standardlayout verwenden"
- Spart Zeit bei neuen Kategorien/Produkten

---

## Medien

Pfad: Inhalte > Medien

Zentrale Medienbibliothek. Details: `sw-merchant-content-media`

## Themes

Pfad: Inhalte > Themes

Design-Konfiguration (Farben, Schriften, Logos). Details: `sw-merchant-content-themes`

## CMS-Erweiterungen

Pfad: Erweiterungen > CMS-Erweiterungen (Shopware Evolve+)

Details: `sw-merchant-content-cms-extensions`
