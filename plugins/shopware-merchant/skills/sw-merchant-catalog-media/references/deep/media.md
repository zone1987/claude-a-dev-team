# Shopware 6 – Medienverwaltung: Vollständige Referenz

> Quelle: https://docs.shopware.com/de/shopware-6-de/inhalte/medien  
> Gilt ab: Shopware 6.0.0+

---

## 1. Überblick

Die Medienverwaltung ist das zentrale Repository für alle Dateien in Shopware 6. Von hier aus werden Produktbilder, Kategoriebilder, Dokumente, Videos und 3D-Modelle verwaltet und dem Shop zur Verfügung gestellt.

Pfad: **Inhalte > Medien**

---

## 2. Unterstützte Dateitypen

| Kategorie | Formate |
|---|---|
| **Bilder** | jpg, jpeg, png, webp, gif, svg, bmp, tiff, eps |
| **Videos** | webm, mkv, flv, ogv, ogg, mov, mp4, avi, wmv |
| **Audio** | aac, mp3, wav, flac |
| **Dokumente** | pdf, txt, doc |
| **3D-Modelle** | glb |

---

## 3. Dateien hochladen

### 3.1 Upload-Methoden

| Methode | Beschreibung |
|---|---|
| **Datei-Upload** | Lokale Datei vom Computer hochladen (Klick auf Upload-Button oder Drag & Drop) |
| **URL-Upload** | Öffentlich erreichbare Datei per URL importieren |

### 3.2 Upload-Prozess

1. Inhalte > Medien
2. Gewünschten Ordner auswählen (oder Stammverzeichnis)
3. **„Datei hochladen"** oder URL eingeben
4. Bei Duplikaten: Shopware fragt ob die bestehende Datei ersetzt werden soll

### 3.3 Duplikat-Handling

Wenn eine Datei mit identischem Namen bereits existiert, bietet Shopware an:
- Datei **ersetzen** (Datei wird überschrieben, URL bleibt gleich)
- Datei **umbenennen** (neue Datei wird mit geändertem Namen gespeichert)

---

## 4. Medien-Aktionen

### 4.1 Einzelne Datei

Über das Kontextmenü oder die Datei-Detailansicht stehen zur Verfügung:

| Aktion | Beschreibung |
|---|---|
| **Ersetzen** | Bestehende Datei durch neue Version ersetzen; URL bleibt erhalten |
| **Herunterladen** | Datei auf den lokalen Computer laden |
| **Verschieben** | In einen anderen Ordner verschieben |
| **Link kopieren** | Direkt-URL der Datei in die Zwischenablage |
| **Löschen** | Datei aus dem System entfernen |

> **Hinweis**: Das Löschen einer Datei die noch in Produkten, Kategorien etc. verwendet wird kann zu fehlenden Bildern im Shop führen!

---

## 5. Metadaten bearbeiten

Jede Datei verfügt über bearbeitbare Metadaten:

| Feld | Beschreibung |
|---|---|
| **Dateiname** | Name ohne Dateiendung; bestimmt die URL der Datei |
| **Alt-Text** | Barrierefreiheit und SEO; erscheint wenn Bild nicht geladen werden kann |
| **Meta-Titel** | Titel für SEO-Zwecke |
| **Tags** | Schlagworte für bessere Auffindbarkeit in der Medienverwaltung |
| **Wird verwendet in** | Zeigt alle Entitäten (Produkte, Kategorien etc.) die diese Datei nutzen |

### Metadaten bearbeiten

1. Datei in der Medienverwaltung anklicken
2. Rechte Seitenleiste öffnet Detailansicht
3. Felder bearbeiten
4. Speichern (automatisch oder per Button)

---

## 6. Ordnerverwaltung

### 6.1 Ordner erstellen

- Button **„Ordner hinzufügen"** oder per Kontextmenü
- Beliebig tiefe Verschachtelung möglich
- Ordnernamen sollten aussagekräftig gewählt werden (z. B. „Produkte", „Banner", „Hersteller")

### 6.2 Ordner-Aktionen

| Aktion | Beschreibung |
|---|---|
| **Verschieben** | Ordner in einen anderen Ordner verschieben |
| **Umbenennen** | Ordnerbezeichnung ändern |
| **Auflösen** | Inhalt des Ordners in übergeordneten Ordner verschieben, dann Ordner löschen |
| **Löschen** | Ordner und Inhalt löschen |

### 6.3 Standard-Ordnerstruktur

Shopware legt automatisch Standardordner für verschiedene Entitäten an, z. B.:
- `Produkte` – Produktbilder
- `Kategorien` – Kategoriebilder  
- `Hersteller` – Hersteller-Logos
- `Medienverwaltung` – Allgemeine Dateien

---

## 7. Thumbnail-Konfiguration

Thumbnails sind automatisch generierte Versionen von Bildern in definierten Größen.

### 7.1 Standard-Thumbnail-Größen

| Größe | Verwendung |
|---|---|
| 400×400 px | Produktlisting (Vorschaubilder) |
| 800×800 px | Produktdetailseite (mittlere Qualität) |
| 1920×1920 px | Zoom-Ansicht / hohe Auflösung |

### 7.2 Thumbnail-Einstellungen (pro Ordner konfigurierbar)

| Einstellung | Beschreibung |
|---|---|
| **Größen** | Welche Thumbnail-Größen generiert werden sollen |
| **Qualität** | Komprimierungsgrad (1–100); 80 ist ein guter Standardwert |
| **Seitenverhältnis** | Beschnitt-Verhalten (proportional / füllen / dehnen) |
| **Automatische Generierung** | Thumbnails werden bei Upload automatisch erstellt |

### 7.3 Thumbnails manuell generieren (CLI)

```bash
bin/console media:generate-thumbnails
```

Nützlich nach Änderungen der Thumbnail-Konfiguration oder bei fehlenden Thumbnails.

---

## 8. 3D-Funktionen

### 8.1 Model Viewer

- Ermöglicht die Betrachtung von GLB-Dateien direkt in der Administration
- 3D-Modell kann gedreht, gezoomt und erkundet werden
- Vorschau vor der Einbindung in Produkte

### 8.2 Model Editor

- Bearbeitung von Position, Rotation und Skalierung des 3D-Modells
- Visuelle Echtzeit-Vorschau der Änderungen
- Automatische Speicherung der Einstellungen

### 8.3 AR (Augmented Reality)

Voraussetzungen:
- iOS 12+ (Apple ARKit)
- Android 8.0+ mit ARCore 1.9
- GLB-Format der 3D-Datei
- AR-Aktivierung in den Produkt-Einstellungen

---

## 9. Darstellung und Sortierung anpassen

### 9.1 Ansichtsoptionen

- **Rasteransicht**: Kacheln mit Vorschaubildern
- **Listenansicht**: Tabellarische Darstellung
- Umschaltbar per Dropdown

### 9.2 Sortieroptionen

- Name (A–Z / Z–A)
- Datum hochgeladen (neu/alt zuerst)
- Dateigröße
- Dateityp

---

## 10. AI-Features

### 10.1 AI-Bildgenerierung (ab Shopware Rise)

- **„AI Copilot Bildgenerierung"** direkt in der Medienverwaltung
- Bilder durch natürlichsprachliche Beschreibung generieren
- Generierte Bilder werden direkt in der Medienverwaltung gespeichert
- Geeignet für Stimmungsbilder, Banner, Platzhalterbilder

**Verwendung:**
1. Inhalte > Medien
2. Button **„KI-Bild generieren"** (oder ähnlich)
3. Beschreibung in natürlicher Sprache eingeben
4. Bild generieren lassen
5. In gewünschtem Ordner speichern

---

## 11. Wartung und Bereinigung

### 11.1 Ungenutzte Medien identifizieren

Das Feld **„Wird verwendet in"** zeigt für jede Datei, wo sie eingesetzt wird.
Ist das Feld leer: Datei wird nirgendwo verwendet.

### 11.2 Ungenutzte Medien löschen (CLI)

```bash
bin/console media:delete-unused
```

Löscht alle Mediendateien, die in keiner Shopware-Entität mehr referenziert werden.

> **Vorsicht**: Vor dem Ausführen prüfen ob externe Systeme (Import-Tools, Exporte) Dateien referenzieren, die Shopware nicht als „verwendet" kennt!

---

## 12. Empfehlungen für Produktbilder

| Eigenschaft | Empfehlung |
|---|---|
| Format | JPG (Fotos) oder PNG (mit Transparenz) oder WebP |
| Seitenverhältnis | **Quadratisch** (1:1) für konsistente Darstellung |
| Mindestgröße | 600×600 px |
| Optimalgröße | 1920×1920 px (deckt alle Thumbnail-Größen ab) |
| Dateiname | Sprechend und SEO-freundlich (z. B. `blaues-t-shirt-vorne.jpg`) |
| Alt-Text | Immer ausfüllen für Barrierefreiheit und SEO |

---

## 13. Empfehlungen für Produktvideos

| Eigenschaft | Empfehlung |
|---|---|
| Format | **MP4** (beste Browser-Kompatibilität) |
| Codecs | H.264 Video, AAC Audio |
| Alternative | WebM als Fallback |
| Auflösung | Mindestens 720p (1280×720) |
| Dateigröße | Unter 100 MB (Performance) |

---

*Quelle: https://docs.shopware.com/de/shopware-6-de/inhalte/medien*
