# Shopware 6 – Medien: Vollständige Dokumentation

**Quelle:** https://docs.shopware.com/de/shopware-6-de/Inhalte/medien  
**Version:** ab 6.7.0.0

---

## Screenshots

| Datei | Inhalt |
|---|---|
| `../../assets/medien-uebersicht.png` | Medien-Übersicht |
| `../../assets/medien-ersetzen.png` | Aktionen-Toolbar (Ersetzen, Download, etc.) |
| `../../assets/medien-metadaten.png` | Metadaten-Bearbeitungsbereich |
| `../../assets/medien-verwendung.png` | „Wird verwendet in"-Bereich |
| `../../assets/ordner.png` | Ordnerstruktur-Ansicht |
| `../../assets/ordner-aktionen.png` | Ordner-Kontextmenü |
| `../../assets/ordner-einstellungen.png` | Ordner-Einstellungen-Dialog |
| `../../assets/thumbnails.png` | Thumbnail-Konfiguration |
| `../../assets/bild-generierung.jpg` | AI Bildgenerierung Interface |
| `../../assets/bild-generiert.jpg` | Generiertes Bild Ergebnis |
| `../../assets/model-viewer.png` | 3D Model Viewer in Sidebar |
| `../../assets/model-editor.png` | 3D Model Editor Vollbild |

---

## Übersicht

Pfad: **Inhalte > Medien**

Die Medienverwaltung ist die zentrale Bibliothek für alle Dateien im Shop.
Alle Bereiche (Erlebniswelten, Produkte, Kategorien, Themes) greifen auf
diese Bibliothek zu.

### Interface-Elemente der Übersicht

| Element | Funktion |
|---|---|
| Suchfeld (oben) | Medien nach Name suchen |
| „Dateien hochladen" | Upload-Dialog öffnen |
| URL-Upload | Datei per URL hochladen |
| Anzeige-Optionen | Listen- oder Kachelansicht |
| Sortier-Optionen | Nach Name, Datum, Typ sortieren |
| „Bildgenerierung" | KI-Bildgenerierung (kommerziell) |
| „Neuen Ordner hinzufügen" | Neuen Ordner anlegen |

---

## Unterstützte Dateitypen

### Bilder
jpg, jpeg, png, webp, gif, svg, bmp, tiff, eps

### Video
webm, mkv, flv, ogv, ogg, mov, mp4, avi, wmv

### Dokumente
pdf, txt, doc

### Audio
aac, mp3, wav, flac, oga, wma

### 3D-Modelle
glb (GL Binary – für Model Viewer und 3D-Blöcke in Erlebniswelten)

---

## Dateien hochladen

### Methode 1: Direktupload
1. „Dateien hochladen" anklicken
2. Dateien aus dem Dateisystem auswählen
3. Mehrere Dateien gleichzeitig möglich

### Methode 2: URL-Upload
1. URL-Upload-Symbol anklicken
2. Direkte URL zur Datei eingeben
3. Shopware lädt Datei automatisch herunter und speichert sie

### Duplikat-Handling

Wenn eine Datei mit gleichem Namen bereits existiert, erscheint ein Pop-up:

| Option | Verhalten |
|---|---|
| Hochladen und ersetzen | Vorhandene Datei wird überschrieben |
| Hochladen und umbenennen | Neue Datei erhält automatisch geänderten Namen |
| Vorhandene Datei verwenden | Upload abbrechen, bestehende Datei nutzen |
| Datei überspringen | Upload für diese Datei überspringen |

---

## Medien-Konfiguration (Einzeldatei)

Klick auf ein Medium öffnet das Detailpanel rechts.

### Vorschau
- Bildvorschau oder Datei-Icon
- Bei 3D-Modellen: interaktiver Model Viewer

### Metadaten (editierbar)

| Feld | Beschreibung |
|---|---|
| Name | Anzeigename der Datei (nicht Dateiname) |
| Alt-Text | Barrierefreiheits-Text für Bilder (wichtig für SEO) |
| Meta-Titel | Titel für Suchmaschinen |

### Tags
- Schlagworte zur besseren Auffindbarkeit
- Mehrere Tags möglich

### Aktionen (Toolbar)

| Aktion | Beschreibung |
|---|---|
| Ersetzen | Datei durch neue Version austauschen (URL bleibt gleich) |
| Download | Datei herunterladen |
| Verschieben | In anderen Ordner verschieben |
| Link kopieren | Direkte URL der Datei in Zwischenablage |
| Löschen | Datei permanent entfernen |

### „Wird verwendet in"
- Zeigt alle Stellen, an denen das Medium verwendet wird
- Mit Direktlinks zur jeweiligen Seite/Produkt/Kategorie
- Wichtig: Vor dem Löschen prüfen!

---

## Ordnerverwaltung

### Ordner erstellen
„Neuen Ordner hinzufügen" → Namen eingeben → Bestätigen

### Ordner-Navigation
- Klick auf Ordner öffnet Inhalt
- Zurück-Navigation über Pfeil-Symbol oder Breadcrumb

### Ordner-Aktionen (Kontextmenü)

| Aktion | Beschreibung |
|---|---|
| Verschieben | Ordner in übergeordneten Ordner verschieben |
| Einstellungen | Ordner-Konfiguration öffnen |
| Auflösen | Ordner entfernen; Inhalt in übergeordneten Ordner verschieben |
| Löschen | Ordner und gesamten Inhalt permanent löschen |

**Achtung**: „Löschen" entfernt alle darin enthaltenen Dateien unwiederbringlich.

### Ordner-Einstellungen

**Tab „Allgemein":**
- Namen ändern
- Standard-Speicherort für bestimmte Medientypen definieren
  (z.B. „Alle Produktbilder landen automatisch in diesem Ordner")

**Tab „Thumbnails":**

| Einstellung | Beschreibung |
|---|---|
| Einstellungen vom übergeordneten Ordner übernehmen | Thumbnails von Elternordner erben |
| Thumbnails generieren | Thumbnail-Generierung für diesen Ordner aktivieren |
| Seitenverhältnis beibehalten | Proportionen beim Skalieren beibehalten |
| Thumbnail-Qualität | Wert 1–100 (Komprimierungsqualität) |
| Thumbnail-Größen | Liste der generierten Größen |

**Standard-Thumbnail-Größen:** 400×400, 800×800, 1920×1920

### Thumbnails neu generieren

Via Konsole (SSH/CLI):
```bash
bin/console media:generate-thumbnails
```

---

## Ungenutzte Medien löschen

### Über Konsole (empfohlen bei großer Menge)

```bash
bin/console media:delete-unused
```

Optionale Parameter:
```bash
# Nur Vorschau (trocken laufen lassen)
bin/console media:delete-unused --dry-run

# Bestimmten Ordner prüfen
bin/console media:delete-unused --folder-id=<ID>
```

**Hinweis**: Vor dem Ausführen Backup erstellen. Aktion ist nicht umkehrbar.

---

## AI-Copilot: Bildgenerierung

**Verfügbarkeit:** Shopware Rise Plan oder höher + Shopware Commercial Extension installiert

### Verwendung

1. Inhalte > Medien > Button „Bildgenerierung"
2. Beschreibung des gewünschten Bildes eingeben (Prompt)
3. „Bild generieren" anklicken
4. Generiertes Bild prüfen:
   - „Speichern" → Bild wird in Ordner „AI-generated" abgelegt
   - „Neu generieren" → Neues Bild mit gleichem Prompt erstellen

### Technische Details

- **KI-Modell:** Google Nano Banana 2
- **Bilder pro Anfrage:** 1 Bild
- **Tägliches Limit:** Begrenzte Anzahl Anfragen pro Tag
- **Nachbearbeitung:** Nicht möglich; bei Unzufriedenheit: neu generieren
- **Speicherort:** Automatisch im Ordner „AI-generated"

### Unterstützte Seitenverhältnisse

1:1 | 2:3 | 3:2 | 3:4 | 4:3 | 9:16 | 16:9 | 21:9

### Unterstützte Auflösungen

- 1K (Standard)
- 2K

**Standardwerte:** 16:9 Seitenverhältnis, 1K Auflösung

### Prompt-Tipps für bessere Ergebnisse

- **Konkret sein**: „Produkt-Lifestyle-Bild eines Sneakers auf Holzboden, natürliches Licht, horizontal"
- **Qualitätshinweise**: Adjektive wie „hochwertig", „professionell", „sauber" verwenden
- **Ausrichtung angeben**: Landscape/Portrait explizit nennen
- **Maße optional**: Seitenverhältnis kann im Prompt genannt werden

### Automatische Erkennung aus Prompt

Das System analysiert den Prompt und erkennt automatisch:
- Format (Landscape/Portrait/Square)
- Seitenverhältnis
- Gewünschte Auflösung

---

## 3D-Modelle (GLB-Format)

### Voraussetzungen
- Datei im .glb Format (GL Binary)
- Für 3D-Blöcke in Erlebniswelten: Shopware Rise Plan

### Model Viewer (Vorschau)

Automatisch aktiv wenn GLB-Datei ausgewählt:

| Steuerung | Aktion |
|---|---|
| Linke Maustaste + Ziehen | Modell drehen |
| Rechte Maustaste + Ziehen | Kamera verschieben (Pan) |
| Scrollrad | Zoom In/Out |
| Expand-Button | Model Editor als Modal öffnen |

### Model Editor (Bearbeitung)

Öffnet sich über Expand-Button des Model Viewers.

#### Werkzeuge

**Verschieben-Werkzeug (Move Tool):**
- Blauer Pfeil: Z-Achse (Tiefe)
- Grüner Pfeil: Y-Achse (Höhe)
- Roter Pfeil: X-Achse (Breite)
- Farbige Quadrate: Kombinierte Ebenen (XY, XZ, YZ)

**Drehen-Werkzeug (Rotate Tool):**
- Roter Ring: Vorwärts/Rückwärts kippen (Pitch)
- Blauer Ring: Links/Rechts kippen (Yaw)
- Grüner Ring: Rotation um eigene Achse (Roll)
- Gelber Außenring: Kameraperspektive ändern

**Skalieren-Werkzeug:**
- Standard: Proportionale Skalierung (alle Achsen gleichzeitig)
- Optional: Einzelne Achsen skalieren
  - Grün: Höhe (Y)
  - Rot: Breite (X)
  - Blau: Tiefe (Z)

#### Persistenz
Alle Änderungen im Model Editor werden automatisch in der Datenbank gespeichert.
Kein manuelles Speichern erforderlich.

---

## Best Practices

### Dateiorganisation
- Ordnerstruktur von Anfang an anlegen (z.B. nach Kategorie oder Kampagne)
- Standard-Speicherorte für häufige Medientypen konfigurieren
- Regelmäßig ungenutzte Medien aufräumen (`media:delete-unused`)

### Bildoptimierung
- Webp-Format bevorzugen (bessere Kompression als JPG/PNG)
- Thumbnails für Produktbilder aktivieren
- Alt-Texte immer pflegen (SEO und Barrierefreiheit)

### Performance
- Bilder vor dem Upload komprimieren
- Maximale Dateigröße beachten (je nach Server-Konfiguration)
- Thumbnails nutzen statt Originalgröße auszuliefern

---

## CLI-Befehle (Konsole)

```bash
# Ungenutzte Medien löschen
bin/console media:delete-unused

# Thumbnails neu generieren
bin/console media:generate-thumbnails

# Thumbnails für bestimmten Ordner
bin/console media:generate-thumbnails --folder-id=<ID>
```

Weitere CLI-Dokumentation: https://docs.shopware.com/de/shopware-6-de/tutorials-und-faq/shopware-cli#media
